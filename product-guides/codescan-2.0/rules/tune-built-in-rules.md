---
description: Change a built-in rule's severity or switch it off for one project.
---

# Tune Built-in Rules

You can change how a built-in rule behaves for one project: lower or raise its severity, or switch it off. Changes apply only to that project and take effect on the next scan.

### Changing a Rule

1. Open the Repository, navigate to **`Code Analysis Rules`**.&#x20;
2. Utilise **`Filter`** for faster search.
3. Find the rule.
4. To switch it off, clear **`Enabled`**.
5. To change its severity, choose a new **`Severity`**. To go back to the original, choose **`Default`**.

<figure><img src="../../../.gitbook/assets/Screenshot 2026-10-16 at 17.51.11.png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
**Note:** Rules marked **Dynamic** set the severity of each finding individually. Their severity cannot be overridden.
{% endhint %}

### Before You Switch a Rule Off

Switching a rule off hides it everywhere in the project, including on new code. Consider the lighter options first:

| Situation                                  | What to do                                          |
| ------------------------------------------ | --------------------------------------------------- |
| One finding is wrong, or a risk you accept | Accept the finding. The rule still checks new code. |
| The rule is sometimes useful               | Lower its severity rather than switching it off.    |
| The rule does not apply to this codebase   | Switch it off.                                      |
| You're not sure which rules are noisy      | Run Review Noisy Rules.                             |

Security rules are worth keeping on. If a security rule is noisy on your code, accept the specific findings and tell us, so we can improve the rule.

### Related Articles

* Reduce Noise
* Custom Rules
* Rule Catalogue
