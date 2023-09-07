# Unsupported Metadata Templates

### List of Unsupported Metadata supported <a href="#list-of-unsupported-metadata-supported" id="list-of-unsupported-metadata-supported"></a>

1. Account Teams
2. Add Tabs in App Manager
3. Activity Button Overrides
4. Add Apex Exception Email
5. Add Compliance BCC Email
6. Auto Number Fields
7. Campaign Influences
8. Case Contact Roles
9. Case Team Roles
10. Console Layout Assignment
11. Create Lead Mapping rules
12. Create Organization-Wide Email Footers
13. Case Feed Layouts
14. Create Public Groups
15. Create Web to Case
16. Data Category Visibility Settings
17. Delegated Administration
18. Delete Outbound Messages
19. Delete Scheduled Jobs
20. Delete Time based Workflow
21. Disable Scheduled Reports
22. Edit Queue
23. Email to Case Settings
24. File Upload Download Security
25. Fiscal Year
26. Lead Settings
27. Manage Email Administration Deliverability
28. Manage Email Relay Activation
29. Manage Email Services
30. Manage Libraries
31. Manage Page Layout Assignments
32. Manage User Records
33. Mobile Administration
34. Multi line Layout Fields for Contract Line Items
35. Multi Line Layout Fields for Opportunity Teams
36. New Territory Model
37. Offline Briefcase Configuration
38. Opportunity Big Deal Alerts
39. Opportunity Update Reminders
40. Organization Wide Email Addresses
41. Predefined Case Teams
42. Product Schedule
43. Public Calendar
44. Public Calendars and Resources Sharing
45. Publish Communities
46. Quote Templates
47. AnalyticSettings
48. Report Dashboards Create Manage Folders
49. Resource Calendar
50. Sandbox Refresh
51. Enable Salesforce to Salesforce
52. Schedule Monthly Apex Class Job
53. Schedule Weekly Apex Class Job
54. Search Settings
55. Self Service Public Solutions
56. Site
57. Social Accounts Contacts And Lead Settings
58. Softphone Layouts
59. Solution Categories
60. Solution Settings
61. Tag Settings
62. Territory View Rules
63. User Interface Settings
64. Update Custom Label
65. Update Url for Remote Site Settings
66. Web to Lead

### How to create an Unsupported Metadata template <a href="#how-to-create-an-unsupported-metadata-template" id="how-to-create-an-unsupported-metadata-template"></a>

To create a new unsupported metadata template, please follow the below steps:

1. Login to your AutoRABIT account.
2. Click on **Env. Pro.** module.
3. Click on **Create New Template**.
4. Go to the **Create Unsupported Metadata Template** tab.
5. Give the template a **name** and a **short description** of it.
6. Select the checkboxes for the template types for which you want to create a template. You can create multiple templates at the same time.
7. Click **Add**.
8. On the next screen, you will find a **Test Case Name** appear automatically by default. To add the custom test data, click on **Add** button.

&#x20;

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1631619787581.png" alt=""><figcaption></figcaption></figure>

1.  However, you'll need to add a page layout for the auto-generated or your custom test case name. To do a page layout, do the following,

    1. Click on ![](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1631619313556.png) icon.
    2. Enter the page layout name in the **Page Layout** field.&#x20;
    3. Activate the page layout by selecting the **Active** checkbox.&#x20;
    4. You can even add multiple page layout for the above-generated test case name. Click on the + symbol beside Active and fill in the fields as mentioned in the steps earlier.&#x20;
    5. Click **OK**.



    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1631619843373.png" alt=""><figcaption></figcaption></figure>
2. Click **Save** to save the template.
3. You can find your recently created template on the **Environment Provisioning History** page.
4. The next step is to run the template on your destination Salesforce org.
5. Look for your template on the **Environment Provisioning History** screen and click on **Run**.
6. Select your **destination org** from the dropdown and enter the email address(es) to receive an email notification whenever the operation is carried out.
7. Click **Run**.

### View History <a href="#view-history" id="view-history"></a>

The **View History** screen will display the detailed summary report of the template operation being carried out.

The left side screen will display the template name, the template creation date/time stamp, and the Salesforce org where the template was run.

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1616328277736.png" alt=""><figcaption></figcaption></figure>

Click on the **Log** icon to view the log report on the right side of the page.

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1616328449188.png" alt=""><figcaption></figcaption></figure>

**Result** icon will display the status of the deployment for the template (success or failed), deployed components, deployed components path, and many more.&#x20;

**Re-Run** option allows you to run the template once again.&#x20;

**Info** option allows you to view the input file which you have uploaded in the initial stage for template creation.
