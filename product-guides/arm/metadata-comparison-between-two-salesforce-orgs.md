# Metadata comparison between two Salesforce Orgs

Org Synchronization feature in AutoRABIT does a **component-level metadata comparison** between two Salesforce orgs. With this feature, you can either add or delete an object or metadata member, making sure that both the orgs are in sync. However, you won't be able to see the content level differences.

For **content-related comparison** between two [Salesforce Orgs](arm-features/salesforce-org-management.md), please refer to the following steps:

1. Go to **Menu > Deployment > New Deployment**
2. Give a Label name.
3. Select **Deployment From** as Salesforce Org.
4. Select your **Source** & **Destination Org**.
5. Click on **Retrieve Metadata**.
6. Select the component for which you want to view the content level differences and click on **Compare Metadata & Deploy.**
7. In the next screen, AutoRABIT retrieves the components from both the orgs and generates a difference if it exists and displays the same.
