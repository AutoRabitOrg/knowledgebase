# Checkmarx One Integration

​Checkmarx One is a cloud-native application security platform designed to help organizations secure their software from the first line of code to deployment in the cloud. It offers a suite of integrated application security solutions, including static application security testing (SAST), software composition analysis (SCA), dynamic application security testing (DAST), and more.​

Integrating Checkmarx One into your Continuous Integration (CI) pipeline enhances code security by automating static code analysis. By configuring validation criteria, managing build statuses based on scan results, and utilizing Checkmarx One reporting features, development teams can maintain high code quality and address vulnerabilities promptly. This proactive approach ensures that security is embedded throughout the software development lifecycle, aligning with modern DevSecOps practices.

## **Configure the Checkmarx One Plugin in ARM.**&#x20;

From the Admin Module Navigate to My Account, Plugins. In the Static Code Analysis Category select CheckmarxOne.

<figure><img src="../../../../.gitbook/assets/Screenshot 2025-03-24 at 3.15.23 PM.png" alt=""><figcaption></figcaption></figure>

In the resulting pop-up configure the CX Server, Team Name and Credentials. You will now be able to test the connection and save the Checkmarx One Settings. Once this is saved you can continue on to configuring the criteria.

<figure><img src="../../../../.gitbook/assets/Screenshot 2025-03-24 at 3.19.11 PM.png" alt="" width="375"><figcaption></figcaption></figure>

### **Configuring Validation Criteria in CI Jobs:**

To ensure code quality and security, it's wisel to set up validation criteria for static code analysis within your CI pipeline. Validation criteria are predefined standards or conditions that must be satisfied to progress through the development pipeline, ensuring alignment with business requirements and functional correctness.

In the My Account section, scroll down to the Validation Criteria - Static Code Analysis section. Select CheckMarx One.&#x20;

<figure><img src="../../../../.gitbook/assets/Screenshot 2025-03-24 at 3.33.19 PM (1).png" alt="" width="375"><figcaption></figcaption></figure>

In priority you can choose from the following severity criteria: Critical, High, Medium, Low and Information.&#x20;

Note: The Checkmarx One Plugin introduces a new severity level of critical that is not present in the classic Checkmarx Plugin.&#x20;

<figure><img src="../../../../.gitbook/assets/Screenshot 2025-03-24 at 3.38.08 PM.png" alt=""><figcaption></figcaption></figure>

Multiple criteria can be configured based on your business requirements. \


<figure><img src="../../../../.gitbook/assets/Screenshot 2025-03-24 at 3.43.13 PM (1).png" alt="" width="563"><figcaption></figcaption></figure>

Click Save and you will then receive a notification telling you the Static Code Analysis has been saved successfully.&#x20;

### **Configure Checkmarx One for Commit Validation - Approval Steps**

​Incorporating commit validation allows for early detection of potential issues, ensuring that only high-quality code is integrated into the main codebase. This proactive approach helps maintain code integrity and reduces the risk of introducing defects into the production environment.

Select the checkbox for Checkmarx One and click Save.

<figure><img src="../../../../.gitbook/assets/Screenshot 2025-03-24 at 3.50.10 PM.png" alt="" width="374"><figcaption></figcaption></figure>

### **Configure Checkmarx One for Merge Settings**

Enabling criteria based Review Processes for merges ensures that code merges proceed only when predefined security standards are met, preventing vulnerabilities from entering the main codebase. Requiring Checkmarx scans to pass validation before merging enhances application security, allowing teams to maintain high code quality and reduce the risk of deploying insecure changes.

Select the checkbox for Checkmarx One and click Save.

<figure><img src="../../../../.gitbook/assets/Screenshot 2025-03-24 at 3.50.31 PM.png" alt="" width="338"><figcaption></figcaption></figure>

## Using Checkmarx One in EZ-Commit

Set up a new EZ-Commit with Validation of Changes (Before Commit) enabled.&#x20;

<figure><img src="../../../../.gitbook/assets/Screenshot 2025-03-24 at 4.15.43 PM.png" alt=""><figcaption></figcaption></figure>

Select the desired metadata and click Next.&#x20;

<figure><img src="../../../../.gitbook/assets/Screenshot 2025-03-24 at 4.17.33 PM.png" alt=""><figcaption></figcaption></figure>

This will bring you to the Submit for Validation Step. Since CheckMarx One has been enabled in the Admin Module you will see it is available in the list titled "Available Static Code Analysis Tools".

<figure><img src="../../../../.gitbook/assets/Screenshot 2025-03-24 at 4.27.40 PM.png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/Screenshot 2025-03-24 at 4.28.54 PM.png" alt=""><figcaption></figcaption></figure>



Finish setting up the Validation Reports and click Finish.&#x20;

<figure><img src="../../../../.gitbook/assets/Screenshot 2025-03-24 at 4.31.30 PM.png" alt=""><figcaption></figcaption></figure>

Now that the commit has been initiated you can review the results of the validation in the reports section. In the left side navigation go to the Reports Module and select Static Code Analysis from the horizontal navigation.&#x20;

<figure><img src="../../../../.gitbook/assets/Screenshot 2025-03-24 at 4.36.23 PM.png" alt=""><figcaption></figcaption></figure>

Then click on the results icon next to the report you would like to view.&#x20;

<figure><img src="../../../../.gitbook/assets/Screenshot 2025-03-24 at 4.39.38 PM.png" alt="" width="79"><figcaption></figcaption></figure>

You will now see the full report of vulnerabilities by severity. When clicking on the files on the left side you will see just the issues related to that file.&#x20;

<figure><img src="../../../../.gitbook/assets/Screenshot 2025-03-24 at 4.41.53 PM.png" alt=""><figcaption></figcaption></figure>

When you click into the vulnerability you will see the English Language description. This is a notable improvement from the classic Checkmarx Plugin, where only the code snippet was available.&#x20;

<figure><img src="../../../../.gitbook/assets/Screenshot 2025-03-24 at 4.45.27 PM.png" alt=""><figcaption></figcaption></figure>

Navigate to the Version Control Module --> Commit History to see the progress of the EZ-Commit you intiatied. In this example, the commit is in the Pending Approval stage where the Static Code Analysis and Validation Checks have been completed.

When you click into the Static Code Analysis you will see the related logs. In this case you can see both the Scan ID and Project ID that were generated.&#x20;

<figure><img src="../../../../.gitbook/assets/Screenshot 2025-03-24 at 4.52.48 PM.png" alt=""><figcaption></figcaption></figure>

When you open the Validation Checks you will see that the criteria that we configured in the Admin Module during setup were not met. This is denoted in the red text and the status is listed as Failed.&#x20;

<figure><img src="../../../../.gitbook/assets/Screenshot 2025-03-24 at 4.57.22 PM.png" alt=""><figcaption></figcaption></figure>

To see more information about the Validation, click into the Code Analysis File available in the horizontal menu.&#x20;

<figure><img src="../../../../.gitbook/assets/Screenshot 2025-03-24 at 5.03.16 PM.png" alt=""><figcaption></figcaption></figure>
