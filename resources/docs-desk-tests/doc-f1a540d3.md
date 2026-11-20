## Guard 26.2.7

**Release date:** 18 November 2026

### New features

#### API Security 2.0

API Security 2.0 replaces Guard’s existing API Security module with updated checks for Salesforce External Client Apps and connected apps. It helps administrators identify risky configurations across app access, credentials, network restrictions and session security. Connected apps also include checks for unverified apps and missing contact email addresses, along with migration guidance.

Guard does not migrate or replace connected apps.&#x20;

To run all available checks, the integration user needs Metadata API access. Guard uses that access to assess configurations; it does not change app settings.

#### Create policies with Guard MCP

Admins and tenant managers can create Authorization, Change Monitoring, or Drift policies through the Guard MCP just by describing what they need in plain language. Guard validates the request, prompts for any missing details, and returns a link to the finished policy, so teams can go from idea to configured policy in a single conversation.

If you have older Change Monitoring policies with multiple rules, review them before editing. Recreate them as separate policies if needed, since editing these older policies in the UI can remove their additional rules.

#### Notification users

Admins can create notification users who can sign in to view notifications addressed to them, without gaining access to Guard’s regular screens or policy controls. Existing Guard users can also open notification details from Notification Centre. Admins can add up to 100 users at once through CSV import.

To help protect sensitive information, notification emails contain the subject and a View details link by default. Admins can choose to include more detail after acknowledging that security information will be sent outside Guard. Personal data remains masked in email, while the Guard detail page retains the full values.

#### Manage tenant features in Settings

Tenant managers can control access to features such as Automated Data Classification, Ask AutoRABIT, Guard CLI and MCP, Risk Auto Resolve, and AI notification summaries from Settings. Guard asks for confirmation before changes and records them in the audit log.

### Enhancements

#### Find and review permissions more efficiently

Permission Explorer now loads user lists and Object Access results more quickly, including in large orgs.&#x20;

Matching Users now shows counts for Explore User Permissions, Object Access and Agentforce, with counts reflecting the selected filters. For very large results, Guard may show an upper bound rather than an exact count. Results stay visible as more users load, and permission details are fetched when you select a user.

Permission History and Support Login Access Login History also load results in pages, making large histories easier to browse. You can still sort and move between pages, though exact totals and a last-page button are no longer shown.

#### Understand who can access classified fields

The Data Classification “Who has access” view now shows profiles, permission sets and groups with user counts. Select a source to view its users in pages, making access reviews more manageable. Results reflect active, non-frozen users with active assignments.

#### Track and retrieve exports

Guard now shows whether supported exports are queued, running, completed or failed, with recent exports and download links. If an export fails, Guard provides a message to help explain why. Export files are available for five days, and run history remains available for 30 days.

Large Permission Explorer exports are processed more efficiently and can recover from temporary failures or interruptions. Public File Exposure exports also process results in pages.

#### Monitor user activity in large orgs

Nightly User Activity Monitoring snapshots now process more efficiently.&#x20;

The Not frozen and Not password locked filters continue to include guest and system users that do not have a UserLogin record.

#### Identify the Guard build before signing in

The Guard version is now displayed on the login screen, so you can confirm which build is running without signing in.

#### Clarify accepted risks in Digital Experience Assessment

Digital Experience Assessment now labels the relevant sites “Risk accepted sites” instead of “Excluded sites.” The updated wording better reflects the decision while leaving the assessment and site selection unchanged.

#### Review generated Test Class for Transaction Security Policies

Generated Transaction Security Policy Apex now includes the test class alongside the policy class. Please review carefully as the generated Apex may not meet every org’s Salesforce code coverage requirements.

### Bug fixes

#### See more consistent Risk Assessment and Public File Exposure results

Guest access and default external access counts in Risk Assessment now align more closely with Salesforce Health Check. Refresh the assessment to see updated values.

Public File Exposure now keeps an org visible and explains when Salesforce Content Deliveries is unavailable. Counts and file actions return when the feature becomes available.

#### Scan Experience sites with custom domains

When a site’s custom hostname cannot resolve, Guard can scan it through its Salesforce-managed URL while keeping the custom URL in the scan record, history and risk acceptances. This fallback requires a site path prefix and a usable Salesforce-managed endpoint.

#### Get more complete Data Classification scans

Automatic scans now process eligible fields individually, so an unreadable field no longer prevents other fields on the same object from being scanned. When an org is detached or unavailable, Guard can still show compliance groups from the last stored analysis.

#### Include the right users and records in reviews

Permission Explorer now handles guest and system users more consistently when excluding frozen users. Executive Reports also count eligible Risky Changes across the last 30 days without the previous 1,000-record cap, and show Risky Permissions holder counts more efficiently.

#### Review Change Monitoring activity more smoothly

Change Monitoring now tracks profile rename events in its activity and policies. Loading has improved for large change histories, and a progress indicator appears while results are being retrieved.

#### Searches in Permission Explorer

Permission Explorer searches now support both permission and permission-set API names.

#### Recover from Salesforce connection issues more clearly

Guard now gives clearer guidance when Salesforce access is revoked or rejected, while treating outages and throttling as temporary conditions. Connections recover more reliably after temporary failures.&#x20;
