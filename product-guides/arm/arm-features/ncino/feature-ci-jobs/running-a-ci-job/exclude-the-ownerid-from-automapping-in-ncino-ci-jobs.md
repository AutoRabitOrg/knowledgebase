# Exclude the OwnerID from Automapping in nCino CI jobs

## **Exclude the OwnerID from Automapping in nCino CI jobs**

To ensure user permissions differences between different environments will not affect the RBC deployments, users are provisioned to disable the auto assignment of users as they trigger the RBC deployments.

<figure><img src="../../../../../../.gitbook/assets/image (21) (4).png" alt=""><figcaption></figcaption></figure>

By default, the option is disabled, which signifies that the user permissions will be auto-assigned if another user continues to trigger a job that was initiated by a different user in another environment.

While triggering the RBC configuration deployment, you must explicitly disable the option to make sure that the users will not be auto-mapped.
