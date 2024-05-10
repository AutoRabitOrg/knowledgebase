# Ignoring violations

There are multiple ways to ignore false positives or avoid unwanted violations in [CodeScan](https://www.codescan.io/).

### Marking False Positives <a href="#marking-false-positives" id="marking-false-positives"></a>

When viewing your violations inline, **SonarQube™** allows you to mark **False Positives** to prevent further alerts about certain issues in your code. This will block that violation from appearing until it is unblocked.

This feature will not carry the false positive between projects.\
**For example**, if you mark an issue as a false positive in ProjectOne and create ProjectTwo from the same code source, the issue will still be present in ProjectTwo until it is marked otherwise.

### Using suppressUnitTestViolations parameter <a href="#using-suppressunittestviolations-parameter" id="using-suppressunittestviolations-parameter"></a>

For each rule we have provided the parameter **suppressUnitTestViolations**. This stops any violations of this rule being reported in test methods.

There are three options for **suppressUnitTestViolations** in the rule configuration when adding a rule to your custom Quality Profile: **Display**, **Suppress** and **Default**.  **Display** will always throw a violation in test classes, **Suppress** will never throw a violation in test classes. **Default** will be either **Suppress** or **Display** based on if the rule applies to test classes. Default will always be set to **Display** unless shown otherwise.\
\
**For example**, setting **suppressUnitTestViolations** to **Suppress** for the rule **AvoidSoqlInLoops** would ignore the violation below:

```
@IsTest
class newClass {
   void method1(){
     for (int i = 0; i < 10; i++){
       insert new Account(name = ‘Name ’ + i);
     }
   }
}

```

### Using @SuppressWarnings <a href="#using-suppresswarnings" id="using-suppresswarnings"></a>

**SonarQube™** allows you to mark **False Positives** to prevent further alerts about certain issues in your code but these changes will not be remembered if you have multiple environments that aren’t linked together.

Using the **@SuppressWarnings** annotation allows you to block rule violations for certain classes and methods.

The following will ignore all rule violations for the **class Test1**:

```
@SuppressWarnings(‘all’)
class newClass {
   void method1(){
     for (int i = 0; i < 10; i++){
       insert new Account(name = ‘Name ’ + i);
     }
   }
}
```

Whereas this would ignore only the rules given to **@SuppressWarnings** as parameters within **method1**:

```
class newClass {
  @SuppressWarnings(‘cs.AvoidSoqlInLoops’)
   void method1(){
     for (int i = 0; i < 10; i++){
       insert new Account(name = ‘Name ’ + i);
     }
   }
}
```

The same method can also be used for **fields**:

```
class newClass {
  @SuppressWarnings(‘sf:UnusedPrivateField’)
  integer x;
}
```

**The names of the rules can be found in:**

* **SonarQube™/**[**CodeScan Cloud**](https://www.codescan.io/products/cloud/), by clicking on a specific rule in the Rules menu.\
  ![image.png](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image\(293\).png)
* **IntelliJ**, next to the rule violations themselves when a violation is selected.\
  CodeScan Rules found in IntelliJ\
  ![image.png](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image\(294\).png)

**The syntax is as follows:**

* Use _**@SuppressWarnings(‘cs.RULENAME’)**_ for a specific rule name
* _**@SuppressWarnings(‘sf:RULENAME’)**_ is also allowed
* Use _**@SuppressWarnings(‘cs.RULENAME, cs.OTHERULE’)**_ to specify multiple rules, separating each new rule with a comma
* Use _**@SuppressWarnings(‘all’)**_ to ignore all rules

### Using //NOSONAR <a href="#using-nosonar" id="using-nosonar"></a>

This can be used to ignore all rules on a single line:

```
class newClass {
   void method1(){
     for (int i = 0; i < 10; i++){
       insert new Account(name = ‘Name ’ + i); //NOSONAR
     }
   }
}
```
