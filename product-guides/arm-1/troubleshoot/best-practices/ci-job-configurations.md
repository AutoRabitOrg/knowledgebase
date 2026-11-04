# CI Job Configurations

Best practices for performing CI/CD based on [Version Control](https://www.autorabit.com/blog/7-tips-for-salesforce-version-control-integration/) are outlined below.

### 1. Automatic Incremental Deployment

**Usage:** Any Test Environment

**Overview:** Can be used for staging/production environments if sufficient test automation is in place. Typically triggered by a merge into `master` that runs a deployment to Staging, executes a full regression test suite, and only deploys to Production if all tests pass.

**Benefits:**

* True Continuous Integration
* Low maintenance
* Full control via Git (Agile AF)

### 2. Manual Incremental Deployment

**Usage:** Environments with scheduled deployment windows (e.g., UAT), or for deploying merged code from a dev branch to dev orgs.

**Overview:** Similar to Automatic Incremental Deployment but without the on-commit trigger.

**Benefits:**

* Low maintenance with better control over schedule
* Enables developers to deploy to dev orgs without altering baseline revisions

### 3. Pull Request Validation

**Usage:** Environments requiring stable testing windows (e.g., UAT) or deploying merged code to dev orgs.

**Overview:** Requires Pull Request Support plugin. Must be paired with a deployment job to maintain validation org synchronization with the upstream branch.

### 4. Continuous Validation

**Usage:** Validate full release packages alongside CI deployments in test environments.

**Overview:** Can be scheduled or triggered on-commit depending on validation time and commit frequency. Ideal for dedicated environments without dev access.

**Limitations:**

* Manual deployment needed to sync with Production.
* Manual baseline revision updates required.
* Risks if manual pre-deployment steps are involved; frequent smaller releases mitigate this.

### 5. Automatic Validation

**Usage:** Production validation during early stages of staging or regression cycles.

**Overview:** Combines Automatic Incremental and Continuous Validation; triggered on commit or post-activity and performs a validate-only build.

**Limitations:**

* Manual deployment needed post-release to sync with Production.
* Requires manual baseline update.
* Risk of failure with manual pre-deployment steps.

### 6. Backup

A scheduled job that pulls changes after a given date into a backup repository.

> **Important Note:** Not a replacement for Branching Baseline. Relies on modification date and is subject to API limits. Should supplement but not replace periodic manual execution of Branching Baseline.

### 7. Test

Executes functional tests (e.g., Provar, AccelQ) independently of code deployment.

**Usage:** Useful for conditional execution (e.g., run tests post-data migration or before another deployment).

### 8. Custom Features

#### Unit Tests

**Defaults:**

* Production orgs: `RunLocalTests`
* Sandbox orgs: `NoTestRun`

**Custom Feature:** `RunTestsBasedOnChanges` generates input dynamically for `RunSelectedTests` based on mappings from **Admin > Salesforce Org Mgmt**.

> **Important Note:** Mapping updates only when a CI Job is manually triggered with Run Code Coverage enabled. Frequent updates needed via manual/scheduled jobs (e.g., weekly). Concurrent deployments or validations during test runs can corrupt data.

#### Rollback

**Usage:** Only in Stage/Production.

* Lower environments should use Git-based rollbacks.
* In Production, enables immediate reversion after detecting critical issues.
* Validate rollback packages in Stage to identify potential rollback-specific errors.
* Optionally validate rollback immediately post-deployment to prepare a Quick Deploy.

#### Profile Packaging

* Avoid special handling by default, except excluding IP Ranges and environment-specific settings.
* EZ Commits can exclude User Permissions (no change = no deployment).
* The "ignore missing visibility settings" is a last-resort workaround that can desync branch and org. Standard fields are unsupported.
