# CodeScan Public Sector: SSO Setup

## CodeScan Public Sector: SSO Setup &#x20;

Use Case: non-dedicated Environments with IDP mapping&#x20;

&#x20;

This guide is intended to be followed sequentially. Please note that there is a combination of steps that must be performed by a CodeScan Org admin and an Azure AD / Entra ID admin.&#x20;

PART 1: Create SAML Group in AD (as needed), and make that SAML group is available in Entra ID.&#x20;

NOTE: These tasks are performed outside of CodeScan&#x20;

PART 2: Configuration Setup

&#x20;

<figure><img src="../../.gitbook/assets/image.png" alt=""><figcaption></figcaption></figure>

NOTE:  For Organizations requiring multiple email domains, this is fully supported. Please specify your primary email domain in CodeScan during this step (this needs to match what will be in Entra ID).

<figure><img src="../../.gitbook/assets/image (1).png" alt=""><figcaption></figcaption></figure>

&#x20;

<figure><img src="../../.gitbook/assets/image (2).png" alt=""><figcaption></figcaption></figure>

NOTE:  For Organizations requiring multiple email domains, this is fully supported.\
\
To enable:

* Recall that you specified your primary email domain in CodeScan previously. This needs to match what will be in Entra ID.
* In Entra ID, create a single SAML IDP using that domain specified in CodeScan previously.
* Then, configure multiple email domains within this single SAML IDP (in Entra ID).
* NOTE: Later in this setup process, you will setup group sync via IDP in CodeScan.

<figure><img src="../../.gitbook/assets/image (3).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (4).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (5).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (6).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (7).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (8).png" alt=""><figcaption></figcaption></figure>

PART 3 – Validate SSO is working:

\
NOTE: For Organizations using multiple email domains

<figure><img src="../../.gitbook/assets/image (9).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (10).png" alt=""><figcaption></figcaption></figure>

When logging in, it is important that users do NOT enter their email ID here; Instead enter the primary email domain that was configured in Entra ID and in CodeScan. Users will be redirected to the SSO sign in, and then they will enter their email address there.

