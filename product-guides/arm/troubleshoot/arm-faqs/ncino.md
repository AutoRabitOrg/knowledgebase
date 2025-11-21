# nCino FAQs

### Can users query other objects without creating a custom community template?

Standard, published nCino templates are locked by design and **cannot be edited** directly. This is to ensure the integrity of the baseline templates provided out-of-the-box. To add custom logic, filters, or query different objects, a user must create a new, editable template. The most efficient way to do this is by cloning an existing standard template. While you cannot edit a standard template, you can achieve your goal by cloning it and then customizing the clone.

**Action Steps**

1. **Clone the Standard Template:** Navigate to the nCino templates in the module. Select the standard template that most closely matches your requirements (e.g., `nCino-Product Hierarchy Template`) and use the **Clone** function.
2. **Customize the Cloned Template:** The new, cloned template is fully editable. Open it and add your desired custom filter (e.g., add a filter on the `Product Type` field on the appropriate object).
3. **Save and Deploy:** Save your customized template. You can now select and use this new template to perform your nCino data deployments with the custom filter applied.

**Best Practice Recommendation for Applying Filters**

* **Standard Scenarios:** The general best practice for standard nCino migrations is to apply filters on the main **"Entry"** object to pull the required data.
* **Custom Scenarios:** However, when adding a custom filter as described above, it is often more effective and reliable to apply the filter directly on the **child object** that contains the specific field, rather than filtering from the parent object.

### Error: "This session is not valid for use with the API"

This error is encountered if you do not have the "AutoRABITOAuth2" installed in your org.

<figure><img src="../../../../.gitbook/assets/image (1889).png" alt=""><figcaption></figcaption></figure>

**Solution:**

1. Log in to the PROD org.
2. Search for the connected app.
3. Select "Connected App OAuth Usage."
4. Install "AutoRABITOAuth2."
5.  Re-run the job.<br>

    <figure><img src="../../../../.gitbook/assets/image (1890).png" alt=""><figcaption></figcaption></figure>

### Record-Based Migration error use case <a href="#recordbased-migration-error-use-case" id="recordbased-migration-error-use-case"></a>

**Description:** The user was deploying nCino records using the nCino standard template from the source environment to the destination environment.

**Problem Statements**:&#x20;

1. ARM not picking up the **Parent route look up** value on the **Route group** object, thereby resulting in empty parent routes in the destination org.
2. Blank lookup fields that were recently updated from not null to null are not being updated by ARM.

**Resolution**:

1. The parent object must also be included in the deployment for the child object's lookup fields' values to be updated.&#x20;
2. Deploying both **Route** and **Route Group** objects while choosing the **"Insert/update with null values"** option will update the Parent Route lookup field with a null value.

**Other Queries:**

_**a. How exactly does ARM go about retrieving datasets?**_

Preparing object sets (from child to parent) that reflect relationships between the chosen objects is the first step in the dataset retrieval process. Next, pull the data of the object on which the filter is applied (entry object). After then, ARM begins processing sets object by object, starting with the object sets that contain the entry object.

_**b. Why is the nForce\_Route\_c object auto-selected on the Record Configuration screen?**_

For the standard templates, ARM has a default **entry object** defined by the nCino team. So when trying to create a template from a standard tile, ARM auto-select that default object and indicate **"E"** to denote it as an entry object. If you are trying to create a new one via the **New +** icon, the first object will be auto-selected. This is the reason why the **nForce\_Route\_c** object is auto-selected in the below screen.\
![](https://support.autorabit.com/api/v1/threads/241415000087954193/inlineImages/edbsn4b39aa565c2906852fbda870302a7600edea2b5e0e6ef9f0c8f341b1b50df84826707526dcc30592fcc8043ff25e0a91b6795283b9b386867eae31919393d32bb35fc4e4c62e54dc5113f6f01a2572b4?et=18466073fc6\&ha=66aed21f10d32604e94b3effa7f3db7567fe1e80ecf6e6fb3f90e91a61142000\&f=1.png)

_**c. To pull all required data from parent and child objects, why apply a filter on the child object?**_

In this current scenario, when Route and Route Group are selected, as per our process, we don prepare object sets first, and below are the object sets prepared. Group object is automatically picked since Route Group has a Master-detail relationship with Group.

_Object Set 1: nFORCE\_\_Route\_Group\_\_c, nFORCE\_\_Route\_\_c_

_Object Set 2: nFORCE\_\_Route\_Group\_\_c, nFORCE\_\_Group\_\_c_

*   _**What if the filter is applied on Route Group?**_

    First, we pull data from Route Group based on the filter, and then as per the set-1, we will pull relations of Route with the help of the below query.

    Select **nFORCE\_\_Route\_\_c,nFORCE\_\_Parent\_Route\_\_c** from **nFORCE\_\_Route\_Group\_\_c** where _Id is (route group id's based on filter applied)_\
    Next, if self-references exist on Route, we do retrieve those relations. In the same way, we do process set-2.
*   _**What if the filter is applied on Route?**_

    First, we pull data from Route based on the filter, and then as per the set-1, we will pull relations of Route Group with the help of the below queries.

    _Select Id from nFORCE\_\_Route\_Group\_\_c where nFORCE\_\_Parent\_Route\_\_c in (route id's based on filter applied)_\
    &#xNAN;_&#x53;elect Id from nFORCE\_\_Route\_Group\_\_c where nFORCE\_\_Route\_\_c in (route id's based on filter applied)_\
    Next, if self-references exist on Route Group, we do retrieve those relations. In the same way, we do process set-2.

In the second case, if Route Group has any other Route via the _nFORCE\_\_Parent\_Route\_\_c_ field other than the route that is picked as a part of the query applied, that will not be considered. But in case one, we do consider data from both _nFORCE\_\_Route\_\_c_ and _nFORCE\_\_Parent\_Route\_\_c_ fields.

So, in the case of custom configuration, the best practice is to apply a filter on the child object.\
\
**Exceptional Scenario:** Now, I would like to highlight here one more exceptional case where you need to have a look at considering the entry object when the below objects are part of your customized scenario.\
\
No matter whether it is parent relation or child relation, as per the nCino design, data for the objects on the right side have to be pulled only based on objects on the left side. So when your scenario includes any of the below object pairs, the filter has to be applied on left-side objects.

### How to send custom label translations from one nCino environment to another

To select the language translations and for you to view them in the list, they need to be enabled under your source salesforce org first. Follow the below steps to perform the translation deployments:

* Under source Salesforce org, go to **Setup > Translation Workbench > Translation Language Settings** and enable the appropriate language.
* Once enabled, go to ARM and try to retrieve the components under **Translations**. You will observe the languages populated.
* Create a new deployment by selecting the **custom object translations**, its relevant languages under translations, and the custom object. Your target environment should have custom label translations now.

Please refer to the article: [Working with Translation in ARM](../best-practices/working-with-translations-in-arm.md) for more detailed information.

### Conditional rendering references in the 'Screen' sections are not included when using the nCino standard UI template <a href="#conditional-rendering-references-in-the-screen-sections-are-not-included-when-using-the-ncino-standa" id="conditional-rendering-references-in-the-screen-sections-are-not-included-when-using-the-ncino-standa"></a>

The _views_ and the _self-references_ screens sections were not picked up during the feature deployment using the nCino standard UI migration template. This is our top priority, and our development team is working hard to remedy the problem as quickly as possible. After running the nCino UI migration template, please run the Screen UI template to pick up all the missing components as a workaround.
