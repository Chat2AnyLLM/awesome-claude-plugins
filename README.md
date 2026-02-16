# [![Awesome](https://awesome.re/badge.svg)](https://awesome.re) Awesome Claude Plugins

A curated list of awesome Claude marketplaces and plugins to enhance your Claude Code experience.

Total Marketplaces: 43 | Total Plugins: 834

Last updated: 2026-01-22 08:40 UTC

## Installation

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

## Table of Contents

- [Automation DevOps](#automation-devops)
- [Business Sales](#business-sales)
- [Code Quality Testing](#code-quality-testing)
- [Data Analytics](#data-analytics)
- [Design UX](#design-ux)
- [Development Engineering](#development-engineering)
- [Documentation](#documentation)
- [Git Workflow](#git-workflow)
- [Marketing Growth](#marketing-growth)
- [Official Claude Code Plugins](#official-claude-code-plugins)
- [Project & Product Management](#project--product-management)
- [Security, Compliance, & Legal](#security-compliance--legal)
- [Uncategorized](#uncategorized)
- [Workflow Orchestration](#workflow-orchestration)
- [abap](#abap)
- [accessibility](#accessibility)
- [agents](#agents)
- [ai](#ai)
- [ai-agency](#ai-agency)
- [ai-ml](#ai-ml)
- [api](#api)
- [api-development](#api-development)
- [assets](#assets)
- [automation](#automation)
- [blockchain](#blockchain)
- [btp](#btp)
- [business](#business)
- [business-marketing](#business-marketing)
- [business-tools](#business-tools)
- [cap](#cap)
- [code-quality](#code-quality)
- [code-review](#code-review)
- [communication](#communication)
- [communication-writing](#communication-writing)
- [community](#community)
- [content](#content)
- [creative-media](#creative-media)
- [crypto](#crypto)
- [customization](#customization)
- [data](#data)
- [data-analytics](#data-analytics)
- [database](#database)
- [debugging](#debugging)
- [deployment](#deployment)
- [design](#design)
- [dev-tools](#dev-tools)
- [developer-tools](#developer-tools)
- [development](#development)
- [devops](#devops)
- [document-conversion](#document-conversion)
- [documentation](#documentation)
- [example](#example)
- [explore](#explore)
- [finance](#finance)
- [fullstack](#fullstack)
- [gaming](#gaming)
- [general](#general)
- [hana](#hana)
- [infrastructure](#infrastructure)
- [languages](#languages)
- [learning](#learning)
- [marketing](#marketing)
- [media](#media)
- [modernization](#modernization)
- [monitoring](#monitoring)
- [operations](#operations)
- [packages](#packages)
- [payments](#payments)
- [performance](#performance)
- [plan](#plan)
- [productivity](#productivity)
- [productivity-organization](#productivity-organization)
- [quality](#quality)
- [refactoring](#refactoring)
- [security](#security)
- [skill-enhancers](#skill-enhancers)
- [testing](#testing)
- [tooling](#tooling)
- [ui-development](#ui-development)
- [utilities](#utilities)
- [workflow](#workflow)
- [workflows](#workflows)
- [Contributing](#contributing)
## Automation DevOps

| Plugin | Marketplace | Description | Author | Version |
|--------|-------------|-------------|--------|---------|
| [aws-cost-saver](https://github.com/prajapatimehul/aws-cost-saver) | aws-cost-saver-marketplace | AWS cost optimization scanner with 173 automated checks across 11 domains. Features AWS Compute Optimizer ML integration, Zero Hallucination Pricing System (21 rules), and parallel scanning. Real result: 60% cost reduction ($105/day → $42/day). Read-only and safe. | Mehul Prajapati | 1.0.0 |
| [deployment-engineer](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/deployment-engineer) | awesome-claude-code-plugins | Use this agent when setting up CI/CD pipelines, configuring Docker containers, deploying applications to cloud platforms, setting up Kubernetes clu... | Jure Šunić | 1.0.0 |
| [devops-automator](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/devops-automator) | awesome-claude-code-plugins | Use this agent when setting up CI/CD pipelines, configuring cloud infrastructure, implementing monitoring systems, or automating deployment process... | Michael Galpert | 1.0.0 |
| [infrastructure-maintainer](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/infrastructure-maintainer) | awesome-claude-code-plugins | Use this agent when monitoring system health, optimizing performance, managing scaling, or ensuring infrastructure reliability. This agent excels a... | Michael Galpert | 1.0.0 |
| [monitoring-observability-specialist](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/monitoring-observability-specialist) | awesome-claude-code-plugins | Use this agent when you need to implement comprehensive monitoring, observability, and alerting systems for enterprise B2B applications. This agent... | Alysson Franklin | 1.0.0 |
| [n8n-workflow-builder](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/n8n-workflow-builder) | awesome-claude-code-plugins | Use this agent when you need to design, build, or validate n8n automation workflows. This agent specializes in creating efficient n8n workflows usi... | Jure Šunić | 1.0.0 |

## Business Sales

| Plugin | Marketplace | Description | Author | Version |
|--------|-------------|-------------|--------|---------|
| [b2b-project-shipper](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/b2b-project-shipper) | awesome-claude-code-plugins | PROACTIVELY use this agent when approaching B2B launch milestones, enterprise release deadlines, or B2B go-to-market activities. This agent special... | Alysson Franklin | 1.0.0 |
| [customer-success-manager](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/customer-success-manager) | awesome-claude-code-plugins | Use this agent when you need to optimize customer success operations for B2B enterprise clients. This agent specializes in customer health monitori... | Alysson Franklin | 1.0.0 |
| [enterprise-onboarding-specialist](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/enterprise-onboarding-specialist) | awesome-claude-code-plugins | Use this agent when you need to design and optimize complex enterprise customer onboarding processes involving multiple stakeholders, change manage... | Alysson Franklin | 1.0.0 |
| [finance-tracker](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/finance-tracker) | awesome-claude-code-plugins | Use this agent when managing budgets, optimizing costs, forecasting revenue, or analyzing financial performance. This agent excels at transforming ... | Michael Galpert | 1.0.0 |
| [pricing-packaging-specialist](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/pricing-packaging-specialist) | awesome-claude-code-plugins | Use this agent when you need to optimize B2B pricing strategies, packaging models, and revenue optimization for enterprise sales. This agent specia... | Alysson Franklin | 1.0.0 |
| [product-sales-specialist](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/product-sales-specialist) | awesome-claude-code-plugins | Use this agent when you need to support B2B sales through product design, user research, project management, and creative RFP responses. This agent... | Alysson Franklin | 1.0.0 |
| [support-responder](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/support-responder) | awesome-claude-code-plugins | Use this agent when handling customer support inquiries, creating support documentation, setting up automated responses, or analyzing support patte... | Michael Galpert | 1.0.0 |
| [technical-sales-engineer](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/technical-sales-engineer) | awesome-claude-code-plugins | Use this agent when you need to bridge technical and sales requirements for B2B enterprise deals. This agent specializes in technical demos, POC de... | Alysson Franklin | 1.0.0 |

## Code Quality Testing

| Plugin | Marketplace | Description | Author | Version |
|--------|-------------|-------------|--------|---------|
| [api-tester](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/api-tester) | awesome-claude-code-plugins | Use this agent for comprehensive API testing including performance testing, load testing, and contract testing. This agent specializes in ensuring ... | Michael Galpert | 1.0.0 |
| [bug-detective](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/bug-detective) | awesome-claude-code-plugins | Systematically debug issues with step-by-step troubleshooting approaches. | Anonymous | 1.0.0 |
| [code-review](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/code-review) | awesome-claude-code-plugins | Perform a comprehensive code review of recent changes |  Anand Tyagi | 1.0.0 |
| [code-review-assistant](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/code-review-assistant) | awesome-claude-code-plugins | Get comprehensive code reviews with suggestions for improvements, best practices, and potential issues. | Anonymous | 1.0.0 |
| [code-reviewer](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/code-reviewer) | awesome-claude-code-plugins | Expert code review specialist. Proactively reviews code for quality, security, and maintainability. Use immediately after writing or modifying code. | Anand Tyagi | 1.0.0 |
| [database-performance-optimizer](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/database-performance-optimizer) | awesome-claude-code-plugins | Use this agent when you need to optimize database performance for B2B applications at enterprise scale. This agent specializes in multi-tenant data... | Alysson Franklin | 1.0.0 |
| [debug-session](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/debug-session) | awesome-claude-code-plugins | Ask Claude Code to help you debug an issue |  Anand Tyagi | 1.0.0 |
| [debugger](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/debugger) | awesome-claude-code-plugins | Debugging specialist for errors, test failures, and unexpected behavior. Use proactively when encountering any issues. | Anand Tyagi | 1.0.0 |
| [double-check](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/double-check) | awesome-claude-code-plugins | An easy way to force agent to think again if it's statement that the "Job is done and production ready" is actually done - usually it's not. Thanks... | Robert S | 1.0.0 |
| [optimize](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/optimize) | awesome-claude-code-plugins | Analyze and optimize code performance |  Anand Tyagi | 1.0.0 |
| [performance-benchmarker](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/performance-benchmarker) | awesome-claude-code-plugins | Use this agent for comprehensive performance testing, profiling, and optimization recommendations. This agent specializes in measuring speed, ident... | Michael Galpert | 1.0.0 |
| [refractor](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/refractor) | awesome-claude-code-plugins | Refactor code following best practices and design patterns |  Anand Tyagi | 1.0.0 |
| [test-file](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/test-file) | awesome-claude-code-plugins | Generate comprehensive tests for a specific file |  Anand Tyagi | 1.0.0 |
| [test-results-analyzer](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/test-results-analyzer) | awesome-claude-code-plugins | Use this agent for analyzing test results, synthesizing test data, identifying trends, and generating quality metrics reports. This agent specializ... | Michael Galpert | 1.0.0 |
| [test-writer-fixer](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/test-writer-fixer) | awesome-claude-code-plugins | Use this agent when code changes have been made and you need to write new tests, run existing tests, analyze failures, and fix them while maintaini... | Michael Galpert | 1.0.0 |
| [unit-test-generator](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/unit-test-generator) | awesome-claude-code-plugins | Expert Flutter/Dart unit test specialist that systematically improves test coverage using automated workflows with strict validation, git managemen... | Community | 1.0.0 |

## Data Analytics

| Plugin | Marketplace | Description | Author | Version |
|--------|-------------|-------------|--------|---------|
| [analytics-reporter](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/analytics-reporter) | awesome-claude-code-plugins | Use this agent when analyzing metrics, generating insights from data, creating performance reports, or making data-driven recommendations. This age... | Michael Galpert | 1.0.0 |
| [data-scientist](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/data-scientist) | awesome-claude-code-plugins | Data analysis expert for SQL queries, BigQuery operations, and data insights. Use proactively for data analysis tasks and queries. | Anand Tyagi | 1.0.0 |
| [experiment-tracker](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/experiment-tracker) | awesome-claude-code-plugins | PROACTIVELY use this agent when experiments are started, modified, or when results need analysis. This agent specializes in tracking A/B tests, fea... | Michael Galpert | 1.0.0 |
| [feedback-synthesizer](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/feedback-synthesizer) | awesome-claude-code-plugins | Use this agent when you need to analyze user feedback from multiple sources, identify patterns in user complaints or requests, synthesize insights ... | Michael Galpert | 1.0.0 |
| [trend-researcher](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/trend-researcher) | awesome-claude-code-plugins | Use this agent when you need to identify market opportunities, analyze trending topics, research viral content, or understand emerging user behavio... | Michael Galpert | 1.0.0 |

## Design UX

| Plugin | Marketplace | Description | Author | Version |
|--------|-------------|-------------|--------|---------|
| [brand-guardian](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/brand-guardian) | awesome-claude-code-plugins | Use this agent when establishing brand guidelines, ensuring visual consistency, managing brand assets, or evolving brand identity. This agent speci... | Michael Galpert | 1.0.0 |
| [joker](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/joker) | awesome-claude-code-plugins | Use this agent when you need to lighten the mood, create funny content, or add humor to any situation. This agent specializes in dad jokes, program... | Michael Galpert | 1.0.0 |
| [mobile-ux-optimizer](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/mobile-ux-optimizer) | awesome-claude-code-plugins | Use this agent when you need to optimize UI/UX components or interfaces for mobile-first experiences, analyze existing design themes, or ensure mob... | abhishek shah | 1.0.0 |
| [onomastophes](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/onomastophes) | awesome-claude-code-plugins | Use proactively for generating creative non-olympian Greek god names with rich backstories, mythological authenticity, and modern accessibility for... | normalnormie | 1.0.0 |
| [ui-designer](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/ui-designer) | awesome-claude-code-plugins | Use this agent when creating user interfaces, designing components, building design systems, or improving visual aesthetics. This agent specializes... | Michael Galpert | 1.0.0 |
| [ux-researcher](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/ux-researcher) | awesome-claude-code-plugins | Use this agent when conducting user research, analyzing user behavior, creating journey maps, or validating design decisions through testing. This ... | Michael Galpert | 1.0.0 |
| [visual-storyteller](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/visual-storyteller) | awesome-claude-code-plugins | Use this agent when creating visual narratives, designing infographics, building presentations, or communicating complex ideas through imagery. Thi... | Michael Galpert | 1.0.0 |
| [whimsy-injector](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/whimsy-injector) | awesome-claude-code-plugins | PROACTIVELY use this agent after any UI/UX changes to ensure delightful, playful elements are incorporated. This agent specializes in adding joy, s... | Michael Galpert | 1.0.0 |

## Development Engineering

| Plugin | Marketplace | Description | Author | Version |
|--------|-------------|-------------|--------|---------|
| [ai-engineer](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/ai-engineer) | awesome-claude-code-plugins | Use this agent when implementing AI/ML features, integrating language models, building recommendation systems, or adding intelligent automation to ... | Michael Galpert | 1.0.0 |
| [api-integration-specialist](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/api-integration-specialist) | awesome-claude-code-plugins | Use this agent when you need to design and implement internal API architecture, developer experience, and API infrastructure for B2B applications. ... | Alysson Franklin | 1.0.0 |
| [backend-architect](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/backend-architect) | awesome-claude-code-plugins | Use this agent when designing APIs, building server-side logic, implementing databases, or architecting scalable backend systems. This agent specia... | Michael Galpert | 1.0.0 |
| [code-architect](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/code-architect) | awesome-claude-code-plugins | Use this agent when you need to design scalable architecture and folder structures for new features or projects. Examples include: when starting a ... | abhishek shah | 1.0.0 |
| [desktop-app-dev](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/desktop-app-dev) | awesome-claude-code-plugins | Desktop App Dev subagent | safayavatsal | 1.0.0 |
| [enterprise-integrator-architect](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/enterprise-integrator-architect) | awesome-claude-code-plugins | Use this agent when you need to design and implement complex external enterprise system integrations for B2B applications. This agent specializes i... | Alysson Franklin | 1.0.0 |
| [flutter-mobile-app-dev](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/flutter-mobile-app-dev) | awesome-claude-code-plugins | Use this agent when you need expert assistance with Flutter mobile development tasks, including code analysis, widget creation, debugging, performa... | safayavatsal | 1.0.0 |
| [frontend-developer](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/frontend-developer) | awesome-claude-code-plugins | Use this agent when building user interfaces, implementing React/Vue/Angular components, handling state management, or optimizing frontend performa... | Michael Galpert | 1.0.0 |
| [mobile-app-builder](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/mobile-app-builder) | awesome-claude-code-plugins | Use this agent when developing native iOS or Android applications, implementing React Native features, or optimizing mobile performance. This agent... | Michael Galpert | 1.0.0 |
| [project-curator](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/project-curator) | awesome-claude-code-plugins | Reorganizes project structure by cleaning root clutter, creating logical folder hierarchies, and moving files to optimal locations. Tracks dependen... | alanKerrigan | 1.0.0 |
| [python-expert](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/python-expert) | awesome-claude-code-plugins | Use this agent when working with Python code that requires advanced features, performance optimization, or comprehensive refactoring. Examples: <ex... | Jure Šunić | 1.0.0 |
| [rapid-prototyper](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/rapid-prototyper) | awesome-claude-code-plugins | Use this agent when you need to quickly create a new application prototype, MVP, or proof-of-concept within the 6-day development cycle. This agent... | Michael Galpert | 1.0.0 |
| [react-native-dev](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/react-native-dev) | awesome-claude-code-plugins | Use this agent when you need expert assistance with React Native development tasks including code analysis, component creation, debugging, performa... | abhishek shah | 1.0.0 |
| [vision-specialist](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/vision-specialist) | awesome-claude-code-plugins | Expert in vision models, OCR systems, barcode detection, and visual AI. Stays current with latest models (GPT-4V, Claude Vision, Mistral-OCR, etc.)... | alanKerrigan | 1.0.0 |
| [web-dev](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/web-dev) | awesome-claude-code-plugins | Use this agent for expert assistance with web development tasks using React, Next.js, NestJS, and other modern web frameworks with TypeScript and T... | safayavatsal | 1.0.0 |

## Documentation

| Plugin | Marketplace | Description | Author | Version |
|--------|-------------|-------------|--------|---------|
| [analyze-codebase](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/analyze-codebase) | awesome-claude-code-plugins | Generate comprehensive analysis and documentation of entire codebase |  Anand Tyagi | 1.0.0 |
| [changelog-generator](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/changelog-generator) | awesome-claude-code-plugins | Changelog Generator subagent | Joe Heitzeberg | 1.0.0 |
| [codebase-documenter](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/codebase-documenter) | awesome-claude-code-plugins | Use this agent when you need to analyze a service or codebase component and create comprehensive documentation in CLAUDE.md files. This agent shoul... | Anand Tyagi | 1.0.0 |
| [context7-docs-fetcher](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/context7-docs-fetcher) | awesome-claude-code-plugins | Use this agent when you need to fetch and utilize documentation from Context7 for specific libraries or frameworks. Examples: <example>Context: Use... | normalnormie | 1.0.0 |
| [documentation-generator](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/documentation-generator) | awesome-claude-code-plugins | Create comprehensive documentation for code, APIs, and projects. | Anonymous | 1.0.0 |
| [generate-api-docs](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/generate-api-docs) | awesome-claude-code-plugins | Generate API documentation for endpoints |  Anand Tyagi | 1.0.0 |
| [openapi-expert](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/openapi-expert) | awesome-claude-code-plugins | Use this agent to update, synchronize, or validate the OpenAPI specification (openapi.yml) against the actual REST API implementation. This include... | Meiring de Wet | 1.0.0 |
| [update-claudemd](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/update-claudemd) | awesome-claude-code-plugins | Automatically update CLAUDE.md file based on recent code changes |  Anand Tyagi | 1.0.0 |

## Git Workflow

| Plugin | Marketplace | Description | Author | Version |
|--------|-------------|-------------|--------|---------|
| [analyze-issue](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/analyze-issue) | awesome-claude-code-plugins | Fetches GitHub issue details to create comprehensive implementation specifications, analyzing requirements and planning structured approach with cl... | jerseycheese | 1.0.0 |
| [bug-fix](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/bug-fix) | awesome-claude-code-plugins | Streamlines bug fixing by creating a GitHub issue first, then a feature branch for implementing and thoroughly testing the solution before merging. | danielscholl | 1.0.0 |
| [commit](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/commit) | awesome-claude-code-plugins | Creates git commits using conventional commit format with appropriate emojis, following project standards and creating descriptive messages that ex... | evmts | 1.0.0 |
| [create-pr](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/create-pr) | awesome-claude-code-plugins | Streamlines pull request creation by handling the entire workflow: creating a new branch, committing changes, formatting modified files with Biome,... | toyamarinyon | 1.0.0 |
| [create-pull-request](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/create-pull-request) | awesome-claude-code-plugins | Provides comprehensive PR creation guidance with GitHub CLI, enforcing title conventions, following template structure, and offering concrete comma... | liam-hq | 1.0.0 |
| [create-worktrees](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/create-worktrees) | awesome-claude-code-plugins | Creates git worktrees for all open PRs or specific branches, handling branches with slashes, cleaning up stale worktrees, and supporting custom bra... | evmts | 1.0.0 |
| [fix-github-issue](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/fix-github-issue) | awesome-claude-code-plugins | Analyzes and fixes GitHub issues using a structured approach with GitHub CLI for issue details, implementing necessary code changes, running tests,... | jeremymailen | 1.0.0 |
| [fix-issue](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/fix-issue) | awesome-claude-code-plugins | Addresses GitHub issues by taking issue number as parameter, analyzing context, implementing solution, and testing/validating the fix for proper in... | metabase | 1.0.0 |
| [fix-pr](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/fix-pr) | awesome-claude-code-plugins | Fetches and fixes unresolved PR comments by automatically retrieving feedback, addressing reviewer concerns, making targeted code improvements, and... | metabase | 1.0.0 |
| [github-issue-fix](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/github-issue-fix) | awesome-claude-code-plugins | This is a detailed way you can analyze the GitHub issues and let Claude handle them in best possible way. | safayavatsal | 1.0.0 |
| [husky](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/husky) | awesome-claude-code-plugins | Sets up and manages Husky Git hooks by configuring pre-commit hooks, establishing commit message standards, integrating with linting tools, and ens... | evmts | 1.0.0 |
| [pr-issue-resolve](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/pr-issue-resolve) | awesome-claude-code-plugins | this is to analyze the PRs and solve the requested changes in them | safayavatsal | 1.0.0 |
| [pr-review](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/pr-review) | awesome-claude-code-plugins | Reviews pull request changes to provide feedback, check for issues, and suggest improvements before merging into the main codebase. | arkavo-org | 1.0.0 |
| [update-branch-name](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/update-branch-name) | awesome-claude-code-plugins | Updates branch names with proper prefixes and formats, enforcing naming conventions, supporting semantic prefixes, and managing remote branch updates. | giselles-ai | 1.0.0 |

## Marketing Growth

| Plugin | Marketplace | Description | Author | Version |
|--------|-------------|-------------|--------|---------|
| [app-store-optimizer](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/app-store-optimizer) | awesome-claude-code-plugins | Use this agent when preparing app store listings, researching keywords, optimizing app metadata, improving conversion rates, or analyzing app store... | Michael Galpert | 1.0.0 |
| [content-creator](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/content-creator) | awesome-claude-code-plugins | Content Creator subagent | Michael Galpert | 1.0.0 |
| [growth-hacker](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/growth-hacker) | awesome-claude-code-plugins | Growth Hacker subagent | Michael Galpert | 1.0.0 |
| [instagram-curator](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/instagram-curator) | awesome-claude-code-plugins | Instagram Curator subagent | Michael Galpert | 1.0.0 |
| [reddit-community-builder](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/reddit-community-builder) | awesome-claude-code-plugins | Reddit Community Builder subagent | Michael Galpert | 1.0.0 |
| [tiktok-strategist](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/tiktok-strategist) | awesome-claude-code-plugins | Use this agent when you need to create TikTok marketing strategies, develop viral content ideas, plan TikTok campaigns, or optimize for TikTok's al... | Michael Galpert | 1.0.0 |
| [twitter-engager](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/twitter-engager) | awesome-claude-code-plugins | Twitter Engager subagent | Michael Galpert | 1.0.0 |

## Official Claude Code Plugins

| Plugin | Marketplace | Description | Author | Version |
|--------|-------------|-------------|--------|---------|
| [agent-sdk-dev](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/agent-sdk-dev) | awesome-claude-code-plugins | Development kit for working with the Claude Agent SDK | None | 1.0.0 |
| [commit-commands](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/commit-commands) | awesome-claude-code-plugins | Commands for git commit workflows including commit, push, and PR creation | Anthropic | 1.0.0 |
| [feature-dev](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/feature-dev) | awesome-claude-code-plugins | Comprehensive feature development workflow with specialized agents for codebase exploration, architecture design, and quality review | Siddharth Bidasaria | 1.0.0 |
| [pr-review-toolkit](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/pr-review-toolkit) | awesome-claude-code-plugins | Comprehensive PR review agents specializing in comments, tests, error handling, type design, code quality, and code simplification | Anthropic | 1.0.0 |
| [security-guidance](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/security-guidance) | awesome-claude-code-plugins | Security reminder hook that warns about potential security issues when editing files, including command injection, XSS, and unsafe code patterns | David Dworken | 1.0.0 |

## Project & Product Management

| Plugin | Marketplace | Description | Author | Version |
|--------|-------------|-------------|--------|---------|
| [discuss](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/discuss) | awesome-claude-code-plugins | Collaborative technical discussion with proactive requirements gathering | Bohdan Triapitsyn | 1.0.0 |
| [explore](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/explore) | awesome-claude-code-plugins | Helps Claude read a planning document and explore related files to get familiar with a topic. Asking Claude to prepare to discuss seems to work bet... | Galen Ward | 1.0.0 |
| [plan](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/plan) | awesome-claude-code-plugins | For easy problems, start here. For harder problems, do this after Explore. | Galen Ward | 1.0.0 |
| [planning-prd-agent](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/planning-prd-agent) | awesome-claude-code-plugins | 'MUST BE USED PROACTIVELY when user mentions: planning, PRD, product requirements document, project plan, roadmap, specification, requirements anal... | clouddna-au | 1.0.0 |
| [prd-specialist](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/prd-specialist) | awesome-claude-code-plugins | Use this agent when you need to create comprehensive Product Requirements Documents (PRDs) that combine business strategy, technical architecture, ... | Jure Šunić | 1.0.0 |
| [project-shipper](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/project-shipper) | awesome-claude-code-plugins | PROACTIVELY use this agent when approaching launch milestones, release deadlines, or go-to-market activities. This agent specializes in coordinatin... | Michael Galpert | 1.0.0 |
| [sprint-prioritizer](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/sprint-prioritizer) | awesome-claude-code-plugins | Use this agent when planning 6-day development cycles, prioritizing features, managing product roadmaps, or making trade-off decisions. This agent ... | Michael Galpert | 1.0.0 |
| [studio-producer](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/studio-producer) | awesome-claude-code-plugins | PROACTIVELY use this agent when coordinating across multiple teams, allocating resources, or optimizing studio workflows. This agent specializes in... | Michael Galpert | 1.0.0 |
| [tool-evaluator](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/tool-evaluator) | awesome-claude-code-plugins | Use this agent when evaluating new development tools, frameworks, or services for the studio. This agent specializes in rapid tool assessment, comp... | Michael Galpert | 1.0.0 |
| [workflow-optimizer](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/workflow-optimizer) | awesome-claude-code-plugins | Use this agent for optimizing human-agent collaboration workflows and analyzing workflow efficiency. This agent specializes in identifying bottlene... | Michael Galpert | 1.0.0 |

## Security, Compliance, & Legal

| Plugin | Marketplace | Description | Author | Version |
|--------|-------------|-------------|--------|---------|
| [ai-ethics-governance-specialist](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/ai-ethics-governance-specialist) | awesome-claude-code-plugins | Use this agent when you need to implement AI ethics frameworks, governance policies, and responsible AI practices for B2B applications. This agent ... | Alysson Franklin | 1.0.0 |
| [audit](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/audit) | awesome-claude-code-plugins | Perform security audit on codebase |  Anand Tyagi | 1.0.0 |
| [compliance-automation-specialist](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/compliance-automation-specialist) | awesome-claude-code-plugins | Use this agent when you need to automate compliance processes for SOC 2, ISO 27001, GDPR, HIPAA, and other enterprise regulatory requirements. This... | Alysson Franklin | 1.0.0 |
| [data-privacy-engineer](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/data-privacy-engineer) | awesome-claude-code-plugins | Use this agent when you need to implement data privacy engineering, GDPR compliance, data protection frameworks, and privacy-by-design principles f... | Alysson Franklin | 1.0.0 |
| [enterprise-security-reviewer](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/enterprise-security-reviewer) | awesome-claude-code-plugins | Use this agent for comprehensive B2B security assessments, enterprise compliance validation, multi-tenant security reviews, and security audit prep... | Alysson Franklin | 1.0.0 |
| [legal-advisor](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/legal-advisor) | awesome-claude-code-plugins | Use this agent when you need legal advisory, compliance documentation, RFP response creation, and enterprise contract support for B2B applications.... | Alysson Franklin | 1.0.0 |
| [legal-compliance-checker](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/legal-compliance-checker) | awesome-claude-code-plugins | Use this agent when reviewing terms of service, privacy policies, ensuring regulatory compliance, or handling legal requirements. This agent excels... | Michael Galpert | 1.0.0 |

## Uncategorized

| Plugin | Marketplace | Description | Author | Version |
|--------|-------------|-------------|--------|---------|
| [abstract](https://github.com/athola/claude-night-market/tree/main/plugins/abstract) | athola/claude-night-market | Meta-skills infrastructure for Claude Code plugin ecosystem - skill authoring, hook development, modular design patterns, and evaluation frameworks | None | 1.3.1 |
| [ai-ml-toolkit](https://github.com/davila7/claude-code-templates/tree/main/) | claude-code-templates | AI and Machine Learning development suite with data engineering and model deployment tools | Daniel Avila | 1.0.0 |
| [archetypes](https://github.com/athola/claude-night-market/tree/main/plugins/archetypes) | athola/claude-night-market | Architecture paradigm selection and implementation planning - 14 paradigm skills from functional-core to microservices | None | 1.3.1 |
| [ash](https://github.com/bradleygolden/claude-marketplace-elixir/tree/main/plugins/ash) | bradleygolden/claude-marketplace-elixir | Ash Framework code generation validation and automation | None | 1.0.0 |
| [attune](https://github.com/athola/claude-night-market/tree/main/plugins/attune) | athola/claude-night-market | Full-cycle project development - brainstorm ideas, create specifications, plan architecture, initialize projects, and execute implementation with i... | None | 1.3.1 |
| [browser](https://github.com/iamzhihuix/happy-claude-skills/tree/main/) | iamzhihuix/happy-claude-skills | Browser automation with Chrome DevTools Protocol for scraping, testing, and visual verification | None | 1.0.0 |
| [claude-mem](https://github.com/thedotmack/claude-mem/tree/main/plugin) | thedotmack | Persistent memory system for Claude Code - context compression across sessions | None | 9.0.5 |
| [coding-tutor](https://github.com/EveryInc/compounding-engineering-plugin/tree/main/plugins/coding-tutor) | compounding-engineering | Personalized coding tutorials that build on your existing knowledge and use your actual codebase for examples. Includes spaced repetition quizzes t... | Nityesh Agarwal | 1.2.1 |
| [compound-engineering](https://github.com/EveryInc/compounding-engineering-plugin/tree/main/plugins/compound-engineering) | compounding-engineering | AI-powered development tools that get smarter with every use. Make each unit of engineering work easier than the last. Includes 27 specialized agen... | Kieran Klaassen | 2.27.0 |
| [conjure](https://github.com/athola/claude-night-market/tree/main/plugins/conjure) | athola/claude-night-market | Intelligent delegation framework for routing tasks to external LLMs (Gemini, Qwen) while retaining strategic oversight | None | 1.3.1 |
| [conserve](https://github.com/athola/claude-night-market/tree/main/plugins/conserve) | athola/claude-night-market | Resource optimization and bloat detection - CPU/GPU performance monitoring, token conservation, bloat detection, and codebase cleanup | None | 1.3.1 |
| [core](https://github.com/bradleygolden/claude-marketplace-elixir/tree/main/plugins/core) | bradleygolden/claude-marketplace-elixir | Essential Elixir development support with hooks and automation | None | 1.0.0 |
| [credo](https://github.com/bradleygolden/claude-marketplace-elixir/tree/main/plugins/credo) | bradleygolden/claude-marketplace-elixir | Credo static code analysis for Elixir projects | None | 1.0.0 |
| [dev-browser](https://github.com/SawyerHood/dev-browser/tree/main/) | SawyerHood/dev-browser | Browser automation skill with persistent page state for developers and AI agents | None | 1.0.0 |
| [devops-automation](https://github.com/davila7/claude-code-templates/tree/main/) | claude-code-templates | DevOps automation suite with CI/CD, infrastructure management, and deployment orchestration | Daniel Avila | 1.0.0 |
| [dialyzer](https://github.com/bradleygolden/claude-marketplace-elixir/tree/main/plugins/dialyzer) | bradleygolden/claude-marketplace-elixir | Dialyzer static type analysis for Elixir projects | None | 1.0.0 |
| [document-skills](https://github.com/anthropics/skills/tree/main/) | anthropic-agent-skills | Collection of document processing suite including Excel, Word, PowerPoint, and PDF capabilities | None | 1.0.0 |
| [documentation-generator](https://github.com/davila7/claude-code-templates/tree/main/) | claude-code-templates | Automated documentation generation with API docs, technical writing, and content management | Daniel Avila | 1.0.0 |
| [docx-format-replicator](https://github.com/iamzhihuix/happy-claude-skills/tree/main/) | iamzhihuix/happy-claude-skills | Extract formatting from Word documents and generate new documents with the same format | None | 1.0.0 |
| [double-shot-latte](https://github.com/obra/double-shot-latte.git) | superpowers-marketplace | Stop 'Would you like me to continue?' interruptions. Automatically evaluates whether Claude should continue working using Claude-judged decision ma... | None | 1.1.5 |
| [elements-of-style](https://github.com/obra/the-elements-of-style.git) | superpowers-marketplace | Writing guidance based on William Strunk Jr.'s The Elements of Style (1918) - foundational rules for clear, concise, grammatically correct writing | None | 1.0.0 |
| [elixir](https://github.com/bradleygolden/claude-marketplace-elixir/tree/main/plugins/elixir) | bradleygolden/claude-marketplace-elixir | Comprehensive Elixir development support - formatting, compilation, testing, and static analysis in one plugin (recommended) | None | 1.0.0 |
| [episodic-memory](https://github.com/obra/episodic-memory.git) | superpowers-marketplace | Semantic search for Claude Code conversations. Remember past discussions, decisions, and patterns across sessions. Gives you memory that persists b... | None | 1.0.15 |
| [ex_doc](https://github.com/bradleygolden/claude-marketplace-elixir/tree/main/plugins/ex_doc) | bradleygolden/claude-marketplace-elixir | ExDoc documentation validation plugin that checks for documentation issues before commits | None | 1.0.0 |
| [ex_unit](https://github.com/bradleygolden/claude-marketplace-elixir/tree/main/plugins/ex_unit) | bradleygolden/claude-marketplace-elixir | ExUnit testing automation with pre-commit test validation | None | 1.0.0 |
| [example-skills](https://github.com/anthropics/skills/tree/main/) | anthropic-agent-skills | Collection of example skills demonstrating various capabilities including skill creation, MCP building, visual design, algorithmic art, internal co... | None | 1.0.0 |
| [git-workflow](https://github.com/davila7/claude-code-templates/tree/main/) | claude-code-templates | Git workflow automation: feature, release, and hotfix commands with git specialists | Daniel Avila | 1.0.0 |
| [hookify](https://github.com/athola/claude-night-market/tree/main/plugins/hookify) | athola/claude-night-market | Create custom behavioral rules through markdown configuration - prevent unwanted behaviors with pattern matching and zero-code rule authoring | None | 1.3.1 |
| [imbue](https://github.com/athola/claude-night-market/tree/main/plugins/imbue) | athola/claude-night-market | Intelligent workflow methodologies - review-core scaffolding, diff analysis, evidence logging, and catchup patterns | None | 1.3.1 |
| [iothackbot](https://github.com/BrownFineSecurity/iothackbot/tree/master/) | BrownFineSecurity/iothackbot | IoT security testing toolkit with skills for firmware analysis, network reconnaissance, UEFI security, and device exploitation | None | 1.0.0 |
| [leyline](https://github.com/athola/claude-night-market/tree/main/plugins/leyline) | athola/claude-night-market | Storage and persistence patterns - templates for data management and storage solutions | None | 1.3.1 |
| [math](https://github.com/ananddtyagi/claude-code-marketplace/tree/main/plugins/math) | cc-marketplace | Deterministic math operations using SymPy - arithmetic, algebra, calculus, linear algebra, number theory, and statistics | Anand Tyagi | 1.0.0 |
| [memory-palace](https://github.com/athola/claude-night-market/tree/main/plugins/memory-palace) | athola/claude-night-market | Spatial knowledge organization with memory palace techniques - includes skill execution memory storage for continual learning | None | 1.3.1 |
| [microsoft-docs](https://github.com/MicrosoftDocs/mcp/tree/main/) | microsoft-docs-mcp | Access official Microsoft documentation, API references, and code samples for Azure, .NET, Windows, and more. | None | 1.0.0 |
| [minister](https://github.com/athola/claude-night-market/tree/main/plugins/minister) | athola/claude-night-market | Project management plugin that aligns initiatives with GitHub data - turns repositories, issues, and projects into status dashboards | None | 1.3.1 |
| [mix_audit](https://github.com/bradleygolden/claude-marketplace-elixir/tree/main/plugins/mix_audit) | bradleygolden/claude-marketplace-elixir | Dependency security audit plugin that scans Mix dependencies for known vulnerabilities | None | 1.0.0 |
| [nextjs-vercel-pro](https://github.com/davila7/claude-code-templates/tree/main/) | claude-code-templates | Complete Next.js and Vercel development toolkit with deployment automation and performance optimization | Daniel Avila | 1.0.0 |
| [obsidian](https://github.com/kepano/obsidian-skills/tree/main/) | kepano/obsidian-skills | Claude Skills for Obsidian | None | 1.0.0 |
| [parseltongue](https://github.com/athola/claude-night-market/tree/main/plugins/parseltongue) | athola/claude-night-market | Language detection, pattern matching, and testing guidance for multi-language codebases | None | 1.3.1 |
| [pensive](https://github.com/athola/claude-night-market/tree/main/plugins/pensive) | athola/claude-night-market | Reflective code review toolkit - domain reviews (architecture, bugs, APIs, math, Rust, tests, Makefiles) plus skill performance analysis with stabi... | None | 1.3.1 |
| [performance-optimizer](https://github.com/davila7/claude-code-templates/tree/main/) | claude-code-templates | Performance optimization suite with profiling, bundle analysis, and speed improvement tools | Daniel Avila | 1.0.0 |
| [precommit](https://github.com/bradleygolden/claude-marketplace-elixir/tree/main/plugins/precommit) | bradleygolden/claude-marketplace-elixir | Phoenix precommit alias automation - runs mix precommit before git commits if alias exists | None | 1.0.0 |
| [project-management-suite](https://github.com/davila7/claude-code-templates/tree/main/) | claude-code-templates | Project management toolkit with sprint planning, task automation, and team collaboration tools | Daniel Avila | 1.0.0 |
| [sanctum](https://github.com/athola/claude-night-market/tree/main/plugins/sanctum) | athola/claude-night-market | Git and workspace operations - commit messages, PR prep, documentation updates, version bumping | None | 1.3.1 |
| [scry](https://github.com/athola/claude-night-market/tree/main/plugins/scry) | athola/claude-night-market | Media generation - terminal recordings (VHS), browser recordings (Playwright), GIF processing, and media composition | None | 1.3.1 |
| [security-pro](https://github.com/davila7/claude-code-templates/tree/main/) | claude-code-templates | Enterprise security toolkit with auditing, penetration testing, and compliance automation | Daniel Avila | 1.0.0 |
| [sobelow](https://github.com/bradleygolden/claude-marketplace-elixir/tree/main/plugins/sobelow) | bradleygolden/claude-marketplace-elixir | Sobelow security-focused static analysis for Phoenix and Elixir projects | None | 1.0.0 |
| [spec-kit](https://github.com/athola/claude-night-market/tree/main/plugins/spec-kit) | athola/claude-night-market | Specification-driven development - spec writing, implementation planning, and task orchestration | None | 1.3.1 |
| [supabase-toolkit](https://github.com/davila7/claude-code-templates/tree/main/) | claude-code-templates | Complete Supabase workflow with specialized commands, data engineering agents, and MCP integrations | Daniel Avila | 1.0.0 |
| [superpowers](https://github.com/obra/superpowers.git) | superpowers-marketplace | Core skills library: TDD, debugging, collaboration patterns, and proven techniques | None | 4.0.3 |
| [superpowers](https://github.com/obra/superpowers/tree/main/) | superpowers-dev | Core skills library for Claude Code: TDD, debugging, collaboration patterns, and proven techniques | Jesse Vincent | 4.0.3 |
| [superpowers-chrome](https://github.com/obra/superpowers-chrome.git) | superpowers-marketplace | BETA: VERY LIGHTLY TESTED - Direct Chrome DevTools Protocol access via 'browsing' skill. Skill mode (17 CLI commands) + MCP mode (single use_browse... | None | 1.6.2 |
| [superpowers-developing-for-claude-code](https://github.com/obra/superpowers-developing-for-claude-code.git) | superpowers-marketplace | Skills and resources for developing Claude Code plugins, skills, MCP servers, and extensions. Includes comprehensive official documentation and sel... | None | 0.3.1 |
| [superpowers-lab](https://github.com/obra/superpowers-lab.git) | superpowers-marketplace | Experimental skills for Superpowers: Control interactive CLI tools (vim, menuconfig, REPLs, git rebase -i) through tmux automation | None | 0.1.0 |
| [testing-suite](https://github.com/davila7/claude-code-templates/tree/main/) | claude-code-templates | Comprehensive testing toolkit with E2E, unit, integration, and visual testing automation | Daniel Avila | 1.0.0 |
| [trading-ideas](https://github.com/quant-sentiment-ai/claude-equity-research/tree/main/trading-ideas.md) | claude-equity-research-marketplace | Institutional-grade equity research reports via /trading-ideas command. Analyzes company financials, technical indicators, market positioning, insi... | quant-sentiment-ai | 1.0.0 |
| [video-processor](https://github.com/iamzhihuix/happy-claude-skills/tree/main/) | iamzhihuix/happy-claude-skills | Download and process videos from YouTube with audio extraction, format conversion, and Whisper transcription | None | 1.0.0 |
| [wechat-article-writer](https://github.com/iamzhihuix/happy-claude-skills/tree/main/) | iamzhihuix/happy-claude-skills | WeChat article writing workflow with research, writing, title generation, and formatting optimization | None | 1.0.0 |

## Workflow Orchestration

| Plugin | Marketplace | Description | Author | Version |
|--------|-------------|-------------|--------|---------|
| [angelos-symbo](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/angelos-symbo) | awesome-claude-code-plugins | Use this agent when you need to create or convert prompts using the SYMBO (symbolic) notation system. This agent MUST be activated whenever generat... | normalnormie | 1.0.0 |
| [ceo-quality-controller-agent](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/ceo-quality-controller-agent) | awesome-claude-code-plugins | Universal quality control orchestrator and final authority for any software development project. Dynamically discovers and coordinates with availab... | Beau Lewis | 1.0.0 |
| [claude-desktop-extension](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/claude-desktop-extension) | awesome-claude-code-plugins | This command provides the context necessary for Claude Code to create the Desktop Extension or .dxt file of an MCP. |  Anand Tyagi | 1.0.0 |
| [lyra](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/lyra) | awesome-claude-code-plugins | Lyra - a master-level AI prompt optimization specialist. |  Anand Tyagi | 1.0.0 |
| [model-context-protocol-mcp-expert](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/model-context-protocol-mcp-expert) | awesome-claude-code-plugins | Model Context Protocol Mcp Expert subagent | Community | 1.0.0 |
| [problem-solver-specialist](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/problem-solver-specialist) | awesome-claude-code-plugins | Universal expert problem-solving agent specializing in complex debugging, mysterious runtime behavior, integration issues, and multi-layered techni... | Beau Lewis | 1.0.0 |
| [studio-coach](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/studio-coach) | awesome-claude-code-plugins | PROACTIVELY use this agent when complex multi-agent tasks begin, when agents seem stuck or overwhelmed, or when the team needs motivation and coord... | Michael Galpert | 1.0.0 |
| [ultrathink](https://github.com/ccplugins/awesome-claude-code-plugins/tree/main/plugins/ultrathink) | awesome-claude-code-plugins | Use /ultrathink <TASK_DESCRIPTION> to launch a Coordinator Agent that directs four specialist sub-agents—Architect, Research, Coder, and Tester—to ... | Jeronim Morina | 1.0.0 |

## abap

| Plugin | Marketplace | Description | Author | Version |
|--------|-------------|-------------|--------|---------|
| [sap-abap](https://github.com/secondsky/sap-skills/tree/main/plugins/sap-abap) | secondsky/sap-skills | Comprehensive ABAP development skill for SAP systems. Use when writing ABAP code, working with internal tables, structures, ABAP SQL, object-orient... | None | 2.1.0 |
| [sap-abap-cds](https://github.com/secondsky/sap-skills/tree/main/plugins/sap-abap-cds) | secondsky/sap-skills | Comprehensive SAP ABAP CDS (Core Data Services) reference for data modeling, view development, and semantic enrichment. Use when creating CDS views... | None | 2.1.0 |

## accessibility

| Plugin | Marketplace | Description | Author | Version |
|--------|-------------|-------------|--------|---------|
| [accessibility-compliance](https://github.com/wshobson/agents/tree/main/plugins/accessibility-compliance) | claude-code-workflows | WCAG accessibility auditing, compliance validation, UI testing for screen readers, keyboard navigation, and inclusive design | Seth Hobson | 1.2.1 |

## agents

| Plugin | Marketplace | Description | Author | Version |
|--------|-------------|-------------|--------|---------|
| [accessibility-expert](https://github.com/ccplugins/awesome-claude-code-plugins) | awesome-claude-code-plugins | Examples: | Alysson Franklin | 1.0.0 |
| [accessibility-expert](https://github.com/ananddtyagi/claude-code-marketplace/tree/main/plugins/accessibility-expert) | cc-marketplace | Examples: | Alysson Franklin | 1.0.0 |
| [ai-engineer](https://github.com/ananddtyagi/claude-code-marketplace/tree/main/plugins/ai-engineer) | cc-marketplace | Use this agent when implementing AI/ML features, integrating language models, building recommendation systems, or adding intelligent automation to ... | Michael Galpert | 1.0.0 |
| [ai-ethics-governance-specialist](https://github.com/ananddtyagi/claude-code-marketplace/tree/main/plugins/ai-ethics-governance-specialist) | cc-marketplace | Use this agent when you need to implement AI ethics frameworks, governance policies, and responsible AI practices for B2B applications. This agent ... | Alysson Franklin | 1.0.0 |
| [analytics-reporter](https://github.com/ananddtyagi/claude-code-marketplace/tree/main/plugins/analytics-reporter) | cc-marketplace | Use this agent when analyzing metrics, generating insights from data, creating performance reports, or making data-driven recommendations. This age... | Michael Galpert | 1.0.0 |
| [angelos-symbo](https://github.com/ananddtyagi/claude-code-marketplace/tree/main/plugins/angelos-symbo) | cc-marketplace | Use this agent when you need to create or convert prompts using the SYMBO (symbolic) notation system. This agent MUST be activated whenever generat... | normalnormie | 1.0.0 |
| [api-integration-specialist](https://github.com/ananddtyagi/claude-code-marketplace/tree/main/plugins/api-integration-specialist) | cc-marketplace | Use this agent when you need to design and implement internal API architecture, developer experience, and API infrastructure for B2B applications. ... | Alysson Franklin | 1.0.0 |
| [api-tester](https://github.com/ananddtyagi/claude-code-marketplace/tree/main/plugins/api-tester) | cc-marketplace | Use this agent for comprehensive API testing including performance testing, load testing, and contract testing. This agent specializes in ensuring ... | Michael Galpert | 1.0.0 |
| [app-store-optimizer](https://github.com/ananddtyagi/claude-code-marketplace/tree/main/plugins/app-store-optimizer) | cc-marketplace | Use this agent when preparing app store listings, researching keywords, optimizing app metadata, improving conversion rates, or analyzing app store... | Michael Galpert | 1.0.0 |
| [b2b-project-shipper](https://github.com/ananddtyagi/claude-code-marketplace) | cc-marketplace | PROACTIVELY use this agent when approaching B2B launch milestones, enterprise release deadlines, or B2B go-to-market activities. This agent special... | Alysson Franklin | 1.0.0 |
| [backend-architect](https://github.com/ananddtyagi/claude-code-marketplace) | cc-marketplace | Use this agent when designing APIs, building server-side logic, implementing databases, or architecting scalable backend systems. This agent specia... | Michael Galpert | 1.0.0 |
| [brand-guardian](https://github.com/ananddtyagi/claude-code-marketplace) | cc-marketplace | Use this agent when establishing brand guidelines, ensuring visual consistency, managing brand assets, or evolving brand identity. This agent speci... | Michael Galpert | 1.0.0 |
| [ceo-quality-controller-agent](https://github.com/ananddtyagi/claude-code-marketplace) | cc-marketplace | Universal quality control orchestrator and final authority for any software development project. Dynamically discovers and coordinates with availab... | Beau Lewis | 1.0.0 |
| [changelog-generator](https://github.com/ananddtyagi/claude-code-marketplace) | cc-marketplace | Changelog Generator subagent | Joe Heitzeberg | 1.0.0 |
| [code-architect](https://github.com/ananddtyagi/claude-code-marketplace) | cc-marketplace | Use this agent when you need to design scalable architecture and folder structures for new features or projects. Examples include: when starting a ... | abhishek shah | 1.0.0 |
| [code-reviewer](https://github.com/ananddtyagi/claude-code-marketplace) | cc-marketplace | Expert code review specialist. Proactively reviews code for quality, security, and maintainability. Use immediately after writing or modifying code. | Anand Tyagi | 1.0.0 |
| [codebase-documenter](https://github.com/ananddtyagi/claude-code-marketplace) | cc-marketplace | Use this agent when you need to analyze a service or codebase component and create comprehensive documentation in CLAUDE.md files. This agent shoul... | Anand Tyagi | 1.0.0 |
| [compliance-automation-specialist](https://github.com/ananddtyagi/claude-code-marketplace) | cc-marketplace | Use this agent when you need to automate compliance processes for SOC 2, ISO 27001, GDPR, HIPAA, and other enterprise regulatory requirements. This... | Alysson Franklin | 1.0.0 |
| [content-creator](https://github.com/ananddtyagi/claude-code-marketplace) | cc-marketplace | Content Creator subagent | Michael Galpert | 1.0.0 |
| [context7-docs-fetcher](https://github.com/ananddtyagi/claude-code-marketplace) | cc-marketplace | Use this agent when you need to fetch and utilize documentation from Context7 for specific libraries or frameworks. Examples: <example>Context: Use... | normalnormie | 1.0.0 |
| [customer-success-manager](https://github.com/ananddtyagi/claude-code-marketplace) | cc-marketplace | Use this agent when you need to optimize customer success operations for B2B enterprise clients. This agent specializes in customer health monitori... | Alysson Franklin | 1.0.0 |
| [data-privacy-engineer](https://github.com/ananddtyagi/claude-code-marketplace) | cc-marketplace | Use this agent when you need to implement data privacy engineering, GDPR compliance, data protection frameworks, and privacy-by-design principles f... | Alysson Franklin | 1.0.0 |
| [data-scientist](https://github.com/ananddtyagi/claude-code-marketplace) | cc-marketplace | Data analysis expert for SQL queries, BigQuery operations, and data insights. Use proactively for data analysis tasks and queries. | Anand Tyagi | 1.0.0 |
| [database-performance-optimizer](https://github.com/ananddtyagi/claude-code-marketplace) | cc-marketplace | Use this agent when you need to optimize database performance for B2B applications at enterprise scale. This agent specializes in multi-tenant data... | Alysson Franklin | 1.0.0 |
| [debugger](https://github.com/ananddtyagi/claude-code-marketplace) | cc-marketplace | Debugging specialist for errors, test failures, and unexpected behavior. Use proactively when encountering any issues. | Anand Tyagi | 1.0.0 |
| [deployment-engineer](https://github.com/ananddtyagi/claude-code-marketplace) | cc-marketplace | Use this agent when setting up CI/CD pipelines, configuring Docker containers, deploying applications to cloud platforms, setting up Kubernetes clu... | Jure Šunić | 1.0.0 |
| [desktop-app-dev](https://github.com/ananddtyagi/claude-code-marketplace) | cc-marketplace | Desktop App Dev subagent | safayavatsal | 1.0.0 |
| [devops-automator](https://github.com/ananddtyagi/claude-code-marketplace) | cc-marketplace | Use this agent when setting up CI/CD pipelines, configuring cloud infrastructure, implementing monitoring systems, or automating deployment process... | Michael Galpert | 1.0.0 |
| [enterprise-integrator-architect](https://github.com/ananddtyagi/claude-code-marketplace) | cc-marketplace | Use this agent when you need to design and implement complex external enterprise system integrations for B2B applications. This agent specializes i... | Alysson Franklin | 1.0.0 |
| [enterprise-onboarding-specialist](https://github.com/ananddtyagi/claude-code-marketplace) | cc-marketplace | Use this agent when you need to design and optimize complex enterprise customer onboarding processes involving multiple stakeholders, change manage... | Alysson Franklin | 1.0.0 |
| [enterprise-security-reviewer](https://github.com/ananddtyagi/claude-code-marketplace) | cc-marketplace | Use this agent for comprehensive B2B security assessments, enterprise compliance validation, multi-tenant security reviews, and security audit prep... | Alysson Franklin | 1.0.0 |
| [experiment-tracker](https://github.com/ananddtyagi/claude-code-marketplace) | cc-marketplace | PROACTIVELY use this agent when experiments are started, modified, or when results need analysis. This agent specializes in tracking A/B tests, fea... | Michael Galpert | 1.0.0 |
| [feedback-synthesizer](https://github.com/ananddtyagi/claude-code-marketplace) | cc-marketplace | Use this agent when you need to analyze user feedback from multiple sources, identify patterns in user complaints or requests, synthesize insights ... | Michael Galpert | 1.0.0 |
| [finance-tracker](https://github.com/ananddtyagi/claude-code-marketplace) | cc-marketplace | Use this agent when managing budgets, optimizing costs, forecasting revenue, or analyzing financial performance. This agent excels at transforming ... | Michael Galpert | 1.0.0 |
| [flutter-mobile-app-dev](https://github.com/ananddtyagi/claude-code-marketplace) | cc-marketplace | Use this agent when you need expert assistance with Flutter mobile development tasks, including code analysis, widget creation, debugging, performa... | safayavatsal | 1.0.0 |
| [frontend-developer](https://github.com/ananddtyagi/claude-code-marketplace) | cc-marketplace | Use this agent when building user interfaces, implementing React/Vue/Angular components, handling state management, or optimizing frontend performa... | Michael Galpert | 1.0.0 |
| [growth-hacker](https://github.com/ananddtyagi/claude-code-marketplace) | cc-marketplace | Growth Hacker subagent | Michael Galpert | 1.0.0 |
| [infrastructure-maintainer](https://github.com/ananddtyagi/claude-code-marketplace) | cc-marketplace | Use this agent when monitoring system health, optimizing performance, managing scaling, or ensuring infrastructure reliability. This agent excels a... | Michael Galpert | 1.0.0 |
| [instagram-curator](https://github.com/ananddtyagi/claude-code-marketplace) | cc-marketplace | Instagram Curator subagent | Michael Galpert | 1.0.0 |
| [joker](https://github.com/ananddtyagi/claude-code-marketplace) | cc-marketplace | Use this agent when you need to lighten the mood, create funny content, or add humor to any situation. This agent specializes in dad jokes, program... | Michael Galpert | 1.0.0 |
| [legal-advisor](https://github.com/ananddtyagi/claude-code-marketplace) | cc-marketplace | Use this agent when you need legal advisory, compliance documentation, RFP response creation, and enterprise contract support for B2B applications.... | Alysson Franklin | 1.0.0 |
| [legal-compliance-checker](https://github.com/ananddtyagi/claude-code-marketplace) | cc-marketplace | Use this agent when reviewing terms of service, privacy policies, ensuring regulatory compliance, or handling legal requirements. This agent excels... | Michael Galpert | 1.0.0 |
| [mobile-app-builder](https://github.com/ananddtyagi/claude-code-marketplace) | cc-marketplace | Use this agent when developing native iOS or Android applications, implementing React Native features, or optimizing mobile performance. This agent... | Michael Galpert | 1.0.0 |
| [mobile-ux-optimizer](https://github.com/ananddtyagi/claude-code-marketplace) | cc-marketplace | Use this agent when you need to optimize UI/UX components or interfaces for mobile-first experiences, analyze existing design themes, or ensure mob... | abhishek shah | 1.0.0 |
| [model-context-protocol-mcp-expert](https://github.com/ananddtyagi/claude-code-marketplace) | cc-marketplace | Model Context Protocol Mcp Expert subagent | Community | 1.0.0 |
| [monitoring-observability-specialist](https://github.com/ananddtyagi/claude-code-marketplace) | cc-marketplace | Use this agent when you need to implement comprehensive monitoring, observability, and alerting systems for enterprise B2B applications. This agent... | Alysson Franklin | 1.0.0 |
| [n8n-workflow-builder](https://github.com/ananddtyagi/claude-code-marketplace) | cc-marketplace | Use this agent when you need to design, build, or validate n8n automation workflows. This agent specializes in creating efficient n8n workflows usi... | Jure Šunić | 1.0.0 |
| [onomastophes](https://github.com/ananddtyagi/claude-code-marketplace) | cc-marketplace | Use proactively for generating creative non-olympian Greek god names with rich backstories, mythological authenticity, and modern accessibility for... | normalnormie | 1.0.0 |
| [performance-benchmarker](https://github.com/ananddtyagi/claude-code-marketplace) | cc-marketplace | Use this agent for comprehensive performance testing, profiling, and optimization recommendations. This agent specializes in measuring speed, ident... | Michael Galpert | 1.0.0 |
| [planning-prd-agent](https://github.com/ananddtyagi/claude-code-marketplace) | cc-marketplace | 'MUST BE USED PROACTIVELY when user mentions: planning, PRD, product requirements document, project plan, roadmap, specification, requirements anal... | clouddna-au | 1.0.0 |
| [prd-specialist](https://github.com/ananddtyagi/claude-code-marketplace) | cc-marketplace | Use this agent when you need to create comprehensive Product Requirements Documents (PRDs) that combine business strategy, technical architecture, ... | Jure Šunić | 1.0.0 |
| [pricing-packaging-specialist](https://github.com/ananddtyagi/claude-code-marketplace) | cc-marketplace | Use this agent when you need to optimize B2B pricing strategies, packaging models, and revenue optimization for enterprise sales. This agent specia... | Alysson Franklin | 1.0.0 |
| [problem-solver-specialist](https://github.com/ananddtyagi/claude-code-marketplace) | cc-marketplace | Universal expert problem-solving agent specializing in complex debugging, mysterious runtime behavior, integration issues, and multi-layered techni... | Beau Lewis | 1.0.0 |
| [product-sales-specialist](https://github.com/ananddtyagi/claude-code-marketplace) | cc-marketplace | Use this agent when you need to support B2B sales through product design, user research, project management, and creative RFP responses. This agent... | Alysson Franklin | 1.0.0 |
| [project-curator](https://github.com/ananddtyagi/claude-code-marketplace) | cc-marketplace | Reorganizes project structure by cleaning root clutter, creating logical folder hierarchies, and moving files to optimal locations. Tracks dependen... | alanKerrigan | 1.0.0 |
| [project-shipper](https://github.com/ananddtyagi/claude-code-marketplace) | cc-marketplace | PROACTIVELY use this agent when approaching launch milestones, release deadlines, or go-to-market activities. This agent specializes in coordinatin... | Michael Galpert | 1.0.0 |
| [python-expert](https://github.com/ananddtyagi/claude-code-marketplace) | cc-marketplace | Use this agent when working with Python code that requires advanced features, performance optimization, or comprehensive refactoring. Examples: <ex... | Jure Šunić | 1.0.0 |
| [rapid-prototyper](https://github.com/ananddtyagi/claude-code-marketplace) | cc-marketplace | Use this agent when you need to quickly create a new application prototype, MVP, or proof-of-concept within the 6-day development cycle. This agent... | Michael Galpert | 1.0.0 |
| [react-native-dev](https://github.com/ananddtyagi/claude-code-marketplace) | cc-marketplace | Use this agent when you need expert assistance with React Native development tasks including code analysis, component creation, debugging, performa... | abhishek shah | 1.0.0 |
| [reddit-community-builder](https://github.com/ananddtyagi/claude-code-marketplace) | cc-marketplace | Reddit Community Builder subagent | Michael Galpert | 1.0.0 |
| [sprint-prioritizer](https://github.com/ananddtyagi/claude-code-marketplace) | cc-marketplace | Use this agent when planning 6-day development cycles, prioritizing features, managing product roadmaps, or making trade-off decisions. This agent ... | Michael Galpert | 1.0.0 |
| [studio-coach](https://github.com/ananddtyagi/claude-code-marketplace) | cc-marketplace | PROACTIVELY use this agent when complex multi-agent tasks begin, when agents seem stuck or overwhelmed, or when the team needs motivation and coord... | Michael Galpert | 1.0.0 |
| [studio-producer](https://github.com/ananddtyagi/claude-code-marketplace) | cc-marketplace | PROACTIVELY use this agent when coordinating across multiple teams, allocating resources, or optimizing studio workflows. This agent specializes in... | Michael Galpert | 1.0.0 |
| [support-responder](https://github.com/ananddtyagi/claude-code-marketplace) | cc-marketplace | Use this agent when handling customer support inquiries, creating support documentation, setting up automated responses, or analyzing support patte... | Michael Galpert | 1.0.0 |
| [technical-sales-engineer](https://github.com/ananddtyagi/claude-code-marketplace) | cc-marketplace | Use this agent when you need to bridge technical and sales requirements for B2B enterprise deals. This agent specializes in technical demos, POC de... | Alysson Franklin | 1.0.0 |
| [test-results-analyzer](https://github.com/ananddtyagi/claude-code-marketplace) | cc-marketplace | Use this agent for analyzing test results, synthesizing test data, identifying trends, and generating quality metrics reports. This agent specializ... | Michael Galpert | 1.0.0 |
| [test-writer-fixer](https://github.com/ananddtyagi/claude-code-marketplace) | cc-marketplace | Use this agent when code changes have been made and you need to write new tests, run existing tests, analyze failures, and fix them while maintaini... | Michael Galpert | 1.0.0 |
| [tiktok-strategist](https://github.com/ananddtyagi/claude-code-marketplace) | cc-marketplace | Use this agent when you need to create TikTok marketing strategies, develop viral content ideas, plan TikTok campaigns, or optimize for TikTok's al... | Michael Galpert | 1.0.0 |
| [tool-evaluator](https://github.com/ananddtyagi/claude-code-marketplace) | cc-marketplace | Use this agent when evaluating new development tools, frameworks, or services for the studio. This agent specializes in rapid tool assessment, comp... | Michael Galpert | 1.0.0 |
| [trend-researcher](https://github.com/ananddtyagi/claude-code-marketplace) | cc-marketplace | Use this agent when you need to identify market opportunities, analyze trending topics, research viral content, or understand emerging user behavio... | Michael Galpert | 1.0.0 |
| [twitter-engager](https://github.com/ananddtyagi/claude-code-marketplace) | cc-marketplace | Twitter Engager subagent | Michael Galpert | 1.0.0 |
| [ui-designer](https://github.com/ananddtyagi/claude-code-marketplace) | cc-marketplace | Use this agent when creating user interfaces, designing components, building design systems, or improving visual aesthetics. This agent specializes... | Michael Galpert | 1.0.0 |
| [unit-test-generator](https://github.com/ananddtyagi/claude-code-marketplace) | cc-marketplace | Expert Flutter/Dart unit test specialist that systematically improves test coverage using automated workflows with strict validation, git managemen... | Community | 1.0.0 |
| [ux-researcher](https://github.com/ananddtyagi/claude-code-marketplace) | cc-marketplace | Use this agent when conducting user research, analyzing user behavior, creating journey maps, or validating design decisions through testing. This ... | Michael Galpert | 1.0.0 |
| [vision-specialist](https://github.com/ananddtyagi/claude-code-marketplace) | cc-marketplace | Expert in vision models, OCR systems, barcode detection, and visual AI. Stays current with latest models (GPT-4V, Claude Vision, Mistral-OCR, etc.)... | alanKerrigan | 1.0.0 |
| [visual-storyteller](https://github.com/ananddtyagi/claude-code-marketplace) | cc-marketplace | Use this agent when creating visual narratives, designing infographics, building presentations, or communicating complex ideas through imagery. Thi... | Michael Galpert | 1.0.0 |
| [web-dev](https://github.com/ananddtyagi/claude-code-marketplace) | cc-marketplace | Use this agent for expert assistance with web development tasks using React, Next.js, NestJS, and other modern web frameworks with TypeScript and T... | safayavatsal | 1.0.0 |
| [whimsy-injector](https://github.com/ananddtyagi/claude-code-marketplace) | cc-marketplace | PROACTIVELY use this agent after any UI/UX changes to ensure delightful, playful elements are incorporated. This agent specializes in adding joy, s... | Michael Galpert | 1.0.0 |
| [workflow-optimizer](https://github.com/ananddtyagi/claude-code-marketplace) | cc-marketplace | Use this agent for optimizing human-agent collaboration workflows and analyzing workflow efficiency. This agent specializes in identifying bottlene... | Michael Galpert | 1.0.0 |

## ai

| Plugin | Marketplace | Description | Author | Version |
|--------|-------------|-------------|--------|---------|
| [sap-ai-core](https://github.com/secondsky/sap-skills/tree/main/plugins/sap-ai-core) | secondsky/sap-skills | Guides development with SAP AI Core and SAP AI Launchpad for enterprise AI/ML workloads on SAP BTP. Use when: deploying generative AI models (GPT, ... | None | 2.1.0 |
| [sap-cloud-sdk-ai](https://github.com/secondsky/sap-skills/tree/main/plugins/sap-cloud-sdk-ai) | secondsky/sap-skills | Integrates SAP Cloud SDK for AI into JavaScript/TypeScript and Java applications. Use when building applications with SAP AI Core, Generative AI Hu... | None | 2.1.0 |

## ai-agency

| Plugin | Marketplace | Description | Author | Version |
|--------|-------------|-------------|--------|---------|
| [discovery-questionnaire](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/ai-agency/discovery-questionnaire) | claude-code-plugins-plus | Generate custom discovery questionnaires for AI agency prospects | Claude Code Plugin Hub | 1.0.0 |
| [make-scenario-builder](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/ai-agency/make-scenario-builder) | claude-code-plugins-plus | Create Make.com (Integromat) scenarios with AI assistance | Claude Code Plugin Hub | 1.0.0 |
| [n8n-workflow-designer](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/ai-agency/n8n-workflow-designer) | claude-code-plugins-plus | Design complex n8n workflows with AI assistance - loops, branching, error handling | Claude Code Plugin Hub | 1.0.0 |
| [roi-calculator](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/ai-agency/roi-calculator) | claude-code-plugins-plus | Calculate and present ROI for AI automation projects | Claude Code Plugin Hub | 1.0.0 |
| [sow-generator](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/ai-agency/sow-generator) | claude-code-plugins-plus | Generate professional Statements of Work for AI projects | Claude Code Plugin Hub | 1.0.0 |
| [zapier-zap-builder](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/ai-agency/zapier-zap-builder) | claude-code-plugins-plus | Create multi-step Zapier Zaps with filters, paths, and formatters | Claude Code Plugin Hub | 1.0.0 |

## ai-ml

| Plugin | Marketplace | Description | Author | Version |
|--------|-------------|-------------|--------|---------|
| [agent-orchestration](https://github.com/wshobson/agents) | claude-code-workflows | Multi-agent system optimization, agent improvement workflows, and context management | Seth Hobson | 1.2.0 |
| [ai-ethics-validator](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/ai-ml/ai-ethics-validator) | claude-code-plugins-plus | AI ethics and fairness validation | Jeremy Longshore | 1.0.0 |
| [ai-experiment-logger](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/mcp/ai-experiment-logger) | claude-code-plugins-plus | Track and analyze AI experiments with a web dashboard and MCP tools | Claude Code Plugins | 1.0.0 |
| [ai-ml-engineering-pack](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/packages/ai-ml-engineering-pack) | claude-code-plugins-plus | Professional AI/ML Engineering toolkit: Prompt engineering, LLM integration, RAG systems, AI safety with 12 expert plugins | Jeremy Longshore | 1.0.0 |
| [ai-sdk-agents](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/ai-ml/ai-sdk-agents) | claude-code-plugins-plus | Multi-agent orchestration with AI SDK v5 - handoffs, routing, and coordination for any AI provider (OpenAI, Anthropic, Google) | Jeremy Longshore | 1.0.0 |
| [anomaly-detection-system](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/ai-ml/anomaly-detection-system) | claude-code-plugins-plus | Detect anomalies and outliers in data | Jeremy Longshore | 1.0.0 |
| [automl-pipeline-builder](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/ai-ml/automl-pipeline-builder) | claude-code-plugins-plus | Build AutoML pipelines | Jeremy Longshore | 1.0.0 |
| [classification-model-builder](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/ai-ml/classification-model-builder) | claude-code-plugins-plus | Build classification models | Jeremy Longshore | 1.0.0 |
| [clustering-algorithm-runner](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/ai-ml/clustering-algorithm-runner) | claude-code-plugins-plus | Run clustering algorithms on datasets | Jeremy Longshore | 1.0.0 |
| [computer-vision-processor](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/ai-ml/computer-vision-processor) | claude-code-plugins-plus | Computer vision image processing and analysis | Jeremy Longshore | 1.0.0 |
| [context-management](https://github.com/wshobson/agents) | claude-code-workflows | Context persistence, restoration, and long-running conversation management | Seth Hobson | 1.2.0 |
| [data-preprocessing-pipeline](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/ai-ml/data-preprocessing-pipeline) | claude-code-plugins-plus | Automated data preprocessing and cleaning pipelines | Jeremy Longshore | 1.0.0 |
| [data-visualization-creator](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/ai-ml/data-visualization-creator) | claude-code-plugins-plus | Create data visualizations and plots | Jeremy Longshore | 1.0.0 |
| [dataset-splitter](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/ai-ml/dataset-splitter) | claude-code-plugins-plus | Split datasets for training, validation, and testing | Jeremy Longshore | 1.0.0 |
| [deep-learning-optimizer](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/ai-ml/deep-learning-optimizer) | claude-code-plugins-plus | Deep learning optimization techniques | Jeremy Longshore | 1.0.0 |
| [deepgram-pack](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/saas-packs/deepgram-pack) | claude-code-plugins-plus | Complete Deepgram integration skill pack with 24 skills covering speech-to-text, real-time transcription, voice intelligence, and audio processing.... | Jeremy Longshore | 1.0.0 |
| [experiment-tracking-setup](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/ai-ml/experiment-tracking-setup) | claude-code-plugins-plus | Set up ML experiment tracking | Jeremy Longshore | 1.0.0 |
| [feature-engineering-toolkit](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/ai-ml/feature-engineering-toolkit) | claude-code-plugins-plus | Feature creation, selection, and transformation tools | Jeremy Longshore | 1.0.0 |
| [geepers-agents](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/community/geepers-agents) | claude-code-plugins-plus | Multi-agent orchestration system with 51 specialized agents for development workflows, code quality, deployment, research, games, and more. Include... | Luke Steuber | 1.0.0 |
| [hyperparameter-tuner](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/ai-ml/hyperparameter-tuner) | claude-code-plugins-plus | Optimize hyperparameters using grid/random/bayesian search | Jeremy Longshore | 1.0.0 |
| [jeremy-adk-orchestrator](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/ai-ml/jeremy-adk-orchestrator) | claude-code-plugins-plus | Production ADK orchestrator for A2A protocol and multi-agent coordination on Vertex AI | Jeremy Longshore | 1.0.0 |
| [jeremy-adk-software-engineer](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/ai-ml/jeremy-adk-software-engineer) | claude-code-plugins-plus | ADK software engineer for creating production-ready agents (placeholder - to be implemented) | Jeremy Longshore | 1.0.0 |
| [jeremy-gcp-starter-examples](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/ai-ml/jeremy-gcp-starter-examples) | claude-code-plugins-plus | Google Cloud starter kits and example code aggregator with ADK samples | Jeremy Longshore | 1.0.0 |
| [jeremy-genkit-pro](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/ai-ml/jeremy-genkit-pro) | claude-code-plugins-plus | Firebase Genkit expert for production-ready AI workflows with RAG and tool calling | Jeremy Longshore | 1.0.0 |
| [jeremy-google-adk](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/jeremy-google-adk) | claude-code-plugins-plus | Google Agent Development Kit (ADK) SDK starter kit for building Claude-powered AI agents with React patterns, multi-agent orchestration, and tool i... | Jeremy Longshore | 1.0.0 |
| [jeremy-vertex-ai](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/jeremy-vertex-ai) | claude-code-plugins-plus | Comprehensive Vertex AI integration plugin for building generative AI agents with Gemini, Vertex AI Studio, and production deployment on Google Cloud | Jeremy Longshore | 1.0.0 |
| [jeremy-vertex-engine](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/ai-ml/jeremy-vertex-engine) | claude-code-plugins-plus | Vertex AI Agent Engine deployment inspector and runtime validator | Jeremy Longshore | 1.0.0 |
| [jeremy-vertex-validator](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/ai-ml/jeremy-vertex-validator) | claude-code-plugins-plus | Production readiness validator for Vertex AI deployments and configurations | Jeremy Longshore | 1.0.0 |
| [langchain-pack](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/saas-packs/langchain-pack) | claude-code-plugins-plus | Complete LangChain integration skill pack with 24 skills covering chains, agents, RAG pipelines, memory, and LLM application development. Flagship ... | Jeremy Longshore | 1.0.0 |
| [lindy-pack](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/saas-packs/lindy-pack) | claude-code-plugins-plus | Complete Lindy integration skill pack with 24 skills covering AI assistants, task automation, workflows, and intelligent automation. Flagship tier ... | Jeremy Longshore | 1.0.0 |
| [llm-application-dev](https://github.com/wshobson/agents) | claude-code-workflows | LLM application development with LangGraph, RAG systems, vector search, and AI agent architectures for Claude 4.5 and GPT-5.2 | Seth Hobson | 2.0.2 |
| [machine-learning-ops](https://github.com/wshobson/agents) | claude-code-workflows | ML model training pipelines, hyperparameter tuning, model deployment automation, experiment tracking, and MLOps workflows | Seth Hobson | 1.2.1 |
| [ml-model-trainer](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/ai-ml/ml-model-trainer) | claude-code-plugins-plus | Train and optimize machine learning models with automated workflows | Jeremy Longshore | 1.0.0 |
| [model-deployment-helper](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/ai-ml/model-deployment-helper) | claude-code-plugins-plus | Deploy ML models to production | Jeremy Longshore | 1.0.0 |
| [model-evaluation-suite](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/ai-ml/model-evaluation-suite) | claude-code-plugins-plus | Comprehensive model evaluation with multiple metrics | Jeremy Longshore | 1.0.0 |
| [model-explainability-tool](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/ai-ml/model-explainability-tool) | claude-code-plugins-plus | Model interpretability and explainability | Jeremy Longshore | 1.0.0 |
| [model-versioning-tracker](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/ai-ml/model-versioning-tracker) | claude-code-plugins-plus | Track and manage model versions | Jeremy Longshore | 1.0.0 |
| [neural-network-builder](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/ai-ml/neural-network-builder) | claude-code-plugins-plus | Build and configure neural network architectures | Jeremy Longshore | 1.0.0 |
| [nlp-text-analyzer](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/ai-ml/nlp-text-analyzer) | claude-code-plugins-plus | Natural language processing and text analysis | Jeremy Longshore | 1.0.0 |
| [ollama-local-ai](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/ai-ml/ollama-local-ai) | claude-code-plugins-plus | Run AI models locally with Ollama - free alternative to OpenAI, Anthropic, and other paid LLM APIs. Zero-cost, privacy-first AI infrastructure. | Jeremy Longshore | 1.0.0 |
| [recommendation-engine](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/ai-ml/recommendation-engine) | claude-code-plugins-plus | Build recommendation systems and engines | Jeremy Longshore | 1.0.0 |
| [regression-analysis-tool](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/ai-ml/regression-analysis-tool) | claude-code-plugins-plus | Regression analysis and modeling | Jeremy Longshore | 1.0.0 |
| [sentiment-analysis-tool](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/ai-ml/sentiment-analysis-tool) | claude-code-plugins-plus | Sentiment analysis on text data | Jeremy Longshore | 1.0.0 |
| [time-series-forecaster](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/ai-ml/time-series-forecaster) | claude-code-plugins-plus | Time series forecasting and analysis | Jeremy Longshore | 1.0.0 |
| [transfer-learning-adapter](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/ai-ml/transfer-learning-adapter) | claude-code-plugins-plus | Transfer learning adaptation | Jeremy Longshore | 1.0.0 |

## api

| Plugin | Marketplace | Description | Author | Version |
|--------|-------------|-------------|--------|---------|
| [api-scaffolding](https://github.com/wshobson/agents) | claude-code-workflows | REST and GraphQL API scaffolding, framework selection, backend architecture, and API generation | Seth Hobson | 1.2.1 |
| [api-testing-observability](https://github.com/wshobson/agents) | claude-code-workflows | API testing automation, request mocking, OpenAPI documentation generation, observability setup, and monitoring | Seth Hobson | 1.2.0 |

## api-development

| Plugin | Marketplace | Description | Author | Version |
|--------|-------------|-------------|--------|---------|
| [api-authentication-builder](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/api-development/api-authentication-builder) | claude-code-plugins-plus | Build authentication systems with JWT, OAuth2, and API keys | Jeremy Longshore | 1.0.0 |
| [api-batch-processor](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/api-development/api-batch-processor) | claude-code-plugins-plus | Implement batch API operations with bulk processing and job queues | Jeremy Longshore | 1.0.0 |
| [api-cache-manager](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/api-development/api-cache-manager) | claude-code-plugins-plus | Implement caching strategies with Redis, CDN, and HTTP headers | Jeremy Longshore | 1.0.0 |
| [api-contract-generator](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/api-development/api-contract-generator) | claude-code-plugins-plus | Generate API contracts for consumer-driven contract testing | Jeremy Longshore | 1.0.0 |
| [api-documentation-generator](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/api-development/api-documentation-generator) | claude-code-plugins-plus | Generate comprehensive API documentation from OpenAPI/Swagger specs | Jeremy Longshore | 1.0.0 |
| [api-error-handler](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/api-development/api-error-handler) | claude-code-plugins-plus | Implement standardized error handling with proper HTTP status codes | Jeremy Longshore | 1.0.0 |
| [api-event-emitter](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/api-development/api-event-emitter) | claude-code-plugins-plus | Implement event-driven APIs with message queues and event streaming | Jeremy Longshore | 1.0.0 |
| [api-gateway-builder](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/api-development/api-gateway-builder) | claude-code-plugins-plus | Build API gateway with routing, authentication, and rate limiting | Jeremy Longshore | 1.0.0 |
| [api-load-tester](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/api-development/api-load-tester) | claude-code-plugins-plus | Load test APIs with k6, Gatling, or Artillery | Jeremy Longshore | 1.0.0 |
| [api-migration-tool](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/api-development/api-migration-tool) | claude-code-plugins-plus | Migrate APIs between versions with backward compatibility | Jeremy Longshore | 1.0.0 |
| [api-mock-server](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/api-development/api-mock-server) | claude-code-plugins-plus | Create mock API servers from OpenAPI specs for testing | Jeremy Longshore | 1.0.0 |
| [api-monitoring-dashboard](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/api-development/api-monitoring-dashboard) | claude-code-plugins-plus | Create monitoring dashboards for API health, metrics, and alerts | Jeremy Longshore | 1.0.0 |
| [api-rate-limiter](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/api-development/api-rate-limiter) | claude-code-plugins-plus | Implement rate limiting with token bucket, sliding window, and Redis | Jeremy Longshore | 1.0.0 |
| [api-request-logger](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/api-development/api-request-logger) | claude-code-plugins-plus | Log API requests with structured logging and correlation IDs | Jeremy Longshore | 1.0.0 |
| [api-response-validator](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/api-development/api-response-validator) | claude-code-plugins-plus | Validate API responses against schemas and contracts | Jeremy Longshore | 1.0.0 |
| [api-schema-validator](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/api-development/api-schema-validator) | claude-code-plugins-plus | Validate API schemas with JSON Schema, Joi, Yup, or Zod | Jeremy Longshore | 1.0.0 |
| [api-sdk-generator](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/api-development/api-sdk-generator) | claude-code-plugins-plus | Generate client SDKs from OpenAPI specs for multiple languages | Jeremy Longshore | 1.0.0 |
| [api-security-scanner](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/api-development/api-security-scanner) | claude-code-plugins-plus | Scan APIs for security vulnerabilities and OWASP API Top 10 | Jeremy Longshore | 1.0.0 |
| [api-throttling-manager](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/api-development/api-throttling-manager) | claude-code-plugins-plus | Manage API throttling with dynamic rate limits and quota management | Jeremy Longshore | 1.0.0 |
| [api-versioning-manager](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/api-development/api-versioning-manager) | claude-code-plugins-plus | Manage API versions with migration strategies and backward compatibility | Jeremy Longshore | 1.0.0 |
| [graphql-server-builder](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/api-development/graphql-server-builder) | claude-code-plugins-plus | Build GraphQL servers with schema-first design, resolvers, and subscriptions | Jeremy Longshore | 1.0.0 |
| [grpc-service-generator](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/api-development/grpc-service-generator) | claude-code-plugins-plus | Generate gRPC services with Protocol Buffers and streaming support | Jeremy Longshore | 1.0.0 |
| [rest-api-generator](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/api-development/rest-api-generator) | claude-code-plugins-plus | Generate RESTful APIs from schemas with proper routing, validation, and documentation | Jeremy Longshore | 1.0.0 |
| [webhook-handler-creator](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/api-development/webhook-handler-creator) | claude-code-plugins-plus | Create secure webhook endpoints with signature verification and retry logic | Jeremy Longshore | 1.0.0 |
| [websocket-server-builder](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/api-development/websocket-server-builder) | claude-code-plugins-plus | Build WebSocket servers for real-time bidirectional communication | Jeremy Longshore | 1.0.0 |

## assets

| Plugin | Marketplace | Description | Author | Version |
|--------|-------------|-------------|--------|---------|
| [llm-icon-finder](https://github.com/daymade/claude-code-skills/tree/main/) | daymade/claude-code-skills | Find and access AI/LLM model brand icons from lobe-icons library in SVG/PNG/WEBP formats | None | 1.0.0 |

## automation

| Plugin | Marketplace | Description | Author | Version |
|--------|-------------|-------------|--------|---------|
| [mattyp-changelog](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/automation/mattyp-changelog) | claude-code-plugins-plus | Automates changelog generation from git history with config validation and quality scoring. Use when publishing weekly updates, release notes, or P... | Mattyp | 0.1.0 |
| [n8n-mcp-skills](https://github.com/czlonkowski/n8n-skills/tree/main/) | czlonkowski/n8n-skills | Complete bundle: 7 expert skills for building flawless n8n workflows using n8n-mcp MCP server. Includes skills for expression syntax, MCP tools usa... | Romuald Członkowski | 1.0.0 |
| [workflow-orchestrator](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/mcp/workflow-orchestrator) | claude-code-plugins-plus | DAG-based workflow automation with parallel task execution and dependency management | Jeremy Longshore | 1.0.0 |

## blockchain

| Plugin | Marketplace | Description | Author | Version |
|--------|-------------|-------------|--------|---------|
| [blockchain-web3](https://github.com/wshobson/agents) | claude-code-workflows | Smart contract development with Solidity, DeFi protocol implementation, NFT platforms, and Web3 application architecture | Seth Hobson | 1.2.1 |

## btp

| Plugin | Marketplace | Description | Author | Version |
|--------|-------------|-------------|--------|---------|
| [sap-btp-best-practices](https://github.com/secondsky/sap-skills/tree/main/plugins/sap-btp-best-practices) | secondsky/sap-skills | Production-ready SAP BTP best practices for enterprise architecture, account management, security, and operations. Use when planning BTP implementa... | None | 2.1.0 |
| [sap-btp-build-work-zone-advanced](https://github.com/secondsky/sap-skills/tree/main/plugins/sap-btp-build-work-zone-advanced) | secondsky/sap-skills | Develops and administers SAP Build Work Zone, advanced edition digital workplace solutions. Use when creating workspaces, workpages, and collaborat... | None | 2.1.0 |
| [sap-btp-business-application-studio](https://github.com/secondsky/sap-skills/tree/main/plugins/sap-btp-business-application-studio) | secondsky/sap-skills | This skill provides comprehensive guidance for SAP Business Application Studio (BAS), the cloud-based IDE on SAP BTP built on Code-OSS. Use when se... | None | 2.1.0 |
| [sap-btp-cias](https://github.com/secondsky/sap-skills/tree/main/plugins/sap-btp-cias) | secondsky/sap-skills | SAP BTP Cloud Integration Automation Service (CIAS) skill for guided integration workflows. Use when: setting up CIAS subscriptions, configuring de... | None | 2.1.0 |
| [sap-btp-cloud-logging](https://github.com/secondsky/sap-skills/tree/main/plugins/sap-btp-cloud-logging) | secondsky/sap-skills | This skill provides comprehensive guidance for SAP Cloud Logging service on SAP BTP. Use when setting up Cloud Logging instances, configuring log i... | None | 2.1.0 |
| [sap-btp-cloud-platform](https://github.com/secondsky/sap-skills/tree/main/plugins/sap-btp-cloud-platform) | secondsky/sap-skills | Comprehensive SAP Business Technology Platform (BTP) reference for cloud development, deployment, and operations. Use when setting up BTP accounts ... | None | 2.1.0 |
| [sap-btp-cloud-transport-management](https://github.com/secondsky/sap-skills/tree/main/plugins/sap-btp-cloud-transport-management) | secondsky/sap-skills | Comprehensive skill for SAP Cloud Transport Management service on SAP BTP. Use when setting up transport landscapes, configuring transport nodes an... | None | 2.1.0 |
| [sap-btp-connectivity](https://github.com/secondsky/sap-skills/tree/main/plugins/sap-btp-connectivity) | secondsky/sap-skills | This skill provides comprehensive knowledge for SAP BTP Connectivity, including the Destination Service, Connectivity Service, Cloud Connector, Con... | None | 2.1.0 |
| [sap-btp-developer-guide](https://github.com/secondsky/sap-skills/tree/main/plugins/sap-btp-developer-guide) | secondsky/sap-skills | Develops business applications on SAP Business Technology Platform (BTP) using CAP (Node.js/Java) or ABAP Cloud.  Use when: building cloud applicat... | None | 2.1.0 |
| [sap-btp-integration-suite](https://github.com/secondsky/sap-skills/tree/main/plugins/sap-btp-integration-suite) | secondsky/sap-skills | Develops and operates enterprise integration solutions using SAP Integration Suite on Business Technology Platform. Covers Cloud Integration (iFlow... | None | 2.1.0 |
| [sap-btp-intelligent-situation-automation](https://github.com/secondsky/sap-skills/tree/main/plugins/sap-btp-intelligent-situation-automation) | secondsky/sap-skills | This skill provides comprehensive guidance for SAP BTP Intelligent Situation Automation setup, configuration, and operations. It should be used whe... | None | 2.1.0 |
| [sap-btp-job-scheduling](https://github.com/secondsky/sap-skills/tree/main/plugins/sap-btp-job-scheduling) | secondsky/sap-skills | This skill provides comprehensive guidance for SAP BTP Job Scheduling Service development, configuration, and operations. It should be used when cr... | None | 2.1.0 |
| [sap-btp-master-data-integration](https://github.com/secondsky/sap-skills/tree/main/plugins/sap-btp-master-data-integration) | secondsky/sap-skills | Configures and integrates SAP Master Data Integration (MDI) service on SAP Business Technology Platform. Use when setting up MDI tenants, connectin... | None | 2.1.0 |
| [sap-btp-service-manager](https://github.com/secondsky/sap-skills/tree/main/plugins/sap-btp-service-manager) | secondsky/sap-skills | This skill provides comprehensive knowledge for SAP Service Manager on SAP Business Technology Platform (BTP). It should be used when managing serv... | None | 2.1.0 |

## business

| Plugin | Marketplace | Description | Author | Version |
|--------|-------------|-------------|--------|---------|
| [business-analytics](https://github.com/wshobson/agents) | claude-code-workflows | Business metrics analysis, KPI tracking, financial reporting, and data-driven decision making | Seth Hobson | 1.2.1 |
| [customer-sales-automation](https://github.com/wshobson/agents) | claude-code-workflows | Customer support workflow automation, sales pipeline management, email campaigns, and CRM integration | Seth Hobson | 1.2.0 |
| [hr-legal-compliance](https://github.com/wshobson/agents) | claude-code-workflows | HR policy documentation, legal compliance templates (GDPR/SOC2/HIPAA), employment contracts, and regulatory documentation | Seth Hobson | 1.2.1 |
| [startup-business-analyst](https://github.com/wshobson/agents) | claude-code-workflows | Comprehensive startup business analysis with market sizing (TAM/SAM/SOM), financial modeling, team planning, and strategic research for early-stage... | Seth Hobson | 1.0.3 |

## business-marketing

| Plugin | Marketplace | Description | Author | Version |
|--------|-------------|-------------|--------|---------|
| [brand-guidelines](https://github.com/ComposioHQ/awesome-claude-skills/tree/master/brand-guidelines) | awesome-claude-skills | Applies Anthropic's official brand colors and typography to artifacts for consistent visual identity and professional design standards. | None | 1.0.0 |
| [competitive-ads-extractor](https://github.com/ComposioHQ/awesome-claude-skills/tree/master/competitive-ads-extractor) | awesome-claude-skills | Extracts and analyzes competitors' ads from ad libraries to understand messaging and creative approaches that resonate. | None | 1.0.0 |
| [domain-name-brainstormer](https://github.com/ComposioHQ/awesome-claude-skills/tree/master/domain-name-brainstormer) | awesome-claude-skills | Generates creative domain name ideas and checks availability across multiple TLDs including .com, .io, .dev, and .ai extensions. | None | 1.0.0 |
| [internal-comms](https://github.com/ComposioHQ/awesome-claude-skills/tree/master/internal-comms) | awesome-claude-skills | Helps write internal communications including 3P updates, company newsletters, FAQs, status reports, and project updates using company-specific for... | None | 1.0.0 |
| [lead-research-assistant](https://github.com/ComposioHQ/awesome-claude-skills/tree/master/lead-research-assistant) | awesome-claude-skills | Identifies and qualifies high-quality leads by analyzing your product, searching for target companies, and providing actionable outreach strategies. | None | 1.0.0 |

## business-tools

| Plugin | Marketplace | Description | Author | Version |
|--------|-------------|-------------|--------|---------|
| [apollo-pack](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/saas-packs/apollo-pack) | claude-code-plugins-plus | Complete Apollo integration skill pack with 24 skills covering sales engagement, prospecting, sequencing, analytics, and outbound automation. Flags... | Jeremy Longshore | 1.0.0 |
| [brand-strategy-framework](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/business-tools/brand-strategy-framework) | claude-code-plugins-plus | A 7-part brand strategy framework for building comprehensive brand foundations - the same methodology top agencies use with Fortune 500 clients. | Rowan Brooks | 1.0.0 |
| [customerio-pack](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/saas-packs/customerio-pack) | claude-code-plugins-plus | Complete Customer.io integration skill pack with 24 skills covering marketing automation, email campaigns, SMS, push notifications, and customer jo... | Jeremy Longshore | 1.0.0 |
| [excel-analyst-pro](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/business-tools/excel-analyst-pro) | claude-code-plugins-plus | Professional financial modeling toolkit for Claude Code with auto-invoked Skills and Excel MCP integration. Build DCF models, LBO analysis, varianc... | ClaudeCodePlugins | 1.0.0 |
| [juicebox-pack](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/saas-packs/juicebox-pack) | claude-code-plugins-plus | Complete Juicebox integration skill pack with 24 skills covering people data, enrichment, contact search, and AI-powered discovery. Flagship tier v... | Jeremy Longshore | 1.0.0 |

## cap

| Plugin | Marketplace | Description | Author | Version |
|--------|-------------|-------------|--------|---------|
| [sap-cap-capire](https://github.com/secondsky/sap-skills/tree/main/plugins/sap-cap-capire) | secondsky/sap-skills | SAP Cloud Application Programming Model (CAP) development skill using Capire documentation. Use when: building CAP applications, defining CDS model... | None | 2.1.0 |

## code-quality

| Plugin | Marketplace | Description | Author | Version |
|--------|-------------|-------------|--------|---------|
| [project-health-auditor](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/mcp/project-health-auditor) | claude-code-plugins-plus | Multi-dimensional code health analysis with complexity, churn, and test coverage - identifies technical debt hot spots | Jeremy Longshore | 1.0.0 |

## code-review

| Plugin | Marketplace | Description | Author | Version |
|--------|-------------|-------------|--------|---------|
| [audit](https://github.com/ananddtyagi/claude-code-marketplace) | cc-marketplace | Perform security audit on codebase |  Anand Tyagi | 1.0.0 |
| [code-review](https://github.com/ananddtyagi/claude-code-marketplace) | cc-marketplace | Perform a comprehensive code review of recent changes |  Anand Tyagi | 1.0.0 |
| [code-review-assistant](https://github.com/ananddtyagi/claude-code-marketplace) | cc-marketplace | Get comprehensive code reviews with suggestions for improvements, best practices, and potential issues. | Anonymous | 1.0.0 |
| [pr-issue-resolve](https://github.com/ananddtyagi/claude-code-marketplace) | cc-marketplace | this is to analyze the PRs and solve the requested changes in them | safayavatsal | 1.0.0 |
| [update-claudemd](https://github.com/ananddtyagi/claude-code-marketplace) | cc-marketplace | Automatically update CLAUDE.md file based on recent code changes |  Anand Tyagi | 1.0.0 |

## communication

| Plugin | Marketplace | Description | Author | Version |
|--------|-------------|-------------|--------|---------|
| [teams-channel-post-writer](https://github.com/daymade/claude-code-skills/tree/main/) | daymade/claude-code-skills | Create professional Microsoft Teams channel posts with Adaptive Cards, formatted announcements, and corporate communication standards | None | 1.0.0 |

## communication-writing

| Plugin | Marketplace | Description | Author | Version |
|--------|-------------|-------------|--------|---------|
| [content-research-writer](https://github.com/ComposioHQ/awesome-claude-skills/tree/master/content-research-writer) | awesome-claude-skills | Assists in writing high-quality content by conducting research, adding citations, improving hooks, and providing section-by-section feedback. | None | 1.0.0 |
| [meeting-insights-analyzer](https://github.com/ComposioHQ/awesome-claude-skills/tree/master/meeting-insights-analyzer) | awesome-claude-skills | Analyzes meeting transcripts to uncover behavioral patterns including conflict avoidance, speaking ratios, filler words, and leadership style. | None | 1.0.0 |
| [twitter-algorithm-optimizer](https://github.com/ComposioHQ/awesome-claude-skills/tree/master/twitter-algorithm-optimizer) | awesome-claude-skills | Analyze and optimize tweets for maximum reach using Twitter's open-source algorithm insights. Rewrite and edit tweets to improve engagement and vis... | None | 1.0.0 |

## community

| Plugin | Marketplace | Description | Author | Version |
|--------|-------------|-------------|--------|---------|
| [claude-reflect](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/community/claude-reflect) | claude-code-plugins-plus | Self-learning system for Claude Code that captures corrections and updates CLAUDE.md automatically | Bayram Annakov | 1.4.1 |
| [gastown](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/community/gastown) | claude-code-plugins-plus | Multi-agent orchestrator for Claude Code. Track work with convoys, sling to polecats. The Cognition Engine for AI-powered software factories. | Numman Ali | 1.0.0 |
| [jeremy-firebase](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/community/jeremy-firebase) | claude-code-plugins-plus | Firebase platform expert for Firestore, Auth, Functions, and Vertex AI integration | Jeremy Longshore | 1.0.0 |
| [zai-cli](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/community/zai-cli) | claude-code-plugins-plus | Z.AI vision, search, reader, and GitHub exploration via CLI and MCP. Analyze images, search the web, read pages as markdown, explore repos. | Numman Ali | 1.0.0 |

## content

| Plugin | Marketplace | Description | Author | Version |
|--------|-------------|-------------|--------|---------|
| [seo](https://github.com/MadAppGang/claude-code/tree/main/plugins/seo) | mag-claude-plugins | Highly autonomous SEO toolkit (~80% autonomy) with AUTO GATEs, self-correction loops, and multi-model validation. v1.5.1: Fixed hooks configuration... | Jack Rudenko | 1.5.1 |

## creative-media

| Plugin | Marketplace | Description | Author | Version |
|--------|-------------|-------------|--------|---------|
| [algorithmic-art](https://github.com/ComposioHQ/awesome-claude-skills/tree/master/algorithmic-art) | awesome-claude-skills | Creates algorithmic art and generative designs using computational creativity techniques. | None | 1.0.0 |
| [canvas-design](https://github.com/ComposioHQ/awesome-claude-skills/tree/master/canvas-design) | awesome-claude-skills | Creates beautiful visual art in PNG and PDF documents using design philosophy and aesthetic principles for posters, designs, and static pieces. | None | 1.0.0 |
| [image-enhancer](https://github.com/ComposioHQ/awesome-claude-skills/tree/master/image-enhancer) | awesome-claude-skills | Improves image and screenshot quality by enhancing resolution, sharpness, and clarity for professional presentations and documentation. | None | 1.0.0 |
| [slack-gif-creator](https://github.com/ComposioHQ/awesome-claude-skills/tree/master/slack-gif-creator) | awesome-claude-skills | Creates animated GIFs optimized for Slack with validators for size constraints and composable animation primitives. | None | 1.0.0 |
| [theme-factory](https://github.com/ComposioHQ/awesome-claude-skills/tree/master/theme-factory) | awesome-claude-skills | Applies professional font and color themes to artifacts including slides, docs, reports, and HTML landing pages with 10 pre-set themes. | None | 1.0.0 |
| [video-downloader](https://github.com/ComposioHQ/awesome-claude-skills/tree/master/video-downloader) | awesome-claude-skills | Downloads videos from YouTube and other platforms for offline viewing, editing, or archival with support for various formats and quality options. | None | 1.0.0 |

## crypto

| Plugin | Marketplace | Description | Author | Version |
|--------|-------------|-------------|--------|---------|
| [arbitrage-opportunity-finder](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/crypto/arbitrage-opportunity-finder) | claude-code-plugins-plus | Find and analyze arbitrage opportunities across exchanges and DeFi protocols | Jeremy Longshore | 1.0.0 |
| [blockchain-explorer-cli](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/crypto/blockchain-explorer-cli) | claude-code-plugins-plus | Command-line blockchain explorer for transactions, addresses, and contracts | Jeremy Longshore | 1.0.0 |
| [cross-chain-bridge-monitor](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/crypto/cross-chain-bridge-monitor) | claude-code-plugins-plus | Monitor cross-chain bridge activity, track transfers, analyze security, and detect bridge exploits | Jeremy Longshore | 1.0.0 |
| [crypto-derivatives-tracker](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/crypto/crypto-derivatives-tracker) | claude-code-plugins-plus | Track crypto futures, options, perpetual swaps with funding rates, open interest, and derivatives market analysis | Jeremy Longshore | 1.0.0 |
| [crypto-news-aggregator](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/crypto/crypto-news-aggregator) | claude-code-plugins-plus | Aggregate and analyze crypto news from multiple sources with sentiment analysis | Jeremy Longshore | 1.0.0 |
| [crypto-portfolio-tracker](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/crypto/crypto-portfolio-tracker) | claude-code-plugins-plus | Professional crypto portfolio tracking with real-time prices, PnL analysis, and risk metrics | Jeremy Longshore | 1.0.0 |
| [crypto-signal-generator](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/crypto/crypto-signal-generator) | claude-code-plugins-plus | Generate trading signals from technical indicators and market analysis | Jeremy Longshore | 1.0.0 |
| [crypto-tax-calculator](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/crypto/crypto-tax-calculator) | claude-code-plugins-plus | Calculate crypto taxes with FIFO/LIFO methods and generate tax reports | Jeremy Longshore | 1.0.0 |
| [defi-yield-optimizer](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/crypto/defi-yield-optimizer) | claude-code-plugins-plus | Optimize DeFi yield farming strategies across protocols with APY tracking and risk assessment | Jeremy Longshore | 1.0.0 |
| [dex-aggregator-router](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/crypto/dex-aggregator-router) | claude-code-plugins-plus | Find optimal DEX routes for token swaps across multiple exchanges | Jeremy Longshore | 1.0.0 |
| [flash-loan-simulator](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/crypto/flash-loan-simulator) | claude-code-plugins-plus | Simulate and analyze flash loan strategies including arbitrage, liquidations, and collateral swaps | Jeremy Longshore | 1.0.0 |
| [gas-fee-optimizer](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/crypto/gas-fee-optimizer) | claude-code-plugins-plus | Optimize transaction gas fees with timing and routing recommendations | Jeremy Longshore | 1.0.0 |
| [liquidity-pool-analyzer](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/crypto/liquidity-pool-analyzer) | claude-code-plugins-plus | Analyze DeFi liquidity pools for impermanent loss, APY, and optimization opportunities | Jeremy Longshore | 1.0.0 |
| [market-movers-scanner](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/crypto/market-movers-scanner) | claude-code-plugins-plus | Scan for top market movers - gainers, losers, volume spikes, and unusual activity | Jeremy Longshore | 1.0.0 |
| [market-price-tracker](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/crypto/market-price-tracker) | claude-code-plugins-plus | Real-time market price tracking with multi-exchange feeds and advanced alerts | Jeremy Longshore | 1.0.0 |
| [market-sentiment-analyzer](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/crypto/market-sentiment-analyzer) | claude-code-plugins-plus | Analyze market sentiment from social media, news, and on-chain data | Jeremy Longshore | 1.0.0 |
| [mempool-analyzer](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/crypto/mempool-analyzer) | claude-code-plugins-plus | Advanced mempool analysis for MEV opportunities, pending transaction monitoring, and gas price optimization | Jeremy Longshore | 1.0.0 |
| [nft-rarity-analyzer](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/crypto/nft-rarity-analyzer) | claude-code-plugins-plus | Analyze NFT rarity scores and valuations across collections | Jeremy Longshore | 1.0.0 |
| [on-chain-analytics](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/crypto/on-chain-analytics) | claude-code-plugins-plus | Analyze on-chain metrics including whale movements, network activity, and holder distribution | Jeremy Longshore | 1.0.0 |
| [options-flow-analyzer](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/crypto/options-flow-analyzer) | claude-code-plugins-plus | Track institutional options flow, unusual activity, and smart money movements | Jeremy Longshore | 1.0.0 |
| [staking-rewards-optimizer](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/crypto/staking-rewards-optimizer) | claude-code-plugins-plus | Optimize staking rewards across multiple protocols and chains | Jeremy Longshore | 1.0.0 |
| [token-launch-tracker](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/crypto/token-launch-tracker) | claude-code-plugins-plus | Track new token launches, detect rugpulls, and analyze contract security for early-stage crypto projects | Jeremy Longshore | 1.0.0 |
| [trading-strategy-backtester](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/crypto/trading-strategy-backtester) | claude-code-plugins-plus | Backtest trading strategies with historical data, performance metrics, and risk analysis | Jeremy Longshore | 1.0.0 |
| [wallet-portfolio-tracker](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/crypto/wallet-portfolio-tracker) | claude-code-plugins-plus | Track crypto wallets across multiple chains with portfolio analytics and transaction history | Jeremy Longshore | 1.0.0 |
| [wallet-security-auditor](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/crypto/wallet-security-auditor) | claude-code-plugins-plus | Crypto wallet security auditor for reviewing wallet implementations, key management, signing flows, and common vulnerability patterns. | Jeremy Longshore | 1.0.0 |
| [whale-alert-monitor](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/crypto/whale-alert-monitor) | claude-code-plugins-plus | Monitor large crypto transactions and whale wallet movements in real-time | Jeremy Longshore | 1.0.0 |

## customization

| Plugin | Marketplace | Description | Author | Version |
|--------|-------------|-------------|--------|---------|
| [statusline-generator](https://github.com/daymade/claude-code-skills/tree/main/) | daymade/claude-code-skills | Configure Claude Code statuslines with multi-line layouts, cost tracking via ccusage, git status, and customizable colors | None | 1.0.0 |

## data

| Plugin | Marketplace | Description | Author | Version |
|--------|-------------|-------------|--------|---------|
| [data-engineering](https://github.com/wshobson/agents) | claude-code-workflows | ETL pipeline construction, data warehouse design, batch processing workflows, and data-driven feature development | Seth Hobson | 1.2.2 |
| [data-validation-suite](https://github.com/wshobson/agents) | claude-code-workflows | Schema validation, data quality monitoring, streaming validation pipelines, and input validation for backend APIs | Seth Hobson | 1.2.0 |

## data-analytics

| Plugin | Marketplace | Description | Author | Version |
|--------|-------------|-------------|--------|---------|
| [sap-datasphere](https://github.com/secondsky/sap-skills/tree/main/plugins/sap-datasphere) | secondsky/sap-skills | Comprehensive plugin for SAP Datasphere development with 3 specialized agents, 4 slash commands, and validation hooks. Use when building data wareh... | None | 2.1.0 |
| [sap-sac-custom-widget](https://github.com/secondsky/sap-skills/tree/main/plugins/sap-sac-custom-widget) | secondsky/sap-skills | SAP Analytics Cloud (SAC) Custom Widget development skill. Use when building custom visualizations, interactive components, extending SAC with Web ... | None | 2.1.0 |
| [sap-sac-planning](https://github.com/secondsky/sap-skills/tree/main/plugins/sap-sac-planning) | secondsky/sap-skills | This skill should be used when developing SAP Analytics Cloud (SAC) planning applications, including building planning-enabled stories, analytics d... | None | 2.1.0 |
| [sap-sac-scripting](https://github.com/secondsky/sap-skills/tree/main/plugins/sap-sac-scripting) | secondsky/sap-skills | Comprehensive SAC scripting skill for SAP Analytics Cloud Analytics Designer and Optimized Story Experience. This skill should be used when the use... | None | 2.1.0 |
| [sap-sqlscript](https://github.com/secondsky/sap-skills/tree/main/plugins/sap-sqlscript) | secondsky/sap-skills | This skill should be used when the user asks to "write a SQLScript procedure", "create HANA stored procedure", "implement AMDP method", "optimize S... | None | 2.1.0 |

## database

| Plugin | Marketplace | Description | Author | Version |
|--------|-------------|-------------|--------|---------|
| [data-seeder-generator](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/database/data-seeder-generator) | claude-code-plugins-plus | Generate realistic test data and database seed scripts for development and testing environments | Jeremy Longshore | 1.0.0 |
| [data-validation-engine](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/database/data-validation-engine) | claude-code-plugins-plus | Database plugin for data-validation-engine | Jeremy Longshore | 1.0.0 |
| [database-archival-system](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/database/database-archival-system) | claude-code-plugins-plus | Database plugin for database-archival-system | Jeremy Longshore | 1.0.0 |
| [database-audit-logger](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/database/database-audit-logger) | claude-code-plugins-plus | Database plugin for database-audit-logger | Jeremy Longshore | 1.0.0 |
| [database-backup-automator](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/database/database-backup-automator) | claude-code-plugins-plus | Automate database backups with scheduling, compression, encryption, and restore procedures | Jeremy Longshore | 1.0.0 |
| [database-cache-layer](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/database/database-cache-layer) | claude-code-plugins-plus | Database plugin for database-cache-layer | Jeremy Longshore | 1.0.0 |
| [database-connection-pooler](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/database/database-connection-pooler) | claude-code-plugins-plus | Implement and optimize database connection pooling for improved performance and resource management | Jeremy Longshore | 1.0.0 |
| [database-deadlock-detector](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/database/database-deadlock-detector) | claude-code-plugins-plus | Database plugin for database-deadlock-detector | Jeremy Longshore | 1.0.0 |
| [database-design](https://github.com/wshobson/agents) | claude-code-workflows | Database architecture, schema design, and SQL optimization for production systems | Seth Hobson | 1.2.0 |
| [database-diff-tool](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/database/database-diff-tool) | claude-code-plugins-plus | Database plugin for database-diff-tool | Jeremy Longshore | 1.0.0 |
| [database-documentation-gen](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/database/database-documentation-gen) | claude-code-plugins-plus | Database plugin for database-documentation-gen | Jeremy Longshore | 1.0.0 |
| [database-health-monitor](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/database/database-health-monitor) | claude-code-plugins-plus | Database plugin for database-health-monitor | Jeremy Longshore | 1.0.0 |
| [database-index-advisor](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/database/database-index-advisor) | claude-code-plugins-plus | Analyze query patterns and recommend optimal database indexes with impact analysis | Jeremy Longshore | 1.0.0 |
| [database-migration-manager](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/database/database-migration-manager) | claude-code-plugins-plus | Manage database migrations with version control, rollback capabilities, and automated schema evolution tracking | Jeremy Longshore | 1.0.0 |
| [database-migrations](https://github.com/wshobson/agents) | claude-code-workflows | Database migration automation, observability, and cross-database migration strategies | Seth Hobson | 1.2.0 |
| [database-partition-manager](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/database/database-partition-manager) | claude-code-plugins-plus | Database plugin for database-partition-manager | Jeremy Longshore | 1.0.0 |
| [database-recovery-manager](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/database/database-recovery-manager) | claude-code-plugins-plus | Database plugin for database-recovery-manager | Jeremy Longshore | 1.0.0 |
| [database-replication-manager](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/database/database-replication-manager) | claude-code-plugins-plus | Manage database replication, failover, and high availability configurations | Jeremy Longshore | 1.0.0 |
| [database-schema-designer](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/database/database-schema-designer) | claude-code-plugins-plus | Design and visualize database schemas with normalization guidance, relationship mapping, and ERD generation | Jeremy Longshore | 1.0.0 |
| [database-security-scanner](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/database/database-security-scanner) | claude-code-plugins-plus | Database plugin for database-security-scanner | Jeremy Longshore | 1.0.0 |
| [database-sharding-manager](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/database/database-sharding-manager) | claude-code-plugins-plus | Database plugin for database-sharding-manager | Jeremy Longshore | 1.0.0 |
| [database-transaction-monitor](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/database/database-transaction-monitor) | claude-code-plugins-plus | Database plugin for database-transaction-monitor | Jeremy Longshore | 1.0.0 |
| [fairdb-ops-manager](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/community/fairdb-ops-manager) | claude-code-plugins-plus | Database operations management for FairDB PostgreSQL clusters | Community | 1.0.0 |
| [firebase](https://github.com/anthropics/claude-plugins-official/tree/main/external_plugins/firebase) | anthropics/claude-plugins-official | Google Firebase MCP integration. Manage Firestore databases, authentication, cloud functions, hosting, and storage. Build and manage your Firebase ... | None | 1.0.0 |
| [jeremy-firestore](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/community/jeremy-firestore) | claude-code-plugins-plus | Firestore database specialist for schema design, queries, and real-time sync | Jeremy Longshore | 1.0.0 |
| [nosql-data-modeler](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/database/nosql-data-modeler) | claude-code-plugins-plus | Database plugin for nosql-data-modeler | Jeremy Longshore | 1.0.0 |
| [orm-code-generator](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/database/orm-code-generator) | claude-code-plugins-plus | Generate ORM models from database schemas or create database schemas from models for TypeORM, Prisma, Sequelize, SQLAlchemy, and more | Jeremy Longshore | 1.0.0 |
| [pinecone](https://github.com/pinecone-io/pinecone-claude-code-plugin.git) | anthropics/claude-plugins-official | Pinecone vector database integration. Streamline your Pinecone development with powerful tools for managing vector indexes, querying data, and rapi... | None | 1.0.0 |
| [query-performance-analyzer](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/database/query-performance-analyzer) | claude-code-plugins-plus | Analyze query performance with EXPLAIN plan interpretation, bottleneck identification, and optimization recommendations | Jeremy Longshore | 1.0.0 |
| [sql-query-optimizer](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/database/sql-query-optimizer) | claude-code-plugins-plus | Analyze and optimize SQL queries for better performance, suggesting indexes, query rewrites, and execution plan improvements | Jeremy Longshore | 1.0.0 |
| [stored-procedure-generator](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/database/stored-procedure-generator) | claude-code-plugins-plus | Database plugin for stored-procedure-generator | Jeremy Longshore | 1.0.0 |
| [supabase](https://github.com/anthropics/claude-plugins-official/tree/main/external_plugins/supabase) | anthropics/claude-plugins-official | Supabase MCP integration for database operations, authentication, storage, and real-time subscriptions. Manage your Supabase projects, run SQL quer... | None | 1.0.0 |
| [supabase-pack](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/saas-packs/supabase-pack) | claude-code-plugins-plus | Complete Supabase integration skill pack with 30 skills covering authentication, database, storage, realtime, edge functions, and production operat... | Jeremy Longshore | 1.0.0 |

## debugging

| Plugin | Marketplace | Description | Author | Version |
|--------|-------------|-------------|--------|---------|
| [bug-detective](https://github.com/ananddtyagi/claude-code-marketplace) | cc-marketplace | Systematically debug issues with step-by-step troubleshooting approaches. | Anonymous | 1.0.0 |
| [conversational-api-debugger](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/mcp/conversational-api-debugger) | claude-code-plugins-plus | Debug REST API failures using OpenAPI specs and HTTP logs (HAR) - root cause analysis with cURL generation | Jeremy Longshore | 1.0.0 |
| [debug-session](https://github.com/ananddtyagi/claude-code-marketplace) | cc-marketplace | Ask Claude Code to help you debug an issue |  Anand Tyagi | 1.0.0 |
| [github-issue-fix](https://github.com/ananddtyagi/claude-code-marketplace) | cc-marketplace | This is a detailed way you can analyze the GitHub issues and let Claude handle them in best possible way. | safayavatsal | 1.0.0 |

## deployment

| Plugin | Marketplace | Description | Author | Version |
|--------|-------------|-------------|--------|---------|
| [vercel](https://github.com/vercel/vercel-deploy-claude-code-plugin.git) | anthropics/claude-plugins-official | Vercel deployment platform integration. Manage deployments, check build status, access logs, configure domains, and control your frontend infrastru... | None | 1.0.0 |

## design

| Plugin | Marketplace | Description | Author | Version |
|--------|-------------|-------------|--------|---------|
| [design-to-code](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/mcp/design-to-code) | claude-code-plugins-plus | Convert Figma designs and screenshots to React/Svelte/Vue components with built-in accessibility | Jeremy Longshore | 1.0.0 |
| [figma](https://github.com/figma/mcp-server-guide.git) | anthropics/claude-plugins-official | Figma design platform integration. Access design files, extract component information, read design tokens, and translate designs into code. Bridge ... | None | 1.0.0 |
| [ui-designer](https://github.com/daymade/claude-code-skills/tree/main/) | daymade/claude-code-skills | Extract design systems from reference UI images and generate implementation-ready UI design prompts. Use when users provide UI screenshots/mockups ... | None | 1.0.0 |

## dev-tools

| Plugin | Marketplace | Description | Author | Version |
|--------|-------------|-------------|--------|---------|
| [kreatsaas](https://github.com/ananddtyagi/claude-code-marketplace) | cc-marketplace | SaaS Builder Guide - Build production-ready SaaS from design to deployment with 11 skill guides, 5 AI agents, and beginner-friendly FAQ | johunsang | 1.0.0 |

## developer-tools

| Plugin | Marketplace | Description | Author | Version |
|--------|-------------|-------------|--------|---------|
| [claude-code-history-files-finder](https://github.com/daymade/claude-code-skills/tree/main/) | daymade/claude-code-skills | Find and recover content from Claude Code session history files. Use when searching for deleted files, tracking changes across sessions, analyzing ... | None | 1.0.0 |
| [cli-demo-generator](https://github.com/daymade/claude-code-skills/tree/main/) | daymade/claude-code-skills | Generate professional animated CLI demos and terminal recordings with VHS. Supports automated generation, batch processing, and interactive recordi... | None | 1.0.0 |
| [cloudflare-troubleshooting](https://github.com/daymade/claude-code-skills/tree/main/) | daymade/claude-code-skills | Investigate and resolve Cloudflare configuration issues using API-driven evidence gathering. Use when troubleshooting ERR_TOO_MANY_REDIRECTS, SSL e... | None | 1.0.0 |
| [github-contributor](https://github.com/daymade/claude-code-skills/tree/main/) | daymade/claude-code-skills | Strategic guide for becoming an effective GitHub contributor. Covers opportunity discovery, project selection, high-quality PR creation, and reputa... | None | 1.0.0 |
| [github-ops](https://github.com/daymade/claude-code-skills/tree/main/) | daymade/claude-code-skills | Comprehensive GitHub operations using gh CLI and GitHub API for pull requests, issues, repositories, workflows, and API interactions | None | 1.0.0 |
| [iOS-APP-developer](https://github.com/daymade/claude-code-skills/tree/main/) | daymade/claude-code-skills | Develops iOS applications with XcodeGen, SwiftUI, and SPM. Use when configuring XcodeGen project.yml, resolving SPM dependency issues, deploying to... | None | 1.1.0 |
| [promptfoo-evaluation](https://github.com/daymade/claude-code-skills/tree/main/) | daymade/claude-code-skills | Configures and runs LLM evaluation using Promptfoo framework. Use when setting up prompt testing, creating evaluation configs (promptfooconfig.yaml... | None | 1.0.0 |
| [qa-expert](https://github.com/daymade/claude-code-skills/tree/main/) | daymade/claude-code-skills | Comprehensive QA testing infrastructure with autonomous LLM execution, Google Testing Standards (AAA pattern), and OWASP security testing. Use when... | None | 1.0.0 |
| [skill-creator](https://github.com/daymade/claude-code-skills/tree/main/) | daymade/claude-code-skills | Essential meta-skill for creating effective Claude Code skills with initialization scripts, validation, packaging, marketplace registration, and pr... | None | 1.2.2 |
| [skill-reviewer](https://github.com/daymade/claude-code-skills/tree/main/) | daymade/claude-code-skills | Reviews and improves Claude Code skills against official best practices. Supports three modes - self-review (validate your own skills), external re... | None | 1.0.0 |
| [skills-search](https://github.com/daymade/claude-code-skills/tree/main/) | daymade/claude-code-skills | Search, discover, install, and manage Claude Code skills from the CCPM registry. Use when users want to find skills for specific tasks, install ski... | None | 1.0.0 |

## development

| Plugin | Marketplace | Description | Author | Version |
|--------|-------------|-------------|--------|---------|
| [agent-sdk-dev](https://github.com/anthropics/claude-plugins-official/tree/main/plugins/agent-sdk-dev) | anthropics/claude-plugins-official | Development kit for working with the Claude Agent SDK | Anthropic | 1.0.0 |
| [agent-sdk-dev](https://github.com/anthropics/claude-code/tree/main/plugins/agent-sdk-dev) | anthropics/claude-code | Development kit for working with the Claude Agent SDK | None | 1.0.0 |
| [agentdev](https://github.com/MadAppGang/claude-code/tree/main/plugins/agentdev) | mag-claude-plugins | Create, implement, and review Claude Code agents and commands with multi-model validation, LLM performance tracking, and session-based artifact iso... | Jack Rudenko | 1.4.0 |
| [api-contract-sync-manager](https://github.com/ananddtyagi/claude-code-marketplace) | cc-marketplace | Validate and synchronize API contracts (OpenAPI, GraphQL) with implementation, detect breaking changes, and generate type-safe client code | Claude Code Marketplace | 1.0.0 |
| [artifacts-builder](https://github.com/ComposioHQ/awesome-claude-skills/tree/master/artifacts-builder) | awesome-claude-skills | Builds elaborate, multi-component Claude.ai HTML artifacts using modern frontend technologies including React, Tailwind CSS, and shadcn/ui. | None | 1.0.0 |
| [backend-development](https://github.com/wshobson/agents) | claude-code-workflows | Backend API design, GraphQL architecture, workflow orchestration with Temporal, and test-driven backend development | Seth Hobson | 1.2.4 |
| [basedpyright](https://github.com/Piebald-AI/claude-code-lsps/tree/main/basedpyright) | Piebald-AI/claude-code-lsps | Python language server using basedpyright with stricter type checking | Tyler Laprade | 0.1.0 |
| [bsl-lsp](https://github.com/Piebald-AI/claude-code-lsps/tree/main/bsl-lsp) | Piebald-AI/claude-code-lsps | BSL Language Server for 1C:Enterprise and OneScript | Nikita Fedkin | 0.1.0 |
| [changelog-generator](https://github.com/ComposioHQ/awesome-claude-skills/tree/master/changelog-generator) | awesome-claude-skills | Automatically creates user-facing changelogs from git commits by analyzing history and transforming technical commits into customer-friendly releas... | None | 1.0.0 |
| [clangd](https://github.com/Piebald-AI/claude-code-lsps/tree/main/clangd) | Piebald-AI/claude-code-lsps | LLVM-based language server for C and C++ | Piebald LLC | 0.1.0 |
| [clangd-lsp](https://github.com/anthropics/claude-plugins-official/tree/main/plugins/clangd-lsp) | anthropics/claude-plugins-official | C/C++ language server (clangd) for code intelligence | Anthropic | 1.0.0 |
| [claude-dev-infrastructure](https://github.com/ananddtyagi/claude-code-marketplace) | cc-marketplace | Complete development infrastructure for Claude Code projects - 12 AI skills, task coordination hooks, multi-instance locking, templates, and visual... | endlessblink | 1.0.0 |
| [claude-opus-4-5-migration](https://github.com/anthropics/claude-code/tree/main/plugins/claude-opus-4-5-migration) | anthropics/claude-code | Migrate your code and prompts from Sonnet 4.x and Opus 4.1 to Opus 4.5. | William Hu | 1.0.0 |
| [code-analysis](https://github.com/MadAppGang/claude-code/tree/main/plugins/code-analysis) | mag-claude-plugins | Deep code investigation with claudemem. v3.0.0: ENRICHMENT MODE - hooks enhance native tools with AST context instead of blocking. Grep/Glob/Bash s... | Jack Rudenko | 3.0.0 |
| [context7](https://github.com/anthropics/claude-plugins-official/tree/main/external_plugins/context7) | anthropics/claude-plugins-official | Upstash Context7 MCP server for up-to-date documentation lookup. Pull version-specific documentation and code examples directly from source reposit... | None | 1.0.0 |
| [csharp-lsp](https://github.com/anthropics/claude-plugins-official/tree/main/plugins/csharp-lsp) | anthropics/claude-plugins-official | C# language server for code intelligence | Anthropic | 1.0.0 |
| [debugging-toolkit](https://github.com/wshobson/agents) | claude-code-workflows | Interactive debugging, developer experience optimization, and smart debugging workflows | Seth Hobson | 1.2.0 |
| [dev](https://github.com/MadAppGang/claude-code/tree/main/plugins/dev) | mag-claude-plugins | Universal development assistant with documentation, deep research, interviews, and DevOps guidance. v1.19.0: Avant-Garde UI Engineer for Awwwards-q... | Jack Rudenko | 1.19.0 |
| [developer-essentials](https://github.com/wshobson/agents) | claude-code-workflows | Essential developer skills including Git workflows, SQL optimization, error handling, code review, E2E testing, authentication, debugging, and mono... | Seth Hobson | 1.0.1 |
| [developer-growth-analysis](https://github.com/ComposioHQ/awesome-claude-skills/tree/master/developer-growth-analysis) | awesome-claude-skills | Analyzes your recent Claude Code chat history to identify coding patterns, development gaps, and areas for improvement, curates relevant learning r... | None | 1.0.0 |
| [feature-dev](https://github.com/anthropics/claude-plugins-official/tree/main/plugins/feature-dev) | anthropics/claude-plugins-official | Comprehensive feature development workflow with specialized agents for codebase exploration, architecture design, and quality review | Anthropic | 1.0.0 |
| [feature-dev](https://github.com/anthropics/claude-code/tree/main/plugins/feature-dev) | anthropics/claude-code | Comprehensive feature development workflow with specialized agents for codebase exploration, architecture design, and quality review | Siddharth Bidasaria | 1.0.0 |
| [frontend-design](https://github.com/anthropics/claude-plugins-official/tree/main/plugins/frontend-design) | anthropics/claude-plugins-official | Create distinctive, production-grade frontend interfaces with high design quality. Generates creative, polished code that avoids generic AI aesthet... | Anthropic | 1.0.0 |
| [frontend-design](https://github.com/anthropics/claude-code/tree/main/plugins/frontend-design) | anthropics/claude-code | Create distinctive, production-grade frontend interfaces with high design quality. Generates creative, polished code that avoids generic AI aesthet... | Prithvi Rajasekaran & Alexander Bricken | 1.0.0 |
| [frontend-mobile-development](https://github.com/wshobson/agents) | claude-code-workflows | Frontend UI development and mobile application implementation across platforms | Seth Hobson | 1.2.1 |
| [gopls](https://github.com/Piebald-AI/claude-code-lsps/tree/main/gopls) | Piebald-AI/claude-code-lsps | Official Go language server | Piebald LLC | 0.1.0 |
| [gopls-lsp](https://github.com/anthropics/claude-plugins-official/tree/main/plugins/gopls-lsp) | anthropics/claude-plugins-official | Go language server for code intelligence and refactoring | Anthropic | 1.0.0 |
| [greptile](https://github.com/anthropics/claude-plugins-official/tree/main/external_plugins/greptile) | anthropics/claude-plugins-official | AI-powered codebase search and understanding. Query your repositories using natural language to find relevant code, understand dependencies, and ge... | None | 1.0.0 |
| [huggingface-skills](https://github.com/huggingface/skills.git) | anthropics/claude-plugins-official | Build, train, evaluate, and use open source AI models, datasets, and spaces. | None | 1.0.0 |
| [jdtls](https://github.com/Piebald-AI/claude-code-lsps/tree/main/jdtls) | Piebald-AI/claude-code-lsps | Eclipse JDT Language Server for Java | Piebald LLC | 0.1.0 |
| [jdtls-lsp](https://github.com/anthropics/claude-plugins-official/tree/main/plugins/jdtls-lsp) | anthropics/claude-plugins-official | Java language server (Eclipse JDT.LS) for code intelligence | Anthropic | 1.0.0 |
| [julia-lsp](https://github.com/Piebald-AI/claude-code-lsps/tree/main/julia-lsp) | Piebald-AI/claude-code-lsps | Julia language server using LanguageServer.jl | Piebald LLC | 0.1.0 |
| [kotlin-lsp](https://github.com/Piebald-AI/claude-code-lsps/tree/main/kotlin-lsp) | Piebald-AI/claude-code-lsps | Kotlin language server by JetBrains | Piebald LLC | 0.1.0 |
| [kotlin-lsp](https://github.com/anthropics/claude-plugins-official/tree/main/plugins/kotlin-lsp) | anthropics/claude-plugins-official | Kotlin language server for code intelligence | Anthropic | 1.0.0 |
| [laravel-boost](https://github.com/anthropics/claude-plugins-official/tree/main/external_plugins/laravel-boost) | anthropics/claude-plugins-official | Laravel development toolkit MCP server. Provides intelligent assistance for Laravel applications including Artisan commands, Eloquent queries, rout... | None | 1.0.0 |
| [lua-lsp](https://github.com/anthropics/claude-plugins-official/tree/main/plugins/lua-lsp) | anthropics/claude-plugins-official | Lua language server for code intelligence | Anthropic | 1.0.0 |
| [mcp-builder](https://github.com/ComposioHQ/awesome-claude-skills/tree/master/mcp-builder) | awesome-claude-skills | Guides creation of high-quality MCP (Model Context Protocol) servers for integrating external APIs and services with LLMs using Python or TypeScript. | None | 1.0.0 |
| [multi-platform-apps](https://github.com/wshobson/agents) | claude-code-workflows | Cross-platform application development coordinating web, iOS, Android, and desktop implementations | Seth Hobson | 1.2.1 |
| [multimodel](https://github.com/MadAppGang/claude-code/tree/main/plugins/multimodel) | mag-claude-plugins | Multi-model collaboration and blind voting. Run tasks across multiple AI models in parallel, collect independent votes (APPROVE/REJECT/ABSTAIN), an... | Jack Rudenko | 1.0.0 |
| [omnisharp](https://github.com/Piebald-AI/claude-code-lsps/tree/main/omnisharp) | Piebald-AI/claude-code-lsps | Official .NET language server with rich C# support | Piebald LLC | 0.1.0 |
| [php-lsp](https://github.com/anthropics/claude-plugins-official/tree/main/plugins/php-lsp) | anthropics/claude-plugins-official | PHP language server (Intelephense) for code intelligence | Anthropic | 1.0.0 |
| [phpactor](https://github.com/Piebald-AI/claude-code-lsps/tree/main/phpactor) | Piebald-AI/claude-code-lsps | Intelligent PHP completion and refactoring language server | Piebald LLC | 0.1.0 |
| [plugin-dev](https://github.com/anthropics/claude-plugins-official/tree/main/plugins/plugin-dev) | anthropics/claude-plugins-official | Comprehensive toolkit for developing Claude Code plugins. Includes 7 expert skills covering hooks, MCP integration, commands, agents, and best prac... | Anthropic | 1.0.0 |
| [plugin-dev](https://github.com/anthropics/claude-code/tree/main/plugins/plugin-dev) | anthropics/claude-code | Comprehensive toolkit for developing Claude Code plugins. Includes 7 expert skills covering hooks, MCP integration, commands, agents, and best prac... | Daisy Hollman | 0.1.0 |
| [powershell-editor-services](https://github.com/Piebald-AI/claude-code-lsps/tree/main/powershell-editor-services) | Piebald-AI/claude-code-lsps | Official PowerShell language server by Microsoft | Piebald LLC | 0.1.0 |
| [pyright](https://github.com/Piebald-AI/claude-code-lsps/tree/main/pyright) | Piebald-AI/claude-code-lsps | Python language server with excellent type checking | Piebald LLC | 0.1.0 |
| [pyright-lsp](https://github.com/anthropics/claude-plugins-official/tree/main/plugins/pyright-lsp) | anthropics/claude-plugins-official | Python language server (Pyright) for type checking and code intelligence | Anthropic | 1.0.0 |
| [ralph-loop](https://github.com/anthropics/claude-plugins-official/tree/main/plugins/ralph-loop) | anthropics/claude-plugins-official | Interactive self-referential AI loops for iterative development, implementing the Ralph Wiggum technique. Claude works on the same task repeatedly,... | Anthropic | 1.0.0 |
| [ralph-wiggum](https://github.com/anthropics/claude-code/tree/main/plugins/ralph-wiggum) | anthropics/claude-code | Interactive self-referential AI loops for iterative development. Claude works on the same task repeatedly, seeing its previous work, until completion. | Daisy Hollman | 1.0.0 |
| [ruby-lsp](https://github.com/Piebald-AI/claude-code-lsps/tree/main/ruby-lsp) | Piebald-AI/claude-code-lsps | Modern Ruby language server by Shopify | Piebald LLC | 0.1.0 |
| [rust-analyzer](https://github.com/Piebald-AI/claude-code-lsps/tree/main/rust-analyzer) | Piebald-AI/claude-code-lsps | Rust language server integration with rust-analyzer | Piebald LLC | 0.1.0 |
| [rust-analyzer-lsp](https://github.com/anthropics/claude-plugins-official/tree/main/plugins/rust-analyzer-lsp) | anthropics/claude-plugins-official | Rust language server for code intelligence and analysis | Anthropic | 1.0.0 |
| [serena](https://github.com/anthropics/claude-plugins-official/tree/main/external_plugins/serena) | anthropics/claude-plugins-official | Semantic code analysis MCP server providing intelligent code understanding, refactoring suggestions, and codebase navigation through language serve... | None | 1.0.0 |
| [skill-creator](https://github.com/ComposioHQ/awesome-claude-skills/tree/master/skill-creator) | awesome-claude-skills | Provides guidance for creating effective Claude Skills that extend capabilities with specialized knowledge, workflows, and tool integrations. | None | 1.0.0 |
| [sprint](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/community/sprint) | claude-code-plugins-plus | Autonomous multi-agent development framework with spec-driven sprints. Write specs, run /sprint, and let coordinated agents (backend, frontend, QA,... | Damien Laine | 1.0.0 |
| [stripe](https://github.com/anthropics/claude-plugins-official/tree/main/external_plugins/stripe) | anthropics/claude-plugins-official | Stripe development plugin for Claude | None | 1.0.0 |
| [superpowers](https://github.com/obra/superpowers.git) | anthropics/claude-plugins-official | Superpowers teaches Claude brainstorming, subagent driven development with built in code review, systematic debugging, and red/green TDD. Additiona... | None | 1.0.0 |
| [swift-lsp](https://github.com/anthropics/claude-plugins-official/tree/main/plugins/swift-lsp) | anthropics/claude-plugins-official | Swift language server (SourceKit-LSP) for code intelligence | Anthropic | 1.0.0 |
| [template-skill](https://github.com/ComposioHQ/awesome-claude-skills/tree/master/template-skill) | awesome-claude-skills | A template skill that demonstrates the structure and format for creating new Claude Skills. | None | 1.0.0 |
| [terraform-lsp](https://github.com/hashi-demo-lab/claude-skill-hcp-terraform/tree/main/plugins/terraform-lsp) | hcp-terraform-skills | HashiCorp Terraform language server for enhanced code intelligence | None | 1.0.0 |
| [terraform-mcp-as-code](https://github.com/hashi-demo-lab/claude-skill-hcp-terraform/tree/main/terraform-mcp-as-code) | hcp-terraform-skills | Automate Terraform Cloud/Enterprise operations programmatically via the HashiCorp MCP server | None | 1.0.0 |
| [terraform-stacks](https://github.com/hashi-demo-lab/claude-skill-hcp-terraform/tree/main/terraform-stacks) | hcp-terraform-skills | Comprehensive guide for HCP Terraform Stacks configurations including components, deployments, and OIDC authentication | None | 1.0.0 |
| [terraform-style-guide](https://github.com/hashi-demo-lab/claude-skill-hcp-terraform/tree/main/terraform-style-guide) | hcp-terraform-skills | Comprehensive guide for Terraform code style, formatting, and best practices based on HashiCorp's official standards and Azure Verified Modules (AV... | None | 1.0.0 |
| [terraform-test](https://github.com/hashi-demo-lab/claude-skill-hcp-terraform/tree/main/terraform-test) | hcp-terraform-skills | Comprehensive guide for writing and running Terraform tests with run blocks, assertions, mock providers, and CI/CD integration | None | 1.0.0 |
| [texlab](https://github.com/Piebald-AI/claude-code-lsps/tree/main/texlab) | Piebald-AI/claude-code-lsps | LaTeX language server with completion, references, and document symbols | Micah Stubbs | 0.1.0 |
| [typescript-lsp](https://github.com/anthropics/claude-plugins-official/tree/main/plugins/typescript-lsp) | anthropics/claude-plugins-official | TypeScript/JavaScript language server for enhanced code intelligence | Anthropic | 1.0.0 |
| [ui-design](https://github.com/wshobson/agents) | claude-code-workflows | Comprehensive UI/UX design plugin for mobile (iOS, Android, React Native) and web applications with design systems, accessibility, and modern patterns | Seth Hobson | 1.0.1 |
| [vscode-langservers](https://github.com/Piebald-AI/claude-code-lsps/tree/main/vscode-langservers) | Piebald-AI/claude-code-lsps | HTML and CSS language servers from VS Code | Piebald LLC | 0.1.0 |
| [vtsls](https://github.com/Piebald-AI/claude-code-lsps/tree/main/vtsls) | Piebald-AI/claude-code-lsps | TypeScript and JavaScript language server integration (using vtsls) | Piebald LLC | 0.1.0 |
| [vue-volar](https://github.com/Piebald-AI/claude-code-lsps/tree/main/vue-volar) | Piebald-AI/claude-code-lsps | Vue.js language server integration (Volar) | Piebald LLC | 0.1.0 |
| [webapp-testing](https://github.com/ComposioHQ/awesome-claude-skills/tree/master/webapp-testing) | awesome-claude-skills | Tests local web applications using Playwright for verifying frontend functionality, debugging UI behavior, and capturing screenshots. | None | 1.0.0 |

## devops

| Plugin | Marketplace | Description | Author | Version |
|--------|-------------|-------------|--------|---------|
| [ansible-playbook-creator](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/devops/ansible-playbook-creator) | claude-code-plugins-plus | Create Ansible playbooks for configuration management | Jeremy Longshore | 1.0.0 |
| [auto-scaling-configurator](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/devops/auto-scaling-configurator) | claude-code-plugins-plus | Configure auto-scaling policies for applications and infrastructure | Jeremy Longshore | 1.0.0 |
| [backup-strategy-implementor](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/devops/backup-strategy-implementor) | claude-code-plugins-plus | Implement backup strategies for databases and applications | Jeremy Longshore | 1.0.0 |
| [ci-cd-pipeline-builder](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/devops/ci-cd-pipeline-builder) | claude-code-plugins-plus | Build CI/CD pipelines for GitHub Actions, GitLab CI, Jenkins, and more | Jeremy Longshore | 1.0.0 |
| [cloud-cost-optimizer](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/devops/cloud-cost-optimizer) | claude-code-plugins-plus | Optimize cloud costs and generate cost reports | Jeremy Longshore | 1.0.0 |
| [compliance-checker](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/devops/compliance-checker) | claude-code-plugins-plus | Check infrastructure compliance (SOC2, HIPAA, PCI-DSS) | Jeremy Longshore | 1.0.0 |
| [container-registry-manager](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/devops/container-registry-manager) | claude-code-plugins-plus | Manage container registries (ECR, GCR, Harbor) | Jeremy Longshore | 1.0.0 |
| [container-security-scanner](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/devops/container-security-scanner) | claude-code-plugins-plus | Scan containers for vulnerabilities using Trivy, Snyk, and other security tools | Jeremy Longshore | 1.0.0 |
| [deployment-pipeline-orchestrator](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/devops/deployment-pipeline-orchestrator) | claude-code-plugins-plus | Orchestrate complex multi-stage deployment pipelines | Jeremy Longshore | 1.0.0 |
| [deployment-rollback-manager](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/devops/deployment-rollback-manager) | claude-code-plugins-plus | Manage and execute deployment rollbacks with safety checks | Jeremy Longshore | 1.0.0 |
| [devops-automation-pack](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/packages/devops-automation-pack) | claude-code-plugins-plus | Complete DevOps automation suite with 25 plugins covering Git workflows, CI/CD pipelines, Docker optimization, Kubernetes management, Terraform IaC... | Jeremy Longshore | 1.0.0 |
| [disaster-recovery-planner](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/devops/disaster-recovery-planner) | claude-code-plugins-plus | Plan and implement disaster recovery procedures | Jeremy Longshore | 1.0.0 |
| [docker-compose-generator](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/devops/docker-compose-generator) | claude-code-plugins-plus | Generate Docker Compose configurations for multi-container applications with best practices | Jeremy Longshore | 1.0.0 |
| [environment-config-manager](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/devops/environment-config-manager) | claude-code-plugins-plus | Manage environment configurations and secrets across deployments | Jeremy Longshore | 1.0.0 |
| [fairdb-operations-kit](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/devops/fairdb-operations-kit) | claude-code-plugins-plus | Complete operations kit for FairDB PostgreSQL as a Service - VPS setup, PostgreSQL management, customer provisioning, monitoring, and backup automa... | Jeremy Longshore | 1.0.0 |
| [gh-dash](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/devops/gh-dash) | claude-code-plugins-plus | GitHub PR dashboard for Claude Code. View PR status, CI/CD progress, bot comments, and merge PRs directly from your terminal. | Jake Kozloski | 1.0.0 |
| [git-commit-smart](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/devops/git-commit-smart) | claude-code-plugins-plus | AI-powered conventional commit message generator with smart analysis | Jeremy Longshore | 1.0.0 |
| [gitops-workflow-builder](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/devops/gitops-workflow-builder) | claude-code-plugins-plus | Build GitOps workflows with ArgoCD and Flux | Jeremy Longshore | 1.0.0 |
| [helm-chart-generator](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/devops/helm-chart-generator) | claude-code-plugins-plus | Generate Helm charts for Kubernetes applications | Jeremy Longshore | 1.0.0 |
| [infrastructure-as-code-generator](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/devops/infrastructure-as-code-generator) | claude-code-plugins-plus | Generate Infrastructure as Code for Terraform, CloudFormation, Pulumi, and more | Jeremy Longshore | 1.0.0 |
| [infrastructure-drift-detector](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/devops/infrastructure-drift-detector) | claude-code-plugins-plus | Detect infrastructure drift from desired state | Jeremy Longshore | 1.0.0 |
| [jeremy-adk-terraform](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/devops/jeremy-adk-terraform) | claude-code-plugins-plus | Terraform infrastructure as code for ADK and Vertex AI Agent Engine deployments | Jeremy Longshore | 1.0.0 |
| [jeremy-genkit-terraform](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/devops/jeremy-genkit-terraform) | claude-code-plugins-plus | Terraform modules for Firebase Genkit infrastructure and deployments | Jeremy Longshore | 1.0.0 |
| [jeremy-github-actions-gcp](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/devops/jeremy-github-actions-gcp) | claude-code-plugins-plus | GitHub Actions CI/CD workflows for Google Cloud and Vertex AI deployments | Jeremy Longshore | 1.0.0 |
| [jeremy-vertex-terraform](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/devops/jeremy-vertex-terraform) | claude-code-plugins-plus | Terraform configurations for Vertex AI platform and Agent Engine | Jeremy Longshore | 1.0.0 |
| [kubernetes-deployment-creator](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/devops/kubernetes-deployment-creator) | claude-code-plugins-plus | Create Kubernetes deployments, services, and configurations with best practices | Jeremy Longshore | 1.0.0 |
| [load-balancer-configurator](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/devops/load-balancer-configurator) | claude-code-plugins-plus | Configure load balancers (ALB, NLB, Nginx, HAProxy) | Jeremy Longshore | 1.0.0 |
| [log-aggregation-setup](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/devops/log-aggregation-setup) | claude-code-plugins-plus | Set up log aggregation (ELK, Loki, Splunk) | Jeremy Longshore | 1.0.0 |
| [monitoring-stack-deployer](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/devops/monitoring-stack-deployer) | claude-code-plugins-plus | Deploy monitoring stacks (Prometheus, Grafana, Datadog) | Jeremy Longshore | 1.0.0 |
| [network-policy-manager](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/devops/network-policy-manager) | claude-code-plugins-plus | Manage Kubernetes network policies and firewall rules | Jeremy Longshore | 1.0.0 |
| [secrets-manager-integrator](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/devops/secrets-manager-integrator) | claude-code-plugins-plus | Integrate with secrets managers (Vault, AWS Secrets Manager, etc) | Jeremy Longshore | 1.0.0 |
| [service-mesh-configurator](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/devops/service-mesh-configurator) | claude-code-plugins-plus | Configure service mesh (Istio, Linkerd) for microservices | Jeremy Longshore | 1.0.0 |
| [sugar](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/devops/sugar) | claude-code-plugins-plus | Transform Claude Code into an autonomous AI development powerhouse with rich task context, specialized agents, and intelligent workflow automation | Steven Leggett | 2.0.0 |
| [terraform-module-builder](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/devops/terraform-module-builder) | claude-code-plugins-plus | Build reusable Terraform modules | Jeremy Longshore | 1.0.0 |
| [vercel-pack](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/saas-packs/vercel-pack) | claude-code-plugins-plus | Complete Vercel integration skill pack with 30 skills covering deployments, edge functions, preview environments, performance optimization, and pro... | Jeremy Longshore | 1.0.0 |

## document-conversion

| Plugin | Marketplace | Description | Author | Version |
|--------|-------------|-------------|--------|---------|
| [markdown-tools](https://github.com/daymade/claude-code-skills/tree/main/) | daymade/claude-code-skills | Convert documents (PDFs, Word, PowerPoint, Confluence exports) to markdown with Windows/WSL path handling and PDF image extraction support | None | 1.1.0 |
| [pdf-creator](https://github.com/daymade/claude-code-skills/tree/main/) | daymade/claude-code-skills | Create PDF documents from markdown with proper Chinese font support using weasyprint. Use when converting markdown to PDF, generating formal docume... | None | 1.0.0 |

## documentation

| Plugin | Marketplace | Description | Author | Version |
|--------|-------------|-------------|--------|---------|
| [c4-architecture](https://github.com/wshobson/agents) | claude-code-workflows | Comprehensive C4 architecture documentation workflow with bottom-up code analysis, component synthesis, container mapping, and context diagram gene... | Seth Hobson | 1.0.0 |
| [code-documentation](https://github.com/wshobson/agents) | claude-code-workflows | Documentation generation, code explanation, and technical writing with automated doc generation and tutorial creation | Seth Hobson | 1.2.0 |
| [documentation-generation](https://github.com/wshobson/agents) | claude-code-workflows | OpenAPI specification generation, Mermaid diagram creation, tutorial writing, API reference documentation | Seth Hobson | 1.2.1 |
| [documentation-generator](https://github.com/ananddtyagi/claude-code-marketplace) | cc-marketplace | Create comprehensive documentation for code, APIs, and projects. | Anonymous | 1.0.0 |
| [generate-api-docs](https://github.com/ananddtyagi/claude-code-marketplace) | cc-marketplace | Generate API documentation for endpoints |  Anand Tyagi | 1.0.0 |
| [mermaid-tools](https://github.com/daymade/claude-code-skills/tree/main/) | daymade/claude-code-skills | Generate Mermaid diagrams from markdown with automatic PNG/SVG rendering and extraction from documents | None | 1.0.0 |
| [openapi-expert](https://github.com/ananddtyagi/claude-code-marketplace) | cc-marketplace | Use this agent to update, synchronize, or validate the OpenAPI specification (openapi.yml) against the actual REST API implementation. This include... | Meiring de Wet | 1.0.0 |

## example

| Plugin | Marketplace | Description | Author | Version |
|--------|-------------|-------------|--------|---------|
| [hello-world](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/examples/hello-world) | claude-code-plugins-plus | Simple example plugin demonstrating basic slash commands | Jeremy Longshore | 1.0.0 |
| [jeremy-plugin-tool](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/examples/jeremy-plugin-tool) | claude-code-plugins-plus | Production-grade plugin creator with nixtla-validated quality standards. 4 Agent Skills automate creating, validating, auditing, and versioning plu... | Claude Code Plugins | 2.0.0 |
| [pi-pathfinder](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/examples/pi-pathfinder) | claude-code-plugins-plus | PI Pathfinder - Finds the path through 229 plugins. Automatically picks the best plugin for your task, extracts its skills, and applies them. You d... | Jeremy Longshore | 1.0.0 |

## explore

| Plugin | Marketplace | Description | Author | Version |
|--------|-------------|-------------|--------|---------|
| [analyze-codebase](https://github.com/ananddtyagi/claude-code-marketplace) | cc-marketplace | Generate comprehensive analysis and documentation of entire codebase |  Anand Tyagi | 1.0.0 |
| [explore](https://github.com/ananddtyagi/claude-code-marketplace) | cc-marketplace | Helps Claude read a planning document and explore related files to get familiar with a topic. Asking Claude to prepare to discuss seems to work bet... | Galen Ward | 1.0.0 |

## finance

| Plugin | Marketplace | Description | Author | Version |
|--------|-------------|-------------|--------|---------|
| [openbb-terminal](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/finance/openbb-terminal) | claude-code-plugins-plus | Open-source investment research terminal integration - comprehensive equity analysis, crypto tracking, macro indicators, portfolio optimization, an... | Jeremy Longshore | 1.0.0 |
| [quantitative-trading](https://github.com/wshobson/agents) | claude-code-workflows | Quantitative analysis, algorithmic trading strategies, financial modeling, portfolio risk management, and backtesting | Seth Hobson | 1.2.1 |

## fullstack

| Plugin | Marketplace | Description | Author | Version |
|--------|-------------|-------------|--------|---------|
| [fullstack-starter-pack](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/packages/fullstack-starter-pack) | claude-code-plugins-plus | Complete fullstack development toolkit: React, Express/FastAPI, PostgreSQL scaffolding with AI agents | Jeremy Longshore | 1.0.0 |

## gaming

| Plugin | Marketplace | Description | Author | Version |
|--------|-------------|-------------|--------|---------|
| [game-development](https://github.com/wshobson/agents) | claude-code-workflows | Unity game development with C# scripting, Minecraft server plugin development with Bukkit/Spigot APIs | Seth Hobson | 1.2.1 |

## general

| Plugin | Marketplace | Description | Author | Version |
|--------|-------------|-------------|--------|---------|
| [2-commit-fast](https://github.com/ccplugins/awesome-claude-code-plugins) | awesome-claude-code-plugins | Automates git commit process by selecting the first suggested message, generating structured commits with consistent formatting while skipping manu... | steadycursor | 1.0.0 |
| [2-commit-fast](https://github.com/ananddtyagi/claude-code-marketplace) | cc-marketplace | Automates git commit process by selecting the first suggested message, generating structured commits with consistent formatting while skipping manu... | steadycursor | 1.0.0 |
| [analyze-issue](https://github.com/ananddtyagi/claude-code-marketplace) | cc-marketplace | Fetches GitHub issue details to create comprehensive implementation specifications, analyzing requirements and planning structured approach with cl... | jerseycheese | 1.0.0 |
| [bug-fix](https://github.com/ananddtyagi/claude-code-marketplace) | cc-marketplace | Streamlines bug fixing by creating a GitHub issue first, then a feature branch for implementing and thoroughly testing the solution before merging. | danielscholl | 1.0.0 |
| [commit](https://github.com/ananddtyagi/claude-code-marketplace) | cc-marketplace | Creates git commits using conventional commit format with appropriate emojis, following project standards and creating descriptive messages that ex... | evmts | 1.0.0 |
| [create-pr](https://github.com/ananddtyagi/claude-code-marketplace) | cc-marketplace | Streamlines pull request creation by handling the entire workflow: creating a new branch, committing changes, formatting modified files with Biome,... | toyamarinyon | 1.0.0 |
| [create-pull-request](https://github.com/ananddtyagi/claude-code-marketplace) | cc-marketplace | Provides comprehensive PR creation guidance with GitHub CLI, enforcing title conventions, following template structure, and offering concrete comma... | liam-hq | 1.0.0 |
| [create-worktrees](https://github.com/ananddtyagi/claude-code-marketplace) | cc-marketplace | Creates git worktrees for all open PRs or specific branches, handling branches with slashes, cleaning up stale worktrees, and supporting custom bra... | evmts | 1.0.0 |
| [fix-github-issue](https://github.com/ananddtyagi/claude-code-marketplace) | cc-marketplace | Analyzes and fixes GitHub issues using a structured approach with GitHub CLI for issue details, implementing necessary code changes, running tests,... | jeremymailen | 1.0.0 |
| [fix-issue](https://github.com/ananddtyagi/claude-code-marketplace) | cc-marketplace | Addresses GitHub issues by taking issue number as parameter, analyzing context, implementing solution, and testing/validating the fix for proper in... | metabase | 1.0.0 |
| [fix-pr](https://github.com/ananddtyagi/claude-code-marketplace) | cc-marketplace | Fetches and fixes unresolved PR comments by automatically retrieving feedback, addressing reviewer concerns, making targeted code improvements, and... | metabase | 1.0.0 |
| [husky](https://github.com/ananddtyagi/claude-code-marketplace) | cc-marketplace | Sets up and manages Husky Git hooks by configuring pre-commit hooks, establishing commit message standards, integrating with linting tools, and ens... | evmts | 1.0.0 |
| [pr-review](https://github.com/ananddtyagi/claude-code-marketplace) | cc-marketplace | Reviews pull request changes to provide feedback, check for issues, and suggest improvements before merging into the main codebase. | arkavo-org | 1.0.0 |
| [update-branch-name](https://github.com/ananddtyagi/claude-code-marketplace) | cc-marketplace | Updates branch names with proper prefixes and formats, enforcing naming conventions, supporting semantic prefixes, and managing remote branch updates. | giselles-ai | 1.0.0 |

## hana

| Plugin | Marketplace | Description | Author | Version |
|--------|-------------|-------------|--------|---------|
| [sap-hana-cli](https://github.com/secondsky/sap-skills/tree/main/plugins/sap-hana-cli) | secondsky/sap-skills | Assists with SAP HANA Developer CLI (hana-cli) for database development and administration. Use when: installing hana-cli, connecting to SAP HANA d... | None | 2.1.0 |
| [sap-hana-cloud-data-intelligence](https://github.com/secondsky/sap-skills/tree/main/plugins/sap-hana-cloud-data-intelligence) | secondsky/sap-skills | Develops data processing pipelines, integrations, and machine learning scenarios in SAP Data Intelligence Cloud. Use when building graphs/pipelines... | None | 2.1.0 |
| [sap-hana-ml](https://github.com/secondsky/sap-skills/tree/main/plugins/sap-hana-ml) | secondsky/sap-skills | SAP HANA Machine Learning Python Client (hana-ml) development skill. Use when: Building ML solutions with SAP HANA's in-database machine learning u... | None | 2.1.0 |

## infrastructure

| Plugin | Marketplace | Description | Author | Version |
|--------|-------------|-------------|--------|---------|
| [cicd-automation](https://github.com/wshobson/agents) | claude-code-workflows | CI/CD pipeline configuration, GitHub Actions/GitLab CI workflow setup, and automated deployment pipeline orchestration | Seth Hobson | 1.2.1 |
| [cloud-infrastructure](https://github.com/wshobson/agents) | claude-code-workflows | Cloud architecture design for AWS/Azure/GCP, Kubernetes cluster configuration, Terraform infrastructure-as-code, hybrid cloud networking, and multi... | Seth Hobson | 1.2.2 |
| [deployment-strategies](https://github.com/wshobson/agents) | claude-code-workflows | Deployment patterns, rollback automation, and infrastructure templates | Seth Hobson | 1.2.0 |
| [deployment-validation](https://github.com/wshobson/agents) | claude-code-workflows | Pre-deployment checks, configuration validation, and deployment readiness assessment | Seth Hobson | 1.2.0 |
| [kubernetes-operations](https://github.com/wshobson/agents) | claude-code-workflows | Kubernetes manifest generation, networking configuration, security policies, observability setup, GitOps workflows, and auto-scaling | Seth Hobson | 1.2.1 |

## languages

| Plugin | Marketplace | Description | Author | Version |
|--------|-------------|-------------|--------|---------|
| [arm-cortex-microcontrollers](https://github.com/wshobson/agents) | claude-code-workflows | ARM Cortex-M firmware development for Teensy, STM32, nRF52, and SAMD with peripheral drivers and memory safety patterns | Ryan Snodgrass | 1.2.0 |
| [functional-programming](https://github.com/wshobson/agents) | claude-code-workflows | Functional programming with Elixir, OTP patterns, Phoenix framework, and distributed systems | Seth Hobson | 1.2.0 |
| [javascript-typescript](https://github.com/wshobson/agents) | claude-code-workflows | JavaScript and TypeScript development with ES6+, Node.js, React, and modern web frameworks | Seth Hobson | 1.2.1 |
| [julia-development](https://github.com/wshobson/agents) | claude-code-workflows | Modern Julia development with Julia 1.10+, package management, scientific computing, high-performance numerical code, and production best practices | Community Contribution | 1.0.0 |
| [jvm-languages](https://github.com/wshobson/agents) | claude-code-workflows | JVM language development including Java, Scala, and C# with enterprise patterns and frameworks | Seth Hobson | 1.2.0 |
| [python-development](https://github.com/wshobson/agents) | claude-code-workflows | Modern Python development with Python 3.12+, Django, FastAPI, async patterns, and production best practices | Seth Hobson | 1.2.1 |
| [shell-scripting](https://github.com/wshobson/agents) | claude-code-workflows | Production-grade Bash scripting with defensive programming, POSIX compliance, and comprehensive testing | Ryan Snodgrass | 1.2.1 |
| [systems-programming](https://github.com/wshobson/agents) | claude-code-workflows | Systems programming with Rust, Go, C, and C++ for performance-critical and low-level development | Seth Hobson | 1.2.1 |
| [web-scripting](https://github.com/wshobson/agents) | claude-code-workflows | Web scripting with PHP and Ruby for web applications, CMS development, and backend services | Seth Hobson | 1.2.0 |

## learning

| Plugin | Marketplace | Description | Author | Version |
|--------|-------------|-------------|--------|---------|
| [explanatory-output-style](https://github.com/anthropics/claude-plugins-official/tree/main/plugins/explanatory-output-style) | anthropics/claude-plugins-official | Adds educational insights about implementation choices and codebase patterns (mimics the deprecated Explanatory output style) | Anthropic | 1.0.0 |
| [explanatory-output-style](https://github.com/anthropics/claude-code/tree/main/plugins/explanatory-output-style) | anthropics/claude-code | Adds educational insights about implementation choices and codebase patterns (mimics the deprecated Explanatory output style) | Dickson Tsai | 1.0.0 |
| [learning-output-style](https://github.com/anthropics/claude-plugins-official/tree/main/plugins/learning-output-style) | anthropics/claude-plugins-official | Interactive learning mode that requests meaningful code contributions at decision points (mimics the unshipped Learning output style) | Anthropic | 1.0.0 |
| [learning-output-style](https://github.com/anthropics/claude-code/tree/main/plugins/learning-output-style) | anthropics/claude-code | Interactive learning mode that requests meaningful code contributions at decision points (mimics the unshipped Learning output style) | Boris Cherny | 1.0.0 |

## marketing

| Plugin | Marketplace | Description | Author | Version |
|--------|-------------|-------------|--------|---------|
| [content-marketing](https://github.com/wshobson/agents) | claude-code-workflows | Content marketing strategy, web research, and information synthesis for marketing operations | Seth Hobson | 1.2.0 |
| [seo-analysis-monitoring](https://github.com/wshobson/agents) | claude-code-workflows | Content freshness analysis, cannibalization detection, and authority building for SEO | Seth Hobson | 1.2.0 |
| [seo-content-creation](https://github.com/wshobson/agents) | claude-code-workflows | SEO content writing, planning, and quality auditing with E-E-A-T optimization | Seth Hobson | 1.2.0 |
| [seo-technical-optimization](https://github.com/wshobson/agents) | claude-code-workflows | Technical SEO optimization including meta tags, keywords, structure, and featured snippets | Seth Hobson | 1.2.0 |

## media

| Plugin | Marketplace | Description | Author | Version |
|--------|-------------|-------------|--------|---------|
| [nanobanana](https://github.com/MadAppGang/claude-code/tree/main/plugins/nanobanana) | mag-claude-plugins | AI image generation and editing using Google Gemini 3 Pro Image API (Nano Banana Pro). Simple Node.js CLI with markdown styles, batch generation, r... | Jack Rudenko | 2.2.3 |
| [video-comparer](https://github.com/daymade/claude-code-skills/tree/main/) | daymade/claude-code-skills | Compare two videos and generate interactive HTML reports with quality metrics (PSNR, SSIM) and frame-by-frame visual comparisons. Use when analyzin... | None | 1.0.0 |
| [video-editing](https://github.com/MadAppGang/claude-code/tree/main/plugins/video-editing) | mag-claude-plugins | Professional video editing toolkit with FFmpeg operations, Whisper transcription, and Apple Final Cut Pro project generation. Features intelligent ... | Jack Rudenko | 1.0.1 |

## modernization

| Plugin | Marketplace | Description | Author | Version |
|--------|-------------|-------------|--------|---------|
| [codebase-cleanup](https://github.com/wshobson/agents) | claude-code-workflows | Technical debt reduction, dependency updates, and code refactoring automation | Seth Hobson | 1.2.0 |
| [framework-migration](https://github.com/wshobson/agents) | claude-code-workflows | Framework updates, migration planning, and architectural transformation workflows | Seth Hobson | 1.2.2 |

## monitoring

| Plugin | Marketplace | Description | Author | Version |
|--------|-------------|-------------|--------|---------|
| [sentry](https://github.com/getsentry/sentry-for-claude.git) | anthropics/claude-plugins-official | Sentry error monitoring integration. Access error reports, analyze stack traces, search issues by fingerprint, and debug production errors directly... | None | 1.0.0 |

## operations

| Plugin | Marketplace | Description | Author | Version |
|--------|-------------|-------------|--------|---------|
| [distributed-debugging](https://github.com/wshobson/agents) | claude-code-workflows | Distributed system tracing and debugging across microservices | Seth Hobson | 1.2.0 |
| [error-diagnostics](https://github.com/wshobson/agents) | claude-code-workflows | Error tracing, root cause analysis, and smart debugging for production systems | Seth Hobson | 1.2.0 |
| [incident-response](https://github.com/wshobson/agents) | claude-code-workflows | Production incident management, triage workflows, and automated incident resolution | Seth Hobson | 1.2.2 |
| [observability-monitoring](https://github.com/wshobson/agents) | claude-code-workflows | Metrics collection, logging infrastructure, distributed tracing, SLO implementation, and monitoring dashboards | Seth Hobson | 1.2.1 |

## packages

| Plugin | Marketplace | Description | Author | Version |
|--------|-------------|-------------|--------|---------|
| [creator-studio-pack](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/packages/creator-studio-pack) | claude-code-plugins-plus | Complete plugin suite for builder-filmmakers: Build products AND create viral videos. 20 plugins covering documentation, video production, content ... | Jeremy Longshore | 1.0.0 |

## payments

| Plugin | Marketplace | Description | Author | Version |
|--------|-------------|-------------|--------|---------|
| [payment-processing](https://github.com/wshobson/agents) | claude-code-workflows | Payment gateway integration with Stripe, PayPal, checkout flow implementation, subscription billing, and PCI compliance | Seth Hobson | 1.2.1 |

## performance

| Plugin | Marketplace | Description | Author | Version |
|--------|-------------|-------------|--------|---------|
| [alerting-rule-creator](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/performance/alerting-rule-creator) | claude-code-plugins-plus | Create intelligent alerting rules for performance monitoring | Jeremy Longshore | 1.0.0 |
| [apm-dashboard-creator](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/performance/apm-dashboard-creator) | claude-code-plugins-plus | Create Application Performance Monitoring dashboards | Jeremy Longshore | 1.0.0 |
| [application-performance](https://github.com/wshobson/agents) | claude-code-workflows | Application profiling, performance optimization, and observability for frontend and backend systems | Seth Hobson | 1.2.1 |
| [application-profiler](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/performance/application-profiler) | claude-code-plugins-plus | Profile application performance with CPU, memory, and execution time analysis | Jeremy Longshore | 1.0.0 |
| [bottleneck-detector](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/performance/bottleneck-detector) | claude-code-plugins-plus | Detect and resolve performance bottlenecks | Jeremy Longshore | 1.0.0 |
| [cache-performance-optimizer](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/performance/cache-performance-optimizer) | claude-code-plugins-plus | Optimize caching strategies for improved performance | Jeremy Longshore | 1.0.0 |
| [capacity-planning-analyzer](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/performance/capacity-planning-analyzer) | claude-code-plugins-plus | Analyze and plan for capacity requirements | Jeremy Longshore | 1.0.0 |
| [cpu-usage-monitor](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/performance/cpu-usage-monitor) | claude-code-plugins-plus | Monitor and analyze CPU usage patterns in applications | Jeremy Longshore | 1.0.0 |
| [database-cloud-optimization](https://github.com/wshobson/agents) | claude-code-workflows | Database query optimization, cloud cost optimization, and scalability improvements | Seth Hobson | 1.2.0 |
| [database-query-profiler](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/performance/database-query-profiler) | claude-code-plugins-plus | Profile and optimize database queries for performance | Jeremy Longshore | 1.0.0 |
| [distributed-tracing-setup](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/performance/distributed-tracing-setup) | claude-code-plugins-plus | Set up distributed tracing for microservices | Jeremy Longshore | 1.0.0 |
| [error-rate-monitor](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/performance/error-rate-monitor) | claude-code-plugins-plus | Monitor and analyze application error rates | Jeremy Longshore | 1.0.0 |
| [infrastructure-metrics-collector](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/performance/infrastructure-metrics-collector) | claude-code-plugins-plus | Collect comprehensive infrastructure performance metrics | Jeremy Longshore | 1.0.0 |
| [load-test-runner](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/performance/load-test-runner) | claude-code-plugins-plus | Create and execute load tests for performance validation | Jeremy Longshore | 1.0.0 |
| [log-analysis-tool](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/performance/log-analysis-tool) | claude-code-plugins-plus | Analyze logs for performance insights and issues | Jeremy Longshore | 1.0.0 |
| [memory-leak-detector](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/performance/memory-leak-detector) | claude-code-plugins-plus | Detect memory leaks and analyze memory usage patterns | Jeremy Longshore | 1.0.0 |
| [metrics-aggregator](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/performance/metrics-aggregator) | claude-code-plugins-plus | Aggregate and centralize performance metrics | Jeremy Longshore | 1.0.0 |
| [network-latency-analyzer](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/performance/network-latency-analyzer) | claude-code-plugins-plus | Analyze network latency and optimize request patterns | Jeremy Longshore | 1.0.0 |
| [optimize](https://github.com/ananddtyagi/claude-code-marketplace) | cc-marketplace | Analyze and optimize code performance |  Anand Tyagi | 1.0.0 |
| [performance-budget-validator](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/performance/performance-budget-validator) | claude-code-plugins-plus | Validate application against performance budgets | Jeremy Longshore | 1.0.0 |
| [performance-optimization-advisor](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/performance/performance-optimization-advisor) | claude-code-plugins-plus | Get comprehensive performance optimization recommendations | Jeremy Longshore | 1.0.0 |
| [performance-regression-detector](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/performance/performance-regression-detector) | claude-code-plugins-plus | Detect performance regressions in CI/CD pipeline | Jeremy Longshore | 1.0.0 |
| [real-user-monitoring](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/performance/real-user-monitoring) | claude-code-plugins-plus | Implement Real User Monitoring for actual performance data | Jeremy Longshore | 1.0.0 |
| [resource-usage-tracker](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/performance/resource-usage-tracker) | claude-code-plugins-plus | Track and optimize resource usage across the stack | Jeremy Longshore | 1.0.0 |
| [response-time-tracker](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/performance/response-time-tracker) | claude-code-plugins-plus | Track and optimize application response times | Jeremy Longshore | 1.0.0 |
| [sla-sli-tracker](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/performance/sla-sli-tracker) | claude-code-plugins-plus | Track SLAs, SLIs, and SLOs for service reliability | Jeremy Longshore | 1.0.0 |
| [synthetic-monitoring-setup](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/performance/synthetic-monitoring-setup) | claude-code-plugins-plus | Set up synthetic monitoring for proactive performance tracking | Jeremy Longshore | 1.0.0 |
| [throughput-analyzer](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/performance/throughput-analyzer) | claude-code-plugins-plus | Analyze and optimize system throughput | Jeremy Longshore | 1.0.0 |

## plan

| Plugin | Marketplace | Description | Author | Version |
|--------|-------------|-------------|--------|---------|
| [discuss](https://github.com/ananddtyagi/claude-code-marketplace) | cc-marketplace | Collaborative technical discussion with proactive requirements gathering | Bohdan Triapitsyn | 1.0.0 |
| [double-check](https://github.com/ananddtyagi/claude-code-marketplace) | cc-marketplace | An easy way to force agent to think again if it's statement that the "Job is done and production ready" is actually done - usually it's not. Thanks... | Robert S | 1.0.0 |
| [plan](https://github.com/ananddtyagi/claude-code-marketplace) | cc-marketplace | For easy problems, start here. For harder problems, do this after Explore. | Galen Ward | 1.0.0 |
| [ultrathink](https://github.com/ananddtyagi/claude-code-marketplace) | cc-marketplace | Use /ultrathink <TASK_DESCRIPTION> to launch a Coordinator Agent that directs four specialist sub-agents—Architect, Research, Coder, and Tester—to ... | Jeronim Morina | 1.0.0 |

## productivity

| Plugin | Marketplace | Description | Author | Version |
|--------|-------------|-------------|--------|---------|
| [000-jeremy-content-consistency-validator](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/productivity/000-jeremy-content-consistency-validator) | claude-code-plugins-plus | Read-only validator that generates comprehensive discrepancy reports comparing messaging consistency across ANY HTML-based website (WordPress, Hugo... | Jeremy Longshore | 1.0.0 |
| [002-jeremy-yaml-master-agent](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/productivity/002-jeremy-yaml-master-agent) | claude-code-plugins-plus | Intelligent YAML validation, generation, and transformation agent with schema inference, linting, and format conversion capabilities | Jeremy Longshore | 1.0.0 |
| [003-jeremy-vertex-ai-media-master](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/productivity/003-jeremy-vertex-ai-media-master) | claude-code-plugins-plus | Comprehensive Google Vertex AI multimodal mastery for Jeremy - video processing (6+ hours), audio generation, image creation with Gemini 2.0/2.5 an... | Jeremy Longshore | 1.0.0 |
| [004-jeremy-google-cloud-agent-sdk](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/productivity/004-jeremy-google-cloud-agent-sdk) | claude-code-plugins-plus | Google Cloud Agent Development Kit (ADK) and Agent Starter Pack mastery - build containerized multi-agent systems with production-ready templates, ... | Jeremy Longshore | 1.0.0 |
| [Notion](https://github.com/makenotion/claude-code-notion-plugin.git) | anthropics/claude-plugins-official | Notion workspace integration. Search pages, create and update documents, manage databases, and access your team's knowledge base directly from Clau... | None | 1.0.0 |
| [agent-context-manager](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/productivity/agent-context-manager) | claude-code-plugins-plus | Automatically detects and loads AGENTS.md files to provide agent-specific instructions | Jeremy Longshore | 1.0.0 |
| [ai-commit-gen](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/productivity/ai-commit-gen) | claude-code-plugins-plus | AI-powered commit message generator - analyzes your git diff and creates conventional commit messages instantly | Jeremy Longshore | 1.0.0 |
| [asana](https://github.com/anthropics/claude-plugins-official/tree/main/external_plugins/asana) | anthropics/claude-plugins-official | Asana project management integration. Create and manage tasks, search projects, update assignments, track progress, and integrate your development ... | None | 1.0.0 |
| [atlassian](https://github.com/atlassian/atlassian-mcp-server.git) | anthropics/claude-plugins-official | Connect to Atlassian products including Jira and Confluence. Search and create issues, access documentation, manage sprints, and integrate your dev... | None | 1.0.0 |
| [circleback](https://github.com/circlebackai/claude-code-plugin.git) | anthropics/claude-plugins-official | Circleback conversational context integration. Search and access meetings, emails, calendar events, and more. | None | 1.0.0 |
| [claude-code-setup](https://github.com/anthropics/claude-plugins-official/tree/main/plugins/claude-code-setup) | anthropics/claude-plugins-official | Analyze codebases and recommend tailored Claude Code automations such as hooks, skills, MCP servers, and subagents. | Anthropic | 1.0.0 |
| [claude-md-management](https://github.com/anthropics/claude-plugins-official/tree/main/plugins/claude-md-management) | anthropics/claude-plugins-official | Tools to maintain and improve CLAUDE.md files - audit quality, capture session learnings, and keep project memory current. | Anthropic | 1.0.0 |
| [claude-md-progressive-disclosurer](https://github.com/daymade/claude-code-skills/tree/main/) | daymade/claude-code-skills | Optimize user CLAUDE.md files by applying progressive disclosure principles. This skill should be used when users want to reduce CLAUDE.md bloat, m... | None | 1.0.1 |
| [claude-never-forgets](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/community/claude-never-forgets) | claude-code-plugins-plus | Persistent memory plugin for Claude Code - remembers preferences, decisions, and corrections across sessions and context limits | yldrmahmet | 0.1.0 |
| [code-review](https://github.com/anthropics/claude-plugins-official/tree/main/plugins/code-review) | anthropics/claude-plugins-official | Automated code review for pull requests using multiple specialized agents with confidence-based scoring to filter false positives | Anthropic | 1.0.0 |
| [code-review](https://github.com/anthropics/claude-code/tree/main/plugins/code-review) | anthropics/claude-code | Automated code review for pull requests using multiple specialized agents with confidence-based scoring to filter false positives | Boris Cherny | 1.0.0 |
| [code-simplifier](https://github.com/anthropics/claude-plugins-official/tree/main/plugins/code-simplifier) | anthropics/claude-plugins-official | Agent that simplifies and refines code for clarity, consistency, and maintainability while preserving functionality. Focuses on recently modified c... | Anthropic | 1.0.0 |
| [commit-commands](https://github.com/anthropics/claude-plugins-official/tree/main/plugins/commit-commands) | anthropics/claude-plugins-official | Commands for git commit workflows including commit, push, and PR creation | Anthropic | 1.0.0 |
| [commit-commands](https://github.com/anthropics/claude-code/tree/main/plugins/commit-commands) | anthropics/claude-code | Commands for git commit workflows including commit, push, and PR creation | Anthropic | 1.0.0 |
| [docs-cleaner](https://github.com/daymade/claude-code-skills/tree/main/) | daymade/claude-code-skills | Consolidates redundant documentation while preserving all valuable content. Use when cleaning up documentation bloat, merging redundant docs, reduc... | None | 1.0.0 |
| [domain-memory-agent](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/mcp/domain-memory-agent) | claude-code-plugins-plus | Knowledge base with TF-IDF semantic search and extractive summarization - no ML dependencies required | Jeremy Longshore | 1.0.0 |
| [experienced-engineer](https://github.com/ananddtyagi/claude-code-marketplace) | cc-marketplace | Comprehensive plugin with specialized engineering subagents (API Architect, Security Specialist, Code Quality Reviewer, etc.) and productivity comm... | Anand Tyagi | 1.0.0 |
| [fact-checker](https://github.com/daymade/claude-code-skills/tree/main/) | daymade/claude-code-skills | Verifies factual claims in documents using web search and official sources, then proposes corrections with user confirmation. Use when the user ask... | None | 1.0.0 |
| [formatter](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/examples/formatter) | claude-code-plugins-plus | Code formatting plugin using hooks to auto-format on save | None | 1.0.0 |
| [gamma-pack](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/saas-packs/gamma-pack) | claude-code-plugins-plus | Complete Gamma integration skill pack with 24 skills covering AI presentations, document generation, templates, and visual content creation. Flagsh... | Jeremy Longshore | 1.0.0 |
| [github](https://github.com/anthropics/claude-plugins-official/tree/main/external_plugins/github) | anthropics/claude-plugins-official | Official GitHub MCP server for repository management. Create issues, manage pull requests, review code, search repositories, and interact with GitH... | None | 1.0.0 |
| [gitlab](https://github.com/anthropics/claude-plugins-official/tree/main/external_plugins/gitlab) | anthropics/claude-plugins-official | GitLab DevOps platform integration. Manage repositories, merge requests, CI/CD pipelines, issues, and wikis. Full access to GitLab's comprehensive ... | None | 1.0.0 |
| [granola-pack](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/saas-packs/granola-pack) | claude-code-plugins-plus | Complete Granola integration skill pack with 24 skills covering AI meeting notes, transcription, summaries, and meeting intelligence. Flagship tier... | Jeremy Longshore | 1.0.0 |
| [hookify](https://github.com/anthropics/claude-plugins-official/tree/main/plugins/hookify) | anthropics/claude-plugins-official | Easily create custom hooks to prevent unwanted behaviors by analyzing conversation patterns or from explicit instructions. Define rules via simple ... | Anthropic | 1.0.0 |
| [hookify](https://github.com/anthropics/claude-code/tree/main/plugins/hookify) | anthropics/claude-code | Easily create custom hooks to prevent unwanted behaviors by analyzing conversation patterns or from explicit instructions. Define rules via simple ... | Daisy Hollman | 0.1.0 |
| [linear](https://github.com/anthropics/claude-plugins-official/tree/main/external_plugins/linear) | anthropics/claude-plugins-official | Linear issue tracking integration. Create issues, manage projects, update statuses, search across workspaces, and streamline your software developm... | None | 1.0.0 |
| [linear-pack](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/saas-packs/linear-pack) | claude-code-plugins-plus | Complete Linear integration skill pack with 24 skills covering issue tracking, project management, workflows, and team collaboration. Flagship tier... | Jeremy Longshore | 1.0.0 |
| [neurodivergent-visual-org](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/productivity/neurodivergent-visual-org) | claude-code-plugins-plus | Create ADHD-friendly visual organizational tools (Mermaid diagrams) optimized for neurodivergent thinking patterns with accessibility modes | Jack Reis | 3.1.1 |
| [overnight-dev](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/productivity/overnight-dev) | claude-code-plugins-plus | Run Claude autonomously for 6-8 hours overnight using Git hooks that enforce TDD - wake up to fully tested features | Intent Solutions IO | 1.0.0 |
| [ppt-creator](https://github.com/daymade/claude-code-skills/tree/main/) | daymade/claude-code-skills | Create professional slide decks from topics or documents. Generates structured content with data-driven charts, speaker notes, and complete PPTX fi... | None | 1.0.0 |
| [pr-review-toolkit](https://github.com/anthropics/claude-plugins-official/tree/main/plugins/pr-review-toolkit) | anthropics/claude-plugins-official | Comprehensive PR review agents specializing in comments, tests, error handling, type design, code quality, and code simplification | Anthropic | 1.0.0 |
| [pr-review-toolkit](https://github.com/anthropics/claude-code/tree/main/plugins/pr-review-toolkit) | anthropics/claude-code | Comprehensive PR review agents specializing in comments, tests, error handling, type design, code quality, and code simplification | Anthropic | 1.0.0 |
| [prettier-markdown-hook](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/productivity/prettier-markdown-hook) | claude-code-plugins-plus | Automatically format markdown files with prettier when Claude stops responding, with configurable organization and path exclusions | Terry Li | 1.0.0 |
| [project-planner-skill](https://github.com/adrianpuiu/claude-skills-marketplace/tree/main/project-planner-skill) | adrianpuiu/claude-skills-marketplace | Comprehensive project planning and documentation generator for software projects. Creates structured requirements documents, system design document... | George A Puiu | 1.0.0 |
| [prompt-optimizer](https://github.com/daymade/claude-code-skills/tree/main/) | daymade/claude-code-skills | Transform vague prompts into precise, well-structured specifications using EARS (Easy Approach to Requirements Syntax) methodology. Use when users ... | None | 1.1.0 |
| [slack](https://github.com/anthropics/claude-plugins-official/tree/main/external_plugins/slack) | anthropics/claude-plugins-official | Slack workspace integration. Search messages, access channels, read threads, and stay connected with your team's communications while coding. Find ... | None | 1.0.0 |
| [transcript-fixer](https://github.com/daymade/claude-code-skills/tree/main/) | daymade/claude-code-skills | Corrects speech-to-text (ASR/STT) transcription errors in meeting notes, lecture recordings, interviews, and voice memos through dictionary-based r... | None | 1.1.0 |
| [travel-assistant](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/productivity/travel-assistant) | claude-code-plugins-plus | Intelligent travel assistant with real-time weather, currency conversion, timezone info, and AI-powered itinerary planning. Your complete travel co... | Jeremy Longshore | 1.0.0 |
| [vibe-guide](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/productivity/vibe-guide) | claude-code-plugins-plus | Non-technical progress summaries for Claude Code work (hides diffs/log noise). | Intent Solutions | 1.0.0 |

## productivity-organization

| Plugin | Marketplace | Description | Author | Version |
|--------|-------------|-------------|--------|---------|
| [document-skills-docx](https://github.com/ComposioHQ/awesome-claude-skills/tree/master/document-skills/docx) | awesome-claude-skills | Skills for working with Microsoft Word documents including creation, editing, and formatting using DOCX format. | None | 1.0.0 |
| [document-skills-pdf](https://github.com/ComposioHQ/awesome-claude-skills/tree/master/document-skills/pdf) | awesome-claude-skills | Skills for working with PDF documents including creation, editing, forms, and advanced PDF operations. | None | 1.0.0 |
| [document-skills-pptx](https://github.com/ComposioHQ/awesome-claude-skills/tree/master/document-skills/pptx) | awesome-claude-skills | Skills for working with PowerPoint presentations including creation, editing, and formatting using PPTX format. | None | 1.0.0 |
| [document-skills-xlsx](https://github.com/ComposioHQ/awesome-claude-skills/tree/master/document-skills/xlsx) | awesome-claude-skills | Skills for working with Excel spreadsheets including creation, editing, formulas, and data manipulation. | None | 1.0.0 |
| [file-organizer](https://github.com/ComposioHQ/awesome-claude-skills/tree/master/file-organizer) | awesome-claude-skills | Intelligently organizes files and folders by understanding context, finding duplicates, and suggesting better organizational structures. | None | 1.0.0 |
| [invoice-organizer](https://github.com/ComposioHQ/awesome-claude-skills/tree/master/invoice-organizer) | awesome-claude-skills | Automatically organizes invoices and receipts for tax preparation by reading files, extracting information, and renaming consistently. | None | 1.0.0 |
| [raffle-winner-picker](https://github.com/ComposioHQ/awesome-claude-skills/tree/master/raffle-winner-picker) | awesome-claude-skills | Randomly selects winners from lists, spreadsheets, or Google Sheets for giveaways and contests with cryptographically secure randomness. | None | 1.0.0 |
| [tailored-resume-generator](https://github.com/ComposioHQ/awesome-claude-skills/tree/master/tailored-resume-generator) | awesome-claude-skills | Analyzes job descriptions and generates tailored resumes that highlight relevant experience, skills, and achievements to maximize interview chances. | None | 1.0.0 |

## quality

| Plugin | Marketplace | Description | Author | Version |
|--------|-------------|-------------|--------|---------|
| [code-review-ai](https://github.com/wshobson/agents) | claude-code-workflows | AI-powered architectural review and code quality analysis | Seth Hobson | 1.2.0 |
| [comprehensive-review](https://github.com/wshobson/agents) | claude-code-workflows | Multi-perspective code analysis covering architecture, security, and best practices | Seth Hobson | 1.2.1 |
| [performance-testing-review](https://github.com/wshobson/agents) | claude-code-workflows | Performance analysis, test coverage review, and AI-powered code quality assessment | Seth Hobson | 1.2.0 |

## refactoring

| Plugin | Marketplace | Description | Author | Version |
|--------|-------------|-------------|--------|---------|
| [refractor](https://github.com/ananddtyagi/claude-code-marketplace) | cc-marketplace | Refactor code following best practices and design patterns |  Anand Tyagi | 1.0.0 |

## security

| Plugin | Marketplace | Description | Author | Version |
|--------|-------------|-------------|--------|---------|
| [access-control-auditor](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/security/access-control-auditor) | claude-code-plugins-plus | Audit access control implementations | Jeremy Longshore | 1.0.0 |
| [authentication-validator](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/security/authentication-validator) | claude-code-plugins-plus | Validate authentication implementations | Jeremy Longshore | 1.0.0 |
| [backend-api-security](https://github.com/wshobson/agents) | claude-code-workflows | API security hardening, authentication implementation, authorization patterns, rate limiting, and input validation | Seth Hobson | 1.2.0 |
| [clerk-pack](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/saas-packs/clerk-pack) | claude-code-plugins-plus | Complete Clerk integration skill pack with 24 skills covering authentication, user management, embeddable UIs, and identity platform. Flagship tier... | Jeremy Longshore | 1.0.0 |
| [compliance-report-generator](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/security/compliance-report-generator) | claude-code-plugins-plus | Generate compliance reports | Jeremy Longshore | 1.0.0 |
| [cors-policy-validator](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/security/cors-policy-validator) | claude-code-plugins-plus | Validate CORS policies | Jeremy Longshore | 1.0.0 |
| [csrf-protection-validator](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/security/csrf-protection-validator) | claude-code-plugins-plus | Validate CSRF protection | Jeremy Longshore | 1.0.0 |
| [data-privacy-scanner](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/security/data-privacy-scanner) | claude-code-plugins-plus | Scan for data privacy issues | Jeremy Longshore | 1.0.0 |
| [dependency-checker](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/security/dependency-checker) | claude-code-plugins-plus | Check dependencies for known vulnerabilities, outdated packages, and license compliance | Jeremy Longshore | 1.0.0 |
| [encryption-tool](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/security/encryption-tool) | claude-code-plugins-plus | Encrypt and decrypt data with various algorithms | Jeremy Longshore | 1.0.0 |
| [frontend-mobile-security](https://github.com/wshobson/agents) | claude-code-workflows | XSS prevention, CSRF protection, content security policies, mobile app security, and secure storage patterns | Seth Hobson | 1.2.0 |
| [gdpr-compliance-scanner](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/security/gdpr-compliance-scanner) | claude-code-plugins-plus | Scan for GDPR compliance issues | Jeremy Longshore | 1.0.0 |
| [hipaa-compliance-checker](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/security/hipaa-compliance-checker) | claude-code-plugins-plus | Check HIPAA compliance | Jeremy Longshore | 1.0.0 |
| [input-validation-scanner](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/security/input-validation-scanner) | claude-code-plugins-plus | Scan input validation practices | Jeremy Longshore | 1.0.0 |
| [owasp-compliance-checker](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/security/owasp-compliance-checker) | claude-code-plugins-plus | Check OWASP Top 10 compliance | Jeremy Longshore | 1.0.0 |
| [pci-dss-validator](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/security/pci-dss-validator) | claude-code-plugins-plus | Validate PCI DSS compliance | Jeremy Longshore | 1.0.0 |
| [penetration-tester](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/security/penetration-tester) | claude-code-plugins-plus | Automated penetration testing for web applications with OWASP Top 10 coverage | Jeremy Longshore | 1.0.0 |
| [repomix-safe-mixer](https://github.com/daymade/claude-code-skills/tree/main/) | daymade/claude-code-skills | Safely package codebases with repomix by automatically detecting and removing hardcoded credentials before packing. Use when packaging code for dis... | None | 1.0.0 |
| [reverse-engineering](https://github.com/wshobson/agents) | claude-code-workflows | Binary reverse engineering, malware analysis, firmware security, and software protection research for authorized security research, CTF competition... | Dávid Balatoni | 1.0.0 |
| [secret-scanner](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/security/secret-scanner) | claude-code-plugins-plus | Scan codebase for exposed secrets, API keys, passwords, and sensitive credentials | Jeremy Longshore | 1.0.0 |
| [security-agent](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/examples/security-agent) | claude-code-plugins-plus | Security review subagent for code analysis | None | 1.0.0 |
| [security-audit-reporter](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/security/security-audit-reporter) | claude-code-plugins-plus | Generate comprehensive security audit reports | Jeremy Longshore | 1.0.0 |
| [security-compliance](https://github.com/wshobson/agents) | claude-code-workflows | SOC2, HIPAA, and GDPR compliance validation, secrets scanning, compliance checklists, and regulatory documentation | Seth Hobson | 1.2.0 |
| [security-guidance](https://github.com/anthropics/claude-plugins-official/tree/main/plugins/security-guidance) | anthropics/claude-plugins-official | Security reminder hook that warns about potential security issues when editing files, including command injection, XSS, and unsafe code patterns | Anthropic | 1.0.0 |
| [security-guidance](https://github.com/anthropics/claude-code/tree/main/plugins/security-guidance) | anthropics/claude-code | Security reminder hook that warns about potential security issues when editing files, including command injection, XSS, and unsafe code patterns | David Dworken | 1.0.0 |
| [security-headers-analyzer](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/security/security-headers-analyzer) | claude-code-plugins-plus | Analyze HTTP security headers | Jeremy Longshore | 1.0.0 |
| [security-incident-responder](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/security/security-incident-responder) | claude-code-plugins-plus | Assist with security incident response | Jeremy Longshore | 1.0.0 |
| [security-misconfiguration-finder](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/security/security-misconfiguration-finder) | claude-code-plugins-plus | Find security misconfigurations | Jeremy Longshore | 1.0.0 |
| [security-pro-pack](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/packages/security-pro-pack) | claude-code-plugins-plus | Professional security tools for Claude Code: vulnerability scanning, compliance, cryptography audit, container & API security | Jeremy Longshore | 1.0.0 |
| [security-scanning](https://github.com/wshobson/agents) | claude-code-workflows | SAST analysis, dependency vulnerability scanning, OWASP Top 10 compliance, container security scanning, and automated security hardening | Seth Hobson | 1.2.3 |
| [session-security-checker](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/security/session-security-checker) | claude-code-plugins-plus | Check session security implementation | Jeremy Longshore | 1.0.0 |
| [soc2-audit-helper](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/security/soc2-audit-helper) | claude-code-plugins-plus | Assist with SOC2 audit preparation | Jeremy Longshore | 1.0.0 |
| [sql-injection-detector](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/security/sql-injection-detector) | claude-code-plugins-plus | Detect SQL injection vulnerabilities | Jeremy Longshore | 1.0.0 |
| [ssl-certificate-manager](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/security/ssl-certificate-manager) | claude-code-plugins-plus | Manage and monitor SSL/TLS certificates | Jeremy Longshore | 1.0.0 |
| [vulnerability-scanner](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/security/vulnerability-scanner) | claude-code-plugins-plus | Comprehensive vulnerability scanning for code, dependencies, and configurations with CVE detection | Jeremy Longshore | 1.0.0 |
| [xss-vulnerability-scanner](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/security/xss-vulnerability-scanner) | claude-code-plugins-plus | Scan for XSS vulnerabilities | Jeremy Longshore | 1.0.0 |

## skill-enhancers

| Plugin | Marketplace | Description | Author | Version |
|--------|-------------|-------------|--------|---------|
| [axiom](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/skill-enhancers/axiom) | claude-code-plugins-plus | Battle-tested Claude Code skills for modern xOS (iOS, iPadOS, watchOS, tvOS) development - 13 production-ready skills covering debugging, concurren... | Charles Wiltgen | 0.1.6 |
| [calendar-to-workflow](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/skill-enhancers/calendar-to-workflow) | claude-code-plugins-plus | Enhances calendar Skills by automating meeting prep and workflow triggers | Claude Code Plugins Team | 0.1.0 |
| [file-to-code](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/skill-enhancers/file-to-code) | claude-code-plugins-plus | Converts file references into executable code implementations | Claude Code Plugins Team | 0.1.0 |
| [research-to-deploy](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/skill-enhancers/research-to-deploy) | claude-code-plugins-plus | Transforms research findings into deployed solutions automatically | Claude Code Plugins Team | 0.1.0 |
| [search-to-slack](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/skill-enhancers/search-to-slack) | claude-code-plugins-plus | Automatically posts search results to Slack channels | Claude Code Plugins Team | 0.1.0 |
| [web-to-github-issue](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/skill-enhancers/web-to-github-issue) | claude-code-plugins-plus | Enhances web_search Skill by automatically creating GitHub issues from research findings. Research topics, extract key insights, and generate forma... | Claude Code Plugins Team | 1.0.0 |

## testing

| Plugin | Marketplace | Description | Author | Version |
|--------|-------------|-------------|--------|---------|
| [accessibility-test-scanner](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/testing/accessibility-test-scanner) | claude-code-plugins-plus | A11y compliance testing with WCAG 2.1/2.2 validation, screen reader compatibility, and automated accessibility audits | Claude Code Plugin Hub | 1.0.0 |
| [api-fuzzer](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/testing/api-fuzzer) | claude-code-plugins-plus | Fuzz testing for APIs with malformed inputs, edge cases, and security vulnerability detection | Claude Code Plugin Hub | 1.0.0 |
| [api-test-automation](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/testing/api-test-automation) | claude-code-plugins-plus | Automated API endpoint testing with request generation, validation, and comprehensive test coverage | Jeremy Longshore | 1.0.0 |
| [browser-compatibility-tester](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/testing/browser-compatibility-tester) | claude-code-plugins-plus | Cross-browser testing with BrowserStack, Selenium Grid, and Playwright - test across Chrome, Firefox, Safari, Edge | Claude Code Plugin Hub | 1.0.0 |
| [chaos-engineering-toolkit](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/testing/chaos-engineering-toolkit) | claude-code-plugins-plus | Chaos testing for resilience with failure injection, latency simulation, and system resilience validation | Claude Code Plugin Hub | 1.0.0 |
| [contract-test-validator](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/testing/contract-test-validator) | claude-code-plugins-plus | API contract testing with Pact, OpenAPI validation, and consumer-driven contract verification | Claude Code Plugin Hub | 1.0.0 |
| [database-test-manager](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/testing/database-test-manager) | claude-code-plugins-plus | Database testing utilities with test data setup, transaction rollback, and schema validation | Claude Code Plugin Hub | 1.0.0 |
| [e2e-test-framework](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/testing/e2e-test-framework) | claude-code-plugins-plus | End-to-end test automation with Playwright, Cypress, and Selenium for browser-based testing | Jeremy Longshore | 1.0.0 |
| [integration-test-runner](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/testing/integration-test-runner) | claude-code-plugins-plus | Run and manage integration test suites with environment setup, database seeding, and cleanup | Jeremy Longshore | 1.0.0 |
| [load-balancer-tester](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/testing/load-balancer-tester) | claude-code-plugins-plus | Test load balancing strategies with traffic distribution validation and failover testing | Claude Code Plugin Hub | 1.0.0 |
| [mobile-app-tester](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/testing/mobile-app-tester) | claude-code-plugins-plus | Mobile app test automation with Appium, Detox, XCUITest - test iOS and Android apps | Claude Code Plugin Hub | 1.0.0 |
| [mutation-test-runner](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/testing/mutation-test-runner) | claude-code-plugins-plus | Mutation testing to validate test quality by introducing code changes and verifying tests catch them | Jeremy Longshore | 1.0.0 |
| [performance-test-suite](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/testing/performance-test-suite) | claude-code-plugins-plus | Load testing and performance benchmarking with metrics analysis and bottleneck identification | Jeremy Longshore | 1.0.0 |
| [playwright](https://github.com/anthropics/claude-plugins-official/tree/main/external_plugins/playwright) | anthropics/claude-plugins-official | Browser automation and end-to-end testing MCP server by Microsoft. Enables Claude to interact with web pages, take screenshots, fill forms, click e... | None | 1.0.0 |
| [playwright-skill](https://github.com/lackeyjb/playwright-skill/tree/main/) | lackeyjb/playwright-skill | Claude Code Skill for general-purpose browser automation with Playwright. Claude autonomously writes and executes custom automation for testing pag... | lackeyjb | 4.1.0 |
| [regression-test-tracker](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/testing/regression-test-tracker) | claude-code-plugins-plus | Track and run regression tests to ensure new changes don't break existing functionality | Jeremy Longshore | 1.0.0 |
| [security-test-scanner](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/testing/security-test-scanner) | claude-code-plugins-plus | Automated security vulnerability testing covering OWASP Top 10, SQL injection, XSS, CSRF, and authentication issues | Jeremy Longshore | 1.0.0 |
| [smoke-test-runner](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/testing/smoke-test-runner) | claude-code-plugins-plus | Quick smoke test suites to verify critical functionality after deployments | Claude Code Plugin Hub | 1.0.0 |
| [snapshot-test-manager](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/testing/snapshot-test-manager) | claude-code-plugins-plus | Manage and update snapshot tests with intelligent diff analysis and selective updates | Claude Code Plugin Hub | 1.0.0 |
| [test-coverage-analyzer](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/testing/test-coverage-analyzer) | claude-code-plugins-plus | Analyze code coverage metrics, identify untested code, and generate comprehensive coverage reports | Jeremy Longshore | 1.0.0 |
| [test-data-generator](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/testing/test-data-generator) | claude-code-plugins-plus | Generate realistic test data including users, products, orders, and custom schemas for comprehensive testing | Jeremy Longshore | 1.0.0 |
| [test-doubles-generator](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/testing/test-doubles-generator) | claude-code-plugins-plus | Generate mocks, stubs, spies, and fakes for unit testing with Jest, Sinon, and test frameworks | Claude Code Plugin Hub | 1.0.0 |
| [test-environment-manager](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/testing/test-environment-manager) | claude-code-plugins-plus | Manage test environments with Docker Compose, Testcontainers, and environment isolation | Claude Code Plugin Hub | 1.0.0 |
| [test-file](https://github.com/ananddtyagi/claude-code-marketplace) | cc-marketplace | Generate comprehensive tests for a specific file |  Anand Tyagi | 1.0.0 |
| [test-orchestrator](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/testing/test-orchestrator) | claude-code-plugins-plus | Orchestrate complex test workflows with dependencies, parallel execution, and smart test selection | Claude Code Plugin Hub | 1.0.0 |
| [test-report-generator](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/testing/test-report-generator) | claude-code-plugins-plus | Generate comprehensive test reports with coverage, trends, and stakeholder-friendly formats | Claude Code Plugin Hub | 1.0.0 |
| [unit-test-generator](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/testing/unit-test-generator) | claude-code-plugins-plus | Automatically generate comprehensive unit tests from source code with multiple testing framework support | Jeremy Longshore | 1.0.0 |
| [unit-testing](https://github.com/wshobson/agents) | claude-code-workflows | Unit and integration test automation for Python and JavaScript with debugging support | Seth Hobson | 1.2.0 |
| [visual-regression-tester](https://github.com/jeremylongshore/claude-code-plugins-plus/tree/main/plugins/testing/visual-regression-tester) | claude-code-plugins-plus | Visual diff testing with Percy, Chromatic, BackstopJS - catch unintended UI changes | Claude Code Plugin Hub | 1.0.0 |

## tooling

| Plugin | Marketplace | Description | Author | Version |
|--------|-------------|-------------|--------|---------|
| [sap-api-style](https://github.com/secondsky/sap-skills/tree/main/plugins/sap-api-style) | secondsky/sap-skills | This skill provides comprehensive guidance for documenting SAP APIs following official SAP API Style Guide standards. It should be used when creati... | None | 2.1.0 |
| [skill-review](https://github.com/secondsky/sap-skills/tree/main/plugins/skill-review) | secondsky/sap-skills | Comprehensive deep-dive documentation review process for sap-skills repository. Use this skill when investigating suspected issues in a skill, majo... | None | 2.1.0 |

## ui-development

| Plugin | Marketplace | Description | Author | Version |
|--------|-------------|-------------|--------|---------|
| [sap-fiori-tools](https://github.com/secondsky/sap-skills/tree/main/plugins/sap-fiori-tools) | secondsky/sap-skills | Develops SAP Fiori applications using SAP Fiori tools extensions for VS Code and SAP Business Application Studio. Use when: generating Fiori Elemen... | None | 2.1.0 |
| [sapui5](https://github.com/secondsky/sap-skills/tree/main/plugins/sapui5) | secondsky/sap-skills | This skill should be used when developing SAP UI5 applications, including creating freestyle apps, Fiori Elements apps, custom controls, testing, d... | None | 2.1.0 |
| [sapui5-cli](https://github.com/secondsky/sap-skills/tree/main/plugins/sapui5-cli) | secondsky/sap-skills | Manages SAPUI5/OpenUI5 projects using the UI5 Tooling CLI (@ui5/cli). Use when initializing UI5 projects, configuring ui5.yaml or ui5-workspace.yam... | None | 2.1.0 |
| [sapui5-linter](https://github.com/secondsky/sap-skills/tree/main/plugins/sapui5-linter) | secondsky/sap-skills | Use this skill when working with the UI5 Linter (@ui5/linter) for static code analysis of SAPUI5/OpenUI5 applications and libraries. This skill sho... | None | 2.1.0 |

## utilities

| Plugin | Marketplace | Description | Author | Version |
|--------|-------------|-------------|--------|---------|
| [code-refactoring](https://github.com/wshobson/agents) | claude-code-workflows | Code cleanup, refactoring automation, and technical debt management with context restoration | Seth Hobson | 1.2.0 |
| [dependency-management](https://github.com/wshobson/agents) | claude-code-workflows | Dependency auditing, version management, and security vulnerability scanning | Seth Hobson | 1.2.0 |
| [error-debugging](https://github.com/wshobson/agents) | claude-code-workflows | Error analysis, trace debugging, and multi-agent problem diagnosis | Seth Hobson | 1.2.0 |
| [macos-cleaner](https://github.com/daymade/claude-code-skills/tree/main/) | daymade/claude-code-skills | Intelligent macOS disk space analysis and cleanup with safety-first philosophy. Use when users report disk space issues, need to clean their Mac, o... | None | 1.1.0 |
| [repomix-unmixer](https://github.com/daymade/claude-code-skills/tree/main/) | daymade/claude-code-skills | Extract files from repomix packaged formats (XML, Markdown, JSON) with automatic format detection and validation | None | 1.0.0 |
| [team-collaboration](https://github.com/wshobson/agents) | claude-code-workflows | Team workflows, issue management, standup automation, and developer experience optimization | Seth Hobson | 1.2.0 |
| [twitter-reader](https://github.com/daymade/claude-code-skills/tree/main/) | daymade/claude-code-skills | Fetch Twitter/X post content by URL using jina.ai API to bypass JavaScript restrictions. Use when Claude needs to retrieve tweet content including ... | None | 1.0.0 |
| [youtube-downloader](https://github.com/daymade/claude-code-skills/tree/main/) | daymade/claude-code-skills | Download YouTube videos and HLS streams (m3u8) from platforms like Mux, Vimeo, etc. using yt-dlp and ffmpeg. Use when users request downloading vid... | None | 1.1.0 |

## workflow

| Plugin | Marketplace | Description | Author | Version |
|--------|-------------|-------------|--------|---------|
| [claude-desktop-extension](https://github.com/ananddtyagi/claude-code-marketplace) | cc-marketplace | This command provides the context necessary for Claude Code to create the Desktop Extension or .dxt file of an MCP. |  Anand Tyagi | 1.0.0 |
| [conductor](https://github.com/MadAppGang/claude-code/tree/main/plugins/conductor) | mag-claude-plugins | Context-Driven Development workflow inspired by Gemini Conductor. Full-featured implementation with TDD workflow (Red/Green/Refactor), Phase Comple... | Jack Rudenko | 2.0.1 |
| [lyra](https://github.com/ananddtyagi/claude-code-marketplace) | cc-marketplace | Lyra - a master-level AI prompt optimization specialist. |  Anand Tyagi | 1.0.0 |
| [sugar](https://github.com/ananddtyagi/claude-code-marketplace) | cc-marketplace | Transform Claude Code into an autonomous AI development powerhouse with rich task context, specialized agents, and intelligent workflow automation | Steven Leggett | 2.0.0 |

## workflows

| Plugin | Marketplace | Description | Author | Version |
|--------|-------------|-------------|--------|---------|
| [conductor](https://github.com/wshobson/agents) | claude-code-workflows | Context-Driven Development plugin that transforms Claude Code into a project management tool with structured workflow: Context → Spec & Plan → Impl... | Seth Hobson | 1.2.0 |
| [full-stack-orchestration](https://github.com/wshobson/agents) | claude-code-workflows | End-to-end feature orchestration with testing, security, performance, and deployment | Seth Hobson | 1.2.1 |
| [git-pr-workflows](https://github.com/wshobson/agents) | claude-code-workflows | Git workflow automation, pull request enhancement, and team onboarding processes | Seth Hobson | 1.2.1 |
| [tdd-workflows](https://github.com/wshobson/agents) | claude-code-workflows | Test-driven development methodology with red-green-refactor cycles and code review | Seth Hobson | 1.2.1 |
## Contributing

We welcome contributions! Please see our [contributing guidelines](CONTRIBUTING.md) for details on how to add new marketplaces or plugins.

To add a new plugin or marketplace:
1. Fork this repository
2. Add the entry to the appropriate section
3. Ensure the plugin is verified and documented
4. Submit a pull request with a clear description
