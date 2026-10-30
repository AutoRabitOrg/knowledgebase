---
description: AWS CloudFormation
---

# CloudFormation Stacks

{% hint style="info" %}
To start scanning the stacks, a schedule with the **`AWS CloudFormation Analysis`** job type has to be created - [Schedule Configuration](../schedule-configuration.md)
{% endhint %}

#### What Is Scanned <a href="#what-is-scanned" id="what-is-scanned"></a>

For every stack, the template the stack was deployed from is retrieved and scanned against the CloudFormation rule pack. Issues are reported against `template.yaml`. CloudFormation and SAM templates are both supported.

The same rule pack and scanner are used by IZ Scan to scan templates from a source repository or from the IZ Scan CLI before they are deployed, so a finding reported before deployment and after deployment is the same rule.

#### Which stacks are listed <a href="#which-stacks-are-listed" id="which-stacks-are-listed"></a>

| Listed              | Stack status                                                                                                                                                                        |
| ------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Yes                 | `CREATE_COMPLETE`, `UPDATE_COMPLETE`, `UPDATE_ROLLBACK_COMPLETE`, `ROLLBACK_COMPLETE`, `IMPORT_COMPLETE`, `IMPORT_ROLLBACK_COMPLETE`                                                |
| Yes - failed states | `CREATE_FAILED`, `ROLLBACK_FAILED`, `DELETE_FAILED`, `UPDATE_FAILED`, `UPDATE_ROLLBACK_FAILED`, `IMPORT_ROLLBACK_FAILED`                                                            |
| No                  | `DELETE_COMPLETE` (nothing deployed), `REVIEW_IN_PROGRESS` (change set not yet executed) and transient `*_IN_PROGRESS` states, which are picked up by the next run once they settle |

Stacks in a failed state are listed deliberately: their resources are still deployed and billed, but CloudFormation can no longer manage them reliably. The rule **CloudFormation Stack in a Failed State** reports them.

#### To view all the stacks <a href="#to-view-all-the-stacks" id="to-view-all-the-stacks"></a>

1. Navigate to **`IZ Eye`** -> **`AWS`** -> **`AWS CloudFormation`**. Overview includes -
   1. **`Name`** - Name of the stack
   2. **`Organization`** - The AWS account to which the stack belongs
   3. **`Environment`** - The region to which the stack belongs
2. Click on the **`Plus`** icon to view the details
3. Summary details include -
   1. **`Total Issues`** - Indicates total number of issues once the stack is scanned
   2. **`Status`** - Stack status reported by AWS, for example **`UPDATE_COMPLETE`** or **`DELETE_FAILED`**
   3. **`Last Scan`** - Time since the last scan was performed
4. Actions include -
   1. **`View Dashboard`** - Summary report of all the issues.
   2. **`View Issues`** - Detailed report of the issues with the line numbers in `template.yaml`.
   3. **`View Metrics`** - Includes the resources the stack contains.
