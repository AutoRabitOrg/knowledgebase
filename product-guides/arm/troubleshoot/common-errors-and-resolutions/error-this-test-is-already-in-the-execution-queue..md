# Error: "This test is already in the execution queue."

### Description

When I try to generate a code coverage report for my registered Salesforce org, the test fails with the following error: **"This test is already in the execution queue."**

### Cause

This is most likely to happen if the apex test execution takes a lengthy period.

### Steps for Resolution

Go to **TAF > Apex Test Execution** and clear all of the tests in the queue, then run the code coverage report through ARM again.
