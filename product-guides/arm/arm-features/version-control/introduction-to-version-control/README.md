# Introduction to Version Control

Version Control is an element that is critical to the success of your [DevOps pipeline](https://www.autorabit.com/blog/how-code-quality-tools-help-your-salesforce-devops-pipeline/). If a client is not using a Version Control System, it’s important to convince them to adopt one immediately. This article outlines the key reasons for using the Version Control System as your “source of truth,” rather than using the Salesforce org.

{% hint style="info" %}
Declarative (Point/Click) and Code Changes should not be treated differently. Declarative changes are tied to source control as well. There is a file that is changing and updating behind the scenes. Therefore both should be included in version control. Admins and Developers should have their own Developer Sandboxes in order to make changes. No changes should happen directly in the production environment.
{% endhint %}

### What is Version Control? <a href="#what-is-version-control" id="what-is-version-control"></a>

[Version Control](https://www.autorabit.com/blog/7-tips-for-salesforce-version-control-integration/) is simply the recording of changes to files. By recording changes, you have the ability to recover recorded changes if files are lost or mistakes are made. Additionally, version control allows you to keep files in a more organized structure. With Version Control, you can revert files back to the previous state, compare changes over time, and understand who last modified files.&#x20;

#### What are the Version Control Systems out there? <a href="#what-are-the-version-control-systems-out-there" id="what-are-the-version-control-systems-out-there"></a>

There are two main types of [Version Control](https://www.autorabit.com/blog/8-benefits-of-version-control-in-salesforce-development/) Systems including the following:&#x20;

* Centralized Version Control Systems&#x20;
* Distributed Version Control Systems&#x20;

With a centralized version control system, all files are stored on a central server. No developers have a copy of all files on a local server. The problem with a central server is that, if the central server crashes, all data from the project is lost. The most popular Version Control System used in Salesforce Development is a Distributed [Version Control](https://www.autorabit.com/blog/do-i-really-need-salesforce-version-control/) System. With a Distributed Version Control System, every developer has a copy of all versions of the code on their systems. This enables developers to work offline and not rely on a single location for backups. If the server crashes, there is no threat.&#x20;

There are many high-quality, free commercial hosting options that can be used for GIT or Mercurial Version Control Systems:&#x20;

{% hint style="info" %}
**Best Version Control System Commercial Hosting Options**

* GitHub
* GitLab&#x20;
* AWS CodeCommit&#x20;
* Azure DevOps Server&#x20;
* Bitbucket
{% endhint %}

#### Impacts of Version Control <a href="#impacts-of-version-control" id="impacts-of-version-control"></a>

Without version control, there are many impacts including:&#x20;

* No merge process, leading to overwriting of code&#x20;
* If org is the source of truth, overwritten changes can not be recaptured&#x20;
* The team is limited in its toolbox

#### Benefits of Version Control <a href="#benefits-of-version-control" id="benefits-of-version-control"></a>

With version control, there are many benefits including:&#x20;

* Address merge conflicts upfront and prevents overwriting of code
* Complete Code Reviews&#x20;
* At one point in time, [Salesforce development](https://knowledgebase.autorabit.com/docs/salesforce-deployment-best-practices) will not just be declarative&#x20;
* Improve the quality of work.

### What are Remote Repositories? <a href="#what-are-remote-repositories" id="what-are-remote-repositories"></a>

Remote repositories allow us to share our changes with other members of the team. They can be on a private server, on a different computer than yours, or hosted on a different service. Wherever yours is hosted, you'll need to be able to sync your local repository with the remote repository frequently. To start sharing changes with others, you have to push them to a remote repository. This will cause the remote repository to update and synchronize with your local repository.
