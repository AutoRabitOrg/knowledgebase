# Customizing Quality Profiles

### Overview <a href="#overview" id="overview"></a>

**Quality Profiles** determine the list of rules used in a scan. Quality Profiles can be customized by adding and removing rules, setting severities, and changing scope where applicable.

To make a custom Quality Profile, you can create a new profile or copy one of our default profiles from the list as a starting point.

{% hint style="info" %}
**Note:** Changes **CANNOT** be made to default profiles, only to custom profiles. If you are using a default profile and would like to remove a rule, please make a copy of the default profile and make your changes to the copied profile.
{% endhint %}

### Creating a Quality Profile <a href="#creating-a-quality-profile" id="creating-a-quality-profile"></a>

To customize the Quality Profile, follow the steps below:

1.  Access the Quality Profile menu from the Organization’s home page.<br>

    <figure><img src="../../../.gitbook/assets/image (1726).png" alt="" width="339"><figcaption><p>Quality Profile menu</p></figcaption></figure>
2.  Use the **Create** button at the top right of the page to create a new Quality Profile.<br>

    <figure><img src="../../../.gitbook/assets/image (1727).png" alt=""><figcaption><p>Create Quality Profile</p></figcaption></figure>
3. Enter the **Name** and choose a **Language** for the profile. Additionally, you can either extend/copy an existing Quality Profile or create a blank Quality Profile..

<figure><img src="../../../.gitbook/assets/New QP Select 8.7.png" alt="" width="375"><figcaption><p>New Quality Profile</p></figcaption></figure>

4.  Click **Create**.<br>

    <figure><img src="../../../.gitbook/assets/image (1728).png" alt=""><figcaption><p>Create New Quality Profile</p></figcaption></figure>
5.  Click on the more icon and then click on **Copy** to copy a default profile.<br>

    <figure><img src="../../../.gitbook/assets/image (1729).png" alt=""><figcaption><p>Copy a Default Profile</p></figcaption></figure>
6.  Once you have chosen a name for your profile, click the **Activate More** button to begin your customization.<br>

    <figure><img src="../../../.gitbook/assets/image (1730).png" alt="" width="375"><figcaption><p>Activate More</p></figcaption></figure>
7.  Use the filters on the left to determine the rules you want to see, and click the **Activate/Deactivate** button to add/remove them from your quality profile.<br>

    <figure><img src="../../../.gitbook/assets/image (1731).png" alt=""><figcaption><p>Activate/Deactivate</p></figcaption></figure>
8.  You can bulk activate/deactivate rules for your profile using the **Bulk Change** button.<br>

    <figure><img src="../../../.gitbook/assets/image (1732).png" alt=""><figcaption><p>Bulk Change option</p></figcaption></figure>
9. When activating a rule, you will be given the option to change its **severity** and any other parameters the rule may have.

<figure><img src="../../../.gitbook/assets/Seveirty 9.2.png" alt="" width="375"><figcaption><p>Activate</p></figcaption></figure>

> **Example**:\
> You can update the severity of the rule to `Major/Critical/Minor/Blocker/Info`
>
> ![](<../../../.gitbook/assets/Severity List 9.3.png>)
>
> To use the rule mentioned above, the parameter `minimumCommentDensity` needs to be set to a value. The minimum value is 25. If you use the value of 35 as an example, the density of comment lines of 35 will be considered.
>
> Set the value for `suppressUnitTestViolations`.\
> `Default`: _The Default is actually 'Display' and it will display the unit test violations suppression, means, the issues will get displayed in Test Classes for the parameters._\
> `Display`: _Displays the unit test violations suppression._\
> `Suppress`: _Unit test violations will be suppressed._<br>
>
> ![](<../../../.gitbook/assets/TestList 9.4.png>)

### Updating Quality Profiles

To make sure that Quality Profiles used on CodeScan projects are up to date, you can find information about recently added rules by navigating to Organization → Quality Profiles:

<figure><img src="../../../.gitbook/assets/Recently Added Rules 9.5.png" alt=""><figcaption><p>Quality Profiles</p></figcaption></figure>

You can review updates and assign new rules to your Quality Profiles to make sure your code is clean and secure.

Also, on the right side, the list of recently deprecated rules is available. We recommended you remove these from the Quality Profiles used:

<figure><img src="../../../.gitbook/assets/Deprecated Rules 9.6.png" alt=""><figcaption><p>Deprecated Rules</p></figcaption></figure>
