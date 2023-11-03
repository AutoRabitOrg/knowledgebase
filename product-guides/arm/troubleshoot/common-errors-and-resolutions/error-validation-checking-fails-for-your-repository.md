# Error: "validation checking fails for your repository”

### Description

Merge is getting failed with the error message **"validation checking fails for your repository.”**

### Cause

Your repository credentials are expired or it has been modified and not updated in the ARM application.

### Resolution

1. Navigate to **Admin > VC repos**, select your repository, and perform a test connection. Please verify your repository credentials are not expired or modified.
2. Re-run the CI job after you confirm that the repository connection is successful.

\
