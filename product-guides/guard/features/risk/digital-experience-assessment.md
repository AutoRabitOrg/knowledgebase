# Digital Experience Assessment

#### Overview

**Digital Experience Assessment** helps you find security risks on Salesforce Experience Cloud sites. You run a scan against a specific org and site, then review security findings, exposed objects and external domains.

It supports both **Aura** and **LWR** Experience Cloud sites. Each site type uses its own set of security checks.

#### Key Benefits

* **Framework-aware checks:** Aura and LWR sites are assessed against the corresponding risk library, selected specifically for the risks most appropriate to each framework in digital experience sites.
* **Sensitive data context:** Optionally include Automated Data Classification so exposed fields show sensitivity and regulation labels.
* **Governed risk acceptance:** Admins can accept a known risk for selected sites and keep an activity history of those decisions.

#### Navigation Path

`Guard → Risk → Digital Experience Assessment`

<figure><img src="../../../../.gitbook/assets/image (5110).png" alt=""><figcaption></figcaption></figure>

#### Page Layout

The Digital Experience Assessment page has two tabs:

* **Scan History** (default) – previous scans and their status
* **Security Risks Library** – a full list of possible findings the Digital Experience assessment checks for

#### Getting Started: Run a Scan

1. Open **Risk → Digital Experience Assessment**.
2. Select **New scan**.
3. Choose a Salesforce org.
4. Choose an Experience Cloud site in that org. _Note that an org must be selected first._
5. If Automated Data Classification is available for your Guard instance, leave the classification option enabled if you want sensitive-field context in the results.
6. Select **Scan Site**.

The new scan appears in Scan History. While it is running, the status will show as **in progress** and the row is not clickable.

{% hint style="info" %}
Support users and Realm Managers cannot start a new scan.
{% endhint %}

<figure><img src="../../../../.gitbook/assets/image (5112).png" alt=""><figcaption></figcaption></figure>

#### Scan History

Each row in Scan History shows:

* **Site** – site name, with the site URL underneath
* **Salesforce Org**
* **Security Findings** – count of findings
* **Objects Exposed** – count of exposed objects
* **Framework** – Aura or LWR
* **Date**
* **Scan Status** – successful, failed or in progress

<figure><img src="../../../../.gitbook/assets/image (5113).png" alt=""><figcaption></figcaption></figure>

#### Investigating a Scan

Open a successful scan to review its detail page.

**Security findings**

The security findings table lists checks from the Aura or LWR library that the site failed at the time of the scan. Opening a finding shows:

* Finding name
* Severity (High, Medium or Low), with an explanation of that severity
* Description of why it was flagged
* Remediation guidance (**How to fix it**)

From the finding detail view, an Admin can start **Accept risk** for a finding that has not already been accepted.

<figure><img src="../../../../.gitbook/assets/image (5114).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/image (5115).png" alt=""><figcaption></figcaption></figure>

**Objects exposed**

Opening an exposed object shows:

* Object name
* Number of records exposed
* Up to five sample records from the scan, with values masked
* The object’s fields (scroll when the list is long)

If Automated Data Classification ran with the scan, the object view can also show sensitive field counts, field names and regulation labels. If there are no sensitive fields, that section is omitted.

For **LWR** sites, object detail can also list exposed files.

**External domains**

Scan detail also lists any external domains or trusted sites that the LWR/Aura site is authorized to communicate with.

#### Automated Data Classification

When Automated Data Classification is enabled for your Guard instance, you can include classification in a Digital Experience scan.

Classification follows the settings already configured in Guard’s Data Classification area, including deep data scan settings by org or field.

When classification is included, exposed objects are scanned for sensitive fields and corresponding regulations.

_Note that if data classification is not enabled on your instance, this option will not appear._

{% hint style="info" %}
Realm Managers can see the summary table on scan detail but cannot open risk detail (which includes the classification results).
{% endhint %}

#### Accepting a Risk

Accepting a risk suppresses that finding for the selected org(s) and site(s) in future scans. It is treated as a governance decision.

{% hint style="info" %}
Sites where a risk has been accepted are called risk accepted sites. Earlier versions of Guard called these excluded sites. Only the name has changed.
{% endhint %}

**Who can and cannot accept a risk?**

* **Admin** – **can accept a risk** from a scan finding and can add or remove risk accepted sites in the Security Risks Library
* **Standard users** – can run scans and review findings, but **cannot accept a risk**
* **Support Engineers and Realm Managers** – can view the library, risk accepted sites and activity log, but cannot manage them

For roles that cannot accept risk, the accept and add actions are disabled.

**From a scan finding**

1. Open the finding.
2. Start **Accept risk**.
3. Confirm or cancel.

Accepted findings are left out of future scans for those orgs and sites. They also appear as risk accepted sites on the matching risk in the Security Risks Library. The acting user is recorded in the activity log.

_Removing a risk accepted site does not change past scan results. It only brings the risk back into future scans for that site._

<figure><img src="../../../../.gitbook/assets/image (5116).png" alt=""><figcaption></figcaption></figure>

#### Security Risks Library

The Security Risks Library lists every risk in the Aura and LWR findings libraries, whether or not any scan has previously found it.

Each row shows:

* Risk name
* Framework (Aura or LWR)
* Category (for example API Exposure, Access Control, File Exposure or CSP)
* Severity (High, Medium or Low)
* Last Updated – when risk acceptance for that risk last changed in your tenant. Blank if the risk has never been accepted. _This tracks risk acceptance activity only, not AutoRABIT updates to the risk definition_
* Risk accepted sites – site names, where the risk has been accepted

You can filter by Framework, Category, Severity and Risk accepted sites. Library filters are independent of Scan History filters.

<figure><img src="../../../../.gitbook/assets/image (5117).png" alt=""><figcaption></figcaption></figure>

**Risk detail in the library**

Opening a risk from the library shows:

* Last Updated, Framework, Category and Severity
* Risk accepted sites for that risk
* An activity log of accept and remove events (Action, Site with org, Changed By, Date)

Admins can add risk accepted sites from the risk detail: pick org(s), then one or more sites, confirm the count and save. The risk will then not appear in future scans for the selected sites.

<figure><img src="../../../../.gitbook/assets/image (5118).png" alt=""><figcaption></figcaption></figure>

#### Recommended Best Practices

* Scan important Experience Cloud sites regularly after configuration or permission changes.
* Review High severity findings first, then Medium and Low.
* Use Automated Data Classification on sites that expose customer or regulated data.
* Accept risk only when the exposure is understood and approved. Fix the underlying issue when you can.
* Use the Security Risks Library activity log when you need an audit trail of who accepted or restored a risk.

#### Example Use Case

A security admin scans a customer portal LWR site before a release. The scan reports several security findings and shows Account fields exposed through the site. With Automated Data Classification enabled, some of those fields are labelled as sensitive.

The admin remediates the critical findings but accepts a lower-severity finding for that portal only. On the next scan of the same site, the accepted finding stays suppressed, but the new issues found are displayed clearly.
