---
description: Newest CodeScan Releases
---

# Release Notes 25.0

## CodeScan Cloud

### CodeScan Release 25.0.2&#x20;

#### Release Date: February 05, 2024&#x20;

### Summary:&#x20;

CodeScan 25.0.2 is comprised of the following 4 components:&#x20;

* 1 [New](release-notes-25.0.md#new-features) [Feature](release-notes-25.0.md#new-features)&#x20;
* 1 [Enhancement](release-notes-25.0.md#enhancements)&#x20;
* 2 [Fixes](release-notes-25.0.md#fixes)&#x20;

Component details are listed in their corresponding sections within this document.&#x20;

### New Features:&#x20;

1. **Added “Security Hotspots” in CSV Export**&#x20;

We have had a long-standing capability to export issues directly from the CodeScan U.I.   However, there was not the ability to export Hotspots.&#x20;

With this new feature, we have added a new page in the CodeScan U.I. that allows users to directly export Hotspots.  And, similar to exporting issues, this can be done at the branch or PR level.&#x20;

<figure><img src="../../../../.gitbook/assets/Screenshot 2025-01-31 at 3.40.53 PM.png" alt="" width="563"><figcaption><p>Hotspots Export</p></figcaption></figure>

{% hint style="info" %}
Please note that if the Status selected is “REVIEWED”, then the Resolution field is also added as a selectable input.
{% endhint %}

<figure><img src="../../../../.gitbook/assets/Screenshot 2025-01-31 at 3.43.00 PM.png" alt="" width="563"><figcaption><p>Export Dropdown</p></figcaption></figure>

Further, to make navigation clearer and easier for users, we have renamed the existing CSV export page to “CSV Issues Export”, which is separate from the new “CSV Security Hotspots Export” page. Both pages can be opened under the “More” tab (as long as the user has the proper permissions).



<figure><img src="../../../../.gitbook/assets/Screenshot 2025-01-31 at 3.44.29 PM.png" alt="" width="563"><figcaption><p>More Dropdown</p></figcaption></figure>

Finally, we verified the following scenarios:&#x20;

* Verified that we are able to export security hotspot issues of a selected project &#x20;
* Verified that all the required fields were included in the exported CSV with correct data&#x20;
* Verified that the resolutions are visible only when the status REVIEWED is selected&#x20;

### Enhancements&#x20;

1. &#x20;**Enhanced rule “Avoid Classes Without Explicit Sharing" to account for Interfaces** &#x20;

Previously, this CodeScan did not consider interfaces when flagging violations.  As such, the rule "sf:ClassExplicitSharing" was generating a false positive when applied to interfaces, as the Sharing keyword is not allowed on interfaces in Salesforce. &#x20;

This issue has been remediated. We have updatied the rule to exclude interfaces from its check for the Sharing keyword, ensuring accurate validation and preventing incorrect flags. &#x20;

We have verified the rule: "sf:ClassExplicitSharing" for the following scenarios:&#x20;

* Verified that violation is not thrown if we use with/without sharing for classes&#x20;
* Verified that violation is thrown if we don’t use with/without sharing for classes&#x20;
* Verified that violation is not thrown for interface class even we don’t use with/without sharing &#x20;
* Verified that violation is thrown if we use only sharing for classes.&#x20;

We report that all scenarios are working as expected.&#x20;



### New Rules:&#x20;

There are no New Rules associated with this release &#x20;



### Fixes&#x20;

1. &#x20;**Fixed issue with “Project Search” in CSV Export (within the CodeScan U.I.)** &#x20;

Recently, we added a search function to the drop-down on the CSV export page to allow users to search the name of the project they wish to export.&#x20;

<figure><img src="../../../../.gitbook/assets/Screenshot 2025-01-31 at 3.44.43 PM.png" alt=""><figcaption><p>CSV Export</p></figcaption></figure>

Several customers reported an issue when selecting a project in the new Project Search Window.&#x20;

This updated fully remediates this reported issue.   &#x20;

Further, we have validated the CodeScan export issue is resolved via the following scenario:&#x20;

* Users are able to select the projects in the Project Search Window (on the CSV export page) as expected. &#x20;

2. **Fixed issue where some users are unable to be converted to SAML users when not assigned to SAML org**&#x20;

Some users were receiving the following error:&#x20;

<figure><img src="../../../../.gitbook/assets/Screenshot 2025-01-31 at 3.44.50 PM.png" alt="" width="563"><figcaption><p>Error Msg</p></figcaption></figure>

This was occurring when a user who had previously been either an Auth0 user or a SQ native user, was now attempting to login via SAML BUT that user is not part of SAML org.   This was occurring because CodeScan had been operating under the assumption that the user had previously logged in to codescan at least one time previously.&#x20;

_This assumptive, which triggered the issue, has been fully corrected with this fix._&#x20;
