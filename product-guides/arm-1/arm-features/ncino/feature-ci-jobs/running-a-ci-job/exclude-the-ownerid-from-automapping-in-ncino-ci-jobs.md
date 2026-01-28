# Exclude OwnerID from Automapping in CI Jobs

To ensure user permissions differences between different environments will not affect the RBC deployments, users are provisioned to disable the auto assignment of users as they trigger the RBC deployments.

<figure><img src="https://github.com/AutoRabitOrg/knowledgebase/raw/7744f310785293503dd3729fd9d0403cae3b8211/.gitbook/assets/image%20(21)%20(4).png" alt=""><figcaption></figcaption></figure>

By default, the option is disabled, which signifies that the user permissions will be auto-assigned if another user continues to trigger a job that was initiated by a different user in another environment.

While triggering the RBC configuration deployment, you must explicitly disable the option to make sure that the users will not be auto-mapped.
