"""
WebMCP Model Context Protocol (MCP) server implementation for Oleg Nenashev's site.
Serves key profile information, open-source projects, consulting areas, and integrates with the MkDocs search API.
"""

from __future__ import annotations
import argparse
import json
import os
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional

from mcp.server.mcpserver import MCPServer
from mkdocs_webmcp.scaffolder import SiteScaffolder
from mkdocs_webmcp.search_engine import SiteSearchEngine


def create_mcp_server(root_dir: str | Path = ".", config_file: str = "mkdocs.yml") -> MCPServer:
    """Create and configure MCPServer with all scaffolded resources, tools, and prompts."""
    scaffolder = SiteScaffolder(root_dir=root_dir, config_file=config_file)
    search_engine = SiteSearchEngine(root_dir=root_dir, scaffolder=scaffolder)

    server = MCPServer(
        name="oleg-nenashev-webmcp",
        version="0.1.0",
        instructions="WebMCP server for Oleg Nenashev's personal site and documentation. Provides resources about Oleg's background, open-source projects, consulting, speaking, and full-text search across documentation."
    )

    # -------------------------------------------------------------------------
    # Resources
    # -------------------------------------------------------------------------

    @server.resource("site://metadata")
    def get_metadata_resource() -> str:
        """Site metadata including description, URLs, and repository details."""
        return json.dumps(scaffolder.get_site_metadata(), indent=2)

    @server.resource("site://navigation")
    def get_navigation_resource() -> str:
        """Full navigation tree from mkdocs.yml."""
        return json.dumps(scaffolder.nav_items, indent=2)

    @server.resource("oleg://profile")
    def get_profile_resource() -> str:
        """Executive summary of Oleg Nenashev, including four hats, bio, and credentials."""
        return json.dumps(scaffolder.get_profile_summary(), indent=2)

    @server.resource("oleg://contacts")
    def get_contacts_resource() -> str:
        """Contact channels: email, Calendly meeting scheduler, and social media handles."""
        return json.dumps(scaffolder.get_contacts_info(), indent=2)

    @server.resource("oleg://projects")
    def get_projects_resource() -> str:
        """Open source projects: Jenkins, Testcontainers, WireMock, WinSW, FaaScinator."""
        return json.dumps(scaffolder.get_projects_info(), indent=2)

    @server.resource("oleg://consulting")
    def get_consulting_resource() -> str:
        """Consulting services, community building, DevRel, DevEx, and testimonials."""
        return json.dumps(scaffolder.get_consulting_info(), indent=2)

    @server.resource("oleg://speaking")
    def get_speaking_resource() -> str:
        """Public speaking profile, topics, and speaker invitation guidelines."""
        return json.dumps(scaffolder.get_speaking_info(), indent=2)

    # Dynamic resource registration for individual pages
    for nav_item in scaffolder.nav_items:
        path = nav_item.get("path")
        if not path or path.startswith("http"):
            continue
        clean_path = path.rstrip(".md")
        uri = f"site://pages/{clean_path}"

        def make_page_handler(page_path: str):
            def handler() -> str:
                page_info = scaffolder.pages_cache.get(page_path, {})
                content = page_info.get("body") or page_info.get("raw_content", "")
                if not content:
                    fp = scaffolder.docs_dir / page_path
                    if fp.exists():
                        content = fp.read_text(encoding="utf-8")
                return content or f"No content available for {page_path}"
            return handler

            register_resource = server.resource(
                uri,
                name=f"Page: {nav_item.get('title', clean_path)}",
                description=f"Documentation page at {path}",
                mime_type="text/markdown"
            )
            register_resource(make_page_handler(path))

    # -------------------------------------------------------------------------
    # Tools
    # -------------------------------------------------------------------------

    @server.tool(
        name="search",
        description="Search documentation, talks, CV, projects, and articles on Oleg Nenashev's site."
    )
    def search_tool(query: str, limit: int = 5) -> str:
        """Execute full-text search across documentation."""
        results = search_engine.search(query=query, limit=limit)
        if not results:
            return f"No results found matching query: '{query}'"

        lines = [f"### Search results for: **{query}**\n"]
        for idx, res in enumerate(results, 1):
            lines.append(f"{idx}. [{res['title']}]({res['url']}) (Score: {res['score']})")
            if res.get("snippet"):
                lines.append(f"   > {res['snippet']}\n")
        return "\n".join(lines)

    @server.tool(
        name="get_profile",
        description="Get Oleg Nenashev's executive profile, 4 hats (Engineer, Community Builder, PM, Consultant), and bio."
    )
    def get_profile_tool() -> str:
        """Retrieve executive profile summary."""
        profile = scaffolder.get_profile_summary()
        return json.dumps(profile, indent=2)

    @server.tool(
        name="get_contacts",
        description="Get direct contact channels (email, Calendly booking link, LinkedIn, GitHub, Bluesky, Mastodon)."
    )
    def get_contacts_tool() -> str:
        """Retrieve contact information."""
        contacts = scaffolder.get_contacts_info()
        return json.dumps(contacts, indent=2)

    @server.tool(
        name="get_page_content",
        description="Get raw markdown text of a specific site page (e.g. 'work/cv.md', 'consulting/README.md', 'contacts.md')."
    )
    def get_page_content_tool(path: str) -> str:
        """Retrieve page markdown content."""
        clean_path = path.strip().lstrip("/")
        if not clean_path.endswith(".md"):
            # Try appending .md or README.md
            candidates = [f"{clean_path}.md", f"{clean_path}/README.md", clean_path]
        else:
            candidates = [clean_path]

        for cand in candidates:
            if cand in scaffolder.pages_cache:
                info = scaffolder.pages_cache[cand]
                return f"# {info.get('title')}\n\n{info.get('body', '')}"
            fp = scaffolder.docs_dir / cand
            if fp.exists():
                return fp.read_text(encoding="utf-8")

        return f"Page not found for path: '{path}'. Use list_resources to view available pages."

    @server.tool(
        name="get_projects",
        description="Get open source projects Oleg maintains or actively contributes to (Jenkins, Testcontainers, WireMock, WinSW, FaaScinator)."
    )
    def get_projects_tool() -> str:
        """Retrieve open source projects details."""
        return json.dumps(scaffolder.get_projects_info(), indent=2)

    @server.tool(
        name="get_consulting_info",
        description="Get consulting and advisory offerings, domains of expertise, client testimonials, and availability."
    )
    def get_consulting_info_tool() -> str:
        """Retrieve consulting and advisory offerings."""
        return json.dumps(scaffolder.get_consulting_info(), indent=2)

    @server.tool(
        name="get_speaking_info",
        description="Get public speaking topics, speaker bio, and conference speaker invitation details."
    )
    def get_speaking_info_tool() -> str:
        """Retrieve public speaking details."""
        return json.dumps(scaffolder.get_speaking_info(), indent=2)

    @server.tool(
        name="list_resources",
        description="List all available WebMCP resources and navigation pages."
    )
    def list_resources_tool() -> str:
        """List all scaffolded resources."""
        res_list = scaffolder.scaffold_resources()
        summary = [{"uri": r["uri"], "name": r["name"], "description": r["description"]} for r in res_list]
        return json.dumps(summary, indent=2)

    # -------------------------------------------------------------------------
    # Prompts
    # -------------------------------------------------------------------------

    @server.prompt(
        name="introduce_oleg",
        description="Generate an introduction for Oleg Nenashev tailored to a specific audience."
    )
    def introduce_oleg_prompt(audience: str, focus_area: str = "") -> str:
        profile = scaffolder.get_profile_summary()
        return (
            f"Please introduce Oleg Nenashev for the following audience: {audience}.\n"
            f"Focus Area / Hat: {focus_area or 'General / All Hats'}\n"
            f"Candidate Profile: {json.dumps(profile, indent=2)}\n"
            "Highlight his relevant accomplishments, open-source maintainership, and how to connect."
        )

    @server.prompt(
        name="consulting_inquiry",
        description="Evaluate a consulting engagement opportunity against Oleg's expertise."
    )
    def consulting_inquiry_prompt(project_description: str) -> str:
        consulting = scaffolder.get_consulting_info()
        contacts = scaffolder.get_contacts_info()
        return (
            f"Evaluate the following consulting request:\n{project_description}\n\n"
            f"Oleg's Consulting Profile:\n{json.dumps(consulting, indent=2)}\n\n"
            f"Contact Details:\n{json.dumps(contacts, indent=2)}\n\n"
            "Provide a breakdown of alignment, suggested engagement model, and next steps."
        )

    return server


def main() -> None:
    """CLI entrypoint to launch WebMCP server."""
    parser = argparse.ArgumentParser(description="WebMCP Server for Oleg Nenashev site")
    parser.add_argument("--config", default="mkdocs.yml", help="Path to mkdocs.yml configuration file")
    parser.add_argument("--root", default=".", help="Workspace root directory")
    parser.add_argument("--transport", choices=["stdio", "sse", "streamable-http"], default="stdio", help="MCP transport type")
    parser.add_argument("--port", type=int, default=8000, help="Port for HTTP/SSE transport")
    parser.add_argument("--host", default="0.0.0.0", help="Host binding for HTTP/SSE transport")
    
    args = parser.parse_args()
    server = create_mcp_server(root_dir=args.root, config_file=args.config)

    if args.transport == "stdio":
        server.run(transport="stdio")
    elif args.transport == "sse":
        server.run(transport="sse", host=args.host, port=args.port)
    elif args.transport == "streamable-http":
        server.run(transport="streamable-http", host=args.host, port=args.port)


if __name__ == "__main__":
    main()
