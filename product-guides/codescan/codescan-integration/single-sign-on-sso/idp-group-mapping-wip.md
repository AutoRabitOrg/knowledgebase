---
layout:
  width: default
  title:
    visible: true
  description:
    visible: true
  tableOfContents:
    visible: true
  outline:
    visible: true
  pagination:
    visible: true
  metadata:
    visible: true
  tags:
    visible: true
  actions:
    visible: true
---

# IdP Group Mapping for Dedicated Instances

{% hint style="info" %}
NOTE: This feature is only available to customers who have a dedicated instance. It is not available for customers who are deployed on our SaaS multi-tenant instances.
{% endhint %}

The Org admin can configure mapping between IdP Groups and Codescan Organization Groups on the SAML Configuration screen.

This feature allows to implement **many-to-many** mapping between IdP Groups and Codescan Orgs.&#x20;

When IdP Connection is configured to send the user groups, then **SAML Response** which we receive during User login contains the list of IdP Groups. Based on this data we can do the synchonization every time the user logs in.&#x20;

> **Before configuring the IDP Group Mapping, a SAML connection must be configured.**  [**Find out how in these articles.**](./)

To configure the mapping between IdP Groups and Codescan Orgs and Groups:

1. [Navigate to **Administration > Configuration > General Settings > Organizations:**](#user-content-fn-1)[^1]
   1. Disable `Allow any autheticated user to create organizations`
   2. Disable `Create an organization for each new user`<br>
2. [Navigate to **Administration > Configuration > General Settings > CodeScan**](#user-content-fn-1)[^1]**:**
   1. Enable `CodeScan idp-group-mapping`&#x20;
3. Navigate to **Administration > SAML Connections** and edit the connection of your choice.  There is a **IdP Group Mapping** section on the SAML Configuration screen:

<figure><img src="../../../../.gitbook/assets/image (5) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

You can add multiple rows for the mapping. In each row you define:

1. the IdP Group name - this is the text field;
2. the Codescan Org - this is the selection input
3. the Codescan Org Groups - this is set of checkboxes with the list of all Groups of the selected Org. The default Org Group is selected by default (e.g. Members group).

This configuration can be done only by the Org admin. And the Org Admin can modify this mapping anytime.

The Codescan will go through this list and programmatically add/remove users to Codescan Orgs based on that mapping.

[^1]: This section must be performed by a Platfrom Super Admin User on your dedicated instance
