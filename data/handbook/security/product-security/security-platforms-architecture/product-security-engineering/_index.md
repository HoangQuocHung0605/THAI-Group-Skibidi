---
title: "Product Security Engineering"
description: "Product Security Engineering Team Charter"
---

Product Security Engineering (ProdSecEng) is part of [Security Capabilities Engineering](/handbook/security/product-security/security-capabilities-engineering/) (SecCapEng), alongside the Vulnerability Management and PSIRT teams.

## Mission Statement (Why)

ProdSecEng creates proactive and preventative controls that scale with the organization and improve product security.  We build ["paved roads"](https://netflixtechblog.com/scaling-appsec-at-netflix-part-2-c9e0f1488bc5) through product-first code contributions and automation that enables secure software development while maintaining Engineering's velocity.

## Value Proposition (What)

We provide hands-on engineering expertise, scalable automation solutions, and product contributions to enable the Product Security (ProdSec) department to focus on high-value security initiatives rather than manual work, and GitLab's product teams can rapidly deliver security capabilities that solve real customer problems.

## FY27 Focus Areas

- Vulnerability management product features and automation
- Active maintenance, sunsetting, and integration of tools into the product

## Scope and Responsibilities

### What we own

ProdSecEng owns the management and delivery of security engineering work across the following areas:

1. **Security Enhancement Features**: Security features and improvements that reduce GitLab's product risk and enhance customer security capabilities.
2. **"Paved Roads" for Security**: Product-first solutions that make it easy for development teams to follow security best practices.
3. **ProdSec Automation**: Automation that reduces manual burden for Product Security teams.
4. **Security Requirements Implementation**: Translating Security Division requirements and use cases into product features.
5. **ProdSec Tooling Integration**: Identifying custom ProdSec tools for integration into GitLab, managing implementation, rollout, and handover.
6. **Proof of Concepts and Validation**: Validating proposed security solutions before broader implementation or handoff.
7. **Custom Tooling Maintenance**: Maintaining projects and tooling on behalf of the Security Division. The full inventory, including path-forward categories and maintenance details, is available in the [internal handbook](https://internal.gitlab.com/handbook/security/product_security/product_security_engineering/) (accessible to GitLab team members only).
8. **Documentation and Knowledge Transfer**: Creating and maintaining documentation, runbooks, and guides for our contributions.

### Where we get work from

ProdSecEng sources work from several key areas and interfaces with teams that provide input to our backlog:

1. **ProdSec Automation Requests**: ProdSec teams identify automation candidates; we evaluate against our [intake automation request criteria](/handbook/security/product-security/security-platforms-architecture/security-interlock/prodsec-to-product-workflow/).
2. **Existing GitLab Security Enhancement Issues**: Security-related issues across GitLab projects, labeled `~ProdSecEng Candidate` for evaluation.
3. **Cross-functional Security Requests**: Requests (mentioned via `@gitlab-com/gl-security/product-security/product-security-engineering`) from Vulnerability Management, Security Compliance, Security Risk, Trust & Safety, or SIRT.
4. **Product Security Risk Register (PSRR)**: Systemic risks identified by Security Platforms & Architecture (SPA) and other ProdSec teams that need product engineering solutions.
5. **Security Interlock and Product Validation**: Validating GitLab security features through [Customer Zero](/handbook/security/product-security/security-platforms-architecture/security-interlock/) initiatives.

### Out of Scope

| Area | DRI |
|------|-----|
| Application security standards, reviews, or testing | [AppSec](/handbook/security/product-security/security-platforms-architecture/application-security/) |
| Infrastructure, cloud, or data security tooling or architecture | [InfraSec](/handbook/security/product-security/infrastructure-security/) |
| Vulnerability management operations | [Vulnerability Management](/handbook/security/product-security/vulnerability-management/) |
| Vulnerability disclosure and triage | [PSIRT](/handbook/security/product-security/psirt/) |

## Operating Model

ProdSecEng follows the shared [SecCapEng ways of working](/handbook/security/product-security/security-capabilities-engineering/) for planning, prioritization, sizing, and work tracking.

For details on our team-specific workflows, including backlog management, refinement, development, and handoff processes, see [Detailed Workflows](detailed-workflow/).

## Communication

- **Slack**: Ask in [`#security_help`](https://gitlab.enterprise.slack.com/archives/C094L6F5D2A) or [`#security-capabilities-engineering`](https://gitlab.enterprise.slack.com/archives/C0AEU6LHQ7R) on Slack and @ mention the `@product-security-engineering` handle
- **GitLab**: Mention `@gitlab-com/gl-security/product-security/product-security-engineering`
- **Issues**: Submit to the [ProdSecEng team repository](https://gitlab.com/gitlab-com/gl-security/product-security/product-security-engineering/product-security-engineering-team/-/issues/new)
- **Emergencies**: Page the Security Incident Response Team using `/security` in any Slack channel

We use "ProdSecEng" as our short name to avoid confusion with [Professional Services Engineer](/job-description-library/sales/professional-services-engineer/).

## Success Metrics

ProdSecEng tracks metrics through labeled merge requests and issues. The following metric labels drive our tracking and reporting:

### Metric Labels and Categories

| **Category** | **Label** | **Description** | **Why It Matters** | **Where to Apply** |
| --- | --- | --- | --- | --- |
| **Product Security Requirements** | `~ProdSecEngMetric::ProdSecRequirement` | Functionality within the product required by GitLab Product Security teams | Demonstrates our effectiveness at delivering capabilities that enable Product Security teams to secure GitLab using the product itself | Issues and Merge Requests, sometimes Epics |
| **Defense in Depth** | `~ProdSecEngMetric::Defense in Depth` | Modifications to existing non-vulnerable functionality to be more robust if an "earlier" security control fails | Shows our commitment to layered security approaches that reduce risk even when primary controls are compromised | Issues and Merge Requests, sometimes Epics |
| **Paved Roads** | `~ProdSecEngMetric::Paved Road` | New tools, methods, or checks that give GitLab's contributors an easier way to perform an activity securely | Measures our success at creating scalable, developer-friendly security solutions | Issues and Merge Requests, sometimes Epics |
| **Tooling Integration** | `~ProdSecEngMetric::Tooling Integration` | Work done as part of integrating functionality from custom in-house tooling into GitLab products | Tracks progress on reducing external dependencies and bringing Product Security tooling into the platform | Issues and Merge Requests, sometimes Epics |
| **Custom Tooling** | `~ProdSecEngMetric::Custom Tooling` | Work performed to build, maintain, or augment outside-of-the-product custom tooling needed to satisfy Product Security requirements | Reflects necessary investments in tooling to support Product Security operations | Issues and Merge Requests, sometimes Epics |
| **Sunsetting** | `~ProdSecEngMetric::Sunsetting` | Issues representing specific features or functionality required to deprecate a custom tool | Demonstrates progress toward consolidating tooling into GitLab products | Issues in the [product-security-engineering-team repo](https://gitlab.com/gitlab-com/gl-security/product-security/product-security-engineering/product-security-engineering-team/-/issues) |
| **Pending** | `~ProdSecEngMetric::Pending` | Work type isn't entirely clear yet, but we don't want to block progress | Allows us to track work that needs categorization without delaying momentum | Issues, Merge Requests, and Epics |
| **Internal** | `~ProdSecEngMetric::Internal` | Team tasks, for example processes & planning | Separates internal team operations from external-facing work | Issues and Merge Requests, Epics |

Refer to [our Tableau dashboard](https://10az.online.tableau.com/#/site/gitlab/views/ProductSecurityEngineering/ProdSecEngValueDeliveryMetrics?:iid=6) for metric data based on these labels.

### Strategic KPI

Based off the metrics we collect, below are the strategic Key Performance Indicators (KPI) we track to tell how we are doing on our mission.

| **Metric** | **Why It Matters** | **How it's Calculated** | **Measurement Frequency** | **Reporting Mechanism** |
| --- | --- | --- | --- | --- |
| **Product Security Team Requirements Delivered** | Demonstrates our effectiveness at delivering capabilities that enable Product Security teams to secure GitLab using our product | Count of merged MRs with `~ProdSecEngMetric::ProdSecRequirement` label | TBD | TBD |
| **Security Enhancements and Paved Roads Delivered** | Demonstrates our contribution to improving GitLab's security posture and enabling secure development practices across the organization | Count of merged MRs with `~ProdSecEngMetric::Defense in Depth` or `~ProdSecEngMetric::Paved Road` labels | TBD | TBD |
| **Custom Tool Value Integrated Into Product** | Measures our success at reducing external dependencies and consolidating Product Security tooling into GitLab | Percentage of distinct value propositions in current in-house custom tools that have been contributed to the product (tracked using `~ProdSecEngMetric::Tooling Integration` and `~ProdSecEngMetric::Sunsetting` labels) | TBD | TBD |

### Operational Metrics

To track team efficiency, below are operational KPI we track.

| **Metric** | **Why It Matters** | **How it's Calculated** | **Measurement Frequency** | **Reporting Mechanism** |
| --- | --- | --- | --- | --- |
| **Backlog Health and Refinement** | Ensures we have a well-maintained, prioritized backlog of work ready for development | Count of candidate issues refined, issues in `Ready for Development` status, participation in refinement across milestones | Monthly | TBD |
| **Milestone Predictability** | Tracks our ability to complete committed work within planned milestones | Actual vs. planned work completed in each milestone (measured by weight and metric labels applied) | Monthly | TBD |
| **Metric Label Coverage** | Ensures all work is properly categorized for tracking and reporting | Percentage of merged MRs and closed issues with appropriate `~ProdSecEngMetric::*` labels applied | Monthly | TBD |

## Team Composition

The ProdSecEng team consists of:

- Security Engineering Manager: Leads team prioritization, roadmap planning, and milestone planning; manages cross-functional relationships
- Product Security Engineers: Design, develop, and validate security features, automation solutions, and tooling integrations

### Development Goals

Our team is a mix of software and security engineers. Our plans for internal team growth and development are:

- Expand expertise in scalable security architecture and design patterns
- Develop hands-on experience with GitLab's codebase and development practices
- Build capabilities in AI security integration and implementation
- Enhance product management skills to better translate security requirements into user-centric solutions
- Strengthen cross-team collaboration and communication skills

## Review and Updates

This charter is reviewed quarterly. Next scheduled review: August 1, 2026.
