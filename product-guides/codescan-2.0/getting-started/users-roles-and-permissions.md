# Users, Roles & Permissions

This article lists the CodeScan roles and what each role can do.

{% hint style="danger" %}
**\[TO CONFIRM before publishing]**

* Role names highlighted in yellow are placeholders and may change.
* Cells marked **?** are not yet documented. Replace each with ✓, — or Read-only.
* Tenant manager and ACA admin have identical documented rights. How do they differ?
* Guard admin appears only as able to view AI credit usage. Does this role belong in CodeScan?
* Support engineer entries marked — come from the rule that all write actions are hidden for this role. They are not documented action by action.
{% endhint %}

**Key:** ✓ allowed | — not allowed | Read-only | **?** to confirm

| Role                                                               | View scans | Run Analysis | Accept findings | Edit repositories and projects | Add webhooks | Create custom rules | Review Noisy Rules | Switch AI on per project | Advanced AI Suggestions | Choose AI model | View AI credit usage | Create API keys | View dashboards |
| ------------------------------------------------------------------ | ---------- | ------------ | --------------- | ------------------------------ | ------------ | ------------------- | ------------------ | ------------------------ | ----------------------- | --------------- | -------------------- | --------------- | --------------- |
| <mark style="background-color:yellow;">**Tenant manager**</mark>   | ✓          | **?**        | **?**           | ✓                              | **?**        | **?**               | **?**              | **?**                    | **?**                   | **?**           | ✓                    | ✓               | ✓               |
| <mark style="background-color:yellow;">**ACA admin**</mark>        | ✓          | **?**        | **?**           | ✓                              | **?**        | **?**               | **?**              | **?**                    | **?**                   | **?**           | ✓                    | ✓               | ✓               |
| <mark style="background-color:yellow;">**ACA user**</mark>         | ✓          | **?**        | **?**           | **?**                          | **?**        | **?**               | **?**              | **?**                    | **?**                   | **?**           | **?**                | —               | **?**           |
| <mark style="background-color:yellow;">**Support engineer**</mark> | Read-only  | —            | —               | —                              | —            | —                   | —                  | —                        | —                       | —               | ✓                    | —               | Read-only       |
| <mark style="background-color:yellow;">**Guard admin**</mark>      | **?**      | **?**        | **?**           | **?**                          | **?**        | **?**               | **?**              | **?**                    | **?**                   | **?**           | ✓                    | **?**           | **?**           |

{% hint style="info" %}
**Note:** Creating an API key requires an administrator account. If **`API Keys`** is not visible in your account, ask an administrator to create a key for you.
{% endhint %}

### Related Articles

* What Is CodeScan
* Security and Data Handling
