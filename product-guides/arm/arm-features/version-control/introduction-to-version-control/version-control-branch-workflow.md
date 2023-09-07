# Version Control Branch Workflow

You've been a lone developer, cloning your repository, making changes locally and pushing them back up to your remote. What happens when other developers need to make changes at the same time you do - and in the same repository? How do you ensure the changes follow your coding standards and are of sufficient quality? This is where implementing a [version control](https://www.autorabit.com/blog/7-tips-for-salesforce-version-control-integration/) workflow is crucial, to ensure changes are reviewed and merged back into the main code line.

A common [version control](https://www.autorabit.com/blog/8-benefits-of-version-control-in-salesforce-development/) (git) workflow for a team has the following steps:

* Create a _branch_ for the changes you are going to make. A branch is an isolated version of the code that you can work on offline without impacting other developers on your team. A branch would typically be for a new feature or a defect fix.
* _Commit_ changes to your branch locally. You can keep track of your commit history locally while you work.
* _Push_ your changes to the remote repository
* Create a _Pull request_ so that one or more people on your team can review your changes.
* _Review_ the pull request. One or more team members perform a quality check on the code. The criteria for checks of these changes will often be laid out in a code review checklist, which is likely to include the coding standards of your team or organization.
* _Complete_ the pull request. The team members who are required to review your changes agree that the criteria for changes have been met. The pull request is completed and the changes are merged into the main code line, i.e., the master branch.
* _Delete_ the branch. Once the code changes and history are merged, it's good housekeeping to delete the branch.

This workflow is often called the **Feature Branch Workflow** or **Topic Branch Workflow**
