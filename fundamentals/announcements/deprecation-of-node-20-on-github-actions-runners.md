# Deprecation of Node 20 on GitHub Actions Runners

{% hint style="info" %}
**This change applies only to GitHub projects scanned using GitHub Actions** (a `codescan.yml` workflow that calls the CodeScan scanner action). If you use the native CodeScan–GitHub integration, where scans are triggered from within CodeScan with no YAML workflow file, this change does not affect you, and no action is required.
{% endhint %}

#### **Overview**

As part of GitHub's ongoing platform maintenance, the Node 20 runtime on GitHub Actions runners is being retired and replaced by Node 24. To ensure a seamless transition, CodeScan has released an updated scanner action that runs on Node 24, and we recommend updating your workflow to the latest action versions ahead of GitHub's deadlines.

Your scan functionality remains the same—this is a runtime update only.

#### Key Dates

1. **June 2, 2026:** Runners begin using Node 24 by default. Workflows on older action versions may start to fail.
2. **September 16, 2026:** Node 20 is fully removed. Any workflows not yet updated will stop running.

#### Actions Required

Update the following action versions in your `codescan.yml` workflow:

1. `codescan-io/codescan-scanner-action` : `@2.0` → `@3.0`
2. `actions/checkout` : `@v4` → `@v6`
3. `actions/cache` : `@v4` → `@v5`
4. `github/codeql-action/upload-sarif` : `@v3` → `@v4`
5. `actions/upload-artifact` : `@v3`/`@v4` → `@v6`

#### Runtime Configuration Options

GitHub provides two environment variables to help you manage the transition on your own timeline. These are optional—updating your Action versions as described above is the recommended path.

1. **Test Node 24 ahead of time:** To opt in to Node 24 now and validate your workflow before the June 2, 2026 default switch, set `FORCE_JAVASCRIPT_ACTIONS_TO_NODE24=true` as an environment variable in your workflow file or on the runner.
2. **Temporarily continue on Node 20:** Once Node 24 becomes the default, you can temporarily opt out by setting `ACTIONS_ALLOW_USE_UNSECURE_NODE_VERSION=true`. This is a short-term measure only; **it will stop working once Node 20 is removed on September 16, 2026**.

#### Need Help?

1. Contact AutoRABIT Support ([support@autorabit.com](mailto:support@autorabit.com)).
2. Refer to the [GitHub Changelog](https://github.blog/changelog/2025-09-19-deprecation-of-node-20-on-github-actions-runners/) for additional details.
