# CodeScan Release Notes

{% hint style="info" %}
With the constantly evolving security landscape, we are evolving too. Please note that a number of CodeScan rules will be fully deactivated in 60 days. The rules in question are:

* Custom fields must have a description field (sfmeta:RequireDescriptionField, Salesforce Metadata)
* Unnecessary Parentheses (sf:UnnecessaryParentheses, Apex)
* Use System.Assert instead of System.assertEquals (sf:UseAssertInsteadOfAssertEquals, Apex)
* Use System.assertEquals instead of System.assert (sf:UseAssertEqualsInsteadOfAssertEquality, Apex)
* Use System.assertEquals instead of System.assert (sf:UseAssertEqualsInsteadOfAssert, Apex)

To understand the potential impact on your organization, we recommend reviewing whether any of the soon-to-be-deactivated rules are currently included in your Quality Profiles. You can do so by navigating to _Quality Profiles._ Rules subject to deactivation will be highlighted in red next to the overall rule count within your profiles. Each deprecated rule also includes a reason for deactivation (for example, replacement with an improved rule).Thank you for your continued partnership. Should you have any questions or require assistance, please contact us at [support@autorabit.com](mailto:support@autorabit.com)&#x20;
{% endhint %}

<figure><img src="../../../.gitbook/assets/6df7b327-8177-611d-9374-df5e1c15120e.png" alt=""><figcaption></figcaption></figure>

CodeScan offers three primary deployment options: [Cloud](cloud-releases/), [Self-Hosted](on-premise-releases/), and [Government](../ar-govcloud-documentation/). Release notes and information are available for each deployment type.

{% @mailchimp/mailchimpSubscribe cta="Sign up to receive CodeScan updates!" listId="a085e26e7e" %}
