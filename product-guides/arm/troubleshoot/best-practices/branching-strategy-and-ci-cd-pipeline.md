# Branching Strategy & CI/CD Pipeline

There is no “one size fits all” solution when it comes to branching strategy. This page can only provide general best practices, which need to be adjusted based on specific requirements of the given project (environment landscape and other SDLC details).

### Source of Truth <a href="#source-of-truth" id="source-of-truth"></a>

The GIT repository is the sole Source of Truth for the project. Once established, changes can only go from GIT to Salesforce, with the CI Jobs being the only point of entry. Manual changes in the integrated environments, deployments from multiple branches, or other sources (ChangeSet, Workbench, etc.) will get the environment out of sync with the branch, defeating the purpose of [version control](https://www.autorabit.com/blog/do-i-really-need-salesforce-version-control/).&#x20;

The default main branch in every GIT repository is master and all other branches should be created from it.

### Branching and Merging: What's the Difference? <a href="#branching-baseline" id="branching-baseline"></a>

A **branch** allows you to create a copy (or snapshot) of the repository that you can modify in parallel without altering the main set. You can continue to commit new changes to the branch as you work, while others commit to the trunk or master without the changes affecting each other.

Once you’re comfortable with the experimental code, you will want to make it part of the trunk or master again. This is where **merging** comes in. Since the version control system has recorded every change so far, it knows how each file has been altered. By merging the branch with the trunk or master (or even another branch), your version control tool will attempt to seamlessly merge each file and line of code automatically. Once a branch is merged it then updates the trunk or master with the latest files.

### Branching Baseline

The first step of establishing a [CI/CD Pipeline](https://www.autorabit.com/blog/essential-aspects-of-a-salesforce-ci-cd-suite/) is seeding the repository using the Branching Baseline feature of AutoRABIT. It’s a single commit into the master branch, containing all metadata from Production org.

That baseline revision should be then used as a baseline for all CI Jobs (the only delta after the baseline should be considered for deployments). The Branching Baseline should only be done once in the repository, as for the CI/CD to work correctly, the changes need to be introduced selectively by the developers.

Once the master branch is baselined, all remaining branches can be created.

{% hint style="info" %}
For best tracking and visibility, it’s recommended to have a branch for each Salesforce environment in the Pipeline.&#x20;
{% endhint %}

Branching baseline can also be used for periodical metadata backups into a separate backup repository, which can be used to track unplanned manual changes in the orgs.

{% hint style="info" %}
The backup repository must not be connected to the CI/CD Pipeline.&#x20;
{% endhint %}

### Development <a href="#development" id="development"></a>

Each Sandbox used for development should have a dedicated dev branch. Additional ephemeral branches, usually referred to as feature branches, can be created off of dev and deleted once merged.

For review and approval purposes, the feature branches should be merged to dev using Pull Requests. Every GIT hosting offers its own proprietary API for Pull Requests (GitHub and Bitbucket are currently supported in AutoRABIT, with Azure DevOps to be released soon).

A dedicated CI Job can be created for Pull Request validations, to assist reviewers with Sandbox validation of the code being changed in the Pull Request, as well as running PMD if any Apex changes are present.

The only CI Jobs linked with dev branches would be the Pull Request validation and an on-commit deployment to the Pull Request validation Sandbox, to ensure it’s in sync with the upstream branch.

{% hint style="info" %}
If only one development Sandbox exists, the flow can be simplified: single dev branch + feature branches, with deployment to QA Sandbox directly from dev.
{% endhint %}

Once the code in dev, is ready to be moved to QA, the branch should be merged into an integration branch.

{% hint style="info" %}
It’s a best practice to always use the “Entire Branch” merge in AutoRABIT, as that is the only actual merge operation; all other merge types are custom wrappers built on git cherry-pick commands, which should never be used as a default promotion technique (see more on this in the Hotfix section below).
{% endhint %}

### Back-Sync <a href="#backsync" id="backsync"></a>

It’s imperative that all dev branches continuously pull the integrated code from integration branch, to get changes introduced from other dev branches. The cadence of these downstream merges depends on the release timelines, but in most cases, it can and should be done as often as new work is being committed.

The integrated code merged down to dev should then be deployed to the linked development Sandbox, either using a CI Job (requires elevated access to modify baseline revision) or Selective Deployment (from a revision range or a single revision).

### Integration and Testing <a href="#integration-and-testing" id="integration-and-testing"></a>

Starting from the integration branch, the flow becomes linear all the way to Production (master), with the driving factor being progression through the testing phases of the project. Each branch has a single CI Job listening to a webhook from GIT, triggering incremental deployments to its test environments (e.g. int > QA > UAT).

Once the testing phase is complete and the changes are signed off on, the branch will be merged to the next one in the flow, triggering a deployment, followed by another phase of testing.

### Release <a href="#release" id="release"></a>

The last stage of the [CI/CD Pipeline](https://www.autorabit.com/blog/essential-aspects-of-a-salesforce-ci-cd-suite/) is staging and release to Production. The staging phase is important, as all deployments until this point were incremental, meaning that components that will build up the Production deployment package were being deployed independently; in some scenarios, new issues could come up in Production only because of the components being deployed in a single package.

A dedicated stage branch is a good practice, as it allows for easier tracking of code signed-off for release to Production. It also allows for a consistent CI Job configuration across the pipeline (on-commit deployment upon merge to staging, same as with all lower testing environments.

The code can be promoted to master in parallel with final regression testing in Staging - the sooner the validation against the Production environment happens, the better, as there is always a risk of environment-specific issues happening in Production, which were not observed earlier deployments.

{% hint style="info" %}
To catch potential issues even earlier, a continuous validate-only job running from release branch against Staging can be configured, running a full release package validation either on each commit to release, or on schedule.
{% endhint %}

Both Staging and Production CI Jobs should be configured as non-incremental and on-commit with rollback option enabled; Stage should deploy, while Production only validate, both running Unit Tests (either RunLocalTests or RunTestsBasedOnChanges).

{% hint style="info" %}
If an issue is found during regression in Staging, the release should be reverted using AutoRABIT Rollback feature, with the entire release process restarted after a fix is introduced to the branch; no incremental fix deployments should happen at that stage.
{% endhint %}

### Hotfix <a href="#hotfix" id="hotfix"></a>

A hotfix process, also known as an emergency change request, occurs when there is a critical issue found in Production, which needs to be fixed sooner than the nearest planned release.&#x20;

Such change is exactly the same as other changes (committed to a feature branch, merged into dev branch, and optionally to integration branch), but skips most testing phases.&#x20;

Once hotfix revision is introduced to the dev/integration branch, it can be promoted directly to the stage/master branch for final validation and deployment to Production. This can be achieved either by “Single Revision”, “Commit Label” or “Release Label” merge types in AutoRABIT.&#x20;

{% hint style="info" %}
If the hotfix change is promoted directly from dev to stage, it has to then be merged down (entire branch merge on all branches in the reverse order, from the stage down to integration), in order for all other dev branches to be able to pull it during Back-Sync. If the developer promotes it to integration before cherry-picking to stage, this step can be omitted.
{% endhint %}
