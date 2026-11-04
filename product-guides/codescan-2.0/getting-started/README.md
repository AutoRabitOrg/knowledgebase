---
description: The path from signing up to a working, enforced CodeScan setup, step by step.
---

# Getting Started

**Who this is for:** administrators and developers

This section takes your team from signing up to a working setup: your code scanned, your developers checking their own work, and your main branch protected. Follow the steps in order. Each step links to the next.

### Part 1: Set Up CodeScan

An administrator does these steps.

| Step | What you do                                                   | Article               |
| ---- | ------------------------------------------------------------- | --------------------- |
| 1    | Check that your tools and network meet the requirements       | System Requirements   |
| 2    | Create your account and sign in                               | Sign Up and Sign In   |
| 3    | Register your first repository                                | Register a Repository |
| 4    | Choose the project settings that matter before the first scan | Set Up Your Project   |
| 5    | Start your first scan                                         | Start a Scan          |
| 6    | Read your first results                                       | Reading Scan Results  |

### Part 2: Bring In Your Developers

Developers check their own code before it reaches a pull request.

| Step | What you do                                  | Who           | Article                    |
| ---- | -------------------------------------------- | ------------- | -------------------------- |
| 7    | Create API keys for developers and pipelines | Administrator | Create and Manage API Keys |
| 8    | Connect the VS Code extension                | Developer     | Connect VS Code            |
| 9    | Connect the CodeScan CLI                     | Developer     | Connect the CLI            |

### Part 3: Protect Your Main Branch

| Step | What you do                                                    | Who                     | Article                                                                        |
| ---- | -------------------------------------------------------------- | ----------------------- | ------------------------------------------------------------------------------ |
| 10   | Review every pull request automatically, by webhook or from CI | Administrator or DevOps | Set Up Webhook-Triggered Review or Run CodeScan in CI                          |
| 11   | Make the quality gate stop a merge or a build                  | Administrator or DevOps | Block Merges With a Required Status Check or Fail a CI Build on a Blocked Scan |

### Part 4: Fine-Tune

Once your team has worked with the results for a while:

* Reduce noise with **`Review Noisy Rules`**.
* Add your own standards with Custom Rules.
* Raise the quality gate to include Critical. See How the Quality Gate Works.
* Register your next repository and repeat steps 3 to 6.
