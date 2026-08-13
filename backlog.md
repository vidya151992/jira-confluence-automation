# Jira Delivery Health Automation Backlog

## Planning Context
- Delivery Strategy: MVP first (fastest path to usable dashboard)
- Timebox: 2 week sprint
- Phase Emphasis Order: Core Features, Testing, Documentation, Setup, Integration
- V1 Must-Have Outcomes:
  - Dashboard with key metrics (backlog/in-progress/blocked/completed)
  - Risk/SLA alerts
- Testing Depth: Unit + integration + API contract tests
- Documentation Depth: Standard docs (README, setup, API config, operations)

## Phase 1: Setup
- [ ] Define repository structure for app, jobs, dashboard, and tests.
- [ ] Create environment variable contract (.env.example) for Jira URL, email, API token, and schedule settings.
- [ ] Add configuration loader with validation for required runtime settings.
- [ ] Set up dependency management and lock file for reproducible installs.
- [ ] Configure linting and formatting tools.
- [ ] Configure pre-commit checks for lint, tests, and basic static checks.
- [ ] Add logging framework with structured JSON output.
- [ ] Add base error-handling utilities for retries and failure reporting.
- [ ] Create initial CI pipeline to run lint and test jobs on pull requests.
- [ ] Establish basic project board labels: feature, bug, test, docs, infra.

## Phase 2: Core Features
- [ ] Implement Jira API client with secure auth using email + API token.
- [ ] Implement pagination support for Jira issue retrieval.
- [ ] Build issue ingestion job for sprint, status, assignee, priority, labels, flags, and created/updated timestamps.
- [ ] Build data normalization layer for consistent field mapping.
- [ ] Implement business rule BR-1 to identify blocked items from status + blocker labels/flags.
- [ ] Implement business rule BR-2 to compute SLA risk based on configurable age threshold.
- [ ] Implement business rule BR-3 to preserve Jira priority values without remapping.
- [ ] Implement metric calculator for backlog, in-progress, blocked, completed counts.
- [ ] Implement trend calculator by sprint for velocity and flow-over-time snapshots.
- [ ] Build dashboard backend endpoints for summary metrics and filtered views.
- [ ] Build dashboard UI cards for core metrics and sprint trend.
- [ ] Add dashboard filters for assignee, sprint, and priority.
- [ ] Add risk/SLA alerts panel highlighting issues breaching threshold.
- [ ] Add last-refresh timestamp and data freshness status to dashboard.
- [ ] Add scheduler for automated refresh cadence (default daily, target hourly).
- [ ] Implement idempotent refresh behavior to avoid duplicate records.
- [ ] Add failure notification hook for ingestion or calculation failures.

## Phase 3: Integration
- [ ] Validate Jira API scopes and token permissions for required endpoints.
- [ ] Implement connectivity checks and startup health validation for Jira API.
- [ ] Integrate dashboard data store for persisted snapshots.
- [ ] Implement RBAC checks for dashboard viewers.
- [ ] Add audit log events for refresh start, refresh success, refresh failure, and alert trigger.
- [ ] Integrate TLS-only outbound API communication checks.
- [ ] Add configurable refresh schedule with safe defaults and max frequency guardrails.
- [ ] Validate timezone handling for reporting windows and sprint boundaries.
- [ ] Add fallback handling for Jira rate limits and transient API errors.
- [ ] Verify integration behavior across dev and UAT environments.

## Phase 4: Testing
- [ ] Create unit tests for Jira client auth, pagination, and error handling.
- [ ] Create unit tests for blocked item detection (BR-1).
- [ ] Create unit tests for SLA risk threshold logic (BR-2).
- [ ] Create unit tests for priority handling with no remapping (BR-3).
- [ ] Create unit tests for metric calculations and sprint trend outputs.
- [ ] Create integration tests for end-to-end ingest -> normalize -> compute -> persist flow.
- [ ] Create API contract tests for Jira endpoints used by the ingestion job.
- [ ] Create integration tests for dashboard filters (assignee, sprint, priority).
- [ ] Create integration tests for scheduler runs and idempotent refresh behavior.
- [ ] Create tests for rate-limit retry handling and transient failure recovery.
- [ ] Create tests for RBAC enforcement and unauthorized access rejection.
- [ ] Create tests for audit log emission on success/failure paths.
- [ ] Execute UAT test script with product and stakeholder sign-off criteria.
- [ ] Capture baseline performance results for refresh completion under expected data volume.

## Phase 5: Documentation
- [ ] Create README with architecture summary and local run steps.
- [ ] Create setup guide for environment variables and Jira token configuration.
- [ ] Create API configuration guide listing required Jira endpoints and scopes.
- [ ] Create operations runbook for scheduler management and troubleshooting.
- [ ] Document business rules (BR-1, BR-2, BR-3) with examples.
- [ ] Document dashboard metric definitions and filter behavior.
- [ ] Document alert semantics, thresholds, and expected operator response.
- [ ] Document incident response steps for failed refresh runs.
- [ ] Document UAT checklist and acceptance criteria.
- [ ] Add release notes template for MVP go-live.

## Sprint Exit Criteria (2 Weeks)
- [ ] Core dashboard metrics are visible and correct for latest Jira snapshot.
- [ ] Risk/SLA alerts are generated for threshold breaches.
- [ ] Automated refresh runs on schedule with audit logs.
- [ ] Unit, integration, and API contract tests pass in CI.
- [ ] README, setup, API config, and operations docs are complete.
- [ ] Product manager confirms MVP readiness for UAT.
