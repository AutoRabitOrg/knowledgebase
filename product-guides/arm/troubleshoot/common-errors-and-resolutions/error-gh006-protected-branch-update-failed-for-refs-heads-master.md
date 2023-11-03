# Error: "GH006: Protected branch update failed for refs/heads/master"

### Description

I encountered an error while attempting to commit the changes for the production organization to the GitHub master branch. The error message states, **"remote: error: GH006: Protected branch update failed for refs/heads/master.**\
**remote: error: Cannot force-push to a protected branch."**

### Resolution

It is because protected branch doesn't allow force push. Get in touch with your Administrator to turn off the protection on that branch, it should work.

\
