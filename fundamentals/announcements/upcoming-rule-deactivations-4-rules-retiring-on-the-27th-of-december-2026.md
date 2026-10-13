# Upcoming Rule Deactivations: 4 Rules Retiring on the 27th of December 2026

{% hint style="warning" %}
**Four CodeScan rules will be fully deactivated as of 27th of December 2026.** Each rule below has already been marked **Deprecated** and superseded by an improved rule with better or more accurate coverage. Review your Quality Profiles and switch to the replacement rules listed below.
{% endhint %}

### How to check if you're affected

{% hint style="info" %}
Rules subject to deactivation are highlighted in **red** next to the overall rule count within your Quality Profiles.
{% endhint %}

1. Navigate to **Quality Profiles** in CodeScan.
2. Look for rules highlighted in red next to the overall rule count within each profile.
3. Open any flagged rule to see its specific deactivation reason and recommended replacement.

### Rules being deactivated

#### 1. Disallow octal escape sequences in string literals

Key: `cs-vf:no-octal-escape`

Language: `Visual Force & Lightning`

Type: `Code Smell`

**Why it's flagged**\
As of the ECMAScript 5 specification, octal escape sequences in string literals are deprecated and should not be used. Unicode escape sequences should be used instead.

**Reason for deactivation**\
This rule has been deprecated due to these types of octal escapes being caught by the Javascript parser before a rule can be fired. Please make sure you have the the `cs-js:exception` rule in your javascript Quality Profile to be made aware of these errors.

{% hint style="success" %}
**Action:** Remove this rule from your custom Quality Profile and add `cs-js:exception` instead.
{% endhint %}

#### 2. Disallow octal escape sequences in string literals

Key: `cs-js:no-octal-escape`

Language: `JavaScript`

Type: `Code Smell`

**Why it's flagged**\
As of the ECMAScript 5 specification, octal escape sequences in string literals are deprecated and should not be used. Unicode escape sequences should be used instead.

**Reason for deactivation**\
This rule has been deprecated due to these types of octal escapes being caught by the Javascript parser before a rule can be fired. Please make sure you have the the `cs-js:exception` rule in your javascript Quality Profile to be made aware of these errors.

{% hint style="success" %}
**Action:** Remove this rule from your custom Quality Profile and add `cs-js:exception` instead.
{% endhint %}

#### 3. Disallow irregular whitespace outside of strings and comments

Key: `cs-vf:no-irregular-whitespace`

Language: `Visual Force & Lightning`

Type: `Code Smell`

**Why it's flagged**\
Invalid or irregular whitespace causes issues with ECMAScript 5 parsers and also makes code harder to debug in a similar nature to mixed tabs and spaces.

**Reason for deactivation**\
This rule has been deprecated due to these types of white space being caught by the Javascript parser before a rule can be fired. Please make sure you have the the `cs-js:exception` rule in your javascript Quality Profile to be made aware of these errors.

{% hint style="success" %}
**Action:** Remove this rule from your custom Quality Profile and add `cs-js:exception` instead.
{% endhint %}

#### 4. Disallow irregular whitespace outside of strings and comments

Key: `cs-js:no-irregular-whitespace`

Language: `JavaScript`

Type: `Code Smell`

**Why it's flagged**\
Invalid or irregular whitespace causes issues with ECMAScript 5 parsers and also makes code harder to debug in a similar nature to mixed tabs and spaces.

**Reason for deactivation**\
This rule has been deprecated due to these types of white space being caught by the Javascript parser before a rule can be fired. Please make sure you have the the `cs-js:exception` rule in your javascript Quality Profile to be made aware of these errors.

{% hint style="success" %}
**Action:** Remove this rule from your custom Quality Profile and add `cs-js:exception` instead.
{% endhint %}

### Quick reference table

| Deprecated Rule                                               | Rule ID                         | Replacement Rule  |
| ------------------------------------------------------------- | ------------------------------- | ----------------- |
| Disallow octal escape sequences in string literals            | `cs-vf:no-octal-escape`         | `cs-js:exception` |
| Disallow octal escape sequences in string literals            | `cs-js:no-octal-escape`         | `cs-js:exception` |
| Disallow irregular whitespace outside of strings and comments | `cs-vf:no-irregular-whitespace` | `cs-js:exception` |
| Disallow irregular whitespace outside of strings and comments | `cs-js:no-irregular-whitespace` | `cs-js:exception` |

### What you need to do

1. Check your Quality Profiles for any of the five rules listed above.
2. If found, remove the deprecated rule and add its corresponding replacement rule.
3. Re-run your analysis to confirm the new rule is active and behaving as expected.

{% hint style="info" %}
**Questions?** Contact us at [support@autorabit.com](mailto:support@autorabit.com).
{% endhint %}
