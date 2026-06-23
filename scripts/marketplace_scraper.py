#!/usr/bin/env python3
"""Generate metadata-only README for awesome-claude-plugins."""

import argparse
import logging

try:
    from .config import Config
    from .metadata_catalog import fetch_repos_from_sources, count_plugins, render_readme
except ImportError:
    from config import Config
    from metadata_catalog import fetch_repos_from_sources, count_plugins, render_readme


def setup_logging(level: str = "INFO") -> None:
    numeric_level = getattr(logging, level.upper(), logging.INFO)
    logging.basicConfig(level=numeric_level, format='%(asctime)s - %(levelname)s - %(message)s')


def generate_readme(repositories: list, counts: dict, output_file: str) -> bool:
    content = render_readme(repositories, counts)
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(content)
        logging.getLogger(__name__).info("README generated successfully: %s", output_file)
        return True
    except Exception as e:
        logging.getLogger(__name__).error("Failed to write README: %s", e)
        return False


def cmd_generate_readme(args, config, logger):
    logger.info("Plugin metadata catalog generation starting...")
    sources = config.get_enabled_sources()
    logger.info("Loaded %d enabled sources", len(sources))
    if not sources:
        logger.warning("No enabled sources found in configuration")
        return 0
    repositories = fetch_repos_from_sources(sources)
    logger.info("Loaded %d enabled repositories from source configs", len(repositories))
    counts = count_plugins(repositories, max_workers=8)
    total = sum(v.get('count', 0) for v in counts.values())
    unavailable = sum(1 for v in counts.values() if v.get('status') != 'ok')
    logger.info("Counted %d plugins across %d repos (%d unavailable)", total, len(repositories), unavailable)
    if args.dry_run:
        print(f"Dry run: Would generate README with {len(repositories)} repositories and {total} discoverable plugins")
        return 0
    if generate_readme(repositories, counts, args.output):
        print(f"Successfully generated README with {len(repositories)} repositories and {total} discoverable plugins!")
        return 0
    print("Failed to generate README")
    return 1


def cmd_validate_config(args, config, logger):
    try:
        sources = config.get_enabled_sources()
        print(f"✓ Found {len(sources)} enabled sources")
        print("✓ Configuration is valid")
        return 0
    except Exception as e:
        print(f"✗ Configuration validation failed: {e}")
        return 1


def cmd_list_sources(args, config, logger):
    try:
        sources = config.get_enabled_sources()
        if args.format == "json":
            import json
            print(json.dumps(sources, indent=2))
        else:
            print("Configured Sources:")
            print("-" * 60)
            print(f"{'ID':<25} {'URL':<35}")
            print("-" * 60)
            for source in sources:
                print(f"{source.get('id','unknown'):<25} {source.get('url',''):<35}")
        return 0
    except Exception as e:
        print(f"Failed to list sources: {e}")
        return 1


def main():
    parser = argparse.ArgumentParser(description="Generate metadata-only README for Claude plugin marketplaces")
    parser.add_argument("--config", type=str, default="config.yaml", help="Path to configuration file")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose logging")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")
    generate_parser = subparsers.add_parser("generate-readme", help="Generate README.md from configured sources")
    generate_parser.add_argument("--output", type=str, default="README.md", help="Output file path")
    generate_parser.add_argument("--dry-run", action="store_true", help="Validate configuration and sources without writing output")
    validate_parser = subparsers.add_parser("validate-config", help="Validate configuration file format")
    validate_parser.add_argument("--check-sources", action="store_true", help="No-op compatibility flag")
    list_parser = subparsers.add_parser("list-sources", help="List configured sources with status information")
    list_parser.add_argument("--format", choices=["table", "json"], default="table", help="Output format")
    args = parser.parse_args()
    if not args.command:
        parser.print_help()
        return 1
    try:
        config = Config(args.config)
        log_level = config.logging_config.get("level", "INFO")
        if args.verbose:
            log_level = "DEBUG"
    except Exception as e:
        print(f"Failed to load configuration: {e}")
        return 1
    setup_logging(log_level)
    logger = logging.getLogger(__name__)
    if args.command == "generate-readme":
        return cmd_generate_readme(args, config, logger)
    if args.command == "validate-config":
        return cmd_validate_config(args, config, logger)
    if args.command == "list-sources":
        return cmd_list_sources(args, config, logger)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
