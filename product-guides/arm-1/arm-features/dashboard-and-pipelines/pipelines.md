# Pipelines

### Pipeline: Overview <a href="#pipeline-overview" id="pipeline-overview"></a>

A pipeline is a unidirectional flow that defines how changes progress from development orgs to the production org. It offers real-time visibility into:

1. Branches across DevOps stages: **Development, Integration, QA, UAT, Production**
2. Sync status between mapped Salesforce Orgs and branches (e.g., added/removed components)
3. Commits that are ahead or behind each stage

***

### Navigating to the Pipeline Dashboard Page <a href="#navigating-to-pipeline-dashboard-page" id="navigating-to-pipeline-dashboard-page"></a>

The **Pipeline** screen displays your environments, their connections, commit deltas, and deployment statuses.

**Steps to access the Pipeline view:**

1. Hover over the **DASHBOARD** tile and click **PIPELINE**.
2. Select a **Repository** to view your team’s branching structure.
3. Click the refresh icon:

<figure><img src="../../../../.gitbook/assets/image (936).png" alt="Pipeline refresh icon for latest data"><figcaption></figcaption></figure>

4. If no pipeline is configured for the selected repository, setup instructions are displayed:

<figure><img src="../../../../.gitbook/assets/image (937).png" alt="Pipeline not configured screen"><figcaption></figcaption></figure>

5. If the pipeline is configured, a detailed pipeline visualization is displayed:

<figure><img src="../../../../.gitbook/assets/image (938).png" alt="Configured pipeline dashboard with branch mapping" width="563"><figcaption></figcaption></figure>

6. For each environment, you can view:
   * **Deployment Status**
   * **Commits Ahead/Behind** (Forward arrow: ahead; Backward arrow: behind)

<figure><img src="../../../../.gitbook/assets/image (939).png" alt="Commit direction indicators: ahead and behind" width="317"><figcaption></figcaption></figure>

***

### Known Limitations <a href="#known-limitations" id="known-limitations"></a>

* Pipeline visualization is available **only for GIT repositories**.
* Branch types must be one of the following: **Development, Integration, QA, UAT, Production**. Unsupported branch categories will not display on the pipeline screen.
