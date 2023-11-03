# Error: "Transformed test case failed to compile"

### Description

When I try to execute the test cases task in the ARM TAF Module, it fails. When running a test case, the error message **"Transformed test case failed to compile"** appears.

### Cause

* XPath values in the test file were incorrect
* The test case failed right after login into Salesforce.

### Steps for Resolution

The following is some helpful information that will assist you in resolving the issues mentioned above:

1. Replace the XPath values in the test file and run it again; it should now function.
2. Right after entering into Salesforce, add the **wait seconds**.
