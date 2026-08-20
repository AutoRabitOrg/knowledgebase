# New CodeScan Rules for LWC Server-Side Rendering (SSR) Support

### Overview

CodeScan is expanding its JavaScript/LWC rule coverage with 6 new rules that help identify code incompatible with Lightning Web Components Server-Side Rendering (SSR). These rules are part of our ongoing sync with the latest `@lwc/eslint-plugin-lwc` release.

### What's New

| Rule                                                    | Severity | Type          |
| ------------------------------------------------------- | -------- | ------------- |
| `ssr-no-disallowed-lwc-imports`                         | Critical | Vulnerability |
| `ssr-no-host-mutation-in-connected-callback`            | Critical | Bug           |
| `ssr-no-restricted-browser-globals`                     | Critical | Bug           |
| `ssr-no-unsupported-node-api`                           | Critical | Bug           |
| `ssr-no-form-factor`                                    | Major    | Bug           |
| `ssr-no-static-imports-of-user-specific-scoped-modules` | Major    | Code Smell    |

All 6 rules apply to JavaScript/LWC code and carry the `lightning` and `salesforce` tags.

### Activating the New Rules

These rules are **not active by default**. To include them in your scans:

1. Go to your custom Quality Profile.
2. Search for the `lightning` or `salesforce` tag to locate the new rules.
3. Activate the rules you want included.

Existing scan results will not change until you complete this step.

### Prerequisite: Node.js Version

Supporting these rules requires the scanning engine to run on ESLint 9, which in turn requires **Node.js 18.20.0 or later**.

| Environment                               | Action Needed                                                        |
| ----------------------------------------- | -------------------------------------------------------------------- |
| CodeScan cloud-hosted service             | None — we manage the runtime for you.                                |
| Custom (self-hosted) CI/CD agents/runners | Confirm Node.js 18.20.0+ is installed before enabling the new rules. |
| On-premises CodeScan installation         | Confirm Node.js 18.20.0+ is installed before enabling the new rules. |

If your environment doesn't meet this minimum, activating the new rules may cause scan failures until Node.js is upgraded.

### Need Help?

Contact AutoRABIT Support at [support@autorabit.com](mailto:support@autorabit.com).
