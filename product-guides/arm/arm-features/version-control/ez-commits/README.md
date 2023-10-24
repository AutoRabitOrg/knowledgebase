# EZ-Commits

### About EZ-Commit <a href="#about-ez-commit" id="about-ez-commit"></a>

Commit, in Salesforce terminology, is the process of adding/migrating the changes by developers to a Version Control Branch to record their development progress. As a developer works, the version control system automatically tracks changes they make to files. When a portion of the feature is complete, the developers commit their changes to their branch, accompanied by an informative description.

### Why is it important? <a href="#why-is-it-important" id="why-is-it-important"></a>

If I’ve heard anything from my software development community, it’s “Commit Early and Often!”. But why?

* Periodic Checkpoints in your workflow will give you less time and space between the code you wrote and the thing you broke.
* You can better understand how things in your code were broken.
* Let people see what really happened — unless it’s a public repo or perhaps it isn’t needed, having a version history is important to understand the code.
* If you make a small change in your code and something goes horribly wrong and you lose your work, you’re only losing a small change.
* There can never be TOO many commits. If by some act of God, something needs to be rewritten, it’d be a lot easier to not have to rewrite a huge chunk.

### Prerequisites <a href="#prerequisites" id="prerequisites"></a>

Below are the prerequisites to be performed before proceeding with the commit to AutoRABIT:

1. **Register your Version Control Repository in AutoRABIT:** This step can only be performed by an Admin. Register your Version Control Repositories, such as GIT, SVN, or TFS in AutoRABIT.
2. **Register your Salesforce Organization in AutoRABIT:** AutoRABIT connects to your Salesforce Org using either secure OAuth method or using username/password connections. This step can only be performed by an Admin.
3. **Setup a Branch:** Instead of making changes to the code base directly, you can branch off from the mainline and work on a specific feature in an isolated branch. This step can only be performed by an Admin.
4. **Mapping the users with the Version Control and Salesforce Orgs in the 'My Profile' section:** Set up the permission to create a project in AutoRABIT.
