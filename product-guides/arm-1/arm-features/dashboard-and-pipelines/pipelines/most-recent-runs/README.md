---
description: >-
  Most Recent Runs provides a quick snapshot of the latest execution for each
  release pipeline. It shows the most recent artifact used, the trigger time,
  and the current status of each stage, allowing u
---

# Most recent runs

Release Pipelines – viewing runs and drill down (step-by-step)

1. Most recent runs page\
   When you open Pipelines → Releases, the landing view is Most recent runs. This shows the latest run for each release pipeline so you can quickly see:

* pipeline name and created date
* artifact used for the run
* trigger date and time
* stage flow preview with current status for each stage (success, failed, in progress, pending)
*   a View details button to drill into the run\
    <br>

    <figure><img src="../../../../../../.gitbook/assets/Screenshot 2026-02-04 at 11.10.31 AM.png" alt=""><figcaption></figcaption></figure>



    This view is meant for quick monitoring without opening individual run pages.

    2. Options menu (Trigger, Abort, Clone, Delete pipeline)\
       Each pipeline row includes a three-dot menu with actions:

    * Trigger: starts a new run for that release pipeline using the configured stages (and the selected artifact rules/config).
    * Abort: stops an in-progress run. This is typically available only while a run is executing (if a run is already completed, Abort may be disabled).
    * Clone: creates a copy of the pipeline configuration so you can reuse the same stage structure with minimal changes.
    *   Delete pipeline: removes the pipeline configuration from the Releases list. This does not deploy or change anything in Salesforce; it only affects the pipeline record/configuration in ARM.\
        <br>

        <figure><img src="../../../../../../.gitbook/assets/image (1) (1) (1).png" alt=""><figcaption></figcaption></figure>



        3. First View details (pipeline run history)\
           When you click View details from Most recent runs, you are redirected to the pipeline’s history page. This page lists all runs (iterations) of that pipeline, showing each run’s:

        * artifact reference
        * trigger date
        * stage status preview across the pipeline
        *   View Details button for each run to open that run’s detailed execution\
            <br>

            <figure><img src="../../../../../../.gitbook/assets/image (2) (1).png" alt=""><figcaption></figcaption></figure>

            <br>

            **Run and Edit Release Pipeline**

            From the Releases landing page, each release pipeline provides additional actions that allow you to run or modify the pipeline configuration. These actions apply to the selected pipeline and help teams quickly re-execute or update their release process.<br>



            <figure><img src="../../../../../../.gitbook/assets/image (3).png" alt="" width="563"><figcaption></figcaption></figure>



            **Run Release Pipeline**\
            The Run Release Pipeline option allows you to manually trigger a new execution of the selected release pipeline.

            When you select Run Release Pipeline:

            * A new pipeline run is created using the existing stage configuration
            * The pipeline uses the configured artifact selection rules
            * All stages are executed in the defined order
            * The new run appears immediately in the Most recent runs view

            This option is typically used when you want to redeploy an artifact, retry a release after a failure, or perform a controlled promotion outside of an automated trigger.<br>

            **Edit Release Pipeline**\
            The Edit Release Pipeline option allows you to modify the configuration of the selected pipeline.<br>

            Using Edit Release Pipeline, you can:

            * Add, remove, or reorder stages
            * Update target Salesforce orgs for stages
            * Modify deployment or validation settings
            * Adjust post-deployment activities<br>

            Any changes made while editing affect only future runs of the pipeline. Previously executed runs remain unchanged and are preserved in the release history for audit and tracking purposes.<br>

            Important notes

            * Run Release Pipeline creates a new execution but does not overwrite or modify existing runs
            * Editing a pipeline does not impact runs that have already completed but creates a new version and replaces the original version of the pipeline<br>
