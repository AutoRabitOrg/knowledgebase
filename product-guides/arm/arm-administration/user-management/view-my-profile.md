# View my Profile

Numerous configuration options are available to users when setting up their profile in ARM. The **`Profile`** section allows users to view and update their basic information, personal email settings, etc.&#x20;

To access user preferences, click your user name on the upper right corner and select **`Profile`**.

<figure><img src="../../../../.gitbook/assets/image (5) (1) (1) (1) (1) (1) (1).png" alt="" width="252"><figcaption></figcaption></figure>

#### Personal Details <a href="#personal-details" id="personal-details"></a>

The **`Personal Details`** section displays your full name, ARM user name, email address, phone number, etc. Your personal details will be populated, as the system administrator must enter this information when creating a new user account. In this section, you can update your name, phone number, address, etc., accordingly.

<figure><img src="../../../../.gitbook/assets/image (6) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
**Important Note:**

1. **System Administrators** can change your **Email** and **Username**.
2. To avoid conflicts and get correct data while conducting any activity in ARM, ensure the **Time Zone** you set here matches the time zone you defined in Salesforce.
{% endhint %}

#### My Projects <a href="#my-projects" id="my-projects"></a>

The **`My Projects`** section will list all the projects that you have created or have permission to view. Users with admin-level permissions will have access to all projects.

#### My Roles <a href="#my-roles" id="my-roles"></a>

The **`My Roles`** displays the list of roles assigned to the user. If you have admin roles and permission, you can perform all the tasks an administrator can perform and access all modules within ARM.&#x20;

About Skip MappingsIf users maintain an individual version control branch for every release, they must map every branch to Salesforce Org and Version Control branches to keep synchronizing with Salesforce Org. To overcome this daily routine, ARM provides the option to skip the Org Mappings part and directly perform commits.

#### My Salesforce Orgs <a href="#my-salesforce-orgs" id="my-salesforce-orgs"></a>

View the **`Salesforce Orgs`** assigned to you, or you have permission to view.

<figure><img src="../../../../.gitbook/assets/image (7) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

#### My Version Control Mappings <a href="#my-version-control-mappings" id="my-version-control-mappings"></a>

View the Version Control Repositories here based on the Salesforce Orgs selected in the **My Salesforce Orgs** section. Map the required repositories by choosing the correct **`Credential`** from the drop-down field. Click **`Test Connection`** to determine whether the connection has been authenticated or not.

<figure><img src="../../../../.gitbook/assets/image (8) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

#### My ALM Mappings <a href="#my-alm-mappings" id="my-alm-mappings"></a>

Under **`My ALM Mappings`** section, you can map your ALM using your credentials or **`Re-Authenticate`** Jira ALMs configured with OAuth access.

<figure><img src="../../../../.gitbook/assets/image (9) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

For ALM type **`IBMRTC (IBM Rational Team Concert)`** and **`JIRA`**, we have added the filter to fetch specific work items according to the filter applied.

<figure><img src="../../../../.gitbook/assets/image (10) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/image (11) (1) (1) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

According to the filter set, only specific work items will get fetched. When the developers progress (via EZ-Commit or merge operation in ARM) on updating the ALM status, they are reflected on the corresponding work items. If the user wishes to discard the filter selected, uncheck the **`Apply My Filter`** option, and all work items will get fetched.

#### My Default Page <a href="#my-default-page" id="my-default-page"></a>

**`My Default Page`** is the first page that appears when you log in to ARM. You can customize ARM to open any page as the default page.

<figure><img src="../../../../.gitbook/assets/image (12) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

### Mapping your Profile with Version Control and Salesforce Org <a href="#mapping-your-profile-with-version-control-and-salesforce-org" id="mapping-your-profile-with-version-control-and-salesforce-org"></a>

The next step is to map your profile with the Version Control system you will be working with and the associated Salesforce Org.

1. Go to the **`Profile`** section.

<figure><img src="../../../../.gitbook/assets/image (13) (1) (1) (1) (1) (1) (1).png" alt="" width="252"><figcaption></figcaption></figure>

2. Scroll down to **`My Salesforce Orgs`**.
3. Select the **`Salesforce Org`** and assign the **`Salesforce Org User`** to them.

<figure><img src="../../../../.gitbook/assets/image (14) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

4. Next, Scroll down to **`My Version Control Mappings`**.
5. Select the **`Repository`** and assign the user.

{% hint style="info" %}
**Important Note:** If users maintain an individual Version Control branch for every release, then to keep synchronizing with Salesforce Org and the version control branch, they need to map every branch to Salesforce Org. ARM provides a **Skip Mapping** option under **Profile>My Roles** to skip the org mappings part and directly perform commits to overcome this daily routine.
{% endhint %}

<figure><img src="../../../../.gitbook/assets/image (15) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

6. Click **`Save`**.
7. Go to **`Admin > SF Org Mgmt,`** select your org, and scroll down to **`Salesforce Org - Mappings`**.
8. Select the mapping against the version control that you have set up.

<figure><img src="../../../../.gitbook/assets/image (16) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

9. Click on **`Save Mappings`**.
