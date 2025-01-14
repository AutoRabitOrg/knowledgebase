# Customizing Quality Profiles

### Overview <a href="#overview" id="overview"></a>

**Quality Profiles** determine the list of rules used in a scan. Quality Profiles can be customized by adding and removing rules, setting severities, and changing scope where applicable.

To make a custom Quality Profile, you can create a new profile or copy one of our default profiles from the list as a starting point.

{% hint style="info" %}
**Note:** Changes **CANNOT** be made to default profiles, only to custom profiles. If you are using a default profile and would like to remove a rule, please make a copy of the default profile and make your changes to the copied profile.
{% endhint %}

### Creating a Quality Profile <a href="#creating-a-quality-profile" id="creating-a-quality-profile"></a>

To customize the Quality Profile, follow the steps below:

1. Access the Quality Profile menu from the Organization’s home page.

<figure><img src="../../../.gitbook/assets/image (42) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../.gitbook/assets/image (43) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

2. Use the **Create** button at the top right of the page to create a new Quality Profile.
3. Enter the **Name** and choose a **Language** for the profile. Additionally, you can give your new profile a **Parent** profile.
4. Click **Create**.

<figure><img src="../../../.gitbook/assets/image (44) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

5. Click on the (![](<../../../.gitbook/assets/image (45) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png>)) icon and then click on **Copy** to copy a default profile.

<figure><img src="../../../.gitbook/assets/image (46) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

6. Once you have chosen a name for your profile, click the **Activate More** button to begin your customization.

<figure><img src="../../../.gitbook/assets/image (47) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt="" width="344"><figcaption></figcaption></figure>

7. Use the filters on the left to determine the rules you want to see, and click the **active/inactive** button to add/remove them from your quality profile.

<figure><img src="../../../.gitbook/assets/image (48) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

8. You can bulk activate/deactivate rules for your profile using the **Bulk Change** button.

<figure><img src="../../../.gitbook/assets/image (49) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

9. When activating a rule, you will be given the option to change its **severity** and any other parameters the rule may have.

<figure><img src="../../../.gitbook/assets/image (50) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt="" width="396"><figcaption></figcaption></figure>

> **Example**:\
> You can update the severity of the rule to `Major/Critical/Minor/Blocker/Info`
>
> ![](<../../../.gitbook/assets/image (56) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png>)
>
> To use the rule mentioned above, the parameter `minimumCommentDensity` needs to be set to a value. The minimum value is 25. If you use the value of 35 as an example, the density of comment lines of 35 will be considered.
>
> Set the value for `suppressUnitTestViolations`.\
> `Default`: _The Default is actually 'Display' and it will display the unit test violations suppression, means, the issues will get displayed in Test Classes for the parameters._\
> `Display`: _Displays the unit test violations suppression._\
> `Suppress`: _Unit test violations will be suppressed._\
>
>
> ![](<../../../.gitbook/assets/image (57) (1) (1) (1) (1) (1) (1) (1) (1) (1).png>)

### Updating Quality Profiles

To make sure that Quality Profiles used on CodeScan projects are up to date, you can find information about recently added rules by navigating to Organization → Quality Profiles:

<figure><img src="../../../.gitbook/assets/image (1) (1).png" alt=""><figcaption></figcaption></figure>

You can review updates and assign new rules to your Quality Profiles to make sure your code is clean and secure.

Also, on the right side, the list of recently deprecated rules is available. We recommended you remove these from the Quality Profiles used:

<figure><img src="../../../.gitbook/assets/image (1) (1) (1).png" alt=""><figcaption></figcaption></figure>
