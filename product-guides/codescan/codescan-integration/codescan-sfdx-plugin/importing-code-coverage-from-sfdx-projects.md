# Importing Code Coverage from SFDX projects

CodeScan now provides a way to view your unit test coverage from your SFDX projects in SonarQube™.

### Requirements <a href="#requirements" id="requirements"></a>

* A working **SonarQube™ 9.9+ LTA** installation
* A licensed [**CodeScan**](https://www.codescan.io/) **(4.1+) plugin**
* An [**SFDX**](https://knowledgebase.autorabit.com/codescan/docs/codescan-sfdx-plugin) project linked to your Salesforce Org

### Configuration <a href="#configuration" id="configuration"></a>

Run your tests in your org using _**sfdx force:apex:test:run**_ and the following parameters:

* _**-c**_ This is to return code coverage
* _**-d .**_ This is to define the output directory. In this case the current directory (.).
* _**-u your-username**_ This is the username or alias of the org you would like to run tests in.
* _**-r json**_ This defines the output type as a JSON file.

The end command should look something like as below, run this command:

```
sfdx force:apex:test:run -c -d . -u username -r json
```

If all goes with the plan, you should find a **JSON file** in your project’s directory named this as _**test-result-TESTRUNID.json**_ where _**TESTRUNID**_ is the ID of your test run.

In order to import this into **SonarQube™**, pass the parameter _**sf.testfile**_ with your build.\
For the file you have just created in the root folder of your project, you will need to pass _**sf.testfile=test-result-TESTRUNID.json**_.

If you have created the test file somewhere else, you will need to provide the path relative to the root folder of your project.

With the coverage being imported, the full analysis command will look something like this:

{% code overflow="wrap" %}
```
sfdx codescan:run --token <token> --projectkey my-project-key --organization my-org-key -Dsf.testfile=test-result-TESTRUNID.json
```
{% endcode %}
