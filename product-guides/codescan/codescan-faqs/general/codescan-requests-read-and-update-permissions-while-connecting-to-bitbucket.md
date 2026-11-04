# CodeScan requests read and update permissions while connecting to Bitbucket

**CodeScan requests read and update permissions while establishing a connection with Bitbucket.**

To stop the pull request from being merged if the Quality Gate fails, CodeScan requires the **edit** repository permission. CodeScan will not modify any of the customer code, but it can prohibit customers from making changes.

Webhook is required to start analysis immediately, every time a pull request is sent or a commit is posted directly to a branch.
