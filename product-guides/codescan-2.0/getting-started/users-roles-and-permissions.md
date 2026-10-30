# Users, Roles & Permissions

This article lists the CodeScan roles and what each role can do.

**Key:** ✓ allowed | — not allowed | Read-only&#x20;

<table><thead><tr><th>Role</th><th>View scans</th><th>Run Analysis</th><th>Accept findings</th><th>Edit repositories and projects</th><th>Add webhooks</th><th>Create custom rules</th><th>Review Noisy Rules</th><th>Switch AI on per project</th><th>Advanced AI Suggestions</th><th width="140">View AI credit usage</th><th>Create API keys</th><th>View dashboards</th></tr></thead><tbody><tr><td><strong>Tenant Manager</strong></td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td><p>✓ </p><p>(all features)</p></td><td>✓</td><td>✓</td></tr><tr><td><strong>ACA admin</strong></td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✓<br>(scanner only)</td><td>✓</td><td>✓</td></tr><tr><td><strong>ACA user</strong></td><td>✓</td><td>✓</td><td>✓</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td><strong>Read-only</strong> (can start PR fixes)</td><td>—</td><td>—</td><td>—</td></tr><tr><td><strong>Support Engineer</strong></td><td>Read-only</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>✓</td><td>—</td><td>—</td></tr><tr><td><strong>Guard admin</strong></td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>✓<br>(scanner only)</td><td>—</td><td>—</td></tr></tbody></table>

{% hint style="info" %}
**Note:** Creating an API key requires an administrator account. If **`API Keys`** is not visible in your account, ask an administrator to create a key for you.
{% endhint %}

### Related Articles

* What Is CodeScan
* Security and Data Handling
