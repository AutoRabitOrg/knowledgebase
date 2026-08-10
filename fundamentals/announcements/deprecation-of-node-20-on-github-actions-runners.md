# Deprecation of Node 20 on GitHub Actions Runners

{% hint style="info" %}
**This change applies only to GitHub projects scanned using GitHub Actions** (a `codescan.yml` workflow that calls the CodeScan scanner action). If you use the native CodeScan–GitHub integration, where scans are triggered from within CodeScan with no YAML workflow file, this change does not affect you, and no action is required.
{% endhint %}

#### **Overview**

As part of GitHub's ongoing platform maintenance, the Node 20 runtime on GitHub Actions runners is being retired and replaced by Node 24. To ensure your scans continue running without interruption, CodeScan will release an updated scanner action (`@3.0`) on **October 11, 2026**. We recommend updating your workflow ahead of GitHub's Node 20 removal, which is currently estimated for Fall 2026 (see more [here](https://github.blog/changelog/2025-09-19-deprecation-of-node-20-on-github-actions-runners/)).

Your scan functionality remains the same—this is a runtime update only.

#### Actions Required

Update the following action versions in your `codescan.yml` workflow:

1. `codescan-io/codescan-scanner-action` : `@2.0` → `@3.0`
2. `actions/checkout` : `@v4` → `@v6`
3. `actions/cache` : `@v4` → `@v5`
4. `github/codeql-action/upload-sarif` : `@v3` → `@v4`
5. `actions/upload-artifact` : `@v3`/`@v4` → `@v6`

#### Custom (Self-Hosted) Runners

If you run your GitHub Actions workflows on custom (self-hosted) runners rather than GitHub-hosted ones, an additional step is required beyond updating your action versions:

1. **Update your action versions** in `codescan.yml` (as listed in _Actions Required_ above).
2. **Upgrade your runner** to a version that supports Node 24 (**v2.328.0 or later**), and confirm operating system and architecture compatibility:
   * Node 24 is **not compatible with macOS 13.4 or earlier** — please upgrade the operating system on affected runners.
   * **ARM32 is no longer supported** — these runners will stop working once Node 20 is removed.

#### Runtime Configuration Option

GitHub provides an environmental variable to help you manage the transition on your own timeline. This is optional — updating your Action versions as described above is the recommended path.

**To temporarily continue on Node 20:**&#x20;

Once Node 24 becomes the default, you can temporarily opt out by setting `ACTIONS_ALLOW_USE_UNSECURE_NODE_VERSION=true`&#x20;

{% hint style="info" %}
Please note that this is a temporary measure until Node 20 full removal.&#x20;
{% endhint %}

#### Need Help?

1. Please refer to the [GitHub Changelog](https://github.blog/changelog/2025-09-19-deprecation-of-node-20-on-github-actions-runners/) for additional details.
2. Contact AutoRABIT Support ([support@autorabit.com](mailto:support@autorabit.com)).
