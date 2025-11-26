# Vlocity

### Vlocity Known Limitations <a href="#vlocity-known-limitations" id="vlocity-known-limitations"></a>

1. **Review Artifacts** option is disabled for vlocity components in the **EZ-Commit** screen.
2. Vlocity processing time depends on the size of the Salesforce Org metadata.
3. Vlocity commits remain in an in-progress state for a longer time: This may occur if your org storage limit has been reached. To avoid this, it's better to clean up your unwanted data from your org and re-trigger the vlocity commit once again.
4. AutoRABIT supports the below YAML file structures while uploading the YAML file manually during EZ- Commit operation.

**Structure 1**

<figure><img src="../../../../../.gitbook/assets/image (23) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

**Structure 2**

<figure><img src="../../../../../.gitbook/assets/image (24) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt="" width="498"><figcaption></figcaption></figure>

**Structure 3**

<figure><img src="../../../../../.gitbook/assets/image (25) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
**Note:**

* Structure 1 and Structure 2 can be combined and used together in a single YAML file.
* Structure 3 must be used independently and never be combined with other structures in a single YAML file.
{% endhint %}
