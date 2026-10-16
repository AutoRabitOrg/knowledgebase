---
description: >-
  What uses AI credits, how to monitor usage, and what happens when credits run
  out.
---

# AI Credits

AI features in CodeScan draw on a monthly allowance of AI credits. The deterministic scan never uses credits. This article explains what does, how to keep track, and what happens when credits run out.

## What Uses Credits

| Feature                                      | Where it is switched on                                                                                                                                                                                                                                                                                     |
| -------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| AI finding review, including suggested fixes | Project settings. On by default for new projects, for Blocker and Critical. Also needed before you can create custom rules. Applies to every scan of the project, whether it starts in the web app, a pull request, CI, the CLI or VS Code.roject settings. Also needed before you can create custom rules. |
| AI pull request review                       | Project settings                                                                                                                                                                                                                                                                                            |
| AI test quality review                       | Project settings, or `codescan review --check-tests`                                                                                                                                                                                                                                                        |
| Custom rules and Generate from file          | When you create or generate rules                                                                                                                                                                                                                                                                           |
| Policy as Intent                             | When rules are drafted from a policy                                                                                                                                                                                                                                                                        |
| Review Noisy Rules                           | When you run the review                                                                                                                                                                                                                                                                                     |
| PR fixes                                     | <mark style="color:red;">**\[TO CONFIRM: how PR fixes are billed. The review page shows "Billed: n fixed findings"]**</mark>                                                                                                                                                                                |

Each feature is hidden when AI is switched off for your organisation.

### Scans From VS Code

A scan from VS Code uses the AI settings of the project it belongs to:

* If the repository is already registered in CodeScan, the extension connects to that project and uses its settings.
* If it isn't, the extension creates a project for the repository.&#x20;

So a developer's VS Code scans use AI credits whenever **`AI finding review`** is on for that project. With the default settings, that is from the first scan.

To control this:

* **Register repositories before developers scan them,** so you choose each project's AI settings first. See Register a Repository.
* **Check Repositories from time to time** for projects created from VS Code, and review their AI settings.
* **Use AI Credit Usage** to see VS Code scans per user. See Monitoring Usage.

## Limits

Credits have a monthly limit and a daily limit. <mark style="color:red;">**\[TO CONFIRM: the daily limit, and whether customers can see or change either limit]**</mark>

## Monitoring Usage

* **In the header:** **AI Credits Usage** shows **This Month** as used against your limit. At 80% you see _You're running low on AI credits for this month_.
* **AI Credit Usage page:** the month's total, usage by feature as a percentage of the monthly limit, and a **Usage History** table with date, user, feature, event and credits. You can view the current month or any of the previous 11.
* **Development Dashboard:** AI scan credit usage per user.

The AI Credit Usage page is available to <mark style="background-color:yellow;">**Tenant manager**</mark>, <mark style="background-color:yellow;">**ACA admin**</mark>, <mark style="background-color:yellow;">**Support engineer**</mark> and <mark style="background-color:yellow;">**Guard admin**</mark>.

<figure><img src="../../../.gitbook/assets/Screenshot 2026-10-16 at 17.11.01.png" alt=""><figcaption></figcaption></figure>

## When Credits Run Out

AI review is skipped, and the scan still completes. You get the full scanner results, without likely-false-positive flags or suggested fixes from that pass. Nothing fails because credits reached zero.

The same applies when AI is switched off or the AI service is unavailable. Every AI call is retried before CodeScan falls back to the scanner results.

## Keeping Usage Down

* Choose only the severities you need in **`Severities included in AI review`**. Starting with Blocker and Critical keeps usage focused on the findings that matter most.
* Re-scanning unchanged code costs nothing, because AI verdicts are cached. Changing your rules or the AI model resets the cache, so the next scan reviews afresh.
* Switch on AI features project by project, starting where they add the most value.

## Choosing the AI Model

An administrator can choose which AI model is used for each AI feature, from the models available. By default, high-volume work such as finding review and fixes uses a fast model, and lower-volume reasoning such as rule extraction and noise analysis uses a stronger one. <mark style="color:red;">**\[TO CONFIRM: which roles can change the model, and where]**</mark>

## Related Articles

* [The AI Reviewer](/broken/pages/5957a7e3fd8cac359477cb24a29c02599ef0ab6b)
* [Project Settings](/broken/pages/9130a1cc74fd1ebef58d3563d5a1d2d908986c76)
* [Security and Data Handling](/broken/pages/cde90742926e0b5763adb2fc8c9a7ea1b3b07533)
