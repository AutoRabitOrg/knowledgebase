# CodeScan with Windows Agents

### Requirements <a href="#requirements" id="requirements"></a>

You will need:

1. Jenkins
2. Salesforce CLI
3. Git

### Add Environment Variables <a href="#add-environment-variables" id="add-environment-variables"></a>

* In user environment Path variable, add the **Salesforce CLI** and **Git bin directories**.

<figure><img src="../../../../.gitbook/assets/image (527).png" alt="" width="450"><figcaption></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/image (528).png" alt="" width="395"><figcaption></figcaption></figure>

* In the System environment Path variable add the **Git\cmd**, **Git\usr\bin**, and **Salesforce CLI\bin directories**.

<figure><img src="../../../../.gitbook/assets/image (529).png" alt="" width="450"><figcaption></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/image (530).png" alt="" width="400"><figcaption></figcaption></figure>

### Setup Jenkins <a href="#setup-jenkins" id="setup-jenkins"></a>

1. In [Jenkins](https://knowledgebase.autorabit.com/codescan/docs/jenkins), create a [credential](https://docs.cloudbees.com/docs/cloudbees-ci/latest/cloud-secure-guide/injecting-secrets) containing your CodeScan token ([learn how to find this here](https://knowledgebase.autorabit.com/codescan/docs/generate-a-security-token)).
2. Create a **new Pipeline**.
3. In the **Pipeline script** section you will need to paste in the code with the highlighted variables changed, these are:
   * Your _**credential\_name**_ should be the name of the credential you created.
   * _**my\_project**_ should be the project key you would like to assign to your project.
   * _**my\_organization**_ should be your Organization Key ([learn how to find this here](https://knowledgebase.autorabit.com/codescan/docs/finding-your-organization-keys)).
     * The _**--server=yourserveraddress**_ flag is required for self hosted instances.

{% code overflow="wrap" %}
```
node {

    stage('Pull from Git') {

      git 'https://wherever.com/me/my-repo.git'

    }

    withCredentials([string(credentialsId: 'credential_name', variable: 'codescan_token')]) {
stage('CodeScan') {
sh '''
echo y|sfdx plugins:install sfdx-codescan-plugin
      sfdx codescan:run --token=$codescan_token --projectkey=my_project --organization=my_organization
  exit $?
'''       
}
}
}
```
{% endcode %}

4. Run the **pipeline**. If everything is set up correctly and your Quality Gate passes, you will be able to see you pipeline pass.
5. If your Quality Gate fails, you will see the error in the CodeScan stage of the build.
