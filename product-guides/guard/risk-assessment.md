# Risk Assessment

## Overview

The **Risk Assessment** feature provides a comprehensive overview of your Salesforce organization’s security posture. It analyzes your orgs, checks security settings, and identifies areas of risk—helping you stay compliant and mitigate potential vulnerabilities.

With this tool, you can quickly see where improvements are needed, prioritize critical risks, and maintain a strong security baseline across all environments.

### Getting Started

#### Home Page

On the Risk Assessment home page, you’ll see:

* **Overall Compliance Score**: A summary of your security status across all orgs.
* **Filters for Focus Areas**:
  * **Critical Orgs**: Environments with a high number of severe risks requiring immediate action.
  * **Quick Wins**: Risk factors that can be auto-resolved quickly.
  * **Compliant Orgs**: Salesforce orgs already performing at a high compliance level.

**Tip:** You can toggle between **Card View** and **Table View** for flexible navigation and filtering.

#### Org-Level Health Evaluation

When you select a specific Salesforce org, you can access:

* **Filtered Views**: Narrow results by **Relevant Regulations**
* **Compliance Goals**: Track progress toward key objectives:
  * Establish secure access and identity
  * Harden applications and safeguard data
  * Control exposure
  * Ensure platform integrity

Scrolling further reveals a detailed list of all detected risks for that org.

<figure><img src="../../.gitbook/assets/image (2047).png" alt="Security Goals"><figcaption><p>Security Goals</p></figcaption></figure>

#### Risk Details

Each identified risk is categorized as either:

* **Unresolved**: Requires your action
* **Resolved**: Setting is compliant

Risks are also categorized by two severity levels:

* **Critical**
* **Warning**

For each risk, you can:

* Navigate through risks using the **carousel view**.
* Open the **detail page** for in-depth information and remediation guidance.
* View a detailed **summary** including the description, business impact, and how to fix it.

<figure><img src="../../.gitbook/assets/image (2048).png" alt=""><figcaption><p>Security Setting Details</p></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (2049).png" alt=""><figcaption><p>Risk Details</p></figcaption></figure>

### Acting on Risks

With Risk Assessment insights, you can take recommended steps to remediate issues, strengthen security, and ensure compliance across your Salesforce environments. The tool’s structured breakdown makes it easy to prioritize critical concerns while resolving smaller issues efficiently.

## How the Risk Assessment Works&#x20;

### Baseline Comparison&#x20;

* AutoRABIT Guard compares your Salesforce org’s security settings against a predefined baseline (Salesforce's Health Check or a custom XML, if configured). Any misaligned settings are highlighted as risks.&#x20;

### Triggering the Scan&#x20;

The Risk Assessment scan is triggered in real time whenever:&#x20;

* The Risk Assessment page is loaded.&#x20;
* A new Salesforce org is registered with Guard.&#x20;
* The page is refreshed, executing the scan again.&#x20;

### Where the Baseline Is Stored&#x20;

The scan is always performed live, and the results are stored in memory, not in a database. The scan is not automatic—it’s executed when you actively view it.&#x20;

### How the Baseline Is Determined&#x20;

The baseline (or recommended values) for security settings comes from Salesforce's Health Check. Salesforce allows users to define custom baseline configurations by uploading an XML file. If no custom XML is uploaded, the default Salesforce Health Check baseline is used.&#x20;

**Example of a custom XML configuration**:&#x20;

`<baseline name="SFDC recommended" developerName="SFDCRecommended">` \
&#x20;   `<highRiskSecuritySettings>` \
&#x20;       `<booleanSetting name="SessionSettings.lockSessionsToDomain" compliant="true" nonCompliant="critical"/>` \
&#x20;       `<numericRangeSetting name="FileUploadAndDownloadSecurity.hybridSecurityRiskFileTypes" compliant="0.0" warning="0.5"/>` \
&#x20;   `</highRiskSecuritySettings>` \
&#x20;   `<mediumRiskSecuritySettings>` \
&#x20;       `<booleanSetting name="PasswordPolicies.minOneDayPasswordLifetime" compliant="true" nonCompliant="critical"/>` \
&#x20;   `</mediumRiskSecuritySettings>` \
`</baseline>`&#x20;

## Customizing the Risk Assessment&#x20;

Customers can configure the Risk Assessment by uploading a custom XML to Salesforce. For example, if a customer wishes to treat certain settings (like _PasswordPolicies.minPasswordLength_) as a warning rather than critical, they can modify the custom XML.&#x20;

## Auto-Resolve Functionality&#x20;

Certain risks, such as _PasswordPolicies_ and _SessionSettings_, can be automatically resolved with a single click. These settings are updated via the Tooling API, not the SecurityHealthCheckRisks API.&#x20;

Settings that can be auto-resolved:&#x20;

* Password Policies (e.g., min password length, max login attempts)&#x20;
* Session Settings (e.g., session timeout)&#x20;

Other settings, like sharing settings or file upload configurations, require manual review as they involve additional decision-making.&#x20;

## Understanding the Risk Assessment Score&#x20;

The Risk Assessment feature calculates an overall score based on the number of settings that are noncompliant. The score is determined by the following formula:&#x20;

* Compliance Score = (Number of compliant settings) / (Total number of settings)&#x20;

This score is a simple percentage, with no weighting applied to individual settings. In future releases, we may introduce weighted scoring for certain critical settings.&#x20;

### Why the Score May Differ from Salesforce Health Check&#x20;

While the Risk Assessment is based on Salesforce Health Check, there are a few reasons the scores might differ:&#x20;

* We don’t use weighted scores, so each setting is treated equally.&#x20;
* The Risk Assessment includes additional settings that are not part of the Salesforce Health Check, which can affect the score.&#x20;

## Example Scenario

#### 1. Connect Your Salesforce Org&#x20;

Once your Salesforce org is connected to AutoRABIT Guard, the Risk Assessment will automatically perform a scan.&#x20;

#### 2. Review the Results&#x20;

The results are presented in an easy-to-read table with the following columns:&#x20;

* **Setting**: The security setting being evaluated (e.g., PasswordPolicies.minPasswordLength).&#x20;
* **Category**: The category the setting belongs to (e.g., password policies, session settings).&#x20;
* **Recommended Value**: The value that aligns with the security baseline.&#x20;
* **Current Value in Org**: The actual value currently set in your Salesforce org.&#x20;
* **Severity:** Critical/Warning
* **Status**: Whether the setting meets the baseline or requires action.&#x20;

#### 3. Take Action&#x20;

* **Auto-Fix**: Click the “Auto-Fix” button to resolve the issue automatically (where it's applicable).&#x20;
* **Manual Fixes**: Follow the provided guidance to make manual updates to your Salesforce org.&#x20;

#### 4. Reassess Anytime&#x20;

You can re-run the Risk Assessment at any time to ensure your org remains aligned with the security baseline.&#x20;

## Why It Matters&#x20;

The Risk Assessment helps you:&#x20;

* **Quickly identify and resolve vulnerabilities**: Address security risks before they become issues.&#x20;
* **Maintain compliance with security best practices**: Keep your Salesforce org secure and compliant.&#x20;
* **Save time by automating fixes**: Automatically resolve certain security issues with a single click.&#x20;
* **Centralize all security insights**: View all your security data in one place to simplify management and decision-making.&#x20;

By using the Risk Assessment feature in AutoRABIT Guard, you ensure your Salesforce org remains secure and aligned with both Salesforce’s best practices and your organization’s security policies.&#x20;

&#x20;
