# How is Cyclomatic Complexity calculated?

Cyclomatic complexity in [CodeScan](https://www.codescan.io/) is calculated by the number of decision points in a method.

For example, the below method would have a cyclomatic complexity of **5**.

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
