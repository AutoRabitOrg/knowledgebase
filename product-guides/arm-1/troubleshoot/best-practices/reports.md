# Reports

### How can I calculate the code coverage percentage for specific test classes?

1. Navigate to the **Admin** module.
2. Click on **SF Org Mgmt** (Salesforce Org Management).
3. Find and select the Salesforce org you wish to run the report on.
4. Click the **"Generate Code Coverage Report"** button.
5. A pop-up window will now appear with three options.
6. The correct option for your requirement is the last one: **"Run specified Test"**. Please select this.
7. You can then enter the specific test classes you want to run and review the results.

Please see the screenshot below for your reference.

<figure><img src="../../../../.gitbook/assets/image (2341).png" alt=""><figcaption></figcaption></figure>



### **Why is there a discrepancy between the test coverage average on the SFDC side and our manual calculations?**&#x20;

#### **How Salesforce calculates test coverage**

Salesforce determines aggregate code coverage using the total line ratio method, not by averaging the percentages of individual classes. This means that the overall test coverage is calculated by summing the number of covered lines across all classes and dividing that by the total number of testable lines in the organization. The line ratio method ensures a fair evaluation and focuses on improving the overall quality of the code, rather than allowing smaller classes with perfect coverage to compensate for larger classes that are poorly tested.<br>
