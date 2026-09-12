/**
 * WebMCP Client & Browser Service
 * Exposes Model Context Protocol (MCP) in the browser for web agents, extensions, and AI assistants.
 * Integrates directly with MkDocs search index (search_index.json) and site resources.
 */

(function () {
  'use strict';

  const MCP_VERSION = '2024-11-05';
  const SERVER_INFO = {
    name: 'oleg-nenashev-webmcp-client',
    version: '0.1.0',
    description: "In-browser WebMCP service for Oleg Nenashev's personal site and documentation."
  };

  class WebMCPService {
    constructor() {
      this.initialized = false;
      this.baseUrl = window.location.origin + window.location.pathname.replace(/\/[^/]*$/, '/');
      this.searchIndex = null;
      this.resources = null;
      this.tools = null;
      this.manifest = null;
      this._initPromise = this._init();
    }

    async _init() {
      try {
        await Promise.allSettled([
          this._loadManifest(),
          this._loadResources(),
          this._loadTools(),
          this._loadSearchIndex()
        ]);
        this.initialized = true;
        this._dispatchReadyEvent();
        this._setupPostMessageListener();
      } catch (err) {
        console.warn('[WebMCP] Initialization warning:', err);
      }
    }

    async _loadManifest() {
      try {
        const res = await fetch(new URL('mcp.json', this.baseUrl).href);
        if (res.ok) {
          this.manifest = await res.json();
        }
      } catch (_) {}
    }

    async _loadResources() {
      try {
        const res = await fetch(new URL('assets/mcp/resources.json', this.baseUrl).href);
        if (res.ok) {
          this.resources = await res.json();
        }
      } catch (_) {}
    }

    async _loadTools() {
      try {
        const res = await fetch(new URL('assets/mcp/tools.json', this.baseUrl).href);
        if (res.ok) {
          this.tools = await res.json();
        }
      } catch (_) {}
    }

    async _loadSearchIndex() {
      try {
        const res = await fetch(new URL('search/search_index.json', this.baseUrl).href);
        if (res.ok) {
          const data = await res.json();
          this.searchIndex = data.docs || data;
        }
      } catch (_) {}
    }

    _dispatchReadyEvent() {
      const event = new CustomEvent('webmcp:ready', {
        detail: {
          server: SERVER_INFO,
          service: this
        }
      });
      window.dispatchEvent(event);
    }

    _setupPostMessageListener() {
      window.addEventListener('message', async (event) => {
        if (!event.data || event.data.jsonrpc !== '2.0') return;
        try {
          const response = await this.handleJsonRpc(event.data);
          if (event.source && response) {
            event.source.postMessage(response, event.origin || '*');
          }
        } catch (err) {
          if (event.source) {
            event.source.postMessage({
              jsonrpc: '2.0',
              id: event.data.id || null,
              error: { code: -32603, message: err.message || 'Internal error' }
            }, event.origin || '*');
          }
        }
      });
    }

    /**
     * Search documentation index.
     * @param {string} query
     * @param {number} limit
     */
    async search(query, limit = 5) {
      if (!this.searchIndex) {
        await this._loadSearchIndex();
      }
      if (!this.searchIndex || !query || !query.trim()) {
        return [];
      }

      const cleanQuery = query.trim().toLowerCase();
      const terms = cleanQuery.split(/\s+/).filter(t => t.length > 1);
      const results = [];

      for (const doc of this.searchIndex) {
        const title = (doc.title || '').toLowerCase();
        const text = (doc.text || '').replace(/<[^>]+>/g, ' ').toLowerCase();
        let score = 0;

        if (title.includes(cleanQuery)) score += 50;
        if (text.includes(cleanQuery)) score += 20;

        for (const term of terms) {
          if (title.includes(term)) score += 15;
          const matches = (text.match(new RegExp(term, 'g')) || []).length;
          if (matches > 0) score += Math.min(matches * 2, 20);
        }

        if (score > 0) {
          const loc = doc.location ? doc.location.replace(/^\//, '') : '';
          const url = new URL(loc, this.baseUrl).href;
          results.push({
            title: doc.title,
            location: doc.location,
            url: url,
            snippet: this._makeSnippet(doc.text || '', terms),
            score: score
          });
        }
      }

      results.sort((a, b) => b.score - a.score);
      return results.slice(0, limit);
    }

    _makeSnippet(text, terms, maxLen = 200) {
      const clean = text.replace(/<[^>]+>/g, ' ').replace(/\s+/g, ' ').trim();
      const lower = clean.toLowerCase();
      let firstPos = -1;
      for (const term of terms) {
        const pos = lower.indexOf(term);
        if (pos !== -1 && (firstPos === -1 || pos < firstPos)) {
          firstPos = pos;
        }
      }
      if (firstPos === -1) return clean.slice(0, maxLen);
      const start = Math.max(0, firstPos - 50);
      const end = Math.min(clean.length, firstPos + maxLen - 50);
      return (start > 0 ? '...' : '') + clean.slice(start, end) + (end < clean.length ? '...' : '');
    }

    /**
     * Get all available resources.
     */
    async getResources() {
      if (!this.resources) {
        await this._loadResources();
      }
      return this.resources || [];
    }

    /**
     * Read a specific resource by URI.
     */
    async readResource(uri) {
      const all = await this.getResources();
      const res = all.find(r => r.uri === uri);
      if (res) return res;
      throw new Error(`Resource not found: ${uri}`);
    }

    /**
     * Get list of tools.
     */
    async getTools() {
      if (!this.tools) {
        await this._loadTools();
      }
      return this.tools || [];
    }

    /**
     * Execute a tool by name.
     */
    async callTool(name, args = {}) {
      switch (name) {
        case 'search':
          const results = await this.search(args.query || '', args.limit || 5);
          return {
            content: [
              {
                type: 'text',
                text: results.length ? JSON.stringify(results, null, 2) : `No results for "${args.query}"`
              }
            ]
          };

        case 'get_profile':
        case 'get_contacts':
        case 'get_projects':
        case 'get_consulting_info':
        case 'get_speaking_info':
          const uriMap = {
            get_profile: 'oleg://profile',
            get_contacts: 'oleg://contacts',
            get_projects: 'oleg://projects',
            get_consulting_info: 'oleg://consulting',
            get_speaking_info: 'oleg://speaking'
          };
          const r = await this.readResource(uriMap[name]);
          return {
            content: [{ type: 'text', text: typeof r.content === 'string' ? r.content : JSON.stringify(r.content, null, 2) }]
          };

        case 'get_page_content':
          const cleanPath = (args.path || '').replace(/^\//, '').replace(/\.md$/, '');
          const pageRes = (await this.getResources()).find(item => item.uri === `site://pages/${cleanPath}` || item.uri.endsWith(cleanPath));
          if (pageRes) {
            return {
              content: [{ type: 'text', text: typeof pageRes.content === 'string' ? pageRes.content : JSON.stringify(pageRes.content, null, 2) }]
            };
          }
          throw new Error(`Page not found: ${args.path}`);

        case 'list_resources':
          const resList = await this.getResources();
          return {
            content: [{ type: 'text', text: JSON.stringify(resList.map(item => ({ uri: item.uri, name: item.name, description: item.description })), null, 2) }]
          };

        default:
          throw new Error(`Unknown tool: ${name}`);
      }
    }

    /**
     * Standard JSON-RPC 2.0 message handler for WebMCP protocol.
     */
    async handleJsonRpc(request) {
      const { id, method, params } = request;

      switch (method) {
        case 'initialize':
          return {
            jsonrpc: '2.0',
            id,
            result: {
              protocolVersion: MCP_VERSION,
              capabilities: {
                resources: { subscribe: false, listChanged: false },
                tools: { listChanged: false },
                prompts: { listChanged: false }
              },
              serverInfo: SERVER_INFO
            }
          };

        case 'resources/list':
          const resources = await this.getResources();
          return {
            jsonrpc: '2.0',
            id,
            result: {
              resources: resources.map(r => ({
                uri: r.uri,
                name: r.name,
                description: r.description,
                mimeType: r.mimeType || 'application/json'
              }))
            }
          };

        case 'resources/read':
          const targetUri = params?.uri;
          const resource = await this.readResource(targetUri);
          return {
            jsonrpc: '2.0',
            id,
            result: {
              contents: [
                {
                  uri: resource.uri,
                  mimeType: resource.mimeType || 'application/json',
                  text: typeof resource.content === 'string' ? resource.content : JSON.stringify(resource.content, null, 2)
                }
              ]
            }
          };

        case 'tools/list':
          const tools = await this.getTools();
          return {
            jsonrpc: '2.0',
            id,
            result: { tools }
          };

        case 'tools/call':
          const toolName = params?.name;
          const toolArgs = params?.arguments || {};
          const toolResult = await this.callTool(toolName, toolArgs);
          return {
            jsonrpc: '2.0',
            id,
            result: toolResult
          };

        case 'ping':
          return { jsonrpc: '2.0', id, result: {} };

        default:
          return {
            jsonrpc: '2.0',
            id,
            error: { code: -32601, message: `Method not found: ${method}` }
          };
      }
    }
  }

  // Register globally on window
  const webmcp = new WebMCPService();
  window.WebMCP = webmcp;

  // Integrate with experimental navigator.modelContext if present
  if (typeof navigator !== 'undefined') {
    navigator.modelContext = navigator.modelContext || webmcp;
  }
})();
