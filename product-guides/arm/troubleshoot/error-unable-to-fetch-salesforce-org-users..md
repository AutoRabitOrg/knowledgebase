# Error: "Unable to fetch Salesforce Org Users."

## Description <a href="#description" id="description"></a>

When I try to access the Salesforce Org in the ARM Version Control, CI Jobs, Deployment, and SFDX Modules, it fails, and the error message **"Unable to fetch Salesforce Org Users"** appears.

## Cause <a href="#cause" id="cause"></a>

* Invalid username, password, security token, or user locked out.
* The Salesforce API version is wrongly configured.

## Steps for Resolution <a href="#steps-for-resolution" id="steps-for-resolution"></a>

The following is some helpful information that will assist you in resolving the issues mentioned above:

1. Upgrade the API source flow in your Salesforce org to the most recent version and maintain the same Salesforce version in ARM.
2. To do so, go to **Admin > My Account > My Salesforce Settings** and update the API version.
