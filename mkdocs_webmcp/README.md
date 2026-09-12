# MkDocs WebMCP Plugin & Server

`mkdocs-webmcp` is a Model Context Protocol (MCP) plugin and server for MkDocs documentation and static sites. It dynamically scaffolds MCP resources, tools, prompts, and search integration directly from `mkdocs.yml` metadata and navigation structure.

---

## 🚀 Features

- **Metadata & Navigation Scaffolding**: Automatically generates MCP resources for site metadata, navigation hierarchy, and page content from `mkdocs.yml`.
- **Full-Text Search Tool**: Integrates with the MkDocs search index (`search_index.json`) and raw markdown to provide ranked full-text search with context snippets.
- **Rich Structured Entities**: Exposes dedicated resources and tools for executive profiles, contact info, open-source projects, consulting offerings, and public speaking.
- **Multi-Transport Server**: Run as a standalone MCP server over `stdio`, `sse`, or `streamable-http`.
- **In-Browser WebMCP Client**: Injects `assets/js/webmcp.js` into built pages, providing `window.WebMCP` with full JSON-RPC 2.0 message handling for web agents and browser extensions.
- **Discovery Manifests**: Generates `mcp.json` and `.well-known/mcp.json` along with autodiscovery `<link rel="mcp-server">` HTML tags.

---

## 📦 Quickstart

### 1. Installation

Install the package in your Python environment:

```bash
# In the workspace repository
pip install -e .
```

### 2. Enable in `mkdocs.yml`

Add `webmcp` to the `plugins` section of your `mkdocs.yml`:

```yaml
plugins:
  - search
  - webmcp:
      enabled: true
      export_manifest: true
      export_resources: true
      export_tools: true
      inject_client: true
```

### 3. Build Documentation

Run standard MkDocs build or dev server:

```bash
mkdocs build
# or
mkdocs serve
```

During build, the plugin generates:
- `_site/mcp.json` and `_site/.well-known/mcp.json`
- `_site/assets/mcp/resources.json`, `tools.json`, `prompts.json`
- `_site/assets/js/webmcp.js`

---

## 🛠️ Using the MCP Server

### Running via Command Line

The server supports `stdio` (default), `sse`, and `streamable-http` transports:

```bash
# Standard I/O (for IDEs / CLI tools)
webmcp-server --transport stdio

# SSE transport (for web clients & remote MCP proxies)
webmcp-server --transport sse --host 0.0.0.0 --port 8000

# Streamable HTTP transport
webmcp-server --transport streamable-http --host 0.0.0.0 --port 8000
```

You can also run directly with Python:

```bash
python -m mkdocs_webmcp.server --config mkdocs.yml --transport stdio
```

---

## 💻 Integration with MCP Clients

### VS Code Configuration

Add the server to `.vscode/mcp.json`:

```json
{
  "servers": {
    "webmcp": {
      "command": "python",
      "args": [
        "-m",
        "mkdocs_webmcp.server"
      ]
    }
  }
}
```

### Claude Desktop Configuration

Add to your `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "oleg-nenashev-webmcp": {
      "command": "python",
      "args": [
        "-m",
        "mkdocs_webmcp.server",
        "--root",
        "/path/to/oleg-nenashev"
      ]
    }
  }
}
```

---

## 🌐 In-Browser WebMCP Usage

Built HTML pages include the WebMCP client script automatically. Web agents and extensions can interact with `window.WebMCP` or listen to `window` postMessage events:

```javascript
// Check availability
window.addEventListener('webmcp:ready', (event) => {
  console.log('WebMCP ready:', event.detail.server);
});

// Direct Tool Call
const searchResults = await window.WebMCP.callTool('search', {
  query: 'Jenkins',
  limit: 5
});

// JSON-RPC 2.0 Request
const rpcResponse = await window.WebMCP.handleJsonRpc({
  jsonrpc: '2.0',
  id: 1,
  method: 'tools/call',
  params: {
    name: 'get_profile',
    arguments: {}
  }
});
```

---

## 📚 Resources & Tools Reference

### Resources
- `site://metadata`: Site name, description, URLs, and repository details.
- `site://navigation`: Complete navigation hierarchy from `mkdocs.yml`.
- `oleg://profile`: Executive summary, 4 hats (Engineer, Community Builder, PM, Consultant), bio, credentials.
- `oleg://contacts`: Direct email, Calendly meeting link, social media channels.
- `oleg://projects`: Open-source projects (Jenkins, Testcontainers, WireMock, WinSW, FaaScinator).
- `oleg://consulting`: Consulting domains, experience, availability, client testimonials.
- `oleg://speaking`: Speaker bio, conference topics, speaker invitation guidelines.
- `site://pages/{path}`: Markdown content for individual documentation pages.

### Tools
- `search(query: str, limit: int = 5)`: Full-text search across documentation and CV.
- `get_profile()`: Return executive profile and hat summaries as JSON.
- `get_contacts()`: Return contact details, social links, and scheduling links.
- `get_page_content(path: str)`: Fetch markdown content for a given page.
- `get_projects()`: Return details for open-source projects.
- `get_consulting_info()`: Return consulting offerings and availability.
- `get_speaking_info()`: Return public speaking details and guidelines.
- `list_resources()`: List all scaffolded MCP resources.

### Prompts
- `introduce_oleg(audience: str, focus_area: str = "")`: Generate an audience-tailored introduction.
- `consulting_inquiry(project_description: str)`: Evaluate consulting opportunities against Oleg's expertise.

---

## ⚙️ Plugin Configuration Options

In `mkdocs.yml`:

| Option | Type | Default | Description |
| --- | --- | --- | --- |
| `enabled` | `bool` | `true` | Enable or disable the WebMCP plugin |
| `site_url` | `str` | `""` | Base site URL override for manifests |
| `export_manifest` | `bool` | `true` | Generate `mcp.json` and `.well-known/mcp.json` |
| `export_resources` | `bool` | `true` | Export `assets/mcp/resources.json` |
| `export_tools` | `bool` | `true` | Export `assets/mcp/tools.json` |
| `inject_client` | `bool` | `true` | Include `webmcp.js` in site JavaScript |

---

## 🧪 Testing

Run test suite with `pytest`:

```bash
pytest
```
