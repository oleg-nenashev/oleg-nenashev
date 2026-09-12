"""
Scaffolder module for extracting MkDocs metadata and navbar structure
into Model Context Protocol (MCP) resources, tools, and prompts.
"""

from __future__ import annotations
import os
import re
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple
import yaml


class SafeEnvLoader(yaml.SafeLoader):
    """YAML loader that ignores or handles !ENV and !!python tags gracefully."""
    pass


def _env_constructor(loader: yaml.Loader, node: yaml.Node) -> Any:
    """Handle !ENV [VAR_NAME, default] or !ENV VAR_NAME."""
    if isinstance(node, yaml.SequenceNode):
        seq = loader.construct_sequence(node)
        var_name = seq[0] if seq else ""
        default_val = seq[1] if len(seq) > 1 else None
        return os.environ.get(var_name, default_val)
    elif isinstance(node, yaml.ScalarNode):
        var_name = loader.construct_scalar(node)
        return os.environ.get(var_name, "")
    return None


def _ignore_python_tag_constructor(loader: yaml.Loader, tag_suffix: str, node: yaml.Node) -> str:
    """Ignore python name tags such as !!python/name:material..."""
    if isinstance(node, yaml.ScalarNode):
        return loader.construct_scalar(node)
    return ""


SafeEnvLoader.add_constructor("!ENV", _env_constructor)
SafeEnvLoader.add_multi_constructor("tag:yaml.org,2002:python/", _ignore_python_tag_constructor)
SafeEnvLoader.add_multi_constructor("!python/", _ignore_python_tag_constructor)


def parse_frontmatter(content: str) -> Tuple[Dict[str, Any], str]:
    """Extract YAML frontmatter and body from Markdown text."""
    if content.startswith("---"):
        parts = re.split(r"^---\s*$", content, maxsplit=2, flags=re.MULTILINE)
        if len(parts) >= 3:
            try:
                fm = yaml.load(parts[1], Loader=SafeEnvLoader) or {}
                body = parts[2].strip()
                return fm, body
            except Exception:
                pass
    return {}, content.strip()


def flatten_nav(nav_list: List[Any], prefix: str = "") -> List[Dict[str, Any]]:
    """Flatten nested MkDocs nav items into a list of {title, path, category} items."""
    flattened: List[Dict[str, Any]] = []
    
    for item in nav_list:
        if isinstance(item, dict):
            for title, target in item.items():
                if isinstance(target, list):
                    sub_prefix = f"{prefix} > {title}" if prefix else title
                    flattened.extend(flatten_nav(target, sub_prefix))
                elif isinstance(target, str):
                    flattened.append({
                        "title": title,
                        "path": target,
                        "category": prefix or "General"
                    })
        elif isinstance(item, str):
            flattened.append({
                "title": Path(item).stem.replace("-", " ").title(),
                "path": item,
                "category": prefix or "General"
            })
    return flattened


class SiteScaffolder:
    """Parses MkDocs project configuration and documentation files to scaffold MCP resources and tools."""

    def __init__(self, root_dir: str | Path = ".", config_file: str = "mkdocs.yml"):
        self.root_dir = Path(root_dir).resolve()
        self.config_path = (self.root_dir / config_file).resolve()
        self.config: Dict[str, Any] = {}
        self.nav_items: List[Dict[str, Any]] = []
        self.pages_cache: Dict[str, Dict[str, Any]] = {}
        self.reload()

    def reload(self) -> None:
        """Reload configuration and parse markdown files."""
        if self.config_path.exists():
            with open(self.config_path, "r", encoding="utf-8") as f:
                content = f.read()
                self.config = yaml.load(content, Loader=SafeEnvLoader) or {}
        else:
            self.config = {}

        nav_config = self.config.get("nav", [])
        self.nav_items = flatten_nav(nav_config)
        self.docs_dir = self.root_dir / self.config.get("docs_dir", ".")
        self._load_pages()

    def _load_pages(self) -> None:
        """Pre-read and parse all docs directory markdown files."""
        self.pages_cache = {}
        if not self.docs_dir.exists():
            return

        for root, _, files in os.walk(self.docs_dir):
            for file in files:
                if file.endswith(".md"):
                    full_path = Path(root) / file
                    rel_path = str(full_path.relative_to(self.docs_dir)).replace("\\", "/")
                    try:
                        with open(full_path, "r", encoding="utf-8") as f:
                            raw = f.read()
                        fm, body = parse_frontmatter(raw)
                        self.pages_cache[rel_path] = {
                            "relative_path": rel_path,
                            "frontmatter": fm,
                            "title": fm.get("title") or self._extract_first_h1(body) or rel_path,
                            "description": fm.get("description", "").strip(),
                            "raw_content": raw,
                            "body": body,
                        }
                    except Exception:
                        pass

    @staticmethod
    def _extract_first_h1(markdown: str) -> Optional[str]:
        """Extract first # Heading 1 from markdown."""
        for line in markdown.splitlines():
            line = line.strip()
            if line.startswith("# "):
                return line[2:].strip()
        return None

    def get_site_metadata(self) -> Dict[str, Any]:
        """Return general site metadata from mkdocs.yml."""
        return {
            "site_name": self.config.get("site_name", "Oleg Nenashev"),
            "site_description": self.config.get("site_description", "").strip(),
            "site_url": self.config.get("site_url", "https://oleg-nenashev.github.io/oleg-nenashev"),
            "repo_url": self.config.get("repo_url", "https://github.com/oleg-nenashev/oleg-nenashev"),
            "repo_name": self.config.get("repo_name", "GitHub Repo"),
            "copyright": self.config.get("copyright", "Oleg Nenashev"),
            "total_nav_items": len(self.nav_items),
            "nav_categories": list(dict.fromkeys(item["category"] for item in self.nav_items if item.get("category"))),
        }

    def get_profile_summary(self) -> Dict[str, Any]:
        """Extract structured profile summary about Oleg Nenashev."""
        index_data = self.pages_cache.get("index.md", {})
        contacts_data = self.pages_cache.get("contacts.md", {})
        work_data = self.pages_cache.get("work/README.md", {})
        
        hats = [
            {
                "name": "Engineer",
                "focus": "Developer tools, automation, Jenkins, Testcontainers, WireMock, Embedded & C/C++",
                "links": ["/work/cv.md", "/open-source/projects/README.md", "/open-source/organizations/README.md"]
            },
            {
                "name": "Community Builder",
                "focus": "Open source community leadership, DevRel, governance, CD Foundation TOC chair / board member, InnerSource",
                "links": ["/work/community-building.md", "/open-source/organizations/README.md", "/speaking/README.md"]
            },
            {
                "name": "PM & Project Lead",
                "focus": "Developer experience projects, ecosystem partnerships, agile product ownership, open source programs",
                "links": ["/open-source/projects/README.md"]
            },
            {
                "name": "Consultant",
                "focus": "Independent consultant in developer productivity, open source strategy, community and ecosystem growth, DevRel",
                "links": ["/consulting/README.md"]
            }
        ]

        return {
            "name": "Oleg Nenashev",
            "tagline": "Open source community builder, DevRel consultant, and developer tools engineer based in Switzerland.",
            "credentials": ["Jenkins core maintainer", "CNCF Ambassador", "Testcontainers Champion", "PhD in Electronics & EDA"],
            "hats": hats,
            "tags": ["#OpenSource", "#DevEx", "#DevOps", "#Java", "#Embedded", "#AI", "#Sustainability", "#Mentor", "#Volunteer"],
            "bio": index_data.get("description") or self.config.get("site_description", ""),
            "current_role": "Lead Developer Advocate at Gradle, Inc. (part-time) & Independent Consultant / Open Source Leader",
            "contact_email": "o.v.nenashev@gmail.com",
            "calendly": "https://calendly.com/onenashev/",
            "social": {
                "linkedin": "https://www.linkedin.com/in/onenashev/",
                "github": "https://github.com/oleg-nenashev",
                "bluesky": "https://bsky.app/profile/asciidwarf.bsky.social",
                "mastodon": "https://fosstodon.org/@onenashev",
                "twitter": "https://twitter.com/oleg_nenashev",
                "sponsors": "https://github.com/sponsors/oleg-nenashev"
            }
        }

    def get_contacts_info(self) -> Dict[str, Any]:
        """Extract structured contact information."""
        return {
            "name": "Oleg Nenashev",
            "email": "o.v.nenashev@gmail.com",
            "meeting_scheduler": "https://calendly.com/onenashev/",
            "location": "Switzerland",
            "social_links": [
                {"platform": "LinkedIn", "url": "https://www.linkedin.com/in/onenashev/", "handle": "@onenashev"},
                {"platform": "GitHub", "url": "https://github.com/oleg-nenashev", "handle": "@oleg-nenashev"},
                {"platform": "Bluesky", "url": "https://bsky.app/profile/asciidwarf.bsky.social", "handle": "@asciidwarf.bsky.social"},
                {"platform": "Mastodon", "url": "https://fosstodon.org/@onenashev", "handle": "@onenashev@fosstodon.org"},
                {"platform": "Twitter / X", "url": "https://twitter.com/oleg_nenashev", "handle": "@oleg_nenashev"},
                {"platform": "GitHub Sponsors", "url": "https://github.com/sponsors/oleg-nenashev", "handle": "@oleg-nenashev"}
            ],
            "availability": "Open to consulting, advisory, speaking engagements, and pro-bono support for nonprofits."
        }

    def get_projects_info(self) -> List[Dict[str, Any]]:
        """Return structured information about open source projects."""
        return [
            {
                "name": "Jenkins",
                "url": "https://www.jenkins.io/",
                "roles": ["Core Maintainer", "Board Member", "Event Officer", "Community Builder"],
                "description": "Continuous integration and automation server. Active contributor since 2012, focused on community growth, Jenkins security, and project governance."
            },
            {
                "name": "Testcontainers",
                "url": "https://testcontainers.com/",
                "roles": ["Testcontainers Champion", "Creator of Testcontainers for C/C++"],
                "description": "Modern integration testing library with lightweight, throwaway instances of databases, message brokers, and web browsers in Docker containers."
            },
            {
                "name": "WireMock",
                "url": "https://wiremock.org/",
                "roles": ["Co-maintainer of WireMock core", "DevRel & Community lead"],
                "description": "Flexible open source tool for API mocking and integration testing."
            },
            {
                "name": "Windows Service Wrapper (WinSW)",
                "url": "https://github.com/winsw/winsw",
                "roles": ["Co-maintainer"],
                "description": "Wraps executables as Windows Services, widely used by Jenkins and other enterprise tools."
            },
            {
                "name": "FaaScinator",
                "url": "https://github.com/oleg-nenashev/FaaScinator",
                "roles": ["Creator & Maintainer"],
                "description": "Converts Java CLI applications to FaaS containers and OpenFaaS templates."
            }
        ]

    def get_consulting_info(self) -> Dict[str, Any]:
        """Return structured consulting offerings and areas."""
        consulting_data = self.pages_cache.get("consulting/README.md", {})
        return {
            "title": "Consulting and Advisory Services",
            "experience": "15+ years of experience in DevOps, developer tools, automation, community building, and DevRel.",
            "availability": "Open to new consulting projects: full-time, fractional, advisory roles, and pro-bono for nonprofits.",
            "areas": [
                {
                    "domain": "Community Building & Governance",
                    "offerings": [
                        "Building and growing open source communities and ecosystems",
                        "Organizing and hosting meetups, webinars, and hackathons",
                        "Setting up Community Analytics (GrimoireLab, LFX Insights, Common Room)",
                        "OSPO setup, governance frameworks, and technical partnerships"
                    ]
                },
                {
                    "domain": "Developer Relations & Advocacy",
                    "offerings": [
                        "Developer Advocacy for developer tools and open source projects",
                        "DevRel strategy and team development",
                        "Technical documentation at scale (AsciiDoc, MkDocs, Hugo)",
                        "Workshops, conference talks, and booth advocacy"
                    ]
                },
                {
                    "domain": "Automation & Developer Productivity",
                    "offerings": [
                        "CI/CD pipeline design and scaling",
                        "Integration testing architecture (Testcontainers, WireMock)",
                        "Java, embedded systems, and cloud native tooling"
                    ]
                }
            ],
            "testimonial": "Quadrupled community GitHub contributions to WireMock in 9 months as Software Developer Advocate Consultant."
        }

    def get_speaking_info(self) -> Dict[str, Any]:
        """Return structured public speaking profile and guidelines."""
        return {
            "speaker": "Oleg Nenashev",
            "profile_url": "https://oleg-nenashev.github.io/oleg-nenashev/speaking/",
            "topics": [
                "Open Source Community Building & Governance",
                "Developer Productivity & DevEx",
                "Modern Integration Testing with Testcontainers and WireMock",
                "CI/CD, Jenkins pipelines at scale, and Cloud Native DevOps",
                "InnerSource & Open Source Culture in Enterprise"
            ],
            "invite_guidelines": "Available for keynote, breakout sessions, workshops, and panel discussions. Contact via email or Calendly."
        }

    def scaffold_resources(self) -> List[Dict[str, Any]]:
        """Generate MCP resource definitions."""
        resources: List[Dict[str, Any]] = [
            {
                "uri": "site://metadata",
                "name": "Site Metadata",
                "description": "General site information, site description, links, and copyright",
                "mimeType": "application/json",
                "content": self.get_site_metadata()
            },
            {
                "uri": "site://navigation",
                "name": "Navigation Structure",
                "description": "Full navigation bar hierarchy and links from mkdocs.yml",
                "mimeType": "application/json",
                "content": self.nav_items
            },
            {
                "uri": "oleg://profile",
                "name": "Oleg Nenashev - Executive Profile",
                "description": "Summary of Oleg Nenashev: roles, 4 hats (Engineer, Community Builder, PM, Consultant), bio, credentials, and social channels",
                "mimeType": "application/json",
                "content": self.get_profile_summary()
            },
            {
                "uri": "oleg://contacts",
                "name": "Oleg Nenashev - Contact Information",
                "description": "Direct email, Calendly meeting scheduler, and social media channels",
                "mimeType": "application/json",
                "content": self.get_contacts_info()
            },
            {
                "uri": "oleg://projects",
                "name": "Oleg Nenashev - Open Source Projects",
                "description": "Key open source projects (Jenkins, Testcontainers, WireMock, WinSW, FaaScinator)",
                "mimeType": "application/json",
                "content": self.get_projects_info()
            },
            {
                "uri": "oleg://consulting",
                "name": "Oleg Nenashev - Consulting & Advisory",
                "description": "Consulting areas (Community building, DevRel, DevEx, Automation), availability, and testimonials",
                "mimeType": "application/json",
                "content": self.get_consulting_info()
            },
            {
                "uri": "oleg://speaking",
                "name": "Oleg Nenashev - Public Speaking Profile",
                "description": "Public speaking topics, conference talks, and invitation guidelines",
                "mimeType": "application/json",
                "content": self.get_speaking_info()
            }
        ]

        # Scaffold each page in nav as a resource
        for item in self.nav_items:
            path = item.get("path")
            if not path or path.startswith("http"):
                continue
            
            page_info = self.pages_cache.get(path)
            content_text = page_info.get("body", "") if page_info else ""
            if not content_text and (self.docs_dir / path).exists():
                try:
                    with open(self.docs_dir / path, "r", encoding="utf-8") as pf:
                        _, content_text = parse_frontmatter(pf.read())
                except Exception:
                    pass

            clean_uri = f"site://pages/{path.rstrip('.md')}"
            resources.append({
                "uri": clean_uri,
                "name": f"Page: {item.get('title', path)}",
                "description": f"Documentation page under category '{item.get('category', 'General')}' at {path}",
                "mimeType": "text/markdown",
                "content": content_text or f"# {item.get('title')}\n\nPath: {path}"
            })

        return resources

    def scaffold_tools(self) -> List[Dict[str, Any]]:
        """Generate MCP tool schemas."""
        return [
            {
                "name": "search",
                "description": "Full-text search across all documentation, projects, talks, and CV of Oleg Nenashev.",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "query": {
                            "type": "string",
                            "description": "Search query keywords (e.g. 'Jenkins', 'consulting', 'DevRel', 'Testcontainers', 'talks')"
                        },
                        "limit": {
                            "type": "integer",
                            "description": "Maximum number of search results to return (default: 5)",
                            "default": 5
                        }
                    },
                    "required": ["query"]
                }
            },
            {
                "name": "get_profile",
                "description": "Get executive summary, background, four hats (Engineer, Community Builder, PM, Consultant), and key links for Oleg Nenashev.",
                "inputSchema": {
                    "type": "object",
                    "properties": {}
                }
            },
            {
                "name": "get_contacts",
                "description": "Get direct contact details including email, Calendly meeting booking, and social media channels.",
                "inputSchema": {
                    "type": "object",
                    "properties": {}
                }
            },
            {
                "name": "get_page_content",
                "description": "Get full markdown content of a documentation page by relative path (e.g., 'work/cv.md', 'consulting/README.md', 'speaking/talks.md').",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "path": {
                            "type": "string",
                            "description": "Path to page (e.g. 'index.md', 'work/cv.md', 'contacts.md', 'open-source/projects/README.md')"
                        }
                    },
                    "required": ["path"]
                }
            },
            {
                "name": "get_projects",
                "description": "Get list of open-source projects Oleg contributes to or maintains (Jenkins, Testcontainers, WireMock, etc.).",
                "inputSchema": {
                    "type": "object",
                    "properties": {}
                }
            },
            {
                "name": "get_consulting_info",
                "description": "Get consulting offerings, areas of expertise, availability, and client testimonials.",
                "inputSchema": {
                    "type": "object",
                    "properties": {}
                }
            },
            {
                "name": "get_speaking_info",
                "description": "Get public speaking topics, speaker profile, and guidelines for inviting Oleg to speak at an event.",
                "inputSchema": {
                    "type": "object",
                    "properties": {}
                }
            },
            {
                "name": "list_resources",
                "description": "List all MCP resources and pages scaffolded from the site navigation.",
                "inputSchema": {
                    "type": "object",
                    "properties": {}
                }
            }
        ]

    def scaffold_prompts(self) -> List[Dict[str, Any]]:
        """Generate MCP prompt templates."""
        return [
            {
                "name": "introduce_oleg",
                "description": "Draft an introduction for Oleg Nenashev customized for a specific audience (conference, client, community).",
                "arguments": [
                    {
                        "name": "audience",
                        "description": "Target audience (e.g., 'DevOps conference', 'consulting client', 'open source meetup')",
                        "required": True
                    },
                    {
                        "name": "focus_area",
                        "description": "Area to highlight (e.g., 'Engineer', 'Community Builder', 'DevRel', 'Jenkins/Testcontainers')",
                        "required": False
                    }
                ]
            },
            {
                "name": "consulting_inquiry",
                "description": "Analyze a consulting opportunity against Oleg's expertise and availability.",
                "arguments": [
                    {
                        "name": "project_description",
                        "description": "Brief description of the proposed project, problem, or consulting need",
                        "required": True
                    }
                ]
            }
        ]
