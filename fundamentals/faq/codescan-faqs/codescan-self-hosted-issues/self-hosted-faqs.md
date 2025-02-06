---
description: FAQs specific to self-hosted or on-premises CodeScan use cases
---

# Self-Hosted FAQs

## CodeScan Self-Hosted FAQs

### How do I upgrade an instance?

If you are utilizing an On-Premises Instance and wish to upgrade, follow the steps below to ensure a smooth upgrade process.

1. **Initiate Your Request**: Contact your Customer Success Manager (CSM) or the Support team to request an instance upgrade.
2. **Coordinate with the Release Team**: CSM/Support teams will coordinate with the Release Team to prepare and share the necessary binaries with you.

**Assistance with Installatio**n: If you encounter any challenges while installing the binaries, you can request a call for assistance. One of our Release Team members will guide you through the installation process over the call.

Contact your CSM or the Support team for any further inquiries.

### Is it possible to directly integrate and scan a Salesforce org as part of a single code analysis for SonarQube self-hosted users?&#x20;

In self-hosted environments, Salesforce direct integration is not possible; therefore, CodeScan SCA through direct integration is not possible.

### Can I create a new SonarQube™ instance and use the existing CodeScan license if one of my SonarQube™ instances was mistakenly deleted? <a href="#can-i-create-a-new-sonarqube-instance-and-use-the-existing-codescan-license-if-one-of-my-sonarqube-i" id="can-i-create-a-new-sonarqube-instance-and-use-the-existing-codescan-license-if-one-of-my-sonarqube-i"></a>

Yes, you can reinstall CodeScan Self-Hosted and continue to utilize your existing license.

After you've set up the prerequisites, you can use your existing account and password to log into SonarQube™. If it doesn't work, try logging in with the admin username and password.

1. Login into SonarQube™ using the below credentials:
   * **username:** _admin_
   * **password:** _admin_
2. Go to the top right and select **Administrator**.
3. On the right side, select **General Settings**.
4. On the category list, select **CodeScan**.
5. In the **CodeScan license** text box, type your license key. (key is sf.license.secured)
6. Save the file.

