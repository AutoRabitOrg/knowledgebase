---
hidden: true
---

# Live Data Masking

**Live Data Masking** enables on-the-fly data masking within Salesforce, eliminating the need to build full configurations when masking is required for specific object data. It supports both the use and reuse of existing **Global Rules** and the creation of **Local Rules** for targeted masking. When both global and local rules are defined for the same fields and conditions, local rules take precedence. This approach also supports rule reuse through **cloning**, enhancing flexibility and efficiency in data protection.

**Step-By-Step Guide**:

1. Observe the new module “Live Data Masking” and click on the “JOB CONFIG” to land on the “Live Data Masking Config” creation screen.
2. Observe the “Salesforce Orgs” and the NEW CONFIG creation options available on this screen
3. The drop-down “Salesforce Orgs” contains the list of ORGs available for selection.
4. Select the required ORG at the “Salesforce Orgs” drop-down.
5.  Observe the following screen for the first time creation of the “Masking Rule Config” or first-time creation of “Masking Rule Config” on any ORG.



    ![](../../../../.gitbook/assets/0.png)
6. Once the object is selected, continue with the “Masking Config” creation.

![](../../../../.gitbook/assets/1.png)

1. Click on the “NEW CONFIG” button to initiate the config creation.
2. Now, the flow will navigate to the “Object Info” section of the config creation.

![A screenshot of a computer

AI-generated content may be incorrect.](../../../../.gitbook/assets/2.png)

1. Select the required objects to continue with the rules creation.

![](../../../../.gitbook/assets/3.png)

1. If there any rules available created under that object, all the available rules will come selected as depicted in the above screen.
2. If any object doesn’t hold the rules, the following “No masking rule” will be displayed under the “Selected Masking Rules” column.
   1. **Note: -** All the available selected rules will be displayed in a coma separated fashion under the “Selected Masking Rules”.
3. Click on any object that holds rules to view the available rules

![A screenshot of a computer

AI-generated content may be incorrect.](../../../../.gitbook/assets/4.png)

1. Click on the View icon to view the masking rules.

![A screenshot of a computer

AI-generated content may be incorrect.](../../../../.gitbook/assets/5.png)

1. Observe the rule and click cancel or anywhere outside the “Masking Rule” window to close the window.
2. Every selected object should have at least one rule associated to it. Observe the following screen flows.

![A screenshot of a computer

AI-generated content may be incorrect.](../../../../.gitbook/assets/6.png)

1. Clicking on ”Next” would show the following message prompting to create at least one rule for the selected object.

![A screenshot of a computer

AI-generated content may be incorrect.](../../../../.gitbook/assets/7.png)

1. Click on the “Masking Rules” icon to initiate the rules creation.

![A screenshot of a computer

AI-generated content may be incorrect.](../../../../.gitbook/assets/8.png)

1. A “Selected Object” window will be opened, for creating a new rule.
2. Click on the “NEW MASKING RULE” button to initiate the rule creation.

![A screenshot of a computer

AI-generated content may be incorrect.](../../../../.gitbook/assets/9.png)

1. A “Masking Rule” window will be opened to create the rule.

![A screenshot of a computer

AI-generated content may be incorrect.](../../../../.gitbook/assets/10.png)

1. **Observe the following on the window**:
   1. **Org Name**: Provides the org name.
   2. **Rule Name**: Enter the rule name here.
   3. **Select Object**: It represents the object on which the masking rule is being created.
   4. **Field Type**: Provides the list of “Field Types” from the object.
   5. **Masking Style**: Enter the required pattern which should reflect on the selected ‘Field Type’.
   6. **Masking Value**: Enter the pattern that should be applied for the selected field type.
2. Add to Org “ORGNAME” Masking Rules List:
   1. Selecting this will make sure, the rule being created will be a global rule.
3. Observe the following screen for reference:

![A screenshot of a computer

AI-generated content may be incorrect.](../../../../.gitbook/assets/11.png)

1. Select the “Add to Org ‘ORG NAME” Masking Rule List”, if the rule should be a global rule.
2. On entering all the required details, click on the “SAVE” button to save the created masking rule.
3. On clicking save a dialogue with info would be displayed confirming the save on the masking rule.

![A screenshot of a computer

AI-generated content may be incorrect.](../../../../.gitbook/assets/12.png)

1. Upon saving the masking rule, the workflow automatically navigates to the **Selected Object** screen, where the newly created rule will be displayed and available for further configuration or review..

![A screenshot of a computer

AI-generated content may be incorrect.](../../../../.gitbook/assets/13.png)

1. Observe the upward (Publish) icon beside the “Type Of The Rule” to publish the local to become a global rule.
2. Click on the icon to publish the local rule to become a global rule.

![A screenshot of a computer

AI-generated content may be incorrect.](../../../../.gitbook/assets/14.png)

1. Click on to continue with the rule creation. The flow will navigate to the object info section of the masking config creation.

![A screenshot of a computer

AI-generated content may be incorrect.](../../../../.gitbook/assets/15.png)

1. Observe the account object unchecked during the masking config creation. This will throw a message to the user asking for confirmation about unselecting the object from the flow creation.

![A screenshot of a computer

AI-generated content may be incorrect.](../../../../.gitbook/assets/16.png)

1. On selecting the required objects, click on the “NEXT” to continue with the “masking config” creation
2. Clicking next will navigate to the “Config Details” section of the flow.

![A screenshot of a computer

AI-generated content may be incorrect.](../../../../.gitbook/assets/17.png)

1. Observe the screen for the details:
   1. **Org Name:** Represents the org name
   2. Label: Enter the required label in this field.
   3. **Batch Size:** Specify the batch size at which the data should be processed while the data masking is being performed.
   4. **Email notification**: Select an email from the list. This will send an email to the person whose email is selected
   5. **Disable Workflows**\
      Enable this toggle to temporarily disable active workflows during the data masking operation.
   6. **Disable Validation Rules**\
      Enable this toggle to prevent validation rules from executing while masking data.
   7. **Disable Triggers**\
      Enable this toggle to bypass Apex triggers during the masking process.
   8. **Disable Flows**\
      Enable this toggle to deactivate Salesforce Flows for the duration of the data masking operation.
   9. **Exclude Deleted Records**\
      Enable this toggle to ensure that deleted records are excluded from the masking operation.
   10. **Enable Serial Mode for Bulk API**\
       Enable this toggle to process Bulk API operations sequentially (one after another) to reduce the risk of record-locking or related execution errors.

![A screenshot of a computer

AI-generated content may be incorrect.](../../../../.gitbook/assets/18.png)

1. The **“Masking Info”** section of the **“Config Details”** page will provide the information about the list of rules created per object.

![A screenshot of a computer

AI-generated content may be incorrect.](../../../../.gitbook/assets/19.png)

1. Click **“SAVE”** or **“SAVE & RUN”** to save the config.
2. **SAVE**: Saving the config will show the following screen, followed by a confirmation message on saving the config.

![A screenshot of a computer

AI-generated content may be incorrect.](../../../../.gitbook/assets/20.png)

1. Clicking on “OK” will continue with saving the flow and navigates to the “JOB CONFIG” page.
2. The saved job has to be run on the job config page to perform the actual data masking on the data in the Salesforce.
3. Click on the “Play” icon to run the config.
4. On initiating the job run a “Selected Data To Masking” window will be displayed to verify the details of the run.
5. Observe the icon in the below screen while the job run is in progress.
6. Clicking the “SAVE & RUN” will save the config and run it to perform the data masking.
7. On completing the saving, the flow navigates to the “JOB CONFIG” screen.
8. Observe the Rollback option, which provides the ability to revert any deployed masking operations, if required.
9. Click on the rollback button available to initiate the rollback operation.
   1. To support the rollback operation, the deployed data will be retained for a period of “7 days” and on elapsing the retention period, the data will be deleted permanently.
10. On clicking the rollback, the following “Rollback” window will be displayed.
11. Select the required objects to rollback the masking’s. On selecting at least one object the “Rollback” button will become enabled.
12. On clicking the rollback option, the following window will be displayed for confirming the rollback
13. For every rollback operation performed, a new entry will be created at the “JOB HISTORY” page. This job can be identified with the “Job Type – Rollback”.
14. Click on the “info” icon under the “Job Info” to open the “Live Masking Config Info”.
