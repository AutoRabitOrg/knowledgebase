# Jenkins

### What is Jenkins?&#x20;

Jenkins is an open-source Continuous Integration server written in Java for orchestrating a chain of actions to achieve the Continuous Integration process in an automated fashion. Jenkins supports the complete development life cycle of software from building, testing, documenting the software, deploying, and other software development life cycle stages.

### How to trigger Jenkins job in CI/CD?

Trigger a Jenkins job through CI jobs in AutoRABIT. To do so,

1. Go to the **New CI Job** screen.

<figure><img src="../../../.gitbook/assets/image (879).png" alt=""><figcaption></figcaption></figure>

2. Choose one of the CI Job processes from the below list:
   * _Deploy SFDX source from Version Control_
   * _Deploy from Salesforce Org_
   * &#x20;_Deploy from Salesforce Org with a Version Control backup_
   * _Deploy from Version Control_
   * _Install an Unlocked Package from a Version Control Branch_
3. Go to the **Deploy** section.
4. Select the **On Successful Deployment** checkbox. This feature allows you to run various jobs once the CI job is successfully deployed.&#x20;
5. Select the **Trigger Jenkins Job** checkbox. This will trigger Jenkins jobs on successful deployment.

<figure><img src="../../../.gitbook/assets/image (880).png" alt="" width="563"><figcaption></figcaption></figure>

6.  Fill in the below details:

    * In the **URL** field, enter the _full URL of the Jenkins_. You can either specify **http://localhost:8080** (when connecting from your machine and assuming that you started Jenkins on port 8080 or **http://\<machine\_hostname>:8080** when connecting from anywhere.)

    <figure><img src="../../../.gitbook/assets/image (881).png" alt=""><figcaption></figcaption></figure>

    * In the **Job Name** field, enter the _name of the project_ of the current build. In our example, we're going to name the job e.g. **"HelloWorld"**.

    <figure><img src="../../../.gitbook/assets/image (882).png" alt=""><figcaption></figcaption></figure>

    * For the **Job URL** field, enter the _URL path_ of your project or job (_http://\<machine\_hostname>:8080/**\<Job URL>**/_). For example: **"job/Helloworld"**.

    <figure><img src="../../../.gitbook/assets/image (883).png" alt=""><figcaption></figcaption></figure>

    * Enter the _user credential_ for whom the job is being triggered in the **User ID** field.

    <figure><img src="../../../.gitbook/assets/image (884).png" alt=""><figcaption></figcaption></figure>

    * Enter the **API token key** available for your job. Navigate to your **Profile > Configure** to view your API Token.

    <figure><img src="../../../.gitbook/assets/image (885).png" alt=""><figcaption></figcaption></figure>

    * Jenkins has support for the **parameterized build** as well. Enter the _parameter name_ with the parameter value in this field. To add multiple parameters, click on![](<../../../.gitbook/assets/image (878).png>)sign and enter the parameter value.

{% hint style="info" %}
**Important Note:**&#x20;

Ensure your Jenkins has been configured to allow URL parameters. To be able to access the parameter in your Jenkins job do the following:

* Go to your project configuration, then go to the **General** tab. Select **"This project is parameterized"**.
* Click on **Add Parameter**. From the list of parameters available, select your desired parameter(s) and enter the required parameter values.
* Click **Save**. You should now have your parameters passed to Jenkins.
{% endhint %}
