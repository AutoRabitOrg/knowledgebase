# Installing CodeScan for IntelliJ

### Learning Objectives: <a href="#learning-objectives" id="learning-objectives"></a>

After completing this unit, you'll be able to:

* [Install CodeScan IntelliJ plugin](https://knowledgebase.autorabit.com/codescan/docs/installing-codescan-for-intellij#install-the-codescan-intellij-plugin)
* [Configure CodeScan Plugin in IntelliJ](https://knowledgebase.autorabit.com/codescan/docs/installing-codescan-for-intellij#configuration-of-codescan-plugin-in-intellij)
* [Bind the project with CodeScan](https://knowledgebase.autorabit.com/codescan/docs/installing-codescan-for-intellij#bind-the-project-with-codescan)
* [Find the troubleshooting steps if you encounter IntelliJ CodeScan plugin issues](https://knowledgebase.autorabit.com/codescan/docs/installing-codescan-for-intellij#intellij-troubleshooting).

### Get Started with CodeScan IntelliJ plugin <a href="#get-started-with-codescan-intellij-plugin" id="get-started-with-codescan-intellij-plugin"></a>

The [CodeScan IntelliJ plugin](https://www.codescan.io/products/editor-plugins/) provides on-the-fly feedback to developers on bugs and quality issues. It is a fully-integrated user experience in the IntelliJ IDE.

The plugin is derived from [SonarLint™](https://www.sonarlint.org/).

{% hint style="info" %}
**Note:** As of now, CodeScan and IntelliJ plugins will not work alongside the SonarLint™ installation, so you must first uninstall SonarLint™.
{% endhint %}

#### Prerequisites <a href="#prerequisites" id="prerequisites"></a>

Make sure you have the following:

1. **IntelliJ IDEA** **2022.2** version or above
2. CodeScan for the **Cloud**:
   * Valid **enterprise** license or **trial** (cloud trial **only**—**not** available with self-hosted)
3. For **Self-Hosted (On-Premises) CodeScan**:
   * A working **SonarQube™ 9.9+ LTA** installation
   * A licensed version of **CodeScan 4.4+** plugin to get started ([more info](https://knowledgebase.autorabit.com/codescan/docs/what-is-a-codescan-license-key)) (no trial available with self-hosted/on-premises CodeScan).
4. **JDK version 17** or above
5. Latest available **Node.js LTS** version (v16 as of today)
6. Uninstall **SonarLint™** plug-ins. The CodeScan and IntelliJ plug-in will not work alongside the SonarLint™ installation.

### Install the CodeScan IntelliJ plugin <a href="#install-the-codescan-intellij-plugin" id="install-the-codescan-intellij-plugin"></a>

1. Launch the [IntelliJ IDEA](https://www.jetbrains.com/idea/download/#section=windows) app.
2. Go to **`Plugins`** available on the navigation bar on the left side of the screen.
3. Click on the **`Marketplace`** tab and search for **`CodeScan`**.
4. Click on the **`Install`** button and wait for the installation to complete (click on **`Accept`** if prompted).
5. Restart **IntelliJ** to save the changes.

### Configuration Of CodeScan Plugin in IntelliJ <a href="#configuration-of-codescan-plugin-in-intellij" id="configuration-of-codescan-plugin-in-intellij"></a>

After successfully restarting the IntelliJ platform, you will require to configure the CodeScan plugin inside IntelliJ IDEA app.

1. In the IntelliJ IDEA app, go to **`Settings`** (**`Preferences`** on Mac).

<figure><img src="../../../../.gitbook/assets/image (502).png" alt=""><figcaption></figcaption></figure>

2. Select or double click on **`Tools`** and choose **`CodeScan`** in the dropdown.
3. You will see another **`Settings`** tab under which you can see the (**+**) icon, click on it.

<figure><img src="../../../../.gitbook/assets/image (503).png" alt="" width="563"><figcaption></figcaption></figure>

{% hint style="info" %}
**Note:** Make sure you select the checkbox which says **"`Automatically trigger analysis`"**.
{% endhint %}

4. A new popup window opens where you need to give the **`Configuration Name`** and choose the **`Connection Type`** of your preference. Choose the first option if you are using CodeScan cloud default (_**`https://app.codescan.io`**_) instance, and second option if you are on a different CodeScan instance (other than _**`https://app.codescan.io`**_) or server. For example, if you're using the _CodeScan European_ instance with the CodeScan IntelliJ plugin, select the second option i.e., **`Connect to other CodeScan instances or server`** and enter _**https://app-eu.codescan.io**_ in the **`CodeScan URL`** section.

<figure><img src="../../../../.gitbook/assets/image (504).png" alt="" width="563"><figcaption></figcaption></figure>

5. Click **`Next`**. It will now redirect you to another window where you need to enter your **CodeScan token**.

{% hint style="info" %}
**Note:** If you are a _CodeScan Cloud_ user, selecting create token takes you directly to CodeScan Cloud window where you can generate the token. For more information on how to generate a new token for your account, refer to the article: [Generate a Security Token](https://knowledgebase.autorabit.com/codescan/docs/generate-a-security-token)
{% endhint %}

6. Click **`Next`** after you enter the token.
7. A new window shows up where you can choose the **`Organization`** (If you are part of multiple organizations) which you want to configure.

<figure><img src="../../../../.gitbook/assets/image (505).png" alt="" width="563"><figcaption></figcaption></figure>

8. Once you choose the **`Organization`**, click on **`Next`** and then **`Finish`**.

### Bind the project with CodeScan <a href="#bind-the-project-with-codescan" id="bind-the-project-with-codescan"></a>

1. In IntelliJ IDEA app, go to **`File > Settings > CodeScan > Project settings`**.
2. Select the checkbox which says **`Bind the project with CodeScan/CodeScan Cloud`**.

<figure><img src="../../../../.gitbook/assets/image (506).png" alt="" width="563"><figcaption></figcaption></figure>

3. Select the **`Connection`** under the **`Project binding`** that you have just setup or choose from the existing one and the project you want to bind and analyze.
4. Click on **`Apply`**, for the changes to take effect.
5. You will now be able to see the errors under the CodeScan window at the bottom in the IDE if there are any, automatically, for the file which is open.
6. If the errors don't show up immediately, reopen the **file** and you will be able to see the changes.

<figure><img src="../../../../.gitbook/assets/image (507).png" alt="" width="563"><figcaption></figcaption></figure>

### IntelliJ Troubleshooting <a href="#intellij-troubleshooting" id="intellij-troubleshooting"></a>

#### CodeScan Project binding updates gets failed <a href="#codescan-project-binding-updates-gets-failed" id="codescan-project-binding-updates-gets-failed"></a>

If the CodeScan update binding is getting failed, try disabling the VPN and antivirus, then try updating the binding again.

**If the binding successfully updates,** the error occurred due to antivirus blocking CodeScan. Add CodeScan to the list of allowed sites for the antivirus in use.

**If the binding still fails**, raise a [Support Ticket](https://support.autorabit.com/portal/en/home), including the **analyzer logs** and **verbose logs** in the attachment.

<figure><img src="../../../../.gitbook/assets/image (508).png" alt="" width="563"><figcaption></figcaption></figure>

{% hint style="info" %}
**Note:** When Verbose output is enabled, sensitive data may be exposed and care needs to be taken when sharing the logs.
{% endhint %}
