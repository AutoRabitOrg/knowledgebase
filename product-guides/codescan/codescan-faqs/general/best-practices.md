---
hidden: true
---

# Best Practices

## CodeScan FAQs – Best Practices

### Obtaining the most precise delta scans

Have you noticed irrelevant issues flagged on your latest Pull Request (PR)? Are files other than those selected getting scanned? This article provides guidelines on how to avoid such scenarios when using CodeScan.

#### How Delta scans work

When CodeScan performs a delta scan, the application uses a Diff mechanism to identify the delta. So if there is a Code Diff for some lines, the system will consider it a Delta Code.

If some lines in the project have been modified anytime between scans and respective changes weren't recorded in the reference branch, a comparison will pick them up as part of the delta scan. That’s the reason you may sometimes get unexpected results for a specific scan.

#### What is the best approach for having accurate delta scans?&#x20;

Let’s say you always compare your PRs to the master branch (most common case). The differences between the master and developer branches will depend on how often the Master's scan is updated.

**Keeping the Master scan refreshed is the key to having the most accurate deltas.**

To achieve this, schedule scans of your master branch either daily or on demand. This will help you keep it updated and ensure issues are recorded regularly.

{% hint style="info" %}
**Important note:**&#x20;

If you have an ARM pipeline, make sure NOT to select the "All Supported Metadata Types" checkbox when creating an EZ-Merge from ARM, because it will run CodeScan on all of the Apex Classes, Triggers, Apex Pages & AuraDefinitionBundles.
{% endhint %}

Reference support tickets #120366, #114480&#x20;

