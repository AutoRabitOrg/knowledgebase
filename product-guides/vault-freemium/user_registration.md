# User\_Registration

## AutoRABIT Vault Freemium Registration User Guide

End-to-end workflow for creating and verifying a AutoRABIT Vault freemium account

## Purpose

This guide explains the AutoRABIT Vault freemium registration workflow. The flow starts from the AutoRABIT Vault welcome page, continues through account detail submission and agreement confirmation, and completes after OTP verification from the registered email address.

| **Workflow stage**               | **Outcome**                                                             |
| -------------------------------- | ----------------------------------------------------------------------- |
| **Welcome and access selection** | The registration flow begins from the AutoRABIT Vault welcome page.     |
| **Account information**          | Required details are entered for the freemium account.                  |
| **Agreement confirmation**       | The agreement is reviewed and accepted before OTP generation.           |
| **Email verification**           | The authentication code received through email is entered and verified. |

The AutoRABIT Vault welcome page provides access to sign-in and registration actions. The email field and Send OTP action support existing account access, while the Sign up link starts the freemium registration journey for a new account.

![](<../../.gitbook/assets/Unknown image>)

Registration starts from the AutoRABIT Vault welcome page.

Selecting Sign up opens the registration form. The form collects the information required to create the freemium account and associate it with the intended organization.

![](<../../.gitbook/assets/Unknown image (1)>)

The Sign up action opens the account registration flow.

The registration form captures the first name, last name, email address, organization, and region. The Region field provides the available region options and must be selected before registration can continue.

![](<../../.gitbook/assets/Unknown image (2)>)

The registration form captures account, organization, and region information.

After the required details are entered, the Region selection is retained on the form. The agreement confirmation remains required before the Generate OTP action can be used.

![](<../../.gitbook/assets/Unknown image (3)>)

The selected region is retained with the entered registration details.

The agreement checkbox confirms acceptance of the applicable Terms and Conditions. The confirmation must be selected before OTP generation is enabled.

![](<../../.gitbook/assets/Unknown image (4)>)

The agreement checkbox enables progression toward OTP generation.

After the agreement is accepted, the Generate OTP action is used to submit the registration details. AutoRABIT Vault starts the OTP generation process and shows the request in progress.

![](<../../.gitbook/assets/Unknown image (5)>)

Generate OTP submits the registration request after agreement confirmation.

The Terms and Conditions link opens the agreement page for review. This allows the agreement details to be checked before returning to the registration form.

![](<../../.gitbook/assets/Unknown image (6)>)

The agreement page opens from the Terms and Conditions link.

![](<../../.gitbook/assets/Unknown image (7)>)

AutoRABIT Vault displays the OTP generation request in progress.

### Registration Email Notifications

During the Freemium registration workflow, AutoRABIT Vault sends email notifications to support account verification and trial activation. These emails provide the required verification code, confirm successful registration, and share the trial access details required to begin using AutoRABIT Vault.

#### Verification Code Email

After the registration details are submitted and **Generate OTP** is selected, AutoRABIT Vault sends a verification email to the registered email address. The email is sent from **No Reply Freemium** and uses the subject **Your** AutoRABIT Vault **Verification Code**.

The email contains the **Login OTP**, which is required to complete account verification on the registration screen. The OTP must be entered in the verification field before the registration can proceed. This step confirms that the registered email address is valid and accessible.

The verification email also includes the standard AutoRABIT email footer, support contact information, and a note indicating that the message is auto-generated.

![](<../../.gitbook/assets/Unknown image (8)>)

#### Trial Activation Email

After the OTP is validated successfully, AutoRABIT Vault completes the registration and sends a trial activation email. The email is sent from **No Reply Freemium** and uses the subject **Welcome to** AutoRABIT Vault **– Your Free Trial is Active!**

The email confirms that the registration is complete and that the account is active. It also indicates the next step in the onboarding flow, where a **Source Org** must be added from the AutoRABIT Vault dashboard to begin configuring backup and related activities.

![](<../../.gitbook/assets/Unknown image (9)>)

![](<../../.gitbook/assets/Unknown image (10)>)

The activation email includes the following access details:

| Detail                      | Description                                                                        |
| --------------------------- | ---------------------------------------------------------------------------------- |
| **Subscription Start Date** | Displays the date on which the Freemium trial becomes active.                      |
| **Trial Period**            | Displays the total duration of the Freemium trial.                                 |
| **Trial Expiry Date**       | Displays the date on which the trial access expires.                               |
| **Email**                   | Displays the registered email address associated with the Freemium account.        |
| **Storage Location**        | Displays the configured storage region for the trial account.                      |
| **Instance URL**            | Provides the AutoRABIT Vault instance URL used to access the Freemium environment. |
| **Master Code**             | Provides the account-level code used for verification support where applicable.    |

The email also lists the Freemium trial limits configured for the account:

| Limit                             | Description                                                    |
| --------------------------------- | -------------------------------------------------------------- |
| **Storage**                       | Displays the storage capacity available for the trial.         |
| **Files**                         | Displays the file storage capacity available for the trial.    |
| **Users**                         | Displays the number of admin users allowed in the trial.       |
| **Environments**                  | Displays the number of Salesforce orgs that can be configured. |
| **Backup Configs**                | Displays the number of backup configurations allowed.          |
| **Backup Jobs**                   | Displays the number of backup jobs supported during the trial. |
| **Restore Jobs**                  | Displays the number of restore jobs allowed.                   |
| **Replicate / Data Seeding Jobs** | Displays the number of replicate or data seeding jobs allowed. |
| **Retention Period**              | Displays the retention duration available for trial data.      |

The email confirms that usage and limits can be monitored from the AutoRABIT Vault dashboard. It also includes the standard AutoRABIT footer, support contact information, and the auto-generated email note.

## Complete OTP Verification

The OTP Verification page accepts the code received in the registered email inbox. Once the code is entered, Verify OTP completes the validation process and confirms the registration flow.

![](<../../.gitbook/assets/Unknown image (11)>)

The OTP Verification page validates the authentication code.

## Result

After successful OTP verification, the freemium account registration is completed. The account can then proceed to the next applicable onboarding step within AutoRABIT Vault.

| \*\*Note:\*\*OTP verification must be completed using the code sent to the registered email address. The code should be entered before it expires or becomes invalid. |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
