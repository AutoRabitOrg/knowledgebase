# Integrating CodeScan in GitLab

### Overview <a href="#overview" id="overview"></a>

Integrating CodeScan into your GitLab pipeline is easy with our SFDX plugin. There are only a few lines to add to your **.YML file** to run CodeScan when a build is triggered.

{% hint style="info" %}
**Note:** The following is based on a docker pipeline with **Java** and **Node** installed in the container.
{% endhint %}

### How to do it? <a href="#how-to-do-it" id="how-to-do-it"></a>

First, we'll need to add your CodeScan token as a variable we can access in our **.YML file**.

1. Open your **project** and navigate to **`Settings > CI/CD`** then expand the **`Variables`** section.
2. Add your token with the name **`CODESCAN_TOKEN`** and check the masked variable box. To learn how to generate a token, see [HERE](https://knowledgebase.autorabit.com/codescan/docs/generate-a-security-token).
3. You'll be now be able to access this variable by using **$CODESCAN\_TOKEN** in your **.YML file**.
4. Add the following into your **.YML file**:

<pre data-overflow="wrap" data-full-width="true"><code><strong>image: salesforce/salesforcedx:latest-full
</strong>
CodeScan:
  rules:
- if: $CI_COMMIT_REF_NAME =~ /^[&#x3C;branch>]/ &#x26;&#x26; $CI_PIPELINE_SOURCE =~ /^[push|schedule]/
  variables:
    CODESCAN_CMD: "sfdx codescan:run --token=$CODESCAN_TOKEN --server=&#x3C;server_url> --projectkey=&#x3C;project>--organization=&#x3C;organization> -Dsonar.branch.name=$CI_COMMIT_REF_NAME"
<strong>- if: $CI_PIPELINE_SOURCE == "merge_request_event" &#x26;&#x26; $CI_MERGE_REQUEST_TARGET_BRANCH_NAME =~ /^[&#x3C;branch>]/
</strong>  variables:
    CODESCAN_CMD: "sfdx codescan:run --token=$CODESCAN_TOKEN --server=&#x3C;server_url> --projectkey=&#x3C;project> --organization=&#x3C;organization> -Dsonar.pullrequest.branch=$CI_COMMIT_REF_NAME -Dsonar.pullrequest.base=$CI_MERGE_REQUEST_TARGET_BRANCH_NAME -Dsonar.pullrequest.key=$CI_MERGE_REQUEST_IID"
  script:
- echo y|sfdx plugins:install sfdx-codescan-plugin
<strong>- $CODESCAN_CMD
</strong></code></pre>

| Parameter      | Description                                                                                                                                                                                                                                            |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `project`      | Enter your [project key](https://knowledgebase.autorabit.com/codescan/docs/finding-your-project-key)                                                                                                                                                   |
| `organization` | Enter your [organization key](https://knowledgebase.autorabit.com/codescan/docs/finding-your-organization-keys)                                                                                                                                        |
| `token`        | Enter the CodeScan [security token](https://knowledgebase.autorabit.com/codescan/docs/generate-a-security-token)                                                                                                                                       |
| `server`       | Enter the CodeScan server URL. The default server URL is `https://app.codescan.io`. For _**EU regions**_ users, the server URL would be `https://app-eu.codescan.io`, and for _**AUS regions**_, the server URL will be `https://app-aus.codescan.io.` |
| `branch`       | Name of your branch.                                                                                                                                                                                                                                   |

The pull request details are being set by the following parameters:

* **`sonar.pullrequest.branch:`** Name of the branch containing the changes that need to be merged.
* **`sonar.pullrequest.base:`** The branch where the pull request will be merged.
* **`sonar.pullrequest.key:`** The pull request _key_ or _number_ or _id_.

{% hint style="info" %}
**Note:** The above is a great way to get started scanning with this plugin; however, this script will install the [CodeScan plugin](https://www.codescan.io/products/editor-plugins/) with each run. A better implementation would include this installation in the docker image used.
{% endhint %}

> By default, the **CodeScan SFDX plugin** will fail if the Quality Gate fails. If you would prefer that the build passes despite the quality gate, use the **`--nofail`** tag when calling **`sfdx codescan:run`**.

You can find a complete list of flags and examples on our [npm plugin page](https://www.npmjs.com/package/sfdx-codescan-plugin).

### Scanning Only Pull Request Changes

The script above scans the full branch of the Merge request that triggers the pipeline.

If you want to narrow down results to scanning only files that were changed in this Merge request, there are a couple of additional steps to take.

By adding the following lines to the script, you can generate a comma-separated string of changed files in the Merge request:

{% code overflow="wrap" %}
```
git fetch origin ${CI_MERGE_REQUEST_TARGET_BRANCH_NAME:-$CI_DEFAULT_BRANCH} --quiet

CHANGED_FILES=$(git diff --name-only origin/${CI_MERGE_REQUEST_TARGET_BRANCH_NAME:-$CI_DEFAULT_BRANCH} HEAD | tr '\n' ',' | sed 's/,$//')

echo "CHANGED_FILES=$CHANGED_FILES"
```
{% endcode %}

Then, the **$CHANGED\_FILES** variable can be passed to the merge request scan command. Like this:

**-Dsonar.inclusions=$CHANGED\_FILES**

{% hint style="info" %}
**Note:** The Merge request scan is the one using the **sonar.pullrequest parameters.**
{% endhint %}
