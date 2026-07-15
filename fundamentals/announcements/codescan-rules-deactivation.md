---
description: >-
  Five CodeScan rules are being fully deactivated in 60 days. Review your  
  Quality Profiles and switch to the replacement rules listed below.
hidden: true
---

# CodeScan Rules Deactivation

## Upcoming Rule Deactivations: 5 Rules Retiring in 60 Days

{% hint style="warning" %}
**Five CodeScan rules will be fully deactivated in 60 days, as of 21st September 2026.** Each rule below has already been marked **Deprecated** and superseded by an improved rule with better or more accurate coverage.
{% endhint %}

### How to check if you're affected

{% hint style="info" %}
Rules subject to deactivation are highlighted in **red** next to the overall rule count within your Quality Profiles.
{% endhint %}

1. Navigate to **Quality Profiles** in CodeScan.
2. Look for rules highlighted in red next to the overall rule count within each profile.
3. Open any flagged rule to see its specific deactivation reason and recommended replacement.

### Rules being deactivated

#### 1. Custom fields must have a description field

Key: `sfmeta:RequireDescriptionField`

Language: `Salesforce Metadata`

Type: `Code Smell`

**Why it's flagged**\
Custom fields should have a description of their function to avoid confusion. This rule requires `.object` or `.field-meta.xml` metadata files to be downloaded.

**Reason for deactivation**\
All functionality has been folded into `sfmeta:RequireDescriptionComponent`.

{% hint style="success" %}
**Action:** Remove this rule from your custom Quality Profile and add `sfmeta:RequireDescriptionComponent` instead.
{% endhint %}

#### 2. Unnecessary Parentheses

Key: `sf:UnnecessaryParentheses`

Language: `Apex`

Type: `Code Smell`

**Why it's flagged**\
Expressions are sometimes wrapped in unnecessary parentheses, making them look like function calls.

**Reason for deactivation**\
Superseded by an improved rule covering the same code style concern.

{% hint style="success" %}
**Action:** Remove this rule from your custom Quality Profile and add `sf:UselessParentheses` instead.
{% endhint %}

#### 3. Use System.Assert instead of System.assertEquals

Key: `sf:UseAssertInsteadOfAssertEquals`

Language: `Apex`

Type: `Code Smell`

**Why it's flagged**\
When asserting that a value equals a boolean literal, `System.assert` should be used instead of `System.assertEquals`.

**Reason for deactivation**\
Salesforce now recommends using the `Assert` class for unit tests.

{% hint style="success" %}
**Action:** Remove this rule from your custom Quality Profile and add `sf:UseIsTrueInsteadOfAreEqual` instead.
{% endhint %}

#### 4. Use System.assertEquals instead of System.assert (equality via `==`)

Key: `sf:UseAssertEqualsInsteadOfAssertEquality`

Language: `Apex`

Type: `Code Smell`

**Why it's flagged**\
This rule detects unit test assertions on object reference equality. Instead of using `System.assert` combined with `==` as the equality operator, assertions should use a more specific method like `assertEquals`.

**Reason for deactivation**\
Salesforce now recommends using the `Assert` class for unit tests.

{% hint style="success" %}
**Action:** Remove this rule from your custom Quality Profile and add `sf:UseAreEqualInsteadOfAssertBoolean` instead.
{% endhint %}

#### 5. Use System.assertEquals instead of System.assert (equality via `.equals()`)

Key: `sf:UseAssertEqualsInsteadOfAssert`

Language: `Apex`

Type: `Code Smell`

**Why it's flagged**\
This rule detects unit test assertions on object reference equality. Instead of using `System.assert` combined with `.equals()` as an equality check, assertions should use a more specific method like `assertEquals`.

**Reason for deactivation**\
Salesforce now recommends using the `Assert` class for unit tests.

{% hint style="success" %}
**Action:** Remove this rule from your custom Quality Profile and add `sf:UseAreEqualInsteadOfIsTrue` instead.
{% endhint %}

### Quick reference table

| Deprecated Rule                                                | Rule ID                                     | Replacement Rule                       |
| -------------------------------------------------------------- | ------------------------------------------- | -------------------------------------- |
| Custom fields must have a description field                    | `sfmeta:RequireDescriptionField`            | `sfmeta:RequireDescriptionComponent`   |
| Unnecessary Parentheses                                        | `sf:UnnecessaryParentheses`                 | `sf:UselessParentheses`                |
| Use System.Assert instead of System.assertEquals               | `sf:UseAssertInsteadOfAssertEquals`         | `sf:UseIsTrueInsteadOfAreEqual`        |
| Use System.assertEquals instead of System.assert (`==`)        | `sf:UseAssertEqualsInsteadOfAssertEquality` | `sf:UseAreEqualInsteadOfAssertBoolean` |
| Use System.assertEquals instead of System.assert (`.equals()`) | `sf:UseAssertEqualsInsteadOfAssert`         | `sf:UseAreEqualInsteadOfIsTrue`        |

### What you need to do

1. Check your Quality Profiles for any of the five rules listed above.
2. If found, remove the deprecated rule and add its corresponding replacement rule.
3. Re-run your analysis to confirm the new rule is active and behaving as expected.

{% hint style="info" %}
**Questions?** Contact us at [support@autorabit.com](mailto:support@autorabit.com).
{% endhint %}
