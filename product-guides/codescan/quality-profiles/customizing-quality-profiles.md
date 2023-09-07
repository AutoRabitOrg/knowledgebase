# Customizing Quality Profiles

### Overview <a href="#overview" id="overview"></a>

**Quality Profiles** determine the list of rules used in a scan. Quality Profiles can be customized by adding and removing rules, setting severities, and changing scope where applicable.

To make a custom Quality Profile, you can create a new profile or copy one of our default profiles from the list as a starting point.

Point to Note:

Changes **CAN NOT** be made to the default profiles, only to custom profiles. If you are using a default profile and would like to remove a rule, please make a copy of the default profile and make your changes to the copied profile.

### Creating a Quality Profile <a href="#creating-a-quality-profile" id="creating-a-quality-profile"></a>

To customize the Quality Profile, follow the steps below:

1. Access the Quality Profile menu from the Organization’s home page.\
   ![image.png](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-L9I3GGWQ.png)

![image.png](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-ZN6DBP43.png)

2. Use the **Create** button at the top right of the page to create a new Quality Profile.
3. Enter the **Name** and choose a **Language** for the profile. Additionally, you can give your new profile a **Parent** profile.
4. Click **Create**.\
   ![image.png](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-X2O69ZUR.png)
5. Click on the (![image.png](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image\(246\).png)) icon and then click on **Copy** to copy a default profile.\
   ![image.png](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-87QVNTCL.png)
6. Once you have chosen a name for your profile, click the **Activate More** button to begin your customization.\
   ![image.png](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-MVZOPRZI.png)
7. Use the filters on the left to determine the rules you want to see, and click the **active/inactive** button to add/remove them from your quality profile.\
   ![image.png](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-UQ835NG6.png)
8. You can bulk activate/deactivate rules for your profile using the **Bulk Change** button.\
   ![image.png](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-FRHJH9F7.png)
9. When activating a rule, you will be given the option to change its **severity** and any other parameters the rule may have.\
   ![image.png](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-17UR2Q8T.png)

> **Example**:\
> You can update the severity of the rule to `Major/Critical/Minor/Blocker/Info`![image.png](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-S1CP647S.png)
>
> To use the rule mentioned above, the parameter `minimumCommentDensity` needs to be set to a value. The minimum value is 25. If you use the value of 35 as an example, the density of comment lines of 35 will be considered.
>
> Set the value for `suppressUnitTestViolations`.\
> `Default`: _The Default is actually 'Display' and it will display the unit test violations suppression, means, the issues will get displayed in Test Classes for the parameters._\
> `Display`: _Displays the unit test violations suppression._\
> `Suppress`: _Unit test violations will be suppressed._\
> ![image.png](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-JCL39XMU.png)

### Setting a default Quality Profile <a href="#setting-a-default-quality-profile" id="setting-a-default-quality-profile"></a>

By setting a default Quality Profile, you assign every project without a specific Quality Profile to use the default one. To assign Quality Profiles to specific Projects, use the **Project Settings > Quality Profiles** menu for your project and select the one you would like to use.\
![image.png](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-0IWEUEXH.png)\
\
![image.png](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-AUY9X96R.png)
