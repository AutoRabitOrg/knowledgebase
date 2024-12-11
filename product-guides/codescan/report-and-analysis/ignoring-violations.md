# Ignoring violations

CodeScan offers multiple ways to manage false positives and avoid unwanted violations.

### Marking False Positives <a href="#marking-false-positives" id="marking-false-positives"></a>

When reviewing your violations inline, **SonarQube™** allows you to mark **False Positives** to prevent further alerts about certain issues in your code. This will block that violation from reappearing until it is unblocked.

**Important Note:** False positives are not carried across projects. For example, if you mark an issue as a false positive in Project One and create Project Two from the same source code, the issue will still be present in Project Two until it is marked otherwise.

### Using `suppressUnitTestViolations` parameter <a href="#using-suppressunittestviolations-parameter" id="using-suppressunittestviolations-parameter"></a>

Each rule includes the **`suppressUnitTestViolations`** parameter, which determines whether any violations of this rule are reported in test methods.

There are three options for **`suppressUnitTestViolations`** in the rule configuration when adding a rule to your custom Quality Profile: **Display**, **Suppress** and **Default**. &#x20;

* **Display** will always throw a violation in test classes (default)
* **Suppress** will never throw a violation in test classes.&#x20;
* **Default** will be either **Suppress** or **Display** based on whether the rule applies to test classes, with the default set to **Display** unless specified otherwise.\
  \
  **For example**, setting **`suppressUnitTestViolations`** to **Suppress** for the rule **`AvoidSoqlInLoops`** would ignore the violation below:

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

The `@suppresswarnings` annotation provides a way to block rule violations for specific classes, methods, and fields. Although **SonarQube™** allows you to mark **False Positives** to prevent further alerts about certain issues in your code, these changes are not remembered if you have multiple environments that aren’t linked together. Using the **`@SuppressWarnings`** annotation ensures consistency across multiple environments.

The following will ignore all rule violations for the **class Test1**:

<pre class="language-html"><code class="lang-html"><strong>@SuppressWarnings(‘all’)
</strong>class newClass {
   void method1(){
     for (int i = 0; i &#x3C; 10; i++){
       insert new Account(name = ‘Name ’ + i);
     }
   }
<strong>}
</strong></code></pre>

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

* **SonarQube™/**[**CodeScan Cloud**](https://www.codescan.io/products/cloud/), by clicking on a specific rule in the Rules menu.

<figure><img src="../../../.gitbook/assets/image (427).png" alt=""><figcaption></figcaption></figure>

* **IntelliJ**, next to the rule violations themselves when a violation is selected.\
  CodeScan Rules found in IntelliJ

<figure><img src="../../../.gitbook/assets/image (428).png" alt=""><figcaption></figcaption></figure>

**The syntax is as follows:**

* Use _**@SuppressWarnings(‘cs.RULENAME’)**_ for a specific rule name
* _**@SuppressWarnings(‘sf:RULENAME’)**_ is also allowed
* Use _**@SuppressWarnings(‘cs.RULENAME, cs.OTHERULE’)**_ to specify multiple rules, separating each new rule with a comma
* Use _**@SuppressWarnings(‘all’)**_ to ignore all rules

### Using //NOSONAR <a href="#using-nosonar" id="using-nosonar"></a>

The //NOSONAR comment suppresses all rules for a single line of code:

Example:

```
::: class newClass {
   void method1() {
     for (int i = 0; i < 10; i++) {
       insert new Account(name = 'Name ' + i); //NOSONAR
     }
   }
}
```
