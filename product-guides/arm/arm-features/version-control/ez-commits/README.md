# EZ-Commits

## About EZ-Commit <a href="#about-ez-commit" id="about-ez-commit"></a>

In DevOps, a **commit** is a bundled snapshot of changes made to files under version control. These can include adding, modifying, or deleting code and metadata. Rather than logging every change individually, version control systems group them into a single action—a commit—that marks a specific point in development.

In **AutoRABIT**, a commit is the process of adding or migrating a Salesforce developer’s changes to a version control branch. This records development progress and integrates with CI/CD pipelines for traceability, quality checks, and automation.

As developers build features or fix bugs, their changes are tracked in real time. When a logical unit of work—like an updated Apex class or new Lightning component—is complete, it’s committed to a branch with a descriptive message. These commits often trigger automated testing and deployments, forming the foundation of consistent, high-quality releases.

### **Why Is Committing Important?**

Frequent commits are a best practice in modern software development. They offer several key benefits:

1. **Incremental Progress Tracking**\
   Committing regularly creates checkpoints, making it easier to trace and isolate issues when bugs occur.
2. **Easier Debugging**\
   Smaller commits help identify the exact changes that introduced a problem, streamlining the debugging process.
3. **Clear Version History**\
   A detailed commit history documents how code has evolved, aiding both collaboration and future maintenance.
4. **Reduced Risk of Data Loss**\
   Committing often ensures that only minimal work is lost in the event of an error or system failure.
5. **Simplified Rework and Rollbacks**\
   With more granular commits, reverting or modifying specific changes becomes more manageable.

Regular, meaningful commits contribute to more reliable, traceable, and maintainable code across teams and projects.

### Prerequisites <a href="#prerequisites" id="prerequisites"></a>

Below are the prerequisites to be performed before proceeding with the commit to AutoRABIT:

1. **Register your Version Control Repository in AutoRABIT:** This step can only be performed by an Admin. Register your Version Control Repositories, such as GIT, SVN, or TFS in AutoRABIT.
2. **Register your Salesforce Organization in AutoRABIT:** AutoRABIT connects to your Salesforce Org using either secure OAuth method or using username/password connections. This step can only be performed by an Admin.
3. **Setup a Branch:** Instead of making changes to the code base directly, you can branch off from the mainline and work on a specific feature in an isolated branch. This step can only be performed by an Admin.
4. **Mapping the users with the Version Control and Salesforce Orgs in the 'My Profile' section:** Set up the permission to create a project in AutoRABIT.

### FAQs on Commits

#### **How does Git handle duplicate file change commits?**

Git's handling of duplicate file change commits can be a different aspect of Version Control management, particularly when merging branches with identical changes.\
\
**Why does Git allow duplicate commits when performing duplicate merges in AutoRABIT?**

Git's behavior of creating new commits for each merge, even if the changes are merged multiple times, is intrinsic to its design. This allows Git to maintain a detailed commit history and track changes accurately.
