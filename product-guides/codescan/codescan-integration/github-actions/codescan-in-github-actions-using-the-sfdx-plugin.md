# CodeScan in Github Actions using the SFDX Plugin

Integrating CodeScan into your Github pipeline is easy with our sfdx plugin. There are only a few lines to add to your **.YML file** to run CodeScan when a build is triggered.

{% hint style="info" %}
**Note:** The following is based on a docker pipeline with **Java** and **Node** installed in the container.
{% endhint %}

First, we'll need to add your [CodeScan](https://www.codescan.io/) token as a variable we can access in our **.YML file**.

* Open your project and navigate to **Repository Settings > Repository Variables** (you'll find this under Pipelines).
* Add your token with the name **codescan\_token** and check the **Secured** box. To learn how to generate a token, see [HERE](https://knowledgebase.autorabit.com/codescan/docs/generate-a-security-token).

Now you'll be able to access this variable by using **$codescan\_token** in your **.YML file**.

Add the following into your **.YML file** in the workflow:

{% code overflow="wrap" fullWidth="false" %}
```
name: CI

on:
  push:
    branches:
    - master
  pull_request:
    branches:
      - master
      - feature/**

jobs:
  build:
    runs-on: ubuntu-latest
    env:    # The variables to set for your project and organization
      codescan_org: 'your-organization-key'
      codescan_project_key: 'project-key'
      codescan_token: ${{ secrets.codescan_token }}
    steps:
    - uses: actions/checkout@v1
    - uses: actions/setup-node@v1.1.0
    - name: Install SFDX
      env:
        SFDX_AUTOUPDATE_DISABLE: false
        SFDX_USE_GENERIC_UNIX_KEYCHAIN: true
        SFDX_DOMAIN_RETRY: 300
        SFDX_PROJECT_AUTOUPDATE_DISABLE_FOR_PACKAGE_CREATE: true
        SFDX_PROJECT_AUTOUPDATE_DISABLE_FOR_PACKAGE_VERSION_CREATE: true
      run: |
# Installing the Salesforce CLI
        mkdir /tmp/sfdx
        wget -q https://developer.salesforce.com/media/salesforce-cli/sfdx-linux-amd64.tar.xz -O /tmp/sfdx/sfdx-linux-amd64.tar.xz
        tar xJf /tmp/sfdx/sfdx-linux-amd64.tar.xz -C /tmp/sfdx/ --strip-components 1
        /tmp/sfdx/install
 
# Installing the CodeScan plugin
        echo y|sfdx plugins:install sfdx-codescan-plugin

# What to run if a push triggers the build.
    - name: Run Codescan On Push
      if: github.event_name == 'push'
      env:  
        branch_name: ${{github.ref}}
        branch_type: 'LONG'
      run: |
        sfdx codescan:run --token=$codescan_token --projectkey=$codescan_project_key --organization=$codescan_org -Dsonar.branch.name=${branch_name##*/} -Dsonar.branch.type=$branch_type
    
# What to run if a pull request triggers the build.
    - name: Run Codescan On PR
      if: github.event_name == 'pull_request'
      env:  
        branch_name: ${{github.head_ref}}
        target: ${{github.base_ref}}
        branch_type: SHORT 
      run: |
        sfdx codescan:run --token=$codescan_token --projectkey=$codescan_project_key --organization=$codescan_org -Dsonar.pullrequest.branch=${{github.head_ref}}
-Dsonar.pullrequest.base=${{github.base_ref}} -Dsonar.pullrequest.key=${{github.event.number}}
```
{% endcode %}

You will need to replace the placeholder variables (in **bold**) in the env section of the script with your **Project Key** and **Organization Key**.

The branch names and comparisons are set by the following parameters:

**`sonar.pullrequest.key`**: The pull request number\
**`sonar.pullrequest.base`**: The comparison branch for pull request type branches\
**`sonar.pullrequest.branch`**: The name of the branch

The conditionals in your script determine what triggered the build and by defining the branch type, name and target using [Bitbucket pipeline's built in variables](https://support.atlassian.com/bitbucket-cloud/docs/variables-and-secrets/), you can create a project that gives you visibility on your new code while allowing you to plan your refactoring effort.

By default, the CodeScan SFDX plugin will fail if the Quality Gate fails. If you would prefer that the build passes despite the quality gate, use the **--nofail** tag when calling **sfdx codescan:run**.

You can find a complete list of flags and examples on our [npm plugin page](https://www.npmjs.com/package/sfdx-codescan-plugin).
