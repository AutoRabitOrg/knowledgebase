# What Is Cyclomatic Complexity?

## What Is Cyclomatic Complexity?&#x20;

Cyclomatic complexity in [CodeScan](https://www.codescan.io/) is calculated by the number of decision points in a method (like if, while, for, and case statements), plus one for the method entry. A higher cyclomatic complexity indicates more decision points, making the code harder to read, maintain, and test.

## **Complexity Levels:**

* **1-4 (Low Complexity):** Simple methods, easy to understand and maintain.
* **5-7 (Moderate Complexity):** Acceptable but should be monitored.
* **8-10 (High Complexity):** Consider refactoring to simplify.
* **11+ (Very High Complexity):** Strongly recommended to refactor.

## **Significance of Report Level (default 10):**

The report-level parameter in tools that analyze cyclomatic complexity flags methods with a complexity of 10 or higher for further inspection. This helps identify methods that might need refactoring due to their complexity.

## How Is Cyclomatic Complexity Calculated?

For example, the method below would have a cyclomatic complexity of **5**.

```
public void newMethod() {
     for(Integer i = 0; i < 100; i++){
      if (a == b && b == c){
        doStuff();
      } else if(a != b) {
        doOtherStuff();
      }
     }
   }
```

This counts:

* The entry to the method
* The entry to the _**for**_ loop
* The _**if**_ statement and the first conditional
* The second conditional in the _**if**_ statement
* The _**elseif**_ statement

This does not include:

* _**else**_ statements
* _**when else**_ in switch statements

The cyclomatic complexity for a class will be the average complexity between all methods in that class.

## **How Do I Reduce Cyclomatic Complexity?**

* **Break Down Methods:** Split complex methods into smaller, more focused functions.
* **Use Helper Methods:** Extract repetitive logic into separate methods.
* **Simplify Conditionals:** Refactor nested if statements into simpler, sequential checks.
* **Use Switch Statements:** For multiple conditions, switch statements can streamline the logic.

Following these guidelines will help you write cleaner, more maintainable, and less error-prone Apex code.

