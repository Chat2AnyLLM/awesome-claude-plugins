#!/usr/bin/env python3
"""
README generator for marketplace scraper
"""

import logging
from typing import List, Dict, Any
from collections import defaultdict
import re
import concurrent.futures
from datetime import datetime

import requests

logger = logging.getLogger(__name__)


class ReadmeGenerator:
    """Generates README content from marketplace and plugin data."""

    def __init__(self):
        self.marketplaces: List[Dict[str, Any]] = []
        self.plugins: List[Dict[str, Any]] = []
        self._url_ok_cache: Dict[str, bool] = {}

    def _check_url_availability(self, url: str) -> bool:
        """Check if a URL is available (returns status code < 400)."""
        try:
            resp = requests.head(url, allow_redirects=True, timeout=10)
            if resp.status_code == 405:  # Method not allowed, try GET
                resp = requests.get(
                    url, allow_redirects=True, timeout=10, stream=True
                )
            return resp.status_code < 400
        except Exception:
            return False

    def add_marketplaces(self, marketplaces: List[Dict[str, Any]]):
        """Add marketplace data."""
        self.marketplaces.extend(marketplaces)

    def add_plugins(self, plugins: List[Dict[str, Any]]):
        """Add plugin data."""
        self.plugins.extend(plugins)

    def generate_title(self) -> str:
        """Generate the README title."""
        # Get current UTC timestamp
        current_time = datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")
        return f"""# [![Awesome](https://awesome.re/badge.svg)](https://awesome.re) Awesome Claude Plugins

A curated list of awesome Claude marketplaces and plugins to enhance your Claude Code experience.

Total Marketplaces: {len(self.marketplaces)} | Total Plugins: {len(self.plugins)}

Last updated: {current_time}

"""

    def generate_installation(self) -> str:
        """Generate the installation instructions."""
        return """## Installation

1. Install CAM: `curl -fsSL https://raw.githubusercontent.com/Chat2AnyLLM/code-assistant-manager/main/install.sh | bash`
2. Find the marketplace to install, or install all marketplace
   ```
   cam plugin marketplace install superpowers-marketplace
   ```
   OR
   ```
   cam plugin marketplace install --all -a claude
   ```
3. Install plugin in the marketplaces
   ```
   cam plugin install superpowers
   ```

"""

    def generate_concise_table_of_contents(self) -> str:
        """Generate a concise table of contents."""
        if not self.plugins:
            return ""

        category_names = self._get_sorted_category_names()
        if not category_names:
            return ""

        lines = ["## Table of Contents\n"]
        for category in category_names:
            anchor = self._category_anchor(category)
            lines.append(f"- [{category}](#{anchor})")

        lines.append("- [Contributing](#contributing)")
        lines.append("")
        return "\n".join(lines)

    def generate_table_of_contents(self) -> str:
        """Generate table of contents."""
        return self.generate_concise_table_of_contents().replace(
            "## Table of Contents\n", "## Contents\n", 1
        )

    def generate_plugins_by_category(self) -> str:
        """Generate plugins organized by category with table format."""
        if not self.plugins:
            return ""

        # Group plugins by category
        categories = self._get_categories()

        lines = []
        for category in self._get_sorted_category_names(categories):
            lines.append(f"## {category}\n")

            # Table header
            lines.append("| Plugin | Marketplace | Description | Author | Version |")
            lines.append("|--------|-------------|-------------|--------|---------|")

            # Sort plugins alphabetically within the category
            sorted_plugins = sorted(categories[category], key=lambda p: p.get("name", ""))

            for plugin in sorted_plugins:
                name = plugin.get("name", "Unknown Plugin")
                description = (
                    plugin.get("description", "").replace("\n", " ").strip()
                )
                # Truncate description for table readability
                if len(description) > 150:
                    description = description[:147] + "..."
                author_data = plugin.get("author", "")
                # Handle author as string or dict with name
                if isinstance(author_data, dict):
                    author = author_data.get("name", "")
                else:
                    author = str(author_data)
                version = plugin.get("version", "latest")
                homepage_url = plugin.get("homepage", "")

                # Prefer linking plugin name to a non-404 GitHub source location (or repo) over homepage.
                candidate_urls: List[str] = []
                source_data = plugin.get("source_data", {})
                if isinstance(source_data, dict):
                    source_info = source_data.get("source", {})
                    if isinstance(source_info, dict) and source_info.get("url"):
                        candidate_urls.append(source_info["url"])
                    elif isinstance(source_info, str) and source_info.startswith("./"):
                        repo_url = plugin.get("repo_url", "")
                        repo_branch = plugin.get("repo_branch", "main")
                        if repo_url:
                            relative_path = source_info[2:]  # Remove "./"
                            candidate_urls.extend([
                                f"{repo_url}/tree/{repo_branch}/{relative_path}",
                                f"{repo_url}/blob/{repo_branch}/{relative_path}",
                            ])

                plugin_url = plugin.get("url", "")
                if plugin_url:
                    candidate_urls.append(plugin_url)

                repo_url = plugin.get("repo_url", "")
                if repo_url:
                    candidate_urls.append(repo_url)

                if homepage_url:
                    candidate_urls.append(homepage_url)
                
                # Get marketplace name
                marketplace_id = plugin.get("marketplace_id", "unknown")
                marketplace_name = self._get_marketplace_name(marketplace_id)

                # Create name cell with hyperlink.
                # Only do HTTP availability checks when a homepage is present (we need to choose between links);
                # otherwise, link to the best candidate directly to keep generation offline-friendly.
                name_cell = name
                filtered_urls = [
                    u for u in candidate_urls if isinstance(u, str) and u.startswith("http")
                ]
                if filtered_urls:
                    if not homepage_url:
                        name_cell = f"[{name}]({filtered_urls[0]})"
                    else:
                        # Check URL availability in parallel for better performance
                        urls_to_check = [url for url in filtered_urls if url not in self._url_ok_cache]

                        if urls_to_check:
                            # Use ThreadPoolExecutor to check URLs in parallel
                            with concurrent.futures.ThreadPoolExecutor(max_workers=min(len(urls_to_check), 10)) as executor:
                                # Submit all URL checks
                                future_to_url = {executor.submit(self._check_url_availability, url): url for url in urls_to_check}
                                # Collect results as they complete
                                for future in concurrent.futures.as_completed(future_to_url):
                                    url = future_to_url[future]
                                    try:
                                        ok = future.result()
                                    except Exception as e:
                                        logger.debug(f"Error checking URL {url}: {e}")
                                        ok = False
                                    self._url_ok_cache[url] = ok

                        # Find the first available URL
                        for url in filtered_urls:
                            if self._url_ok_cache.get(url, False):
                                name_cell = f"[{name}]({url})"
                                break

                        # If we couldn't validate (e.g. no network), still pick the preferred candidate.
                        if name_cell == name:
                            name_cell = f"[{name}]({filtered_urls[0]})"

                # Escape pipe characters in description
                description = description.replace("|", "\\|")

                lines.append(
                    f"| {name_cell} | {marketplace_name} | {description} | {author} | {version} |"
                )

            lines.append("")

        return "\n".join(lines)

    def generate_contributing(self) -> str:
        """Generate contributing section."""
        return """## Contributing

We welcome contributions! If you want to contribute by adding a new plugin, please go to [https://github.com/Chat2AnyLLM/awesome-repo-configs](https://github.com/Chat2AnyLLM/awesome-repo-configs) and add your plugin config to the corresponding config file there.

This README is auto-generated from those configs, so that is the right place to make your additions.
"""

    def generate_readme(self) -> str:
        """Generate complete README content."""
        sections = [
            self.generate_title(),
            self.generate_installation(),
            self.generate_concise_table_of_contents(),
            self.generate_plugins_by_category(),
            self.generate_contributing(),
        ]

        content = "".join(sections)

        # Validate markdown format
        if not self.validate_markdown(content):
            logger.warning("Generated markdown failed validation")
        else:
            logger.info("Generated markdown validation successful")

        return content

    def _get_categories(self) -> Dict[str, List[Dict[str, Any]]]:
        """Get plugins grouped by category."""
        categories = defaultdict(list)
        for plugin in self.plugins:
            category = plugin.get("category", "Uncategorized")
            categories[category].append(plugin)
        return categories

    def _get_marketplace_name(self, marketplace_id: str) -> str:
        """Get marketplace name by ID."""
        for marketplace in self.marketplaces:
            if marketplace.get("id") == marketplace_id:
                return marketplace.get("name", marketplace_id)
        return marketplace_id

    def _get_sorted_category_names(
        self, categories: Dict[str, List[Dict[str, Any]]] = None
    ) -> List[str]:
        """Return sorted category names for current plugins."""
        if categories is None:
            categories = self._get_categories()
        return sorted(categories.keys())

    def _category_anchor(self, category: str) -> str:
        """Convert category name to a Markdown anchor (GitHub-style-ish)."""
        return (
            category.lower()
            .replace(" ", "-")
            .replace("&", "")
            .replace(",", "")
            .replace("(", "")
            .replace(")", "")
        )

    def validate_markdown(self, content: str) -> bool:
        """Basic markdown validation for generated content."""
        try:
            # Check for balanced brackets in links [text](url)
            link_pattern = r"\[([^\]]*)\]\(([^)]*)\)"
            links = re.findall(link_pattern, content)

            for text, url in links:
                if not text.strip():
                    logger.warning("Found empty link text in markdown")
                    return False
                if not url.strip():
                    logger.warning("Found empty URL in markdown link")
                    return False

            # Basic check for table structure - just ensure tables have separators
            lines = content.split("\n")
            table_started = False
            has_separator = False

            for line in lines:
                if "|" in line and not line.strip().startswith("#"):
                    if (
                        "|---" in line
                        or "|:--" in line
                        or ":---" in line
                        or "---:" in line
                    ):
                        has_separator = True
                        table_started = False
                    elif not table_started:
                        table_started = True
                    # else: continuing table row

            # If we found tables, ensure they have separators
            if table_started and not has_separator:
                logger.warning("Found table without proper separator")
                return False

            logger.info("Markdown validation passed")
            return True

        except Exception as e:
            logger.error(f"Markdown validation failed: {e}")
            return False
