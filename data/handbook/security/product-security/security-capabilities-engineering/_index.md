---
title: "Security Capabilities Engineering"
description: "Security Capabilities Engineering Team Charter"
---

## Organizational Structure

Security Capabilities Engineering consists of three complementary teams:

### Vulnerability Management

- Focus: Vulnerability detection, workflow automation, and risk visibility
- Key Deliverables: Automated triage, scanning coverage, customer artifacts, FedRAMP automation

### Product Security Incident Response Team (PSIRT)

- Focus: Vulnerability triage, coordinated remediation & disclosure, and security releases
- Key Deliverables: Bug bounty program management, variant hunting, coordinated vulnerability remediation, and security releases coordination

### Product Security Engineering (ProdSecEng)

- Focus: Security automation, product contributions, and tooling integration
- Key Deliverables: Security features, process automation, custom tooling maintenance and migration

## Mission Statement

Security Capabilities Engineering enables GitLab through collaborative processes, data insights, and automation to build customer trust. We serve as the force multiplier for Product Security by transforming vulnerability intelligence into actionable insights, creating scalable security capabilities, and establishing the processes and tooling that enable GitLab to ship secure software at velocity.

## Value Proposition

We provide comprehensive vulnerability lifecycle management, scalable automation solutions, and data-driven security insights so that GitLab's engineering teams can build and ship secure software with confidence, customers receive transparent and timely security information, and Product Security teams can focus on high-value strategic initiatives rather than manual operations.

## Strategic Vision

Security Capabilities Engineering operates at the intersection of three critical capabilities:

- **Data Insights That Inform Decisions**: Transform vulnerability data into actionable intelligence and transparent customer artifacts
- **Product-First Automation That Scales**: Build security capabilities to support using GitLab to secure GitLab, validating solutions before customer adoption
- **Processes That Enable Others**: Establish standardized, documented workflows that create consistency and efficiency across the security lifecycle

## Scope and Responsibilities

### Primary Areas of Ownership

Security Capabilities Engineering owns the end-to-end vulnerability lifecycle and enabling automation across GitLab:

#### Vulnerability Intelligence & Lifecycle Management

- **Detection & Correlation**: Comprehensive vulnerability scanning across GitLab-hosted environments, artifacts, and their associated supply chains
- **Triage & Assessment**: Technical evaluation of vulnerability severity, exploitability, and business impact
- **Remediation Coordination**: Collaboration with Engineering teams to prioritize and verify security fixes
- **Coordinated Disclosure**: Management of bug bounty program and responsible vulnerability disclosure

#### Security Automation & Engineering

- **Product Security Tooling**: Development and maintenance of specialized automation that enables scalable Product Security operations
- **Security Enhancement Features**: Product contributions that reduce GitLab's risk and enhance customer security capabilities
- **Tooling Integration & Sunsetting**: Migration of custom security tooling into GitLab product features

#### Data & Metrics

- **Vulnerability Metrics & Reporting**: Strategic and operational metrics for security posture visibility
- **Compliance Artifacts**: Automated generation of compliance-facing security documentation
- **Risk Communication**: Data-driven narratives that inform strategic decisions across GitLab

### Interface Points

#### Internal Security Team Collaboration

- Application Security (AppSec): Knowledge sharing, specialized product knowledge during incidents
- Security Platforms & Architecture (SPA): Exploitability POC development, Product Security Risk Register (PSRR) alignment
- Infrastructure Security: Cloud/infrastructure vulnerability triage, Wiz integration
- Security Operations (SecOps): Incident support, threat detection IOC/POC development
- Security Assurance: Compliance artifacts

#### Engineering & Product Collaboration

- Development Teams: Vulnerability issues in GitLab, remediation collaboration
- Product Teams: Early engagement on security features, user story validation, tooling integration planning
- Release Management: Security patch coordination, version compatibility assessment

#### External Stakeholders

- Customers: Transparent vulnerability disclosure, security advisories, compliance artifacts
- Security Researchers: HackerOne program management, coordinated disclosure process
- Security Community: Public disclosure coordination, industry best practices sharing

### Out of Scope

Not owned by Security Capabilities Engineering:

- Feature security reviews and threat modeling (owned by AppSec)
- Infrastructure and cloud security architecture (owned by InfraSec)
- End-user system vulnerabilities and patching (owned by CorpSec)
- Direct vulnerability remediation (owned by Engineering)
- Security compliance programs (owned by Security Assurance)
- GitLab Security product features (owned by Sec Section product teams)

## Operating Model

### Core Processes

**Vulnerability Lifecycle Workflow:**

1. **Detection**: Automated scanning across environments using Wiz, Trivy, and custom tooling
2. **Correlation & Enrichment**: VulnMapper normalizes findings and adds contextual data
3. **Triage**: Distributed model based on vulnerability type and team expertise
4. **Remediation**: Coordination with Engineering, tracking through GitLab issues
5. **Verification**: Validation that fixes are complete and not bypassable
6. **Disclosure**: Customer communication through security releases, CVEs, and advisories

**Automation Development:**

1. **Intake & Evaluation**: Requests assessed against automation criteria and product fit
2. **Use Case Documentation**: Clear problem statement and success criteria
3. **Product Alignment**: Assessment of fit with GitLab product vision
4. **Development**: Iterative development following GitLab workflow labels
5. **Validation**: Testing with security team stakeholders (Customer Zero)
6. **Handoff**: Transition to appropriate product team or operations maintenance

**Metrics & Reporting:**

1. **Data Collection**: Automated capture from VulnMapper, GitLab issues, and HackerOne
2. **Analysis**: Contextual enrichment and trend identification
3. **Stakeholder Communication**: Tailored reporting for different audiences
4. **Continuous Improvement**: Feedback loops to refine processes and priorities

### Work Tracking

Data is important to our team. We need data to make sure we are:

- Planning and prioritising the [right type of work](#right-type-of-work) (to make progress on our mission, and help achieve Operating Model goals)
- Making room and picking up work mid-milestone to meet our BAU/KTLO responsibilities and accommodate important, last-minute requests (i.e. unplanned work)
- Scoping and sizing our work accurately (so we can effectively set quarterly and strategic goals)
- Raising risks, dependencies, and blockers early (so we can proactively manage them)
- Providing stakeholders visibility into our progress

In order to make sure we can measure this across all three teams consistently, Security Capabilities Engineering has adopted the following work tracking practices:

| Tracking Dimension | Scale/Labels | What We Measure | Why |
|-------------------|--------------|-----------------|-----|
| Planning Periods | [Product Milestones](/handbook/product/product-processes/milestones/) | How often we plan work | We plan using Product Milestones to align our work with our stakeholders in Product and Engineering |
| **Priority** | `priority::1` (Urgent)<br>`priority::2` (High)<br>`priority::3` (Medium)<br>`priority::4` (Low) | Urgency and importance of work;<br>Target resolution timeframes | Ensures we address critical security work first, set stakeholder expectations, and align on milestones and due dates across teams |
| **Work Planning** | `Unplanned` label | Work added after milestone planning;<br>Planned vs unplanned capacity ratio | Helps us balance proactive work with reactive BAU/KTLO responsibilities and identify sources of interruptions to minimize future disruption |
| **Sizing & Effort** | Weight: 1, 2, 3, 5, 8<br>(Fibonacci sequence) | Complexity and effort required;<br>Team capacity and velocity | Enables accurate milestone and quarterly planning, assists in tracking % of planned/unplanned work, and helps identify when work needs to be broken down into manageable pieces |

Details of these practices are captured below.

#### Right Type of Work

Work for our teams comes from multiple different sources, which varies by team. In general, when striking a balance on the "right" type of work, we always consider:

- If work aligns with company goals
- If work aligns with strategic capabilities development
- If work aligns with building and giving feedback on GitLab product capabilities
- If work is aligned with strategic goals and critical projects
- If work is BAU and/or time sensitive to meet our responsibilities and commitments to customers and GitLab

#### Priority

We use the standard [GitLab Engineering priority scoped labels](/handbook/product-development/how-we-work/issue-triage/#priority) to reflect the priority of individual issues. Specific use cases are:

| Priority | Importance | Intention | Use Case |
| -------- | ---------- | --------- | --- |
| `~"priority::1"` | Urgent | We will address this as soon as possible regardless of the limit on our team capacity. Our target resolution time is 30 days. | Security incidents, active exploits, P1 vulnerabilities, production blockers |
| `~"priority::2"` | High   | We will address this soon and will provide capacity from our team for it in the next few releases. This will likely get resolved in 60-90 days. | Important security improvements, P2 vulnerabilities, planned security features |
| `~"priority::3"` | Medium | We want to address this but may have other higher priority items. This will likely get resolved in 90-120 days. | Standard security work, technical debt, P3 vulnerabilities |
| `~"priority::4"` | Low    | We don't have visibility when this will be addressed. No timeline designated. | Nice-to-have improvements, documentation, minor enhancements |

Priority is decided during milestone planning by the EM, and is informed by company-wide critical projects, stakeholder requests, customer commitments, risk ratings, and team needs.

#### Unplanned work and interruptions

We use the existing `~Unplanned` label on issues and MR that are added to the milestone after planning has been decided. This is regardless if it is work that can be done at any point during the milestone, or is something the team need to immediately switch to (urgent interruption).

This is important so that we can tell if our planned vs unplanned capacity percentages are appropriate, and we can identify the source or reason behind late work items (so we can minimize or set better expectations in the future).

#### Sizing and estimates

We use the standard [(modified) Fibonacci sequence scale](https://docs.gitlab.com/tutorials/scrum_events/standups_retrospectives_velocity/#deciding-the-value-of-story-points) to set issue weight. This allows us to track effort and resources needed to complete the work, based on the complexity.

| Weight | Complexity | Time Estimate | Use Case |
| --- | --- | --- | --- |
| 1 | Trivial, the simplest possible change; We are confident there will be no side effects | 1 day | Documentation updates, simple config changes or bug fix |
| 2 | Small, needs some testing but nothing involved; We understand all of the requirements | 1-2 days | Small bug fixes, minor feature additions |
| 3 | Moderate, will take some time and collaboration; The code footprint is bigger but the requirements are clear | 2-3 days | Standard security reviews, feature work that impacts a few files/tests |
| 5 | Complex, will take significant time and collaboration to finish; Requirements understood but likely gaps to workthrough along the way | 3-5 days | Security architecture changes, complex integrations |
| 8 | Very Complex, requires a high level of investigation and research before starting work; Involves much of the codebase and requires input from many to understand the requirements | 5-10 days | Major security initiatives, large refactors |
| 13+ | Split required, break into smaller issues | N/A |  |

This generally results in about 20 weight of work items per milestone (per team member), and is reduced based on other commitments (i.e. leave, holidays, G&D). A percentage of this would be planned in advanced of the milestone starting (60-80%), and the remaining weight capacity would be allocated during the milestone for unplanned, reactive work.

While milestone capacity is largely driven by time estimates, our team also considers the level of complexity when priorising work too. For example, commiting to multiple complex work items during a milestone carries a high amount of risk as it is possible we uncover gaps or additional work that needs doing and this could increase the time estimate. Our teams focuses on finding a balance of complexity, within a the maximum weight limit, for each milestone.

### Communication Channels

**GitLab:**

- Issue trackers in respective team projects
- MR reviews and collaboration on security fixes
- Epic tracking for cross-team strategic initiatives
- `@gitlab-com/gl-security/product-security/vulnerability-management` (Vulnerability Management)
- `@gitlab-com/gl-security/product-security/psirt-group` (PSIRT)
- `@gitlab-com/gl-security/product-security/product-security-engineering` (ProdSecEng)

**Slack:**

- `#security_help` - Primary channel for security questions and requests
- `#security-discuss` - Broader security discussions and knowledge sharing
- `@vulnerability-management` - Slack handle for VM team
- `@psirt-team` - Slack handle for PSIRT team
- `@product-security-engineering` - Slack handle for ProdSecEng team

## FY27 Initiatives

- Use Data as a Strategic Asset
- Establish a Unified Vulnerability Lifecycle
- Build a Product-First Mindset
