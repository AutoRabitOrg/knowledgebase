# Deploying the Profile and PermissionSets

{% hint style="info" %}
The **Deployment** screen is best viewed when the zoom setting is set to **80%** on your Chrome/Firefox browser.
{% endhint %}

1. Log in to your ARM account.
2. From the top navigation pane, navigate to **`Create New > New Deployment`**.
3. Click on the **`Profile Manager`** button.

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1625587460116.png" alt="" width="563"><figcaption></figcaption></figure>

4. In the **`Profile/PermissionSet Manager`** screen, select the **`Salesforce orgs`** that need to be compared (max 3 Orgs).
5.  Click on either the **`Get Profiles`** or the **`Get PermissionSets`**button.

    1. **`Get Profiles`** will fetch all the profiles available in selected Salesforce Orgs.
    2. **`Get PermissionSets`** will list all available permission sets in Salesforce Orgs



    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1617593219733.png" alt="" width="563"><figcaption></figcaption></figure>
6.  Select the **`Profile/PermissionSets`** type based on the above selection.

    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1617593388191.png" alt="" width="563"><figcaption></figcaption></figure>
7.  Select the metadata components (including its metadata members) for which you want to view the selected profile/permissionset comparison report. A minimum of one metadata component selection is required to proceed further.\


    <figure><img src="../../../../.gitbook/assets/image (5) (1).png" alt=""><figcaption></figcaption></figure>
8.  About Object Permissions in Profiles, Editing standard objects on standard profiles is not supported by Salesforce. Hence, these changes won't show up in your destination environment.\
    \


    <figure><img src="../../../../.gitbook/assets/Screenshot 2023-06-22 at 12.21.49 PM.png" alt=""><figcaption></figcaption></figure>
9. Select the **`'Hide components with no differences'`** checkbox to hide the components with no differences.
10. Give the process a **`Label Name`**. Click **`Compare`**.\
    \


    <figure><img src="../../../../.gitbook/assets/image (3) (1).png" alt=""><figcaption></figcaption></figure>
11. Important Notes:
    1. Based on the size of your Profiles, the time taken for comparison can vary. You can navigate to a different screen and return to the **`Profile Manager`** page once the results are ready and available.
    2. To optimize browser performance, it is recommended to compare one access setting at a time (in case of large profiles).
12. On the next page, you can see a list of permissions available for each metadata component. Here, you can update the permissions for each component for all the orgs at once.
    * Permissions/ Components that are not available will be denoted by **`X`** in the org.
    *   For the fields that are left blank. For example, in **`Apps`** and **`Datasources`**, no related record type is assigned; hence, nothing shows up or will display '**`No Data Found`**'.

        <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1617594161942.png" alt="" width="563"><figcaption></figcaption></figure>
13. You can also download the report on your local machine using the **`Download Report`** icon at the bottom of this page.

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1617594215774.png" alt="" width="563"><figcaption></figcaption></figure>

16. Select the permissions/components that you want to update.
17. Next, select one of the actions listed below:

    * **`Update Change:`** The changes to the metadata components get updated in the same Org.
    * **`Update & Deploy:`** The changes will be updated in the selected source org and deployed to the Destination Org(s).
    * **`Deploy:`** The changes get deployed only in the selected Destination Org(s). No changes occur in the Source Org.



    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1617594263504.png" alt="" width="563"><figcaption></figcaption></figure>
18. Click **`OK`**.
19. You will be redirected to the [**`Deployment History`**](https://knowledgebase.autorabit.com/arm/docs/monitor-deployments) screen, where you can find the deployment process.

Important Note: You can list the previous profile manager labels from the [**`Profile Manager`**](https://knowledgebase.autorabit.com/arm/docs/how-do-i-deploy-profile-permissionsets) screen.
