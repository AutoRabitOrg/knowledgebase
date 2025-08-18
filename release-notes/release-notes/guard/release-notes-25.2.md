# Guard Release Notes 25.2

## Guard 25.2.3 Release Notes

**Release Date: 20 August 2025**

### New User Creation Simplified

Creating new users is now faster and more flexible. Admins can set up accounts with just an **email address** and **role**. Other details (username, first name, and last name) are optional and hidden by default but can be filled out as needed.

* The system now **automatically handles username conflicts** by suggesting available alternatives.
*   The **user list view** and **user icons** have been updated to reflect these enhancements.\


    <figure><img src="../../../.gitbook/assets/image.png" alt=""><figcaption></figcaption></figure>



### Improved Account Protection

To enhance security and prevent accidental or malicious account removals:

* **Admins** can no longer delete or deactivate their own accounts but still can manage Standard User accounts.
* **Standard Users** cannot delete or deactivate their own or any other accounts.

This change helps maintain system stability and protects privileged accounts.

&#x20;

### Stronger Role Management Controls

We’ve introduced new safeguards to reduce the risk of privilege loss or escalation:

* Admins can no longer **downgrade themselves** to Standard User.
* Admins can still **promote Standard Users** to Admin.
* Standard Users cannot change anyone’s role.
* All role changes are now logged for better auditing and compliance.

&#x20;

### Single Sign-On (SSO) with Enhanced Security

Guard now supports **Single Sign-On (SSO)** using **encrypted SAML assertions**.\
&#x20;This ensures:

* Sensitive authentication data is securely transmitted.
* Reduced risk of data interception or tampering.
* Compliance with **federal security standards**.

&#x20;

### Bug Fixes

* **User Unlocking**: Resolved an issue with locked accounts that couldn’t be unlocked from the Settings page. Admins can now restore users' access without any errors.

### Other enhancements

* **Security & Compliance**: We have strengthened our platform’s security by implementing targeted improvements that meet stringent federal standards. These updates reduce potential attack surfaces and further enhance data protection.
* Implemented a few back-end optimizations to enhance system stability and ensure long-term maintainability, supporting a smoother and more reliable user experience.

&#x20;

***

## Guard 25.2.2 Release Notes

**Release Date: 23 July 2025**

1. Risk Assessment is goal-oriented now!

<figure><img src="../../../.gitbook/assets/image (1816).png" alt="" width="563"><figcaption></figcaption></figure>

We have grouped risks under four key Security Goals:

**Goal 1: Establish Secure Access & Identity**

Ensuring only authorized users access Salesforce, their identities are verified, and highly privileged access is governed.

**Goal 2: Harden Application & Session Security**

Protecting the Salesforce application from common web vulnerabilities, ensuring secure communication, and maintaining user session integrity.

**Goal 3: Safeguard Data & Control Exposure**

Protecting data confidentiality and integrity by managing sharing settings, controlling access to sensitive information, and limiting guest user access.

**Goal 4: Ensure Foundational Platform Integrity**

Maintaining the core security of the Salesforce platform via valid configurations for certificates, encryption, and secure external connections.

Users can see their progress towards achieving each Goal and remediate the associated risks accordingly.&#x20;

2. Custom Permission Explorer queries can be saved

Just give your query a name and definitive description, and it will be saved for your future revisits:

<figure><img src="../../../.gitbook/assets/image (1817).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../.gitbook/assets/image (1818).png" alt=""><figcaption></figcaption></figure>

3. New home page

To help navigate and get instant value, we are happy to introduce a brand-new home page:

<figure><img src="../../../.gitbook/assets/image (1819).png" alt=""><figcaption></figcaption></figure>

4. Instance version details are available now in the bottom left corner of the expanded page:

<figure><img src="../../../.gitbook/assets/image (1820).png" alt=""><figcaption></figcaption></figure>

5. New menu

To improve application navigation, in this release we have added a new menu:

<figure><img src="../../../.gitbook/assets/image (1821).png" alt=""><figcaption></figcaption></figure>

6. While we enhance its performance and functionality, we have temporarily removed the Field usage (data) tab from Data Classification UI:

<figure><img src="../../../.gitbook/assets/image (1822).png" alt=""><figcaption></figcaption></figure>

### Bug Fixes

1\.      Zoho desk link now works as expected.

2\.      User menu is no longer cut off by browser window.
