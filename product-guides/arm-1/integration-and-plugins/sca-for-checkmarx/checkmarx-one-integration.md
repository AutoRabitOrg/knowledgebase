# Checkmarx One Integration

​Checkmarx One is a cloud-native application security platform designed to help organizations secure their software from the first line of code to deployment in the cloud. It offers a suite of integrated application security solutions, including static application security testing (SAST), software composition analysis (SCA), dynamic application security testing (DAST), and more.​

Integrating Checkmarx One into your Continuous Integration (CI) pipeline enhances code security by automating static code analysis. By configuring validation criteria, managing build statuses based on scan results, and utilizing Checkmarx One reporting features, development teams can maintain high code quality and address vulnerabilities promptly. This proactive approach ensures security is embedded throughout the software development lifecycle, aligning with modern DevSecOps practices.

## **Configuring the Checkmarx One Plugin in ARM**&#x20;

From the Admin module, navigate to My Account > Plugins. In the Static Code Analysis category, select Checkmarx One.

<figure><img src="../../../../.gitbook/assets/Screenshot 2025-03-24 at 3.15.23 PM.png" alt=""><figcaption></figcaption></figure>

In the resulting pop-up, configure the CX Server, Team Name, and Credentials. You will now be able to test the connection and save the Checkmarx One settings. Once this is saved, you can continue on to configuring the criteria.

<figure><img src="../../../../.gitbook/assets/Screenshot 2025-03-24 at 3.19.11 PM.png" alt="" width="375"><figcaption></figcaption></figure>

### **Configuring Validation Criteria in CI Jobs**

To ensure code quality and security, it's wise to set up validation criteria for static code analysis within your CI pipeline. Validation criteria are predefined standards or conditions that must be satisfied to progress through the development pipeline, ensuring alignment with business requirements and functional correctness.

In the My Account section, scroll down to the Validation Criteria - Static Code Analysis section. Select Checkmarx One.&#x20;

<figure><img src="../../../../.gitbook/assets/Screenshot 2025-03-24 at 3.33.19 PM (1).png" alt="" width="375"><figcaption></figcaption></figure>

For priority, you can choose from the following severity criteria: critical, high, medium, low, and information.&#x20;

**Note**: The Checkmarx One plugin introduces a new severity level that is not present in the classic Checkmarx plugin: critical.&#x20;

<figure><img src="../../../../.gitbook/assets/Screenshot 2025-03-24 at 3.38.08 PM.png" alt=""><figcaption></figcaption></figure>

Multiple criteria can be configured based on your business requirements. <br>

<figure><img src="../../../../.gitbook/assets/Screenshot 2025-03-24 at 3.43.13 PM (1).png" alt="" width="563"><figcaption></figcaption></figure>

Click Save and you will then receive a notification telling you the Static Code Analysis has been saved successfully.&#x20;

### **Configure Checkmarx One for Commit Validation - Approval Steps**

​Incorporating commit validation allows for early detection of potential issues, ensuring that only high-quality code is integrated into the main codebase. This proactive approach helps maintain code integrity and reduces the risk of introducing defects into the production environment.

Select the checkbox for Checkmarx One and click Save.

<figure><img src="../../../../.gitbook/assets/Screenshot 2025-03-24 at 3.50.10 PM.png" alt="" width="374"><figcaption></figcaption></figure>

### **Configure Checkmarx One for Merge Settings**

Enabling criteria-based review processes for merges ensures that code merges proceed only when predefined security standards are met, preventing vulnerabilities from entering the main codebase. Requiring Checkmarx scans to pass validation before merging enhances application security, allowing teams to maintain high code quality and reduce the risk of deploying insecure changes.

Select the checkbox for Checkmarx One and click Save.

<figure><img src="../../../../.gitbook/assets/Screenshot 2025-03-24 at 3.50.31 PM.png" alt="" width="338"><figcaption></figcaption></figure>

## Using Checkmarx One in EZ-Commit

Set up a new EZ-Commit with Validation of Changes (before Commit) is enabled.&#x20;

<figure><img src="../../../../.gitbook/assets/Screenshot 2025-03-24 at 4.15.43 PM.png" alt=""><figcaption></figcaption></figure>

Select the desired metadata and click Next.&#x20;

<figure><img src="../../../../.gitbook/assets/Screenshot 2025-03-24 at 4.17.33 PM.png" alt=""><figcaption></figcaption></figure>

This will bring you to the Submit for Validation Step. Since Checkmarx One has been enabled in the Admin module, you will see it is available in the "Available Static Code Analysis Tools" list.

<figure><img src="../../../../.gitbook/assets/Screenshot 2025-03-24 at 4.27.40 PM.png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/Screenshot 2025-03-24 at 4.28.54 PM.png" alt=""><figcaption></figcaption></figure>



Finailze setting up the Validation reports and click Finish.&#x20;

<figure><img src="../../../../.gitbook/assets/Screenshot 2025-03-24 at 4.31.30 PM.png" alt=""><figcaption></figcaption></figure>

Now that the commit has been initiated, you can review the results of the validation in the reports section. In the left-side navigation, go to the Reports Module and select Static Code Analysis from the horizontal navigation.&#x20;

<figure><img src="../../../../.gitbook/assets/Screenshot 2025-03-24 at 4.36.23 PM.png" alt=""><figcaption></figcaption></figure>

Then click on the results icon next to the report you would like to view.&#x20;

<figure><img src="../../../../.gitbook/assets/Screenshot 2025-03-24 at 4.39.38 PM.png" alt="" width="79"><figcaption></figcaption></figure>

You will now see the full report of vulnerabilities by severity. When clicking on the files on the left, you will see just the issues related to that file.&#x20;

<figure><img src="../../../../.gitbook/assets/Screenshot 2025-03-24 at 4.41.53 PM.png" alt=""><figcaption></figcaption></figure>

When you click into the vulnerability, you will see the English language description. This is a notable improvement from the classic Checkmarx plugin, in which only the code snippet was available.&#x20;

<figure><img src="../../../../.gitbook/assets/Screenshot 2025-03-24 at 4.45.27 PM.png" alt=""><figcaption></figcaption></figure>

Navigate to the Version Control Module --> Commit History to see the progress of the EZ-Commit you initiated. In this example, the commit is in the Pending Approval stage, where the Static Code Analysis and Validation Checks have been completed.

When you click into the Static Code Analysis, you will see the related logs. In this case, you can see both the Scan ID and Project ID that were generated.&#x20;

<figure><img src="../../../../.gitbook/assets/Screenshot 2025-03-24 at 4.52.48 PM.png" alt=""><figcaption></figcaption></figure>

When you open the Validation Checks, you will see that the criteria we configured in the Admin module during setup were not met. This is noted in the red text and the status is listed as Failed.&#x20;

<figure><img src="../../../../.gitbook/assets/Screenshot 2025-03-24 at 4.57.22 PM.png" alt=""><figcaption></figcaption></figure>

To see more information about the Validation, click into the Code Analysis file available in the horizontal menu.&#x20;

<figure><img src="../../../../.gitbook/assets/Screenshot 2025-03-24 at 5.03.16 PM.png" alt=""><figcaption></figcaption></figure>

## Using Checkmarx One in CI Jobs

From CI Jobs, go to Create New in the upper right corner.&#x20;

<figure><img src="../../../../.gitbook/assets/Screenshot 2025-03-27 at 11.31.24 AM.png" alt=""><figcaption></figcaption></figure>

Checkmarx One is available for the following CI Job Types: Package from Salesforce, Backup to Version Control, Package from Version Control, Deploy SFDX Source from Version Control, Deploy from Salesforce Org, Deploy from Salesforce Org with a Version Control Backup, and Deploy from Version Control.&#x20;

Once you've selected the job type, navigate to the build section and select Run Static Analysis Report. In the SCA tool dropdown menu, select Checkmarx One.&#x20;

<figure><img src="../../../../.gitbook/assets/Screenshot 2025-03-27 at 11.40.55 AM.png" alt=""><figcaption></figcaption></figure>

Once Checkmarx One is selected, click the checkbox for Criteria rules for stable build. Once checked, ARM will automatically populate the criteria rules that were set in the Admin module. You have the flexibility to add or delete criteria here (which will not change the global setting in Admin). Be sure to click Save in the upper right corner if you make any changes to the criteria.&#x20;

<figure><img src="../../../../.gitbook/assets/Screenshot 2025-03-27 at 11.44.12 AM.png" alt=""><figcaption></figcaption></figure>

To see the results once a CI Job has run, navigate to the CI Job History. Click the Job Name for the job you want to explore.&#x20;

<figure><img src="../../../../.gitbook/assets/Screenshot 2025-03-27 at 11.48.40 AM.png" alt=""><figcaption></figcaption></figure>

You will then see Build Details for all the builds associated with the CI Jobs. Here you can see that this Build Status is "Build Unstable."&#x20;

<figure><img src="../../../../.gitbook/assets/Screenshot 2025-03-27 at 11.52.33 AM.png" alt=""><figcaption></figcaption></figure>

When you click into the status details, you will see the Build Log. In the Build Log, you can see which criteria were unmet. This has effectively stopped the deployment.&#x20;

<figure><img src="../../../../.gitbook/assets/Screenshot 2025-03-27 at 11.55.45 AM.png" alt=""><figcaption></figcaption></figure>

## Using Checkmarx One in Deployments

In Deployment, click New Deployment. Fill out the Deployment details and click Deploy.&#x20;

<figure><img src="../../../../.gitbook/assets/Screenshot 2025-03-27 at 12.42.22 PM.png" alt=""><figcaption></figcaption></figure>

The Deployment Settings will open automatically. Under Run Static Code Analysis, select Checkmarx One from the dropdown.&#x20;

<figure><img src="../../../../.gitbook/assets/Screenshot 2025-03-27 at 12.42.54 PM (1).png" alt=""><figcaption></figcaption></figure>

You can check the box for "Stop deployment if build does not meet global criteria." This will prevent the deployment if the Static Code Analysis fails. Entering an email address in this section will send a PDF report of the Static Code Analysis. Click OK to proceed with the deployment.&#x20;

<figure><img src="../../../../.gitbook/assets/Screenshot 2025-03-27 at 12.46.40 PM.png" alt=""><figcaption></figcaption></figure>

As in EZ-Commit, for Merge operations, ARM allow you to download the CSV file for the SCA results. Navigate to the Version Control module.&#x20;

<figure><img src="../../../../.gitbook/assets/Screenshot 2025-03-27 at 12.53.12 PM.png" alt=""><figcaption></figcaption></figure>

Select the desired repository and you will see the list of available commits.&#x20;

<figure><img src="../../../../.gitbook/assets/Screenshot 2025-03-27 at 12.56.18 PM.png" alt=""><figcaption></figcaption></figure>

Click on the Commit Name and select Code Analysis File from the horizontal menu. You will then see an option on the right side of the screen to download the Checkmarx One report.&#x20;

<figure><img src="../../../../.gitbook/assets/Screenshot 2025-03-27 at 12.58.20 PM.png" alt=""><figcaption></figcaption></figure>

The .CSV download will show you all the vulnerabilities with the associated detailed information.&#x20;

<figure><img src="../../../../.gitbook/assets/Screenshot 2025-03-27 at 1.00.37 PM.png" alt=""><figcaption></figcaption></figure>

**Note**: There are some structural differences in the file download when compared to the Checkmarx classic reports.&#x20;

