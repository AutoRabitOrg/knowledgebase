# AI Code Assistant: User Guide

### Executive Overview

#### Fix code issues without leaving your review workflow

CodeScan's AI Code Assistant brings AI-powered code remediation directly into your existing analysis workflow. Instead of manually fixing common rule violations one by one, you can assign eligible issues to an AI agent that generates fixes, review the proposed changes in a side-by-side diff, and deliver approved fixes through automatically created Pull Requests — all from within CodeScan.

The AI Code Assistant is designed around a human-in-the-loop model: the AI generates the fix, but you always review, edit, and approve before anything reaches your codebase.

Once enabled for a project, you can:

* See which issues are eligible for AI-assisted fixes at a glance
* Assign single issues or bulk-assign up to 10 issues to the AI agent
* Review AI-generated patches in a dedicated "Fixed by AI" tab with full diff view and inline editing
* Create Pull Requests — individually or in bulk — for approved fixes targeting GitHub or GitLab
* Track every AI fix through its lifecycle with dedicated filters and status labels
* Monitor AI credit consumption through a real-time usage indicator and an administration dashboard<br>

The AI operates on a curated set of high-confidence Apex rules and uses rule-specific context to produce accurate, focused fixes. All fix activity — who assigned, who approved, what changed — is captured for full auditability.

#### Enabling the AI Code Assistant

The AI Code Assistant is controlled at the project level.

To enable:

&#x20;1\.  Navigate to Project Settings → AutoRABIT CodeScan AI.

2. Under AI Automation Mode, select Automatic or Manual.&#x20;

* Automatic: AI handles the code-fix process after an issue is assigned.
* Manual: Users review and approve AI-suggested fixes.

3. Turn on Enable AutoRABIT CodeScan AI Code Assistant.

<figure><img src="../../../.gitbook/assets/image (2978).png" alt=""><figcaption></figcaption></figure>

When  enabled:

* The AI Code Assistant agent appears in the issue Assign dropdown.
* Eligible issues display an "AI Fix Available" indicator.
* The "AI Code Assistant" filter becomes available in the issue filters panel.

When disabled:

* New assignments (single or bulk) to the AI Code Assistant are blocked.
* The AI Code Fixer is removed from the Assign dropdown.
* The "AI Fix Available" indicator is hidden from issues.
* Previously generated AI fixes remain visible in the "Fixed by AI" tab for historical and review purposes — you can still view past AI-generated patches, but cannot initiate new ones.

### AI Fix Eligibility

Not every issue is eligible for AI-assisted fixing. The AI Code Assistant operates on a curated Rules Inclusion List — a set of validated, high-confidence rules where the AI model has been tested to produce accurate, reliable fixes.

#### Currently Supported Rules

The initial inclusion list covers 10 Apex rules:

| Rule                                     | Rule key                      |
| ---------------------------------------- | ----------------------------- |
| Local Variable Could Be Final            | sf:LocalVariableCouldBeFinal  |
| Comment is Required                      | sf:CommentRequired            |
| Left Braces Spacing Should Be Consistent | sf:LeftBracesSpacingPositions |
| Variable Naming Conventions              | sf:VariableNamingConventions  |
| Long Variable Name                       | sf:LongVariable               |
| Unused Local Variable                    | sf:UnusedLocalVariable        |
| Unused Private Field                     | sf:UnusedPrivateField         |
| Avoid Duplicate Literals                 | sf:AvoidDuplicateLiterals     |
| Comment All Hardcoded Values             | sf:CommentHardcodedValues     |
| Short Variable Name                      | sf:ShortVariable              |

Issues flagged by rules outside this list will not show the "AI Fix Available" indicator and cannot be assigned to the AI agent.

#### How the AI Generates Fixes

For each eligible issue, the AI model receives:

* Rule-specific, AI-optimized context — a purpose-built prompt tuned for each rule, rather than the generic rule description.
* Code snippet at the appropriate depth — based on the rule's complexity:
* Low complexity — surrounding lines around the violation
* Medium complexity — the full method containing the violation
* High complexity — the full class where the violation occurs

This approach ensures the AI receives concise, relevant input, improving fix accuracy while minimizing unnecessary processing.

### Assigning Issues to the AI Code Assistant

<figure><img src="../../../.gitbook/assets/image.png" alt=""><figcaption></figcaption></figure>

#### Single Assignment

1. Open any issue that displays the "AI Fix Available" indicator.
2. Click the Assign dropdown.

<figure><img src="../../../.gitbook/assets/image (2979).png" alt=""><figcaption></figcaption></figure>

3. Select AI Code Assistant from the list.
4. The AI agent begins generating a fix. The issue status updates to reflect progress.

#### Bulk Assignment

<figure><img src="../../../.gitbook/assets/image (2971).png" alt=""><figcaption></figcaption></figure>

1. Select the issues you want to assign
2. Click Bulk Change.
3. In the Change Issues dialog, open the Assign dropdown.
4. Select AI Code Assistant.
5. Click Apply to assign the selected issues.

{% hint style="info" %}
You can assign a maximum of 10 issues per bulk action. If you select more than 10, a validation message will be displayed. This limit is enforced to maintain processing stability and control AI consumption.
{% endhint %}

### Reviewing AI Fixes

<figure><img src="../../../.gitbook/assets/image (2972).png" alt=""><figcaption></figcaption></figure>

Once the AI agent generates a fix, a new "Fixed by AI" tab appears in the issue detail view.

#### What You See

* A side-by-side diff view showing the original code on the left and the AI-generated fix on the right.
* Changes are highlighted for easy comparison.
* Each AI-fixed issue is assigned a project-based unique UI ID, which is displayed in the UI and included in any Pull Request created from the fix — providing clear traceability.

#### Inline Editing

* You can edit the AI-generated code directly within the diff view.
* All modifications are auto-saved.
* This allows you to refine the AI's output before creating a Pull Request, ensuring the final fix meets your standards.

#### Fix Statuses

\
After assignment, an issue progresses through these states:

| Status               | Meaning                                                                                                                |
| -------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| AI Fix Available     | The issue is eligible for AI fixing but has not been assigned yet                                                      |
| AI Fix In Progress   | The AI agent is generating a fix                                                                                       |
| AI Fix Generated     | A patch has been generated and is ready for review in the "Fixed by AI" tab                                            |
| Pull Request Created | A PR has been raised for the AI-generated fix                                                                          |
| AI Fix Failed        | The AI attempted to generate a fix but was unsuccessful                                                                |
| AI Fix Not Supported | The specific violation type within the rule is not supported for AI fixing (e.g., certain inner-class field scenarios) |

### Creating Pull Requests

<figure><img src="../../../.gitbook/assets/image (2973).png" alt=""><figcaption></figcaption></figure>

The AI Code Assistant supports two modes for Pull Request creation, configurable in Project Settings.

#### Manual Mode (default)

1. After reviewing the AI-generated fix in the "Fixed by AI" tab, click "Create PR".
2. A popup appears where you can edit:
3. PR name
4. Branch name
5. Related repository information
6. Click Apply to create the Pull Request.

<figure><img src="../../../.gitbook/assets/image (2974).png" alt=""><figcaption></figcaption></figure>

#### Creating Pull Requests in Bulk

To create pull requests for multiple AI-generated fixes:

1. Navigate to the **Issues** tab.
2. Select the issues using the checkboxes.
3. Click **Bulk Change**.
4. In the **Change Issues** window, select **Create Bulk PR for AI Code Generated Issues**.
5. Click **Apply**.

The pull requests are created from the branches where the issues were found, using dedicated AI fix branches.

<figure><img src="../../../.gitbook/assets/image (2975).png" alt=""><figcaption></figcaption></figure>

The PR is created from the branch where the issue was found, using a dedicated AI fix branch. This ensures the fix targets the correct codebase context.

#### Tracking AI Code Assistant Status

You can track the progress of AI-generated fixes from the **Issues** tab.

Under **Filters**, expand **AI Code Assistant** to view issues by their current status:

* **AI Fix Available:** Issues eligible for AI-assisted fixes.
* **AI Fix In Progress:** Issues currently being processed.
* **AI Fix Generated:** Issues for which an AI-generated fix is available.
* **Pull Request Created:** Issues for which a pull request has been created.
* **AI Fix Failed:** Issues where AI fix generation was unsuccessful.

Select a status to filter and view the corresponding issues.

<figure><img src="../../../.gitbook/assets/image (2976).png" alt=""><figcaption></figcaption></figure>

#### Automation Mode

When automation mode is enabled in Project Settings:

* The full lifecycle runs without manual intervention: Generate Fix → Persist Patch → Auto-Create PR.
* PRs are created automatically once the AI successfully generates a fix.
* You can still review the fix in the "Fixed by AI" tab and in the PR itself before merging.

#### Bulk PR Creation

1. From the issues list, select multiple issues in "Fix Generated" status.
2. Open the Bulk Change action.
3. Select "Create Bulk PR for AI Code Generated Issues".
4. The Create PR popup opens, allowing you to configure PR details before submission.
5. A single Pull Request is created containing all selected fixes.

{% hint style="info" %}
The bulk PR option is only available when all selected issues are in "Fix Generated" status.<br>
{% endhint %}

#### Notifications

* A notification banner confirms PR creation in the UI.
* PR creation details also appear in the "Fixed by AI" tab for the relevant issues.

#### Supported Platforms

| Platform | PR Creation | Auto PR (Automation Mode) |
| -------- | ----------- | ------------------------- |
| GitHub   | Supported   | Supported                 |
| GitLab   | Supported   | Supported                 |

GitHub App Users: The CodeScan GitHub App requires Pull Request creation and content write permissions to support AI CodeFix. You will be prompted to accept the updated permissions when upgrading to this release.

### Tracking & Filtering

### AI Code Assistant Filter

A dedicated "AI Code Assistant" filter is available in the issue filters panel when the feature is enabled. It lets you filter issues by their AI fix lifecycle state:

* AI Fix Available — eligible for AI fixing
* AI Fix Generated — AI patch ready for review
* Pull Request Created — PR has been raised
* AI Fix Failed — AI fix attempt was unsuccessful

When a filter is applied, the corresponding status label is shown on each issue card, providing consistent visual feedback.

{% hint style="info" %}
This filter is only visible when the AI Code Assistant is enabled for the project. If the feature is turned off, the filter is hidden to avoid clutter.
{% endhint %}

### AI Credits & Usage Monitoring

AI Code Assistant usage is tracked through a credit-based system integrated with your CodeScan subscription.

#### Real-Time Usage Indicator

A pie-chart icon in the top navigation bar (positioned to the left of the help button) shows your organization's remaining AI credits at a glance.

The icon changes color based on consumption thresholds:

| Threshold               | Color  | Meaning                             |
| ----------------------- | ------ | ----------------------------------- |
| More than 25% remaining | Indigo | Healthy                             |
| 25% or less remaining   | Amber  | Low — consider monitoring usage     |
| 10% or less remaining   | Red    | Critical — credits nearly exhausted |

Hover over the icon to see the exact credit count (e.g., 750 / 1,000).

### AI Billing Administration Page

Administrators can access the **AI Users & Billing** page under **Administration** to monitor AI credit consumption and manage license assignments.

The AI Users & Billing page provides administrators with the following details:

* **Monthly AI Credits Available:** Displays the available monthly AI credits and the reset date.
* **User Search:** Allows administrators to search for users by name or email.
* **Balance Used:** Shows each user's credit consumption as a percentage with a progress indicator.
* **Credits Used:** Displays the number of AI credits consumed by each user.
* **Licenses:** Shows the AI licenses assigned to each user.<br>

<figure><img src="../../../.gitbook/assets/image (2977).png" alt=""><figcaption></figcaption></figure>

**Accessing AI Users & Billing**

1. Navigate to **Administration**.
2. Open **AI Users & Billing**.
3. Review the available monthly AI credits.
4. Use the search field to find users by name or email.
5. Review each user's credit consumption and assigned licenses.

{% hint style="info" %}
Organizations without licensed AI features will not see the AI Billing menu entry. If the URL is accessed directly, a message is displayed directing users to their AutoRABIT Customer Success representative.
{% endhint %}

#### Daily Execution Limit

AI CodeFix executions are subject to a daily limit per organization to maintain service reliability and predictable consumption. When the limit is reached, a notification is displayed:

_"Daily AI CodeFix limit has been reached. Please try again tomorrow."_

### Governance & Auditability

The AI Code Assistant is designed with governance in mind:

| Control                 | Detail                                                                          |
| ----------------------- | ------------------------------------------------------------------------------- |
| Project-level toggle    | Enable or disable AI capabilities per project                                   |
| Bulk assignment limit   | Maximum 10 issues per bulk action                                               |
| Daily execution cap     | Organization-level daily limit on AI fix executions                             |
| Credit tracking         | Real-time consumption visibility for users and administrators                   |
| Assignment tracking     | The user who assigned each issue to the AI agent is recorded                    |
| Approval tracking       | The user who approved and created the PR is recorded                            |
| Fix traceability        | Each fix has a unique UI ID carried through to the Pull Request                 |
| Permission-based access | Only users with appropriate project permissions can assign issues or create PRs |

### FAQ

Q: Does enabling the AI Code Assistant change how my scans work? No. The AI Code Assistant operates entirely post-analysis. Scans, rules, quality gates, and quality profiles are unaffected. The AI only generates fixes for issues already identified by your existing scan configuration.

Q: What happens if I disable the AI Code Assistant after using it? New AI assignments are blocked, and the "AI Fix Available" indicator and filter are hidden. However, all previously generated AI fixes remain visible in the "Fixed by AI" tab for review and historical purposes.

Q: Can the AI fix issues across multiple files? The AI generates fixes on a per-issue, per-file basis. For rules that flag multiple occurrences in a single file, the AI addresses them together. Cross-file fixes are not currently supported.

Q: What if the AI-generated fix introduces a new issue? After merging an AI-generated PR, the next scan will analyze the updated code. If a new issue is introduced, it will be flagged in the scan results like any other issue. This is why reviewing the AI diff before creating a PR is recommended.

Q: How do I know which issues are eligible for AI fixing? Eligible issues display an "AI Fix Available" indicator. You can also use the AI Code Assistant filter in the issues panel and select "AI Fix Available" to see all eligible issues.

Q: Can I edit the AI-generated fix before creating a PR? Yes. The "Fixed by AI" tab provides inline editing with auto-save. You can modify the AI's output to meet your requirements before creating a Pull Request.

Q: What does "AI Fix Not Supported" mean? Some specific violation patterns within a supported rule may not be eligible for AI fixing — for example, certain inner-class field scenarios or violations involving complex variable shadowing. These are marked as "AI Fix Not Supported" rather than "AI Fix Failed."

Q: Is my code sent to a third-party AI provider? The AI Code Assistant uses AI models to generate fixes. Code snippets relevant to the violation (not entire repositories) are sent for processing. Contact your AutoRABIT Customer Success representative for details on data handling and compliance.

***

### Troubleshooting runbooks

#### AI Code Assistant does not appear in the Assign dropdown

* Confirm the AI Code Assistant is enabled: Project Settings → General Settings → CodeScan AI → Enable AI CodeScan Assistant must be toggled ON.
* Confirm you have the necessary project permissions.

***

#### "AI Fix Available" indicator is not showing on issues

* The issue's rule must be in the supported Rules Inclusion List (see "AI Fix Eligibility" above).
* The AI Code Assistant must be enabled for the project.

***

#### AI Fix fails after assignment

* Check the issue status — it will show "AI Fix Failed" or "AI Fix Not Supported" with context.
* Some violation patterns within supported rules may not be fixable by the AI (e.g., field-level violations in inner classes).
* If failures persist across multiple issues, verify that your organization has not exceeded its daily execution limit.

***

#### Pull Request creation fails

* Ensure your project integration (GitHub/GitLab) is properly authorized and the OAuth token has not expired. Re-authorize the integration if necessary.
* For GitHub App users, confirm that Pull Request creation and content write permissions have been granted.
* Verify that your repository user account has write access to the target repository.

***

#### AI credit indicator shows unexpected values

* Credit balances are synced with your Chargebee subscription. If you believe the count is incorrect, contact your AutoRABIT Customer Success representative.
* Credits reset on a monthly cycle aligned with your subscription period.
