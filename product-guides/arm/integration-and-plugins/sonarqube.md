# Sonarqube

### SonarQube: Overview <a href="#sonarqube-overview" id="sonarqube-overview"></a>

SonarQube is an automatic code review tool to detect bugs, vulnerabilities, and code smells in your code. It can integrate with your existing workflow to enable continuous code inspection across your project branches and pull requests.

### Setting Up SonarQube in AutoRABIT <a href="#setting-up-sonarqube-in-autorabit" id="setting-up-sonarqube-in-autorabit"></a>

If you want to integrate all the functionality included in your **SonarQube** license with AutoRABIT, you need to integrate SonarQube as a plugin with your AutoRABIT account. However, it does require some steps in SonarQube as well as in your AutoRABIT account to get it configured.

#### Step 1: Generate a SonarQube Token <a href="#step-1-generate-a-sonarqube-token" id="step-1-generate-a-sonarqube-token"></a>

1. Log in to your SonarQube instance.
2. Go to **User > My Account > Security**. Your existing tokens are listed here, each with a **Revoke** button.
3. The form at the bottom of the page allows you to generate new tokens. Once you click the **Generate** button, you will see the token value. Copy it immediately; once you dismiss the notification you will not be able to retrieve it.
4. This token will be used while storing your credential with AutoRABIT.&#x20;

#### Step 2: Store your SonarQube's credential in AutoRABIT <a href="#step-2-store-your-sonarqubes-credential-in-autorabit" id="step-2-store-your-sonarqubes-credential-in-autorabit"></a>

This is an initial step where your SonarQube credential such as username and password is stored in AutoRABIT.

1. Log in to your AutoRABIT account.
2. Hover your mouse over the **Admin** module and click on the **Credentials** tab.
3. Next, click on **Create Credential** from the right navigation bar.
4. On the next pop-up screen, give a **Credential name**.
5. Choose the Credential Type as '**User name with Password'.**
6. Choose your **Credential Scope**
   * **Global**: Credential can be accessed within the team
   * &#x20;**Private**: Credential for private usage&#x20;
7. Enter your SonarQube account's username. For **password**, use the copied token as mentioned in _**Step 1: Create a SonarQube Token**_
8. Please double-check that you use your SonarQube username instead of the email address that you use to log in to SonarQube.
9. Click **Save**.

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1616325381996.png" alt="" width="375"><figcaption></figcaption></figure>

#### Step 3: Integrate sonarQube with AutoRABIT <a href="#step-3-integrate-sonarqube-with-autorabit" id="step-3-integrate-sonarqube-with-autorabit"></a>

If you're logged out from your account, log in again into AutoRABIT with your credentials.

1. Go to **Admin > My Account** section.
2. Go to the **Plugins** section.
3.  Check the **SonarQube** checkbox under **Static Code Analysis**.\


    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1664796628363.png" alt=""><figcaption></figcaption></figure>
4. Fill in the below details:
   * Enter the SonarQube **hosted URL**. For the SonarQube cloud version use **https://sonarcloud.io**
   * Choose the **Host Type** i.e., _Cloud_ or _On-premise_. For SonarQube hosted on Cloud, you need to add the **Organization Key.**&#x20;
   * Select your **Credential** from the drop-down.
   * Click **Test Connection** to check if the connection has been authenticated or not. A success message is displayed after the authentication is completed.
   *   Click **Save**.\


       <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1664796687941.png" alt="" width="375"><figcaption></figcaption></figure>
5. Click on **Save** once again and you are all set with SonarQube integration.

#### Step 4: Setting SonarQube Global Criteria Settings <a href="#step-4-setting-sonarqube-global-criteria-settings" id="step-4-setting-sonarqube-global-criteria-settings"></a>

You can now set the global Quality Gate criteria to enforce SonarQube Static code analysis tool across CI Jobs, Deployment, and gated Commits. The Quality Gate gives you a Pass or Fail rating for your project in the SonarQube tool depending on the metrics you have provided. Based on the criteria configured in AutoRABIT and if it matches in your SonarQube account, the process gets aborted.

1. Go to **Admin > My Account** section.
2. Next, navigate to the **Validation Criteria-Static Code Analysis** section.
3. Select the **Enable** checkbox.
4.  Enable the **SonarQube** checkbox and assign the Quality Gate status for all your projects. By default, it is set to **ERROR**, however, you can choose the criteria of your own. If the Quality Gate matches with the status assigned to the projects on your SonarQube tool, the validation process gets failed and the build aborts.\


    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1664796890806.png" alt="" width="563"><figcaption></figcaption></figure>
5. Click **Save**.
6. Next, go to the next section i.e., **Commit Validation - Approval Settings**. In this section, you can allow the SonarQube tool to identifying potential software quality issues before the code moves to production and abort the commit process if the Quality Gate set earlier matches with the status in the SonarQube application.&#x20;
7. Select the checkbox: **Enable criteria based Review Process**&#x20;
8. Enable the **Should pass validation criteria for Static Code Analysis** checkbox, select the below checkboxes:
   * **SonarQube**
   *   **Auto reject commit process if the criteria are not met**\


       <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1664796960434.png" alt=""><figcaption></figcaption></figure>
9. Click **Save**.
10. Similar to SonarQube criteria globally configured in AutoRABIT for Commit operation, you can even set the same for Merge Process. Go to the next section: **Merge Settings**
11. Select the **Enable criteria-based Review Process** checkbox.
12. Under **Should pass validation criteria for Static Code Analysis**, select the **SonarQube** checkbox.
13. Finally, click on **Save**.
