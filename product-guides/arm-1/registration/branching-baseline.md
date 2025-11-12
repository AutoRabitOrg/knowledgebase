# Branching Baseline

{% hint style="info" %}
**Note:** This article is for the **Org Administrator** in particular. The actions discussed in the article are not available to general users. &#x20;
{% endhint %}

### Branching Baseline: Overview <a href="#branching-baseline-overview" id="branching-baseline-overview"></a>

Components are retrieved and committed from a Salesforce org to a version control branch using **Branching Baseline**. This helpful feature can deal with a lot of metadata and is ideal for (but not limited to) the following two scenarios:

* Branching Baseline will sync the branch to its mapped Salesforce org, so they are in sync.
* Users can create a new branch and update it with an existing Salesforce Org.

### Execute a Branching Baseline Commit <a href="#execute-a-branching-baseline-commit" id="execute-a-branching-baseline-commit"></a>

1. Log in to your ARM account.
2.  Hover your mouse over the **`Settings`** module and click on **`Branching Baseline`**.\


    <figure><img src="../../../.gitbook/assets/image (5) (1) (1) (1) (1) (1).png" alt="" width="233"><figcaption></figcaption></figure>
3.  From the Branching Baseline screen, click on New Branching Baseline.\
    \


    <figure><img src="../../../.gitbook/assets/image (6) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

&#x20;

4. The Branching Baseline screen appears where you need to fill in the details listed below:&#x20;
   1. Enter a Label Name.&#x20;
   2. Select your Salesforce Org as the source of the commit.&#x20;
   3.  Select your Repository and Branch to which you would like to commit code. \
       \


       <figure><img src="../../../.gitbook/assets/image (7) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

{% hint style="info" %}
**Important Note:** For Version Control registered in the SFDX structure, specify the Source Folder from where the metadata will get fetched. If you cannot view the source folder in the drop-down, the source folder is not listed in the Package Directory under the sfdx-project.json file in your local directory. For a detailed procedure of adding the source folder in the Package Directory, do refer to the article: [Salesforce DX metadata format](https://knowledgebase.autorabit.com/product-guides/arm/arm-features/salesforce-dx/salesforce-dx-metadata-format).
{% endhint %}

5. Exclude baseline managed package changes: This option will ensure that only unpackaged components are retrieved into your version control branch. &#x20;

{% hint style="info" %}
**Important Note:** If a managed package is installed in a Salesforce org on a date, but a different date is given on the CI Job created, then the installed managed package numbers are also loaded. We can exclude baseline managed package changes to skip those installed managed packages. As all installed packages in a Salesforce org come from a Managed source (AppExchange, etc.), such managed components can be excluded from a baseline operation.
{% endhint %}

6. Delete existing metadata and commit new changes: This option will delete all existing metadata and commit all the metadata members from the Salesforce org to the Version Control repository, thereby deleting the existing contents of a branch before the Baseline operation. In short, if you want zero components in your repository, then this option will allow you to delete all the existing metadata and commit all the metadata members from the salesforce org to the version control repository.
7. Use Bulk Retrieve: This option retrieves the components in batches. The users need to specify the batch size for Profile components and other components in which they will get retrieved.&#x20;
8. Specify the batch size for both profile and remaining components to retrieve records: You need to specify for profile components and other components in which ARM will retrieve. So, the default size for the profile is 500, and for other components is 2,000. You can modify it as per your requirement. Bulk retrieval helps run large jobs that would exceed normal processing limits—you can deploy up to 10,000 files at once or a maximum size of 14MB. Using Batch Size, you can process records in batches to stay within platform limits. If you have a lot of records, processing records through batches is the best option.&#x20;
9. When the user selects Salesforce as the retrieval type in the Branching Baseline screen, the system automatically fetches the Automatically Exclude Salesforce Option along with the metadata list based on the global configuration set by the Admin. The user can review these settings and, if necessary, modify the metadata exclusions by adjusting the list according to their specific requirements.&#x20;
10. Click OK. A notification pops up displaying that the branching baseline operation is initiated.&#x20;
11. You will be redirected to the Branching Baseline summary page, where you can find the status of your branching baseline operation recently created. The status column will indicate whether your baseline operation was completed or failed.&#x20;

{% hint style="info" %}
**Point to Note:** Branching baseline commits for the SVN repository may take 10 minutes to complete.&#x20;
{% endhint %}

**More Options**

<figure><img src="../../../.gitbook/assets/image (8) (1).png" alt=""><figcaption></figcaption></figure>

1. Info: This will give information about the Salesforce Org and the Version Control Repository/ Branch selected for the Branching Baseline operation.&#x20;
2. Revision #: View the revision generated at the Version Control along with the filename status. You can even download the report if required.&#x20;
3. Status: View the status of the Branching Baseline operation.
4. Log: View the execution log of the Branching Baseline operation.&#x20;
5. Status Details:  \
   The system now displays the status of the branching baseline, indicating whether it has partially succeeded or failed. In cases of partial success, detailed, batch-wise information is provided, including the reasons for failure within each batch. Additionally, an XML file is available for download for each batch, allowing users to review the details or troubleshoot as needed.&#x20;

<table data-header-hidden><thead><tr><th width="126"></th><th></th></tr></thead><tbody><tr><td>Status </td><td>Description </td></tr><tr><td><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABcAAAAXCAIAAABvSEP3AAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAKqSURBVDhPpVRLaxRBEK6at7sbJy8xxldiWIUYvAVdEE3w4s1bPEgQLyIIevNgQBAPKurP8CfkoBe9BAQPGvVgUCSGkJeJG1mym+2e6bJ6ZvY1myCS77Bd/aivvv6qZ5GIYM8wknFvaNEiFKxLqhCYAL4FngFrAhSAidBl0cJScW5xI1TUvT9zNt+X8+wkLcWyJujjlpIhIEKnBVkTlpmFwEDIkZyefv/u6yKf91z30bXzo/mDSVrqRgGA5NIIzMzxFmkKjlUIJUGl7SAIFWupVEVV8n4DLSw2goOahcGXclGL4ikakLEw69mGnsM+x3FtSx+qIbmRUqyBhVAxIHaHM3MmOAYUJfA2l2KbltZKP1c3Q6X8rDdyvCfnOZxiGFpHwhKGvKuJ/heWZSGjzsJ31sssuWH3v8AONLOslqsrlZCDXRh25EYTaSDndDhWwvL9T+X2zOqHX0K7Gp2IfnmrHjTAE35BJsHlI+6Tc/0HPLvmLqkvG+W7M8uzvwW/jjiJ9+KcaBL1PwkxUHT1RPZp4bDv2K2+KPWjVL31duHTukCqXSEZuduE/HaikCkmT/pTo/29rmnbre5yjxTCXLFy58387IbgirXaTUAwSE3k/YeFY11sB1C6R3GnCXClXL35+tvMcsXUb4x3Y2t40GImTvmPLwzlODdaj1nS3zQf7cs4L8YGxw55JAUFkgKhdCAwlNeH/WcXhzosti6hjpFmYXCVfGfm+fjgSLcJUkAgOR+lvDHcPVUYdKPHGh1rELVp0b3Q9xjwsy+vnBk/2sFEtgomT/feKwz5jpYRI7YiRtqXZvB8frP84NXnfM/++5eGLaCm8gl2djcFzipuS880PMfUGtuwK0t9MUYctYlIsHOPGM0UDM7fjaKOpCwLSSW3I9aYUsr/L4j4F+zjZsSAYyswAAAAAElFTkSuQmCC" alt=""> </td><td>The branching baseline operation is in progress </td></tr><tr><td><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABYAAAARCAIAAABW08vUAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAADGSURBVDhPY/z//z8DZYAJSlMARrAR768sOr790HsoDwhINOL94bwjW1teXJl+9yFUhCQjfrw+mHfk2I4/TBqiDp368lBR4o0A6i87cQKif4q5qRwrVBwIMIwAe3X/659QLhjg0Q8E6EZ8fHi+68Wl9KPLF8FMwa8fCDAT+NfTxxcnvvj4i1G8xjoyjOEEfv1AgDWPwE3hEGX+8RqvfiDAlc1gpjAA9TvPtDGShIpjA0AjcIAfNy6sbz9z+RmUixMMhszOwAAAIsitWpFaAecAAAAASUVORK5CYII=" alt=""> </td><td>The branching baseline is completed </td></tr><tr><td><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABoAAAAYCAIAAABr4HqSAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAOgSURBVEhL5ZRbaBxVGMfnzC1rto25dNesmybpBvvQdkQlBqFItM1LQaEUlELpa6UvpqxNCyUFhRIfqoXkyUukLwYUWrT64O2hBNyk2JfSSIupCU1217Qx2+zOzpyZOVe/yY5Ys6sP0jf/M+zO5f//zTnzzXeQlFJ5dFKj/0ek/xXu30rBKS3Nzd2//pO5sqI5jlA1r6216amdqf7+x3t7I9Pf9Y+40vz86qVLrQu/tuu65FwKgRSkqioRYq2pSdm3b/vBg5phRO4/1Ri3PDtLpz5NYUwDnzIeWlSE4IaUQDR0IxCiaFm7TpwwYrFapKYGuNLCwvr589sqZc/zw3MNKTJEAUxBCAkISE3VdMMoDgzsHh5WNW3jbqjNpRCM5T+ZbFn7vVyxA0Kw6/q2SwkIzijB2KlW4TGe73sYN09PF2ZmouSGNuPy167Fb922bRvsJJlMjo+L3buqq6s+IV7VdjhvHx2NHTqEy2UHuzqlq19+EThOFK7HPcjlmOu6hAaU4bWS2tzcc+4ceu7Z8nLeVVDnmTNtg4PuvXsuIT6ltoeVuZ9Ld+5E4XocLRZd38cwLSndYuHm8eO4WOwbeze2f396ZKT9pZd/eeft+5cvU8PAjDkB4b5fvX0rCtfj8Pq6x6hHYSeBaTpLS9ffOOYWCtbERGJo6Mbp03enpohpepyBB1MaEOo9WI/C9TgPIZ9zL9wFHLiMEcbC7wPKhxBjFDPuMebDLxdg8wWXphmF63HNySRQiBRUClyt6un0Cx99vKW3Nzf85m9Xr/a/937X4cOu4wSCUynBQ5GytXt7FK7HtVkWlQoR0gsCYL04Obk1k/nx5Mn5zz6fPTu6kssNjI11v/4aVMvnjCKkb0t07rGicD2ua2iIdnRwBQWca22tXPDpbHbx++/0zifcSmX6rWxxZuaxri6qKGBAmvbkgQPxdDoKN+yKGxcvzk2ME8YVKaALYCHQDFMJ+wIJCgNCqqZC3zXpRkdfZvCDD+OJRC0I2jw6kHX0aM8rr8Y0TcAQoGN1I3xNQkLzc00jUkIdTF1vTySeGTn1MAvUeAkIguCHCxcqV65Q3wu4YELUTLAOxFQ1ruvmjh192ezTe/duXP5LDXDwmjHGMKnZb79Z+uprI583sAufCWwcvKmUYlnPHznSk8lwzltaWrSHloAGOGj3sGd93zTNcrlcWFxcW16mtq2a5pZEIpXJpLu7wQZBYMXjcXhwLQhqPNn/KEX5A0ThHPOGRbzUAAAAAElFTkSuQmCC" alt=""> </td><td>The baseline operation got failed </td></tr><tr><td><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAeCAYAAABNChwpAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAJMSURBVFhH7ZbNi1JRGMafe71BMLRpo+FOGasZG1y6URA//oOQUNy510UbIVpEq/wnyuyTJAM3bly5EvwaGkUNza8Eo8VEQaadzrmeGZvB8R4jcJE/EM/7eO99H9/zvvdeqfXhI8EGkQiFrzeCzL83xtbAxg38dRPWajWwU6vVKmazGQKBAP9lPdY20Gw2EY/HYTKZMJ1OYbFYUKlUUCqV4Pf7EQqF+JGCMAOiZLNZEolESKPR4MpZEokEcbvdpFgsckUbYQO5XI7EYjHSarW4Qki9XiepVIpHc5iJaDTKI22EmzCfz8Pj8cBsNnOF7p8kqVvyJ8FgEDqdDuVymSurETLQ7/ehKApcLhdX5jADTD8P64NkMsmj1QgZGAwGcDgcPFrADLB/ex6my7JYcYWOYkmWJWq320t1q9UK2h88Wo2QAaPRiNFoxKM5nU4HtDHVMWT8eF/Fp3t38eX5E3xOPkY6nVZ1LYQMLCt1t9uF1+uFz+fDtzfPMDk6xLUHj3D1ToiWX1JNiCBkwGAwYDweYzgccgVwOp2nTSlTg1duL+6EzPDOgQ3fqwKTwMdRE7oFJJPJ8GjB5O0L8rN2yCNCjl895StCaBX46mLEWpWi1+vVXqAm1Kk4QXfDComvjx/GzlSCVUaLtZ8F7AZTKBRgs9nUh5Ddbsckfh/Y3YN8fR8KNcT4+jqJS3u3cHn/QI0vQrgCJ7DE4XBYnXP26fV6UGhiNI5Ok9MtoX0AzeSMf/pOOH33Er/o5WSLFcrNuRktti+lWwNbA/+7AeA3jN4Qa4lHh2oAAAAASUVORK5CYII=" alt=""> </td><td>The branching baseline has been timed out </td></tr><tr><td><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAB4AAAAeCAYAAAA7MK6iAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAFFSURBVEhLY/wPBAwDAJigNN0B4527DwfEx4w/fvwcWUE9ajHdwNC0mPHrYyiLdEC2xYy/PzKwbjVjYH68CSpCGiA7HzOfKWNg5BRjYLy/iuG31xGgF9igMsQBsnzM+OkOA9Pr4wz/RMwZ/iuGMbDcmAaVIR6QZTHLuUqGv0btDMyX2xj+aOQwMN1fysD48y1UljhAssVML/Yz/Adq+yduA+QxMjD8/cnwV6ecgfliI0QBkYA0i///Y2A+V83w17gdzP2nns7AwMrD8Fc+hIHxwzUwJhaQZDHznQVAn9oy/OdVAvMZP1wHpu7PYPZf405gFFSA2cQAklI121plhv9cUkBf8kFFUAEowf1228XwT9gEKoIbkJadgL5j/P8HysEO/rMJAElg3BMAo/Ux3cCoxXQDoxbTDTBeu35nQAqQAeq0MTAAAGLxamzsnAI6AAAAAElFTkSuQmCC" alt=""> </td><td>The branching baseline has been partially successful </td></tr><tr><td><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABoAAAAeCAYAAAAy2w7YAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAD9SURBVEhL7ZZLaoUwFIb/+MAXIugeXIMbdw9uQWkHnTnwMVIElbYnPZfeQe7VG6iDkg/EHA18+OcEIz6/wQVYfP9zxNv7xyVf9P+iMyJtjEhJ3/coy5IrNVqidV3lRVuQJFVVoSgKfqvmpQ27LAv2fUfbtpjnGXEcI4oi2LaNNE15lpqXRNM0oa5rrn5wXRd5nsPzPH6i5nR027ah6zqufrnFeMRTEWV/j2WppwshePSYpyLK/SZzHAdJksjxPUEQyPiOOFyjpmkwDIOUhmGILMswjqNsBhJTQ/i+z7Mfc6oZSEbQohPUeQR121nM/0gbI9LGiLS5THTRkRj4AukYa8KFYY3pAAAAAElFTkSuQmCC" alt=""> </td><td>The branching baseline has no modifications </td></tr></tbody></table>

6. Run: This option allows you to run your branching baseline operation at a later stage. It iterates a new baseline operation to update your branch with the latest metadata from your Salesforce Org.&#x20;
7. Delete: Deletes the branching baseline operation when you don’t require one, like older ones. Once deleted, this cannot be undone.&#x20;

&#x20;
