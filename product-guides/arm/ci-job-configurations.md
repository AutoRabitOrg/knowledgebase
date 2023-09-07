# CI Job Configurations

The best practices to follow while performing CI/CD based on [Version Control](https://www.autorabit.com/blog/7-tips-for-salesforce-version-control-integration/) are discussed in the following article.

### 1. Automatic Incremental Deployment <a href="#1-automatic-incremental-deployment" id="1-automatic-incremental-deployment"></a>

**Usage:** Any Test Environment

**Overview:** Automatic Incremental Deployment can be used for staging/production environment as long as the sufficient test automation is in place (which is triggered by merge into master, which runs deploy to Staging + full regression test suite and only deploys to Production if all tests pass)

**Benefits:**

* the only true Continuous Integration job&#x20;
* low maintenance&#x20;
* full control through GIT (Agile AF)

### 2. Manual Incremental Deployment <a href="#2-manual-incremental-deployment" id="2-manual-incremental-deployment"></a>

**Usage:** Any environment with scheduled deployment windows, i.e. UAT where testers expect stability throughout the testing phase; can also be used to deploy merged code from dev branch to dev orgs.

**Overview:** Same as the above but without the on-commit trigger.

**Benefits:**

* still low maintenance, but better control over deployment schedule
* allows developers to deploy to their dev orgs without requiring access to edit baseline revisions

### 3. Pull Request Validation <a href="#3-pull-request-validation" id="3-pull-request-validation"></a>

**Usage:** Any environment with scheduled deployment windows, i.e. UAT where testers expect stability throughout the testing phase; can also be used to deploy merged code from dev branch to dev orgs.

**Overview:** Requires the Pull Request Support plugin enabled on the repository used. Has to always be accompanied by a deployment job (automatic incremental deployment) that deploys any code from the upstream branch to the validation org; the validation org has to be in sync with the upstream branch at all times.

### 4. Continuous Validation <a href="#4-continuous-validation" id="4-continuous-validation"></a>

**Usage:** Validate the full release package in parallel with CI deployments running in test environments.&#x20;

**Overview:** Can be either on-commit or scheduled, depending on the expected validation time and commit velocity (if running all local tests with a lot of revisions being committed, the schedule makes more sense). This works best if having a dedicated environment, where no developers have access, but can also use the Staging environment (with an on-commit deploy job on a staging branch later on in the flow).

**Limitations:**

* When using a dedicated validation org requires a manual deployment after the release to keep in sync with Production
* Requires a manual baseline revision update after each release
* Can be compromised when deployment depends on pre-deployment manual steps; making the releases as small and as often as possible reduces this risk.

### 5. Automatic Validation <a href="#5-automatic-validation" id="5-automatic-validation"></a>

**Usage:** Production validation at the start of Staging (regression); often the final week or two of a large release will be dedicated to final sign-offs; production validation should be triggered as early as possible.

**Overview:** This is a special case combining types 1 and 4; job fires either on commit or as a post-activity of another job, but runs a validate-only build.

**Limitations**

* When using a dedicated validation org requires a manual deployment after the release to keep in sync with Production
* Requires a manual baseline revision update after each release
* Can be compromised when deployment depends on pre-deployment manual steps; making the releases as small and as often as possible reduces this risk.

### 6. Backup <a href="#6-backup" id="6-backup"></a>

A scheduled job pulling changes after a given date (or last retrieve when incremental) into the backup repository. This can be used to get more granular change tracking, as Branching Baseline cannot be scheduled.

{% hint style="info" %}
**Important Note**: This is not a Branching Baseline, as it bases on a modification date, and it’s susceptible to API limits which Branching Baseline works around. It should only be used in addition to Branching Baseline, which should still be periodically executed manually.
{% endhint %}

### 7. Test <a href="#7-test" id="7-test"></a>

Allows executing functional tests (i.e. Provar, AccelQ) without the need for code deployment.

This can be used to control the execution flow (i.e. trigger tests only after data migration is done by the previous CI Job or trigger another deployment only after tests are done).

### 8. Custom Features <a href="#8-custom-features" id="8-custom-features"></a>

#### Unit Tests <a href="#unit-tests" id="unit-tests"></a>

By default, all jobs will use Salesforce Defaults, which is **RunLocalTests** for Production orgs and **NoTestRun** for Sandbox orgs.

**RunTestsBasedOnChanges** is a custom feature in AutoRABIT, which dynamically generates input for the **RunSelectedTests** test level based on a mapping stored in the **Admin > Salesforce Org Mgmt** page.

{% hint style="info" %}
**Important Note**: The mapping is only updated when a CI Job is triggered manually with the Run Code Coverage option enabled; in orgs that have a large number of tests, as well as in any CI setup, the mapping will not be continuously updated and has to be either updated manually or through scheduled Code Coverage Reports (e.g. once a week over the weekend) - any deployment or validation started while the tests are running will lock the coverage tables in Salesforce, corrupting the mapping data.
{% endhint %}

#### Rollback <a href="#rollback" id="rollback"></a>

Rollback should only be used in the highest environments (Stage/Production). Reverting changes in lower environments should always be done through GIT, to avoid desynchronizing the org from its branch.

In Production, the Rollback can be used to revert the deployment right away, in order to address a critical issue found after the release. The stage can be used to validate the rollback package, as often there will be errors specific to rollback, which would have to be addressed by modifying its contents on the fly (i.e. a new Flow created or a new PermissionSet having users already assigned).

Rollback package can also be validated right after the deployment in Production, to prepare a Quick Deploy, for even faster reaction time in case of issues found during business hours.

#### Profile Packaging <a href="#profile-packaging" id="profile-packaging"></a>

Aside from the option to exclude IP Ranges, which is a security concern, as well as environment-specific configuration (dev and test environments often have different restrictions than Production), none of the special handling options for Profiles should be used by default.

User Permissions can be excluded in EZ Commits, which would not attempt deploying any of them (no change = no deployment)

The option to ignore missing visibility settings is only valid as a last resort workaround, as it gets the branch out of sync from the org anytime it fires: new visibility is added to the profile for a component not yet deployed → visibility is ignored by AutoRABIT → the component is added in subsequent revision and deployed → the build never goes back to the ignored visibility setting (access exists in the branch, but not in the org). Standard fields are not supported for this option.
