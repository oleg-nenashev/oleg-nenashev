"""
MkDocs Plugin for WebMCP Integration.
Automatically scaffolds MCP resources, tools, and discovery manifests from mkdocs.yml and navigation.
"""

from __future__ import annotations
import json
import os
import shutil
from pathlib import Path
from typing import Any, Dict

from mkdocs.config import config_options
from mkdocs.config.base import Config
from mkdocs.plugins import BasePlugin
from mkdocs.structure.pages import Page

from mkdocs_webmcp.scaffolder import SiteScaffolder


class WebMCPPluginConfig(Config):
    enabled = config_options.Type(bool, default=True)
    site_url = config_options.Type(str, default="")
    export_manifest = config_options.Type(bool, default=True)
    export_resources = config_options.Type(bool, default=True)
    export_tools = config_options.Type(bool, default=True)
    inject_client = config_options.Type(bool, default=True)


class WebMCPPlugin(BasePlugin[WebMCPPluginConfig]):
    """MkDocs plugin that exposes site content, metadata, and search as a WebMCP service."""

    def __init__(self):
        super().__init__()
        self.scaffolder: SiteScaffolder | None = None

    def on_config(self, config: Dict[str, Any]) -> Dict[str, Any]:
        """Hook called on MkDocs configuration load."""
        if not self.config.get("enabled", True):
            return config

        # Inject webmcp.js into extra_javascript if client injection enabled
        if self.config.get("inject_client", True):
            extra_js = config.get("extra_javascript", [])
            js_path = "assets/js/webmcp.js"
            if js_path not in extra_js:
                extra_js.append(js_path)
            config["extra_javascript"] = extra_js

        return config

    def on_post_build(self, config: Dict[str, Any]) -> None:
        """Hook called after the full site is built. Generates WebMCP assets and manifests."""
        if not self.config.get("enabled", True):
            return

        site_dir = Path(config.get("site_dir", "_site")).resolve()
        docs_dir = Path(config.get("docs_dir", ".")).resolve()
        config_file_path = config.get("config_file_path", "mkdocs.yml")

        # Initialize Scaffolder
        self.scaffolder = SiteScaffolder(root_dir=Path(config_file_path).parent if config_file_path else ".")
        
        # Collect metadata, resources, tools, prompts
        site_meta = self.scaffolder.get_site_metadata()
        resources = self.scaffolder.scaffold_resources()
        tools = self.scaffolder.scaffold_tools()
        prompts = self.scaffolder.scaffold_prompts()

        site_url = self.config.get("site_url") or site_meta.get("site_url", "")

        # Build MCP Manifest
        mcp_manifest = {
            "$schema": "https://modelcontextprotocol.io/schema.json",
            "mcpVersion": "2024-11-05",
            "serverInfo": {
                "name": "oleg-nenashev-webmcp",
                "title": f"{site_meta['site_name']} - WebMCP Service",
                "version": "0.1.0",
                "description": site_meta.get("site_description", ""),
                "websiteUrl": site_url,
                "repositoryUrl": site_meta.get("repo_url", ""),
            },
            "transports": {
                "in_browser": {
                    "type": "javascript",
                    "clientScript": f"{site_url.rstrip('/')}/assets/js/webmcp.js",
                    "object": "window.WebMCP"
                },
                "stdio": {
                    "type": "stdio",
                    "command": "python",
                    "args": ["-m", "mkdocs_webmcp.server"]
                },
                "sse": {
                    "type": "sse",
                    "endpoint": f"{site_url.rstrip('/')}/mcp/sse"
                }
            },
            "capabilities": {
                "resources": {
                    "listChanged": False,
                    "subscribe": False
                },
                "tools": {
                    "listChanged": False
                },
                "prompts": {
                    "listChanged": False
                }
            },
            "resources": [
                {
                    "uri": r["uri"],
                    "name": r["name"],
                    "description": r["description"],
                    "mimeType": r.get("mimeType", "application/json")
                }
                for r in resources
            ],
            "tools": tools,
            "prompts": prompts
        }

        # Ensure output directories exist
        site_dir.mkdir(parents=True, exist_ok=True)
        mcp_assets_dir = site_dir / "assets" / "mcp"
        mcp_assets_dir.mkdir(parents=True, exist_ok=True)
        well_known_dir = site_dir / ".well-known"
        well_known_dir.mkdir(parents=True, exist_ok=True)
        js_dir = site_dir / "assets" / "js"
        js_dir.mkdir(parents=True, exist_ok=True)

        # Write mcp.json and .well-known/mcp.json
        if self.config.get("export_manifest", True):
            manifest_json = json.dumps(mcp_manifest, indent=2, ensure_ascii=False)
            (site_dir / "mcp.json").write_text(manifest_json, encoding="utf-8")
            (well_known_dir / "mcp.json").write_text(manifest_json, encoding="utf-8")
            (mcp_assets_dir / "manifest.json").write_text(manifest_json, encoding="utf-8")

        # Write resources.json
        if self.config.get("export_resources", True):
            (mcp_assets_dir / "resources.json").write_text(
                json.dumps(resources, indent=2, ensure_ascii=False),
                encoding="utf-8"
            )

        # Write tools.json
        if self.config.get("export_tools", True):
            (mcp_assets_dir / "tools.json").write_text(
                json.dumps(tools, indent=2, ensure_ascii=False),
                encoding="utf-8"
            )

        # Write prompts.json
        (mcp_assets_dir / "prompts.json").write_text(
            json.dumps(prompts, indent=2, ensure_ascii=False),
            encoding="utf-8"
        )

        # Copy webmcp.js client to site_dir and root assets/js/
        package_js = Path(__file__).parent / "assets" / "webmcp.js"
        if package_js.exists():
            shutil.copy2(package_js, js_dir / "webmcp.js")
            # Also keep root assets/js/webmcp.js updated
            root_js_dir = Path("assets/js")
            root_js_dir.mkdir(parents=True, exist_ok=True)
            shutil.copy2(package_js, root_js_dir / "webmcp.js")

    def on_post_page(self, output: str, page: Page, config: Dict[str, Any]) -> str:
        """Inject WebMCP discovery link tags in the HTML header."""
        if not self.config.get("enabled", True):
            return output

        discovery_tags = (
            '\n    <!-- WebMCP (Model Context Protocol) Discovery -->'
            '\n    <link rel="mcp-server" type="application/json" href="./mcp.json" title="WebMCP Server Manifest">'
            '\n    <link rel="alternate" type="application/json+mcp" href="./.well-known/mcp.json" title="WebMCP">'
            '\n    <meta name="mcp-server" content="./mcp.json">'
        )

        if "</head>" in output:
            output = output.replace("</head>", f"{discovery_tags}\n  </head>", 1)

        return output
