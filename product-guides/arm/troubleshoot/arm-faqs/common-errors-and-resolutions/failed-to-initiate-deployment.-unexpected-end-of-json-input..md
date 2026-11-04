# Failed to initiate deployment. Unexpected end of JSON input.

## Error message: Failed to initiate deployment. Unexpected end of JSON input.

When running a CI job, if any of the folders in the remote repository has an empty **JSON** file, that will cause SFDX commands to fail with an incorrect JSON error. Delete the **empty JSON file(s)** from the remote repository to resolve this issue and re-run the CI job.
