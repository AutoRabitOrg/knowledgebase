# Integrating CodeScan with GitHub Actions

{% hint style="info" %}
**Note:** The creation of a project in CodeScan creates a webhook in GitHub.
{% endhint %}

This webhook triggers on pushes to your tracked branch and certain pull request actions. These are: _**pull request opened, reopened, synchronized**_.

The pull request triggers allow your comparisons in CodeScan to be kept up to date if the pull request is updated.

### Running CodeScan SCA jobs from GitHub Workflow <a href="#running-codescan-sca-jobs-from-github-workflow" id="running-codescan-sca-jobs-from-github-workflow"></a>

You can now run CodeScan static code analysis jobs from GitHub workflow. The codescan action will produce a **SARIF report file** with the analysis result.

There are only a few lines to add to your **.YML file** for codescan to be triggered.

First, we'll need to add your CodeScan token as a variable we can access in our **.YML file**.

* Open your project and navigate to **`Repository Settings > Secrets > Add new secret`**.
* Add your token with the name **`codescan_token`** and check the **`Secured`** box. To learn how to generate a token, see [HERE](https://knowledgebase.autorabit.com/codescan/docs/generate-a-security-token).

Now you'll be able to access this variable by using **`$codescan_token`** in your **.YML file**.

If you do not have a workflow setup on your GitHub repository, go to **`Actions > New workflow`** to create a **.yml workflow**.

<figure><img src="../../../../.gitbook/assets/image (522).png" alt=""><figcaption></figcaption></figure>

Add the following into your **.YML file** in the workflow:

```none
name: CI 
on: 
  push: 
    branches: [main] 
  pull_request: 
    branches: [main] 
jobs: 
  build: 
    runs-on: ubuntu-latest 
    steps: 
      - name: Checkout repository 
        uses: actions/checkout@v2 
      - name: Cache files 
        uses: actions/cache@v2 
        with: 
            path: | 
                ~/.sonar 
            key: ${{ runner.os }}-sonar 
            restore-keys: ${{ runner.os }}-sonar 
      - name: Run Codescan On Push 
        if: github.event_name == 'push' 
        uses: codescan-io/codescan-scanner-action@1.5 
        with: 
          organization: ‘Enter organization key here’ 
          projectKey: ‘Enter project key here’ 
          login: ${{ secrets.codescan_token }} 
          generateSarifFile: true 
          failOnRedQualityGate: true 
      - name: Run Codescan On PR 
        if: github.event_name == 'pull_request' 
        uses: codescan-io/codescan-scanner-action@1.5 
        with: 
          organization: ‘Enter organization key here’ 
          projectKey: ‘Enter project key here’ 
          login: ${{ secrets.codescan_token }} 
          scanChangedFilesOnly: true 
          generateSarifFile: true 
          failOnRedQualityGate: true 
          args: | 
            sonar.pullrequest.branch=${{github.head_ref}} 
            sonar.pullrequest.base=${{github.base_ref}} 
            sonar.pullrequest.key=${{github.event.number}} 
      - name: Upload SARIF file 
          uses: github/codeql-action/upload-sarif@v2 
          with: 
            sarif_file: codescan.sarif 
```

You will need to replace the placeholder variables (in single quotes) in the env section of the script with your [**Project Key**](https://knowledgebase.autorabit.com/codescan/docs/finding-your-project-key) and [**Organization Key**](https://knowledgebase.autorabit.com/codescan/docs/finding-your-organization-keys).

**`failOnRedQualityGate`** parameter default status is set to **false**. When set to **true**, the pipeline in the GitHub actions fails if the Quality Gate state changes to red (fails).

The **`failOnRedQualityGate`** parameter is available on _CodeScan scanner action version **1.4**_ and later.

**`scanChangedFilesOnly`** parameter is set to **false** by default.  When set to **true**, the scan will only take changed files into account.

The **`scanChangedFilesOnly`** parameter will only work on a pull request trigger. It is available on CodeScan scanner action version **1.5** and later.

Now, you will be able to view the **.yml workflow** on your repository.

<figure><img src="../../../../.gitbook/assets/image (523).png" alt=""><figcaption></figcaption></figure>

And also check for the name of the master branch on both the CodeScan platform and the Git repository, as the new Git update changed the name of master branch to main.

If the name on the CodeScan platform is not the same as the Git repository, go to your **`CodeScan project`** and then navigate to **`Dashboard > Administration > Branches & Pull Requests > Actions`** and change the **branch name**.

The branch names and comparisons are set by the following parameters:

* **`sonar.pullrequest.key`**: The pull request number
* **`sonar.pullrequest.base`**: The comparison branch for pull request type branches
* **`sonar.pullrequest.branch`**: The name of the branch

The uploaded **SARIF file** in the **.yml** helps you to get the code analysis reports in two ways:

1. For the files already existing in the repository, results can be found under code scanning alerts under the **`Security`** tab on GitHub repository.

<figure><img src="../../../../.gitbook/assets/image (524).png" alt=""><figcaption></figcaption></figure>

2.  For the new files being uploaded to the repository, you can view the analysis during the pull requests on GitHub by clicking on the details:

    * Select the relevant pull request and then click on **`Details`**.

    <figure><img src="../../../../.gitbook/assets/image (525).png" alt=""><figcaption></figcaption></figure>

    * Once you click on the **`Details`**, go to **`Code scanning results > CodeScan`**.

    <figure><img src="../../../../.gitbook/assets/image (526).png" alt=""><figcaption></figcaption></figure>

    * Results are categorized as follows:
      1. **Bugs** and **vulnerabilities** are marked as **ERRORS**.
      2. Major and minor **code smells** are marked as **WARNINGS**.

The **.yml file** helps you run an analysis on the project while linking it to CodeScan.

You can go to the **`CI workflow`** under **`Git actions`** to view the analysis.
