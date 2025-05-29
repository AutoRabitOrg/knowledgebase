# nCino

### Overview <a href="#overview" id="overview"></a>

nCino is the worldwide leader in cloud banking. In today's competitive landscape, customer and employee expectations are changing. Speed, convenience, and trust matter most. To meet these expectations, financial institutions must leverage the right technology to provide the personalized experience customers and employees demand.

With its Bank Operating System, built on the Salesforce platform, financial institutions can deliver the speed and digital experience that customers expect, backed by the quality and transparency that bankers need.

### Why did nCino choose AutoRABIT? <a href="#why-did-ncino-choose-autorabit" id="why-did-ncino-choose-autorabit"></a>

AutoRABIT is designed around the industry’s only CI/CD (Continuous Integration / Continuous Delivery) server purposely built for Salesforce to handle metadata and data. AutoRABIT delivers an integrated suite of tools, including version control, deployment automation, sandbox management, data migration, and test automation. This streamlines processes and automates activities at each stage of the DevOps lifecycle, simplifying deployment from development to production.

nCino chose AutoRABIT as its DevSecOps partner because of our ability to support the unique needs of financial institutions working on Salesforce. AutoRABIT helps nCino deliver secure, compliant, and high-quality solutions at scale by automating key parts of the development lifecycle—from version control and CI/CD to code quality and data backup. What makes this partnership stand out is AutoRABIT’s strong grasp of Salesforce metadata—especially the custom components used by nCino—and our shared focus on meeting the ever-changing needs of the financial services world. We're helping banks and credit unions move faster, stay compliant, and reduce risk along the way.

### Understanding Record-Based Configuration (RBC)&#x20;

With RBC, nCino gives admins the flexibility to shape how the platform behaves depending on the kind of record in use — whether it's a specific loan type, region, or product line. The best part? It doesn’t require any coding. This approach makes it easier for financial institutions to handle complex processes, ensuring users only interact with the fields, workflows, and rules that actually apply to the record they're working on.&#x20;

### Why RBC Makes a Difference &#x20;

1. Keeps things simple for users by showing only the information that pertains to the type of record they’re working with.
2. Reduces mistakes by applying the right validations and making the right fields required based on the record type.
3. Speeds up processes by using workflows built specifically for each loan or product category.&#x20;
4. Makes it easy to adjust as business needs evolve—no code needed, just a few clicks.&#x20;

### Key Benefits: User-Specific Relevance &#x20;

1. Keeps the interface clean: Shows users only what’s relevant to their task—nothing more, nothing less.&#x20;
2. Easy to manage: Admins can quickly make updates using clicks instead of code.&#x20;
3. Built to scale: Whether you're dealing with different products, regions, or business lines, RBC can handle it all smoothly.&#x20;

### Best Practices&#x20;

1. Set up by record type or business line, so it’s easier to manage and understand.&#x20;
2. Take full advantage of RBC by combining it with tools like conditional visibility, validation rules, and flows to make your configurations even smarter.
3. Maintain good documentation for each configuration to help with transparency, governance, and staying audit-ready.

### Before You Begin <a href="#before-you-begin" id="before-you-begin"></a>

Before you start working with the nCino features in AutoRABIT, you need to configure certain things in AutoRABIT to proceed:

1. Register the **nCino configured** [**Salesforce Org**](https://knowledgebase.autorabit.com/docs/salesforce-org) in ARM.
2. The Super Admin should categorize the account type as the appropriate subscription to create either a **Standard** or **Community Template**.
3. Users are allowed to access the **Feature Migration** section. The Admin can assign the required permissions to users by visiting the **Admin > Roles** tab and creating a role with the permissions below enabled.
4. You should only be able to edit/modify your existing CI job if the special permissions for CI Job List are assigned to you. For example, to edit or delete your existing job, you need **Edit** and **Delete** permissions.

<figure><img src="../../../../.gitbook/assets/image (1287).png" alt="" width="563"><figcaption></figcaption></figure>

### Super Admin roles in Account Activation and Categorization (Partner/Customer) <a href="#super-admin-roles-in-account-activation-and-categorization-partnercustomer" id="super-admin-roles-in-account-activation-and-categorization-partnercustomer"></a>

The Super Administrator will have the capability of marking an account as either partner/customer with the user-specific prefix. The accounts marked as a partner will be able to create Standard/ Community templates, whereas customer accounts are restricted to creating only community templates.

Simply log in to the AutoRABIT account using the Super Admin credentials and go to the **My Account** section. Under the **Subscription Details**, assign the user as an **nCino Partner** to allow them to create Standard/Community Templates. If not assigned, the user will be treated as a customer account and is restricted to creating only Community templates.

<figure><img src="../../../../.gitbook/assets/image (1288).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/image (1289).png" alt=""><figcaption></figcaption></figure>

### Registering nCino-Configured Version Control Repository <a href="#registering-ncino-configured-version-control-repository" id="registering-ncino-configured-version-control-repository"></a>

1. Go to the [**Version Control**](https://www.autorabit.com/blog/7-tips-for-salesforce-version-control-integration/) **Repo** tab and click on **Register Repository**.

<figure><img src="../../../../.gitbook/assets/image (1290).png" alt=""><figcaption></figcaption></figure>

2. On the next screen, select your **Version Control System**.
3. Fill in the registration page with necessary details such as repository name, URL, master branch, etc.
4. Tick the checkbox: **Enable nCino**
5. Click on the **Test Connection** button to check whether the connection has been authenticated or not. A success message is displayed after the authentication is completed.
6. Click **Save** to complete the registration process.

<figure><img src="../../../../.gitbook/assets/image (1291).png" alt="" width="390"><figcaption></figcaption></figure>

{% hint style="info" %}
**Important Note**: To quickly identify nCino-registered Version Control Repositories among all other repositories, the nCino logo is marked in front of the Repository name.&#x20;
{% endhint %}

### Registering nCino-Configured Salesforce Org <a href="#registering-ncino-configured-salesforce-org" id="registering-ncino-configured-salesforce-org"></a>

1. Go to the **SF Org Mgmt** tab and click on the **Add** button.

<figure><img src="../../../../.gitbook/assets/image (1292).png" alt=""><figcaption></figcaption></figure>

2. On the next screen, give your Salesforce Org a **Name** and select your Salesforce Org **Type** and **Environment.**
3. Select the authentication method in the **Access Type** dropdown.
4. Select the checkbox: **Is nCino Installed**
5. Click **Validate and Save** to proceed through the OAuth flow and allow AutoRABIT to connect to your Salesforce Org.

<figure><img src="../../../../.gitbook/assets/image (1293).png" alt="" width="375"><figcaption></figcaption></figure>

{% hint style="info" %}
**Important Note**: The **nCino logo** is marked in front of each Salesforce Org for easier identification from other Salesforce Orgs.
{% endhint %}
