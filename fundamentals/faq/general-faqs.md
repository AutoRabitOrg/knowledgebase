# General-FAQs

## What is AutoRABIT? <a href="#what-is-autorabit" id="what-is-autorabit"></a>

AutoRABIT is a cloud-based CI/CD and release automation suite specifically designed for Salesforce.com. AutoRABIT helps Salesforce developers, admins, analysts, and release managers automate version control, deployment, testing, data loading and sandbox management across multiple Salesforce orgs.

## What does AutoRABIT do? <a href="#what-does-autorabit-do" id="what-does-autorabit-do"></a>

AutoRABIT delivers a unified CI/CD solution purpose-built for Salesforce. The ease of use provided by AutoRABIT makes it much easier for Salesforce administrators and developers to leverage an enterprise-class DevOps process to accelerate their journey from defining requirements to deploying code.

## What is Salesforce? <a href="#what-is-salesforce" id="what-is-salesforce"></a>

Salesforce is one of the most widely used customer relationship management (CRM) tools on the market. Salesforce is a web-based, flexible, and powerful database provider.

For more details, please refer to: [What is Salesforce?](https://www.salesforcetutorial.com/what-is-salesforce-all-about-salesforce/)

## What is an object? <a href="#what-is-an-object" id="what-is-an-object"></a>

An object is represented as a database table that stores organization data. Objects consist of a set of fields, and we store data against that field.

## What are the different types of objects in Salesforce?

There are two types of objects in Salesforce:

* **Standard Objects -** Standard Objects are those which Salesforce creates. We can use these standard objects automatically. For example, accounts, contacts, chatter, leads, etc.
* **Custom Objects -** Salesforce Custom objects are those which the user creates. We can create any number of custom objects. For example, student info, college, etc.

## What are the Standard and Custom fields? <a href="#what-are-the-standard-and-custom-fields" id="what-are-the-standard-and-custom-fields"></a>

* **Standard fields** for custom objects store the information created by, modified by, currency, name, owner, and division. These are the standard fields in Salesforce.
* **Custom fields** for custom objects store unique data or information about an organization.

## What are Page Layout and Record Types? <a href="#what-is-page-layout-and-record-types" id="what-is-page-layout-and-record-types"></a>

* **Page Layout -** In page layout, customization can be done like fields, related lists, and custom links can be arranged.
* **Record Types -** Record types help to implement business processes like defining picklist values for standard and custom picklists.

## What is the difference between Profiles and Permission sets? <a href="#difference-between-profiles-and-permission-sets" id="difference-between-profiles-and-permission-sets"></a>

* **Permission Sets -** In the Permission sets, we define the user's access level. Generally, we determine what a user can do in the applications. These are used to grant additional permission to a user.
* **Profiles -** Profiles are assigned to the user by the system administrator. A profile can be assigned to many users, whereas a user can have only one profile.

## What is Field-Level Security? <a href="#briefly-describe-about-fieldlevel-security" id="briefly-describe-about-fieldlevel-security"></a>

Using field-level security, we manage what a user can see, modify, and delete a specific field in an object. In other cases, such as when we want to give a user access control over an object but don't want them to be able to access certain fields in that object, we use field-level security.

## What are Governor Limits in Salesforce?

Governor Limits in Salesforce are the run time limits enforced by the apex runtime engine to write scalable and efficient code.

## What is the difference between a Trigger and Workflow? <a href="#what-is-the-difference-between-trigger-and-workflow" id="what-is-the-difference-between-trigger-and-workflow"></a>

* **Workflow -** Workflow is an automated process, a point-and-click that doesn't need coding. You can use Workflow rules when you want to take action (email, task, field update, or outbound message) for the same object or from Child to parent object. You cannot perform DML operations on workflow. Workflows work only after some actions.
* **Trigger -** Trigger is a programmatic code approach that fires before or after a record is inserted, updated, or deleted. Using triggers, you can work on multiple objects. You can query, and you can perform any DML operation. The trigger works before and after some actions.

## Is AutoRABIT compatible with the deployment of CPQ data? <a href="#is-autorabit-compatible-with-the-deployment-of-cpq-data" id="is-autorabit-compatible-with-the-deployment-of-cpq-data"></a>

Currently, we are supporting CPQ data deployment through Data Loader Pro only. We'll release a beta version exclusively for CPQ deployments in the coming months.
