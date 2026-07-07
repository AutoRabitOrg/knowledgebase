# User\_Registration

### **Vault Freemium User Registration**

#### User Guide

| **Product**      | Vault Freemium by AutoRABIT                                                                              |
| ---------------- | -------------------------------------------------------------------------------------------------------- |
| **Feature Area** | Freemium Registration and OTP Verification                                                               |
| **Audience**     | Trial account registrants and administrators                                                             |
| **Purpose**      | Explains the end-to-end registration journey for creating and activating a Vault Freemium trial account. |

## Overview

The Vault Freemium registration flow enables a new trial account to be created and activated through email-based OTP verification. The journey starts from the Vault login page, continues through the sign-up form, validates the entered details, sends a one-time password, and completes with account activation and trial access details.

The registration experience highlights core trial conditions throughout the flow, including no credit card requirement, 14-day retention, and the option to upgrade when required.

![](<../../.gitbook/assets/Unknown image (22)>)

## Start Registration from the Login Page

The Vault login page opens with email-based sign-in. For an existing account, an Email ID can be entered and Send OTP starts the login process. For a new Freemium trial, Sign up opens the registration form.

![](<../../.gitbook/assets/Unknown image (23)>)

## Enter Trial Registration Details

The sign-up form captures the information required to create a Freemium trial account. The form includes First Name, Last Name, Email ID, Organization, and Region / Location. The Generate OTP action remains unavailable until the required registration details are completed and validated.

| **Field**         | **Expected behavior**                                                                 |
| ----------------- | ------------------------------------------------------------------------------------- |
| First Name        | Captures the registrant first name for account creation and communication.            |
| Last Name         | Captures the registrant last name for account creation and communication.             |
| Email ID          | Receives the verification OTP and becomes the registered email for the trial account. |
| Organization      | Associates the trial account with the organization entered during registration.       |
| Region / Location | Defines the storage location and instance region for the trial account.               |

The enterprise-safe trial note confirms that trial data is encrypted and access-controlled. The account uses the same infrastructure approach as enterprise customers.

![](<../../.gitbook/assets/Unknown image (24)>)

## Select Region / Location

Region / Location is selected from the available options. Each option indicates the region health status. After a valid region is selected and the remaining required fields are complete, Generate OTP becomes available.

![](<../../.gitbook/assets/Unknown image (25)>)

## Generate the Verification OTP

After the registration details are complete, Generate OTP starts OTP generation for the entered Email ID. The action changes to Sending... while the request is processed, preventing duplicate submission during OTP delivery.

![](<../../.gitbook/assets/Unknown image (26)>)

![](<../../.gitbook/assets/Unknown image (27)>)

## Receive Registration Emails

Vault sends an OTP email to the registered Email ID. The email contains the one-time password required to complete verification. After registration is completed successfully, a welcome email confirms that the trial account is active and provides the access details required to continue.

| **Email**     | **Purpose**                                                                                                                                                     |
| ------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| OTP email     | Provides the verification code required to complete the sign-up process.                                                                                        |
| Welcome email | Confirms account activation and provides trial access details, including the instance URL, storage location, subscription dates, Master Code, and trial limits. |

{% hint style="info" %}
Note: The Master Code must be retained securely. It supports account recovery or verification scenarios where applicable.
{% endhint %}

## Complete OTP Verification

The OTP Verification page displays the registered Email ID and provides Change Email ID when the email address must be corrected before verification. The OTP fields accept the code received through email. The timer indicates when Resend code becomes available.

After the OTP is entered, the verification action moves to Verifying OTP while Vault validates the code. A successful validation activates the Freemium trial account and allows the registration journey to proceed to the active trial experience.

## Result

After successful verification, the Freemium trial account is active. The welcome email identifies the next step as adding a Source Org from the dashboard to begin configuring backup and related Vault capabilities.

## System Behavior Summary

| **Scenario**                    | **System behavior**                                                                                 |
| ------------------------------- | --------------------------------------------------------------------------------------------------- |
| Existing account path           | Log in returns to the login flow for accounts that already exist.                                   |
| Incomplete registration details | Generate OTP remains unavailable until required details are completed and validated.                |
| OTP generation in progress      | The action changes to Sending... while Vault processes the OTP request.                             |
| OTP delivery                    | The verification code is sent to the registered Email ID.                                           |
| Email correction                | Change Email ID allows the registration email to be corrected before OTP verification is completed. |
| OTP resend                      | Resend code becomes available after the timer allows another OTP request.                           |
| Successful verification         | The trial account is activated and the welcome email provides access details and trial limits.      |
