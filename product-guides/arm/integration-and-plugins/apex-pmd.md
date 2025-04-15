# Apex PMD

### What is PMD?  <a href="#what-is-pmd" id="what-is-pmd"></a>

PMD stands for Programming Mistake Detector. It is a source code analyzer that finds common mistakes in your code, like unused variables, if-else statements without braces, naming conventions of methods, SOQL in loops, and many more. It also includes CPD (for Copy/Paste Detector), which finds duplicate code in your files and makes you aware of improvements to make your code reusable.

Supported Version: ApexPMD upgraded to the latest 6.49 version.

### Setting up PMD in AutoRABIT <a href="#setting-up-pmd-in-autorabit" id="setting-up-pmd-in-autorabit"></a>

1. Log in to your AutoRABIT account.
2. From the AutoRABIT home page, hover your mouse over the **Admin** module and select the option: **My Account.**

<figure><img src="../../../.gitbook/assets/image (865).png" alt="" width="306"><figcaption></figcaption></figure>

3. Go to the **Plugins** section.
4. Click on the **ApexPMD** checkbox under **Static Code Analysis**.
5. If you do have separate Apex PMD rules that you would like to carry out in AutoRABIT, you can upload the same. Click **Browse** to search for the file in your local machine. Usually, the file is in **XML** format. Once done, click **Upload**.
6. If the user has not uploaded any rules file, AutoRABIT will use the default Apex PMD rules file. However, you can update some of the fields in it.&#x20;
7. Download the default rule set in your local machine using the link as shown below.

<figure><img src="../../../.gitbook/assets/image (1545).png" alt=""><figcaption></figcaption></figure>

8. Edit the content and upload it once again.
9. Click **Save** and you are all set with ApexPMD Integration.

{% hint style="info" %}
**Point to Remember:** The current build of AutoRABIT supports Apex PMD with _Apex Classes, Apex Visualforce pages, and Triggers_.
{% endhint %}

### Running PMD during a CI Job <a href="#running-pmd-during-ci-job" id="running-pmd-during-ci-job"></a>

1. Go to the **New CI Job** screen.

<figure><img src="../../../.gitbook/assets/image (867).png" alt=""><figcaption></figcaption></figure>

2. Select any one of the criteria for your CI job. For example, **Deploy from Salesforce Org.**

<figure><img src="../../../.gitbook/assets/image (868).png" alt=""><figcaption></figcaption></figure>

3. Enter a descriptive name in the **CI Job Name** field.
4. In the **Build** section, select your Salesforce Org or Version Control Repo/Branch.
5. Select the **Run Static Analysis Report** checkbox and choose **Apex PMD**.

<figure><img src="../../../.gitbook/assets/image (869).png" alt=""><figcaption></figcaption></figure>

6. AutoRABIT allows you to set the criteria for running the ApexPMD SCA tool. This means running for all the apex classes or stating the period from when it will run. Also, you can set the priority, which means if the priority set is not achieved, the current build is unstable. This helps us in reporting the code quality of the developer team.
7. Fill in the remaining fields as per your requirements and click on **Save**.
8. Once the build is triggered for your CI Job, the SCA report can be found under the **Build Details** section on the **CI Job Result** page.

<figure><img src="../../../.gitbook/assets/image (870).png" alt=""><figcaption></figcaption></figure>

#### **PMD Report**

<figure><img src="../../../.gitbook/assets/image (871).png" alt=""><figcaption></figcaption></figure>

#### **PMD Report with Violations**

<figure><img src="../../../.gitbook/assets/image (872).png" alt=""><figcaption></figcaption></figure>

### FAQs

#### I see some plugins require keys. Is this a license issue or can we get these keys and use the Static Code Analysis feature? <a href="#i-see-from-the-instructions-that-these-plugins-require-some-keys-is-it-a-license-issue-or-can-we-get" id="i-see-from-the-instructions-that-these-plugins-require-some-keys-is-it-a-license-issue-or-can-we-get"></a>

You can use Apex PMD and execute SCA without having to obtain a license for it. The other plugins are third-party tools and they require the license.

* [SCA for Checkmarx](https://knowledgebase.autorabit.com/product-guides/arm/integration-and-plugins/sca-for-checkmarx)
* [SCA for Apex PMD](https://knowledgebase.autorabit.com/product-guides/arm/integration-and-plugins/apex-pmd)
* [SCA for SonarQube](https://knowledgebase.autorabit.com/product-guides/arm/integration-and-plugins/sonarqube)
