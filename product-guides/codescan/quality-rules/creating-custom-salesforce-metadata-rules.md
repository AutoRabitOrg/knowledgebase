# Configuration for Salesforce Metadata Rules

### Learning Objectives: <a href="#learning-objectives" id="learning-objectives"></a>

After reading this guide, you'll be able to:

* Create a custom Salesforce metadata Quality Profile
* Add Salesforce metadata types for a Salesforce Org analysis
* Add Salesforce metadata suffixes/extension for the analysis

### Create a custom Salesforce Quality Profile <a href="#create-a-custom-salesforce-metadata-rule" id="create-a-custom-salesforce-metadata-rule"></a>

This article explains how to enable the Salesforce Metadata rules in the CodeScan Cloud environment.

1. Login to your **CodeScan** account.
2.  Click on the **`Quality Profiles`** on your main organization page and then click on **`Create`** button.\


    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-SX39IQ7X.png" alt=""><figcaption></figcaption></figure>
3.  Create a new rule by selecting the language as **`Salesforce Metadata`** and name your new profile. You can choose the **`Parent rule`** as an optional.\


    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-GXTN9Z5T.png" alt=""><figcaption></figcaption></figure>
4.  Once you create the new quality profile, you will be navigated to a new page where you need to click on **`Activate More`** button on the left.\


    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-9RF4C3UK.png" alt=""><figcaption></figcaption></figure>
5.  Now, make sure on your left side of the page where you see the name of the rule you created; it is marked as **inactive**.\


    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-MODDGI7N.png" alt=""><figcaption></figcaption></figure>
6. Make sure that you activate the four rules referenced below by clicking on the **`Activate`** button beside the rule.
   * _Record Type ID is Missing_
   * _Object Permissions should not be permissive_
   * _Enforce Org Security Settings_
   * _Custom fields must have a description field_
7.  Once activated, select the **`Active`** button under filters (beside the rule’s name).\


    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-Y9I1SSLZ.png" alt=""><figcaption></figcaption></figure>

### Adding Salesforce metadata types for Salesforce Org analysis <a href="#adding-salesforce-metadata-types-for-the-analysis" id="adding-salesforce-metadata-types-for-the-analysis"></a>

To enable downloading metadata for your Salesforce project, you will need to change some project settings. Remember that the following will only work with code being pulled from Salesforce. &#x20;

If you are using a git repository or any other method of scanning, please skip to the next step.

1.  Once you are done with the activation of the custom rule, go to the project with the rules you wish to run the analysis, and click on **`Project Settings > General settings`**.\


    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-ROWQJY8Z.png" alt=""><figcaption></figcaption></figure>
2.  Click the **`CodeScan`** tab on the left to open the [CodeScan](https://www.codescan.io/) specific settings and access the **`CodeScan Cloud Download Types`**.\


    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-4JN2BR9J.png" alt=""><figcaption></figcaption></figure>
3. The default values are _ApexClass, ApexComponent, ApexPage, ApexTrigger, AuraDefinitionBundle,_ and _LightningComponentBundle_.
4. CodeScan is capable to analyze all metadata types supported by Metadata API of Salesforce. Refer to the [Salesforce Developer API documentation](https://developer.salesforce.com/docs/metadata-coverage) to find the supported metadata types.
5.  Under **`CodeScan Cloud Download Types`**, enter the Salesforce metadata types needed for the analysis, then select the **`Save`** button.\


    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-FNMIT73U.png" alt=""><figcaption></figcaption></figure>

### Adding Salesforce metadata suffixes/extensions for the analysis <a href="#adding-salesforce-metadata-suffixesextensions-for-the-analysis" id="adding-salesforce-metadata-suffixesextensions-for-the-analysis"></a>

1.  On the **`CodeScan`** section, scroll down to **`Scope`**, where you see **`Metadata File Suffixes`**.\


    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-8GI5ZTX1.png" alt=""><figcaption></figcaption></figure>
2.  Add the suffixes for the files to analyze.\


    Point to Note:

    Include your Salesforce metadata types for analysis under the **`Project Settings > General Settings > CodeScan > CodeScan Cloud Download Types`** section for your specific project. Later, add the relevant metadata types' suffixes/extension under the **`Metadata File Suffixes`** section.

    Refer to the [**Salesforce Developer API**](https://developer.salesforce.com/docs/metadata-coverage) documentation to find the supported metadata types and their relevant suffixes/extension.

    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-BDOYFRWV.png" alt=""><figcaption></figcaption></figure>
3. Click **`Save`**.
4.  Run the analysis again by navigating to the **`Project Settings > Project Analysis`** menu and selecting the **`Run Manual Analysis`** button. If your metadata files contain issues, you will see that reflected in the issues list.&#x20;

    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image(179).png" alt=""><figcaption></figcaption></figure>

Note:

Make sure the line count will not show up on the line count breakdown as it is not a **language**. However, the issues will show up in the issues list as seen in the above figure.

### Happy to Help <a href="#happy-to-help" id="happy-to-help"></a>

If you are still having trouble setting up metadata rules after reading the complete documentation, please contact the [support](https://support@codescan.io/) team, and we'll be happy to help.
