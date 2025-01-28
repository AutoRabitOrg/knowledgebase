# ARM User Definitions

## Standard User

A Standard User is an individual authorized by the Customer to log in to and directly use AutoRABIT’s subscribed products.

#### Additional Notes:

* Platform Owners/Admins are included in the Standard User class, allowing customers to manage admin rights without affecting licensing terms.
* The number of licensed users represents the total unique users of the products, calculated throughout the entire course of the Subscription Term.

***

## Platform Integration User

A Platform Integration User is an individual authorized by the Customer to perform actions that trigger the execution of ARM. This is primarily intended represent users who interact with ARM through Git and do not have a Standard User license.&#x20;

### Tracking Platform Integration Users in ARM:

AutoRABIT tracks the usage of ARM as an orchestration engine through version control systems. The unique identifier used is the associated email address. Therefore, it is important that activity be linked to official customer email addresses to avoid double-counting users who may use personal email addresses.

#### Key Points:

* **Code Commits and Licensing:** Any person who commits code to a Source Code Management (SCM) system, where the commit triggers a job in AutoRABIT, requires a Platform Integration License.
* **Service Accounts:** If a service account triggers automation or integrates with AutoRABIT, the individual or team responsible for the actual code commit must still hold a Platform Integration License. This ensures that all contributors whose actions trigger AutoRABIT processes are appropriately licensed.
* **Commit Count in SCM Systems:** For SCM systems such as Git, multiple commits pushed simultaneously are counted separately toward the user license.
* **No Web UI Login Required:** A Platform Integration User does not need to log in to the AutoRABIT Web UI to be counted as a user.
* **Remote Access for Standard Users:** Active Standard Users can use ARM remotely without additional license requirements.

***

### Determining the Count of Platform Integration Users

Platform Integration Users are sold in blocks of 10. This means any user meeting the criteria above who is not also a licensed Standard User will be counted. These are not “named” users; instead, users are defined by their activity within the quarter. The count is recalculated each quarter.

**Calculation:**

* The **average high-water mark** of the two highest quarters is used, rounded up to the nearest block of 10, to determine the total Platform Integration User count for the term.
* Counts reset each quarter and include both new and recurring users.

**Example:**

**ACME Corp purchases 10 Platform Integration User licenses.**

* **Quarter 1:** 15 users
* **Quarter 2:** 8 users
* **Quarter 3:** 17 users
* **Quarter 4:** 5 users

The average of the two highest quarters (15 and 17) is 16. Since licenses are sold in blocks of 10, ACME oversubscribed by 6 users and would need to purchase an additional 10 licenses.

#### **Notes:**

* The subscription model aligns with the **contract start date**, not the fiscal year. For example, if the contract starts in May 2025, the quarterly data points would include: Q2 2025, Q3 2025, Q4 2025, Q1 2026. A partial quarter is not prorated - it would simply be less likely to be one of the highest use quarters used in the average.&#x20;
* **Licenses are sold in blocks of 10 and always round up.** If oversubscribed by 6 licenses, purchase an additional 10. If oversubscribed by 11, purchase an additional 20.
* **Unique Email IDs:** ARM counts users via unique email IDs retrieved from Git. If an individual uses multiple email addresses for commits, they will be counted as separate users. To prevent this, ensure best practices when using Git.
