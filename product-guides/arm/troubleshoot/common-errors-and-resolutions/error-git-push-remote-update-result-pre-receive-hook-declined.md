# Error: GIT Push remote update Result: pre-receive hook declined

### Description

Multiple Branching Baseline jobs show No local Modifications to commit. As a result the following error message is thrown:

AR-Debug:: GIT Push Result: RemoteRefUpdate\[remoteName=refs/heads/release/CI\_UAT2\_Refresh, REJECTED\_OTHER\_REASON, 3235de0aa8e9edd83ab68d4d723c0301847caf78...9b4c80cea9e7217aa7d16486f1f30b609406c2f1, fastForward, srcRef=refs/heads/release/CI\_UAT2\_Refresh, message="pre-receive hook declined"] Status of the GIT Push process: REJECTED\_OTHER\_REASON

### Cause

**One of your commit messages is missing a valid issue key:**

&#x20; 9b4c80c: Commit From AutoRABIT \[Branch Baseline] \[LabelName:UAT2 Baseline]

### Steps for Resolution

Ensure to cross-verify the following things:

Create a new repository link where the key should include part of the commit comment from AutoRABIT.

(or)

Modify the existing Repository Link’s Key to align with the AutoRABIT Branching Baseline commit comment.

(or)

Need to disable the Repository Link.

For more content, go through [![](https://wac-cdn.atlassian.com/assets/img/favicons/atlassian/favicon.png)Link to a web service | Bitbucket Cloud | Atlassian Support](https://support.atlassian.com/bitbucket-cloud/docs/link-to-a-web-service/)
