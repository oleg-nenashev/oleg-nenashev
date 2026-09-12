"""
Search engine integrating with MkDocs search index and raw documentation files.
"""

from __future__ import annotations
import json
import os
import re
from pathlib import Path
from typing import Any, Dict, List, Optional
from mkdocs_webmcp.scaffolder import SiteScaffolder


class SiteSearchEngine:
    """Provides full-text search capabilities over MkDocs documentation and generated search_index.json."""

    def __init__(self, root_dir: str | Path = ".", site_dir: str = "_site", scaffolder: Optional[SiteScaffolder] = None):
        self.root_dir = Path(root_dir).resolve()
        self.site_dir = (self.root_dir / site_dir).resolve()
        self.search_index_path = self.site_dir / "search" / "search_index.json"
        self.scaffolder = scaffolder or SiteScaffolder(root_dir=self.root_dir)
        self._index_data: Optional[List[Dict[str, Any]]] = None

    def _load_search_index(self) -> List[Dict[str, Any]]:
        """Load search_index.json if available, otherwise build an in-memory index from scaffolder."""
        if self.search_index_path.exists():
            try:
                with open(self.search_index_path, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    if isinstance(data, dict) and "docs" in data:
                        return data["docs"]
                    elif isinstance(data, list):
                        return data
            except Exception:
                pass

        # In-memory index fallback
        in_memory_docs: List[Dict[str, Any]] = []
        for path, page in self.scaffolder.pages_cache.items():
            in_memory_docs.append({
                "location": path.replace(".md", "/").replace("README/", ""),
                "title": page.get("title", path),
                "text": page.get("body", "")
            })
        return in_memory_docs

    def search(self, query: str, limit: int = 5) -> List[Dict[str, Any]]:
        """Search documentation index using query string."""
        if not query or not query.strip():
            return []

        clean_query = query.strip().lower()
        terms = [t for t in re.findall(r"\w+", clean_query) if len(t) > 1]
        if not terms:
            terms = [clean_query]

        docs = self._load_search_index()
        scored_results: List[Tuple[float, Dict[str, Any]]] = []

        site_url = self.scaffolder.config.get("site_url", "https://oleg-nenashev.github.io/oleg-nenashev").rstrip("/")

        for doc in docs:
            title = str(doc.get("title", ""))
            text = str(doc.get("text", ""))
            location = str(doc.get("location", ""))
            
            # Strip HTML tags for clean text search
            clean_text = re.sub(r"<[^>]+>", " ", text)
            clean_text = re.sub(r"\s+", " ", clean_text)
            
            score = 0.0
            title_lower = title.lower()
            text_lower = clean_text.lower()

            # Exact query matching bonus
            if clean_query in title_lower:
                score += 50.0
            if clean_query in text_lower:
                score += 20.0

            # Individual term matching
            for term in terms:
                if term in title_lower:
                    score += 15.0
                term_count = text_lower.count(term)
                if term_count > 0:
                    score += min(term_count * 2.0, 20.0)

            if score > 0:
                snippet = self._generate_snippet(clean_text, terms)
                full_url = f"{site_url}/{location.lstrip('/')}" if location else site_url

                scored_results.append((score, {
                    "title": title,
                    "location": location,
                    "url": full_url,
                    "snippet": snippet,
                    "score": round(score, 2)
                }))

        scored_results.sort(key=lambda x: x[0], reverse=True)
        return [r[1] for r in scored_results[:limit]]

    @staticmethod
    def _generate_snippet(text: str, terms: List[str], max_len: int = 240) -> str:
        """Extract relevant text snippet centered around matching terms."""
        if not text:
            return ""

        lower_text = text.lower()
        first_pos = -1
        for term in terms:
            pos = lower_text.find(term)
            if pos != -1 and (first_pos == -1 or pos < first_pos):
                first_pos = pos

        if first_pos == -1:
            snippet = text[:max_len]
            return snippet + "..." if len(text) > max_len else snippet

        start = max(0, first_pos - 60)
        end = min(len(text), first_pos + max_len - 60)
        snippet = text[start:end].strip()

        prefix = "..." if start > 0 else ""
        suffix = "..." if end < len(text) else ""
        return f"{prefix}{snippet}{suffix}"
