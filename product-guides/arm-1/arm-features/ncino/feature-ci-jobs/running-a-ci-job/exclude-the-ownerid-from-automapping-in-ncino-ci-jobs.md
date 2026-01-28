# Exclude OwnerID from Automapping in CI Jobs

To ensure user permissions differences between different environments will not affect the RBC deployments, users are provisioned to disable the auto assignment of users as they trigger the RBC deployments.

By default, the option is disabled, which signifies that the user permissions will be auto-assigned if another user continues to trigger a job that was initiated by a different user in another environment.

While triggering the RBC configuration deployment, you must explicitly disable the option to make sure that the users will not be auto-mapped.
