# Feature Specification: Marketplace Scraper Scripts

**Feature Branch**: `001-marketplace-scraper`
**Created**: 2025-12-23
**Status**: Draft
**Input**: User description: "Build scripts that first: 1. Get a list of claude marketplaces from multiple sources, first source is: https://github.com/Chat2AnyLLM/code-agent-manager/blob/main/code_assistant_manager/plugin_repos.json 2. Then you can use a 'config.yaml' file to specify the sources 3. All sources use the same format as in: https://github.com/Chat2AnyLLM/code-agent-manager/blob/main/code_assistant_manager/plugin_repos.json 4. You read the repo https://github.com/Chat2AnyLLM/code-agent-manager, to find out how it retrieves all the plugins from all the configured plugin_repos.json/from marketplaces Then you create content in readme.md with a top 'menu of content', a table of marketplaces, a table of plugins, organized them with categories"

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Generate README from Marketplace Data (Priority: P1)

As a project maintainer, I want to run a script that fetches current marketplace and plugin data from configured sources and automatically generates an updated README.md with organized tables of marketplaces and categorized plugins.

**Why this priority**: This is the core functionality that delivers the primary value of automating README maintenance.

**Independent Test**: Can be fully tested by running the script with a config.yaml file and verifying that README.md is created with correct structure, all marketplaces listed, and plugins categorized.

**Acceptance Scenarios**:

1. **Given** a valid config.yaml with marketplace sources, **When** I run the script, **Then** README.md is generated with a table of contents, marketplaces table, and plugins organized by categories
2. **Given** multiple sources in config.yaml, **When** I run the script, **Then** all sources are fetched and their data is merged into the README without duplicates
3. **Given** network connectivity issues with one source, **When** I run the script, **Then** the script continues with available sources and logs the failure

---

### User Story 2 - Configure Sources via YAML (Priority: P2)

As a project maintainer, I want to specify marketplace sources in a config.yaml file so I can easily add or remove sources without modifying the script code.

**Why this priority**: This enables flexibility and maintainability of the data sources.

**Independent Test**: Can be tested by creating a config.yaml with different sources and verifying the script reads and processes them correctly.

**Acceptance Scenarios**:

1. **Given** a config.yaml file with multiple source URLs, **When** I run the script, **Then** all specified sources are fetched
2. **Given** an invalid URL in config.yaml, **When** I run the script, **Then** the invalid source is skipped and processing continues with valid sources
3. **Given** a config.yaml with duplicate sources, **When** I run the script, **Then** duplicates are handled gracefully without errors

---

### User Story 3 - Categorize Plugins in README (Priority: P3)

As a project maintainer, I want plugins automatically organized by categories in the generated README for better discoverability.

**Why this priority**: This improves user experience by making it easier to find relevant plugins.

**Independent Test**: Can be tested by examining the generated README structure and verifying plugins are grouped under appropriate category headings.

**Acceptance Scenarios**:

1. **Given** plugins with category metadata, **When** the script generates README, **Then** plugins are grouped under category headings
2. **Given** plugins without category metadata, **When** the script generates README, **Then** they are placed in a "Miscellaneous" or "Uncategorized" section
3. **Given** multiple marketplaces with overlapping categories, **When** the script generates README, **Then** categories are unified across marketplaces

### Edge Cases

- What happens when a source URL is unreachable?
- How does the system handle malformed JSON from a source?
- What if config.yaml is missing or has invalid YAML syntax?
- How are duplicate plugins from different sources handled?
- What if a source has no plugins or marketplaces?
- What if a marketplace repository is private or doesn't exist?
- What if a repository lacks plugin manifest files?
- How to handle plugins with missing or invalid category information?
- What if multiple plugins have the same name across marketplaces?

## Clarifications

### Session 2025-12-23
- Q: Should the script fetch real plugin manifests from GitHub repositories or continue with mock data? → A: Option A - Fetch real plugin manifests from GitHub repositories

### Session 2025-12-23 (continued)
- Q: How should plugins be fetched from configured marketplaces - individual manifest files per plugin or structured marketplace.json files? → A: Option A - Adopt the .claude-plugin/marketplace.json approach where each marketplace repository contains a marketplace.json file with a "plugins" array listing all plugins with metadata
- Q: How should plugins be displayed in the generated README - as bullet lists or tables? → A: Tables - Display plugins in table format with columns for Plugin, Description, Author, and Version
- Q: Should each marketplace and plugin have a URL that users can click to go there? → A: Yes, each marketplace and plugin should have a URL for user navigation

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: System MUST read and parse a config.yaml file containing marketplace source URLs
- **FR-002**: System MUST fetch JSON data from each configured source URL
- **FR-003**: System MUST parse marketplace data from the fetched JSON using the same format as the reference source
- **FR-004**: System MUST fetch real plugin manifests from GitHub repositories associated with each marketplace
- **FR-005**: System MUST analyze the code-agent-manager repository to understand the plugin retrieval mechanism
- **FR-006**: System MUST parse plugin data from manifest files (plugin.json, manifest.json, or .claude/plugin.json) in marketplace repositories
- **FR-007**: System MUST merge data from multiple sources, handling duplicates appropriately
- **FR-008**: System MUST generate README.md with a table of contents at the top
- **FR-009**: System MUST generate a table of marketplaces with columns for name, description, and URL
- **FR-010**: System MUST generate tables of plugins organized by categories, with each plugin displayed in a table format including Plugin name, Description, Author, Version, and URL columns
- **FR-011**: System MUST handle network errors gracefully by logging failures and continuing with available data
- **FR-012**: System MUST validate JSON format and skip malformed data with appropriate error logging
- **FR-013**: System MUST handle repositories that lack plugin manifests or are inaccessible

### Key Entities *(include if feature involves data)*

- **Marketplace**: Represents a plugin marketplace with name, description, URL, and list of associated plugins
- **Plugin**: Represents an individual plugin with name, description, category, marketplace reference, installation details, author, version, and manifest URL
- **Source**: Represents a data source with URL and optional metadata like last fetched timestamp

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: Script completes execution in under 5 minutes for up to 10 sources
- **SC-002**: README.md is generated with valid markdown syntax that renders correctly
- **SC-003**: All configured sources are successfully processed in 90% of runs
- **SC-004**: Generated README includes at least 80% of available marketplaces from sources
- **SC-005**: Generated README includes plugins from at least 50% of accessible marketplace repositories
- **SC-006**: Categories are applied correctly to 95% of successfully parsed plugins
