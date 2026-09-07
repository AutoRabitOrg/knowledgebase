---
description: >-
  Applies to installations where the Multi Tenant license module is enabled. In
  a single-tenant installation every hostname reaches the one tenant and this
  page does not apply
---

# Tenant URLs and Login

### How a Tenant is Identified <a href="#how-a-tenant-is-identified" id="how-a-tenant-is-identified"></a>



IZ Suite identifies the tenant from the **hostname** of every request. The same hostname is used for the web application, single sign-on callbacks, security tokens used by CI/CD scanners and IDE plug-ins, and MCP clients. There is no tenant selector on the login page: the URL a user opens decides which tenant they sign in to.

The hostname is resolved in this order:



1. **Subdomain slug.** The first label of the hostname is compared with the tenants' **`Slug`**. For example `acme.izsuite.example.com` resolves to the tenant with slug `acme`.
2. **External Link.** The full hostname is compared with the tenants' **`External Link`**. This lets a tenant use a hostname of its own, for example `quality.acme.com`. The scheme and a trailing slash are ignored when matching.

The following leading labels are never treated as a tenant slug: `www`, `app`, `localhost`, `izsuite`, `integralzone`. Hostnames that are IP addresses do not resolve a tenant either. Hostnames are matched case-insensitively and the port is ignored.



### Login URL <a href="#login-url" id="login-url"></a>

The login URL for a tenant is `https://<slug>.<your IZ Suite domain>/login`. It is shown as **`Login Link`** in the Tenants grid and on the result panel after onboarding a Tenant. When a tenant uses an External Link, its login URL is `https://<external hostname>/login`.



#### Sign-in Options Shown <a href="#sign-in-options-shown" id="sign-in-options-shown"></a>

The login page lists the sign-in options that are **enabled for that tenant** in its **`Global Settings`** → **`Settings`** (**`IZ Token Auth`**, **`Anypoint Auth`**, **`Google Auth`**, **`Azure Auth`**). A newly onboarded tenant has only **`Signin with IZ Token`** enabled; the tenant administrator enables single sign-on afterwards.



#### Unknown Hostname <a href="#unknown-hostname" id="unknown-hostname"></a>

When the hostname does not resolve to a tenant and cannot be served by the platform tenant, the login page shows:

**Please validate the URL provided for your tenant.**

Check that the hostname matches the tenant's slug or External Link exactly, that DNS points at the IZ Suite instance, and that the proxy forwards the `Host` header. If the tenant's slug or External Link was changed recently, use **`Invalidate Tenant Cache`** in Manage Tenants.



### Single Sign-on Redirect URIs <a href="#single-sign-on-redirect-uris" id="single-sign-on-redirect-uris"></a>

Because the tenant is derived from the hostname, every identity provider must redirect back to the **tenant's own hostname**:

| Provider               | Redirect URI                          |
| ---------------------- | ------------------------------------- |
| Anypoint Connected App | `https://<tenant host>/anypoint_auth` |
| Google                 | `https://<tenant host>/google_auth`   |
| Microsoft Entra ID     | `https://<tenant host>/azure_auth`    |

A Connected App or application registration created for one tenant cannot be reused for another tenant unless the provider allows several redirect URIs.



### Security Tokens, CLI and MCP Clients <a href="#security-tokens-cli-and-mcp-clients" id="security-tokens-cli-and-mcp-clients"></a>



* Security tokens generated under **`Organization`** → **`Tokens`** belong to the tenant they were generated in and are only accepted on that tenant's hostname.
* IZ Scan CLI, Maven and IDE plug-ins must be configured with the tenant URL as the server URL.
* HTTP MCP clients must send the tenant URL in the service URL header; the tenant is resolved from it. A request for an unknown or suspended tenant is rejected.



### Changing a Slug or External Link <a href="#changing-a-slug-or-external-link" id="changing-a-slug-or-external-link"></a>



Editing a tenant's **`Slug`** or **`External Link`** in Manage Tenants changes the URL that users, identity providers, CLI configurations and MCP clients rely on. Plan the change with the tenant and update the redirect URIs at the identity provider before switching. The hostname mapping is refreshed on all server nodes within about 15 seconds; use **`Invalidate Tenant Cache`** if a stale mapping persists.



### Sign Out <a href="#sign-out" id="sign-out"></a>

**`Sign Out`** ends the session and returns the user to the login page of the same tenant hostname.

<br>
