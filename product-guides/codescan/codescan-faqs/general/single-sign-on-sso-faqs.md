# Single Sign-On (SSO) FAQs

A selection of frequently asked questions about Single Sign On.

### What is SSO? <a href="#what-is-sso" id="what-is-sso"></a>

SSO (Single Sign-On) is a sign-in method that allows a user to log into one application and access all of their accounts from one place.

### What Identity Providers does CodeScan integrate with? <a href="#what-identity-providers-does-codescan-integrate-with" id="what-identity-providers-does-codescan-integrate-with"></a>

CodeScan can integrate with any Identity Provider that supports SAML 2.0. In the past, we have worked with:

* ADFS
* Microsoft Entra ID (formerly Azure AD)
* Okta
* PingOne

### What happens to users who try to log in via Auth0 when SSO is enabled? <a href="#what-happens-to-users-who-try-to-login-via-auth0-when-sso-is-enabled" id="what-happens-to-users-who-try-to-login-via-auth0-when-sso-is-enabled"></a>

When SSO is enabled, attempting to log in via Auth0 results in the user account being **locked out**. When a user begins using an SSO login, they should refrain from using Auth0. Any attempt to log in using Auth0 would create a new account. Since CodeScan has a constraint requiring a unique email, the user would be unable to log in because there would be two users in the application with the same email address.

**Resolution steps:** Remove the user from the CodeScan platform and add them back. It necessitates engineering support from CodeScan.

### Is it possible to merge SSO with Auth0? <a href="#is-it-possible-to-merge-sso-with-auth0" id="is-it-possible-to-merge-sso-with-auth0"></a>

CodeScan can combine an existing Auth0 with SSO if the user's email address matches. This ensures all user-related information, such as user permissions, groups, user tokens, and assigned issues, stays intact after switching to SSO login.

### Why are a few users duplicated when SSO is enabled? <a href="#why-there-is-duplication-of-few-users-when-sso-is-enabled" id="why-there-is-duplication-of-few-users-when-sso-is-enabled"></a>

When SSO is enabled, non-Admin users who were previously using Auth0 authentication experience an issue when two users' accounts appear for a single user.

This may occur if:

* The user's Identity Provider was incorrectly configured, preventing CodeScan from receiving emails. Merging will only take place if the **`Email`** field for the SSO user is filled in.
* The SAML attribute, which the non-Admin user uses to pass the email details to CodeScan, contains a different value than the email associated with the Auth0 user account.

**Resolution steps:** The users need to review the SSO configuration in their Identity Provider and identify and fix the issue. They must then ask the CodeScan team to delete the users incorrectly created using SSO.

### What happens to users who are logged in to CodeScan before SSO is enabled? <a href="#what-happens-to-users-who-are-logged-in-to-codescan-before-sso-is-enabled" id="what-happens-to-users-who-are-logged-in-to-codescan-before-sso-is-enabled"></a>

Users who are logged in to CodeScan before SSO is enabled will not be automatically logged out but will have to log in through the Identity Provider upon their next login.

If a user's session times out, CodeScan will direct the user back to the Identity Provider for authentication. If the user logs out of CodeScan, the user will have to log into CodeScan via the Identity Provider.

### How do I add users to CodeScan after SSO is enabled? <a href="#how-do-i-add-users-to-codescan-after-sso-is-enabled" id="how-do-i-add-users-to-codescan-after-sso-is-enabled"></a>

All non-Admin users must log in using the Identity Provider after SSO is enabled. To access your CodeScan organization, new users must first be added to the Identity Provider.

{% hint style="info" %}
**Note:** If your team has single sign-on (SSO) and **`Enforce SSO`** enabled, Admins should not invite new users via the CodeScan app. You must invite new users via your Identity Provider.
{% endhint %}
