# Jenkins

### What is Jenkins?&#x20;

Jenkins is an open-source Continuous Integration server written in Java for orchestrating a chain of actions to achieve the Continuous Integration process in an automated fashion. Jenkins supports the complete development life cycle of software from building, testing, documenting the software, deploying, and other software development life cycle stages.

### How to trigger Jenkins job in CI/CD?

Trigger a Jenkins job through CI jobs in AutoRABIT. To do so,

1.  Go to the **New CI Job** screen.\


    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1664797023189.png" alt=""><figcaption></figcaption></figure>
2. Choose one of the CI Job processes from the below list:
   1. _Deploy SFDX source from Version Control_
   2. _Deploy from Salesforce Org_
   3. &#x20;_Deploy from Salesforce Org with a Version Control backup_
   4. _Deploy from Version Control_
   5. _Install an Unlocked Package from a Version Control Branch_
3. Go to the **Deploy** section.
4. Select the **On Successful Deployment** checkbox. This feature allows you to run various jobs once the CI job is successfully deployed.&#x20;
5.  Select the **Trigger Jenkins Job** checkbox. This will trigger Jenkins jobs on successful deployment.\


    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1664797199606.png" alt="" width="563"><figcaption></figcaption></figure>
6. Fill in the below details:
   1.  In the **URL** field, enter the _full URL of the Jenkins_. You can either specify **http://localhost:8080** (when connecting from your machine and assuming that you started Jenkins on port 8080) or **http://\<machine\_hostname>:8080** when connecting from anywhere.)

       <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1623435606270.png" alt=""><figcaption></figcaption></figure>
   2.  In the **Job Name** field, enter the _name of the project_ of the current build. In our example, we're going to name the job e.g. **"HelloWorld"**.

       <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1623435661572.png" alt=""><figcaption></figcaption></figure>
   3.  For the **Job URL** field, enter the _URL path_ of your project or job (_http://\<machine\_hostname>:8080/**\<Job URL>**/_). For example: **"job/Helloworld"**.

       <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1623435757364.png" alt=""><figcaption></figcaption></figure>
   4.  Enter the _user credential_ for whom the job is being triggered in the **User ID** field.

       <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1623435811854.png" alt=""><figcaption></figcaption></figure>
   5.  Enter the **API token key** available for your job. Navigate to your **Profile > Configure** to view your API Token.

       <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1623435900240.png" alt=""><figcaption></figcaption></figure>
   6. Jenkins has support for the **parameterized build** as well. Enter the _parameter name_ with the parameter value in this field. To add multiple parameters, click on ![](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1623435972842.png) sign and enter the parameter value.

Important Note:Ensure your Jenkins has been configured to allow URL parameters. To be able to access the parameter in your Jenkins job do the following:

* Go to your project configuration, then go to the **General** tab. Select **"This project is parameterized"**.
* Click on **Add Parameter**. From the list of parameters available, select your desired parameter(s) and enter the required parameter values.
* Click **Save**. You should now have your parameters passed to Jenkins.
