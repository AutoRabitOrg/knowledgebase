---
description: >-
  See what else a change affects, which tests to rerun, and how risky the change
  is.
---

# Blast Radius for Pull Requests

When CodeScan scans a change, such as a pull request or your uncommitted edits, it also works out what else that change affects. This is the blast radius. It helps reviewers see beyond the lines in the diff, and tells you which tests to rerun.

The blast radius is worked out by the deterministic engine. No AI is involved and no credits are used.

{% hint style="info" %}
**Note:** A full scan has no change to measure, so it has no **`Blast Radius`** tab. Security findings on a full scan still show an **Impact** section with entry points, callers and test coverage.
{% endhint %}

## Navigation:

Select a Pull Request scan to review, see **`Blast Radius`**:

<figure><img src="../../../.gitbook/assets/Screenshot 2026-10-16 at 15.50.17.png" alt=""><figcaption></figcaption></figure>

## How It Is Worked Out

{% stepper %}
{% step %}
### Start from the change

The files in the pull request or edit.
{% endstep %}

{% step %}
### Walk outwards

CodeScan follows everything that depends on those files: callers, importers, subclasses, and, for Salesforce, metadata that references the changed code. It goes up to three steps out.
{% endstep %}

{% step %}
### Find entry points

It lists entry points and external calls in the affected code.
{% endstep %}

{% step %}
### Find tests

It lists affected tests, and changed files that no test reaches.
{% endstep %}

{% step %}
### Collect findings

It lists findings that fall inside the affected area.
{% endstep %}

{% step %}
### Rate the risk

It gives the change a risk level.
{% endstep %}
{% endstepper %}

## Risk Levels

| Level  | When                                                                                                                                                           |
| ------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| High   | More than 5 modules affected, more than 20 dependent symbols, a guest or public entry point reached, or a Blocker or Critical finding inside the affected area |
| Medium | 3 to 5 modules affected, 6 to 20 dependent symbols, or any entry point reached                                                                                 |
| Low    | Anything else                                                                                                                                                  |

## What You See

On the **`Blast Radius`** tab of the scan page:

* Dependent code, with the entry points it exposes
* Affected tests, and changed files no test reaches
* Findings in the affected area
* The risk level

The CLI prints a one-line blast-radius summary, and the full detail is in the `blastRadius` field of `--json` output.

<figure><img src="../../../.gitbook/assets/Screenshot 2026-10-16 at 15.43.26.png" alt="" width="563"><figcaption></figcaption></figure>

## Using It in a Review

* **High risk:** ask for a second reviewer and rerun the affected tests.
* **A guest or public entry point is reached:** review the change with your security lead.
* **A changed file no test reaches:** this is new behaviour with no test. Add one before merging.
* **Combine with coverage:** look up each affected file on the **Coverage** tab. A changed file that is uncovered is the highest priority. See [Test Quality and Coverage](/broken/pages/cd9ab9172a7048137880bf9d5981711455cf7434).

## How Deep It Goes by Language

| Depth                    | Languages                                          |
| ------------------------ | -------------------------------------------------- |
| Method level             | Apex, Java                                         |
| File level, from imports | TypeScript, JavaScript (including LWC), Python, Go |
| File level, estimated    | Rust, C#, C++, Kotlin, Scala, F#                   |

For Salesforce, CodeScan also follows LWC imports of Apex, Visualforce controllers, Aura controllers, Flow action calls and guest-profile class grants.

{% hint style="warning" %}
**Important Note:** Reflection, dependency injection and dynamic queries are invisible to static analysis. Treat the blast radius as the minimum a change affects, not a guarantee.
{% endhint %}

For the affected-tests list to work, set your **`Tests Folders`**. See [Exclusions and Test Folders](/broken/pages/b34368acc65d5a91c52d4fe449c256b290a96d4c).

## Related Articles

* [Scan Types and Branches](/broken/pages/9d7729a5755d937d2fd7f2bcfd0f92a6c720e92e)
* [Pull-Request Review Overview](/broken/pages/c6f315bca41020fb9aad5e9c4615b97cb79ecde2)
