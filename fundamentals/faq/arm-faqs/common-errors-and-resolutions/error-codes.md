# Error Codes

### **GH006: Protected branch update failed for refs/heads/master. Remote: error: Cannot force-push to a protected branch.**

This error may be encountered while attempting to commit changes for a production organization to the GitHub master branch. This occurred because protected branches are not allow force pushes. Get in touch with your Administrator to turn off the protection on that branch.

### **TF402455: Pushes to this branch are not permitted; you must use a pull request to update this branch.**

This error may be encountered while attempting to commit changes for the production organization to the GitHub master branch.  This is expected. When the branch is set with the branch policy, you cannot push it directly and need to create a pull request to update it. Once you remove the branch policy, you should have the ability to push changes to the master branch. Please contact the GitHub Administrator to request push permissions.

###
