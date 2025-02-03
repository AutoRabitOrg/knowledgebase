# Error: "Failed to initiate deployment. Unexpected end of JSON input."

## Description <a href="#description" id="description"></a>

&#x20;When I run a CI job, it fails, and the error message '**Failed to initiate deployment. Unexpected end of JSON input**' appears.

## Cause <a href="#cause" id="cause"></a>

If any of the folders in the remote repository has an empty **JSON** file, that will cause SFDX commands to fail with an incorrect JSON error.&#x20;

## **Steps for resolution** <a href="#steps-for-resolution" id="steps-for-resolution"></a>

Delete the **empty JSON file(s)** from the remote repository to resolve this issue and rerun the CI job.
