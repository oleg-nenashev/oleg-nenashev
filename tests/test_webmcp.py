"""
Test suite for WebMCP plugin, scaffolder, search engine, and server.
"""

import json
import pytest
from pathlib import Path

from mkdocs_webmcp.scaffolder import SiteScaffolder
from mkdocs_webmcp.search_engine import SiteSearchEngine
from mkdocs_webmcp.server import create_mcp_server


def test_scaffolder_metadata():
    scaffolder = SiteScaffolder(root_dir=".")
    meta = scaffolder.get_site_metadata()
    assert meta["site_name"] == "Oleg Nenashev"
    assert "Jenkins" in meta["site_description"] or "community" in meta["site_description"].lower()
    assert len(scaffolder.nav_items) > 0


def test_scaffolder_profile_and_hats():
    scaffolder = SiteScaffolder(root_dir=".")
    profile = scaffolder.get_profile_summary()
    assert profile["name"] == "Oleg Nenashev"
    assert len(profile["hats"]) == 4
    hat_names = [h["name"] for h in profile["hats"]]
    assert "Engineer" in hat_names
    assert "Community Builder" in hat_names
    assert "PM & Project Lead" in hat_names
    assert "Consultant" in hat_names


def test_scaffolder_contacts():
    scaffolder = SiteScaffolder(root_dir=".")
    contacts = scaffolder.get_contacts_info()
    assert contacts["email"] == "o.v.nenashev@gmail.com"
    assert "calendly.com" in contacts["meeting_scheduler"]
    assert any(s["platform"] == "LinkedIn" for s in contacts["social_links"])
    assert any(s["platform"] == "GitHub" for s in contacts["social_links"])


def test_scaffolder_resources_and_tools():
    scaffolder = SiteScaffolder(root_dir=".")
    resources = scaffolder.scaffold_resources()
    tools = scaffolder.scaffold_tools()
    
    resource_uris = [r["uri"] for r in resources]
    assert "site://metadata" in resource_uris
    assert "site://navigation" in resource_uris
    assert "oleg://profile" in resource_uris
    assert "oleg://contacts" in resource_uris
    assert "oleg://projects" in resource_uris
    assert "oleg://consulting" in resource_uris
    assert "oleg://speaking" in resource_uris
    assert any(uri.startswith("site://pages/") for uri in resource_uris)

    tool_names = [t["name"] for t in tools]
    assert "search" in tool_names
    assert "get_profile" in tool_names
    assert "get_contacts" in tool_names
    assert "get_page_content" in tool_names
    assert "get_projects" in tool_names
    assert "get_consulting_info" in tool_names
    assert "get_speaking_info" in tool_names
    assert "list_resources" in tool_names


def test_search_engine():
    search_engine = SiteSearchEngine(root_dir=".")
    
    # Test search for Jenkins
    jenkins_res = search_engine.search("Jenkins", limit=5)
    assert len(jenkins_res) > 0
    assert any("Jenkins" in r["title"] or "Jenkins" in r["snippet"] or "jenkins" in r["url"] for r in jenkins_res)

    # Test search for consulting
    consulting_res = search_engine.search("consulting", limit=5)
    assert len(consulting_res) > 0

    # Test search for Testcontainers
    testcontainers_res = search_engine.search("Testcontainers", limit=5)
    assert len(testcontainers_res) > 0


def test_mcp_server_initialization():
    server = create_mcp_server(root_dir=".")
    assert server.name == "oleg-nenashev-webmcp"
    assert server.version == "0.1.0"


@pytest.mark.anyio
async def test_mcp_server_tools_and_prompts():
    server = create_mcp_server(root_dir=".")
    
    # Test tool listing
    tools = await server.list_tools()
    tool_names = [t.name for t in tools]
    assert "search" in tool_names
    assert "get_profile" in tool_names
    assert "get_contacts" in tool_names
    assert "get_page_content" in tool_names

    # Test calling search tool
    search_result = await server.call_tool("search", {"query": "Jenkins", "limit": 3})
    assert len(search_result.content) > 0
    assert "Jenkins" in search_result.content[0].text

    # Test calling get_profile tool
    profile_result = await server.call_tool("get_profile", {})
    assert len(profile_result.content) > 0
    profile_data = json.loads(profile_result.content[0].text)
    assert profile_data["name"] == "Oleg Nenashev"

    # Test calling get_contacts tool
    contacts_result = await server.call_tool("get_contacts", {})
    assert len(contacts_result.content) > 0
    contacts_data = json.loads(contacts_result.content[0].text)
    assert contacts_data["email"] == "o.v.nenashev@gmail.com"

    # Test calling get_page_content tool
    page_result = await server.call_tool("get_page_content", {"path": "contacts.md"})
    assert len(page_result.content) > 0
    assert "Contacts" in page_result.content[0].text or "E-mail" in page_result.content[0].text

    # Test prompt listing and rendering
    prompts = await server.list_prompts()
    prompt_names = [p.name for p in prompts]
    assert "introduce_oleg" in prompt_names

    prompt_res = await server.get_prompt("introduce_oleg", {"audience": "DevOps Summit", "focus_area": "Community Builder"})
    assert len(prompt_res.messages) > 0
    assert "DevOps Summit" in prompt_res.messages[0].content.text


def test_generated_mcp_manifest():
    site_dir = Path("_site")
    mcp_file = site_dir / "mcp.json"
    well_known = site_dir / ".well-known" / "mcp.json"
    resources_file = site_dir / "assets" / "mcp" / "resources.json"
    tools_file = site_dir / "assets" / "mcp" / "tools.json"
    client_js = site_dir / "assets" / "js" / "webmcp.js"

    assert mcp_file.exists()
    assert well_known.exists()
    assert resources_file.exists()
    assert tools_file.exists()
    assert client_js.exists()

    data = json.loads(mcp_file.read_text(encoding="utf-8"))
    assert data["serverInfo"]["name"] == "oleg-nenashev-webmcp"
    assert len(data["resources"]) > 0
    assert len(data["tools"]) > 0
