# Email Relay Activation

The **EmailRelayActivation** template enables configuration and activation of email relaying settings in Salesforce using AutoRABIT.

## Steps to Create the Email Relay Activation Template

1. Log in to your AutoRABIT account.
2. Navigate to the **Env. Pro.** module.
3. Click **Create New Template**.
4. Open the **Create Unsupported Metadata Template** tab.
5. Provide a **template name** and a **short description**.
6. Select the **EmailRelayActivation** checkbox under **Manage Email Relay Activation**.
7. Click **Add**.
8.  On the next screen:

    * A **Test Case Name** appears automatically.
    * Click **Add** to enter custom test data.
    * Complete the following fields:
      * **Email Host**
      * **Port**
      * **TLS setting**
      * **Restrict Relay to Domain**
    * Enable the options:
      * **Restrict relay**
      * **Enable Email relaying**

    ![Email Relay Activation Settings](<../../../../../.gitbook/assets/image (74).png>)

    * Click **Save** to finalize the configuration.
9. Click **Save** again to complete the template creation.
10. You will be redirected to the **Environment Provisioning History** screen.
11. Click **Run** to execute the template on your destination org.
12. Select your **destination org** from the dropdown and specify the **email address(es)** for notifications.
13. In the **Post Deployment Steps**, choose the test cases you recently created.
14. Refer to the **View History** page for a detailed report of the operation.
