# Jenkins: java.lang.OutOfMemoryError: Java heap space

This error can be solved by manually adding a parameter to dedicate memory to the build process.

* In your Jenkins project, click **configure**.
* Scroll down to the **Build** section of the page to the Build Step titled **Invoke Ant** with the fields:
  * **Ant Version**: [CodeScan](https://www.codescan.io/) Bundled Ant
  * **Targets**: sonar
* Click on **Advanced**.
* In the **Java Options** field, add the parameter -**Xmx2000m**. This will assign **2000mb** of memory to you build.

If after increasing the heap space you get the error:

{% code fullWidth="true" %}
```
Error occurred during initialization of VM Could not reserve enough space for xxxxxxKB object heap
```
{% endcode %}

The problem may be that you are using a **32 bit version of Java**. Please refer to the following [article](https://knowledgebase.autorabit.com/codescan/docs/error-occurred-during-initialization-of-vm-could-not-reserve) for more details.
