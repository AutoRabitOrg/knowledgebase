# Copado SFDX Integration

Our Integration with Copado SFDX pipelines is currently a modification of their extension from their DevOps exchange. These modifications to the function script and Static Code Analysis Violation object add the following functionality:

* **User stories are scanned after Commit.**\
  This adds a quality gate result to the User Story and creates a branch on the CodeScan project.
* **The Production branch scans are updated on Promotion.**\
  When a change is made in your main branch, CodeScan will scan it to give you a view of the state of your production and accurate delta scans for your User Stories.
* **All User Story results are added to the Static Analysis Results object for review on the Copado platform.**
* **A single project will exist in CodeScan for each Copado Pipeline.**

{% hint style="info" %}
**Note**: Copado cannot be integrated with On-Premises/Self-Hosted CodeScan.
{% endhint %}

### CodeScan Project Setup

First create a GitHub, BitBucket, or GitLab project in CodeScan.  This will serve as the project for your Copado Pipeline and will run the analysis in CodeScan for all Production deployments automatically.  Make sure to create the project on the main/master branch of your repository.

See below for our articles on creating these projects:

* [Creating a GitHub Project](../../getting-started/using-codescan/adding-projects-to-codescan/add-a-project-to-codescan-from-github.md)
* [Creating a Bitbucket Project](../../getting-started/using-codescan/adding-projects-to-codescan/add-a-project-to-codescan-from-bitbucket.md)
* [Creating a GitLab Project](../../getting-started/using-codescan/adding-projects-to-codescan/adding-a-project-to-codescan-from-gitlab.md)

### Copado Extensions Setup

As mentioned, this is an extension of Copado's SFDX integration with CodeScan. &#x20;

If you haven't already, please follow the instructions on their SFDX Pipelines documentation or use the PDF attached here.

{% file src="../../../../.gitbook/assets/Copado Labs - CodeScan Integration.pdf" %}

After installing the CodeScan Integration as Copado intended, you can make some improvements.

### CodeScan Object Modifications

First, you will need to add two fields to the copado\_\_Static\_Code\_Analysis\_Violation\_\_c object in setup.

1. **Field Name**: CSExtKey\
   **API Name**: CSExtKey\_\_c\
   **Type**: text\
   **Length**: 255\
   **ExternalId**: true
2. **Field Name**: CSProject\
   **API Name**: CSProject\_\_c\
   **Type**: text\
   **Length**: 255\
   **ExternalId**: false

### Function Modifications

Then, navigate to the functions tab and find the **Run CodeScan QIF** function.

<figure><img src="../../../../.gitbook/assets/image (1546).png" alt=""><figcaption></figcaption></figure>

Under the script tab, click the lower edit button and replace the script with the following:

<details>

<summary>Expand to view script</summary>

```
echo $DataJson
echo $branchesAndFileIdJson
echo $git_json
USER_STORY=$(jq -r '.userStoryId' <<< $DataJson)
BRANCH=$(jq -r '.originBranch' <<< $branchesAndFileIdJson)
echo "param branchesAndFileIdJson =  $branchesAndFileIdJson"
echo "param TOKEN = $TOKEN"
echo "param SERVER = $SERVER"
echo "param PROJECT_ID = $PROJECT_ID"
echo "param ORGANIZATION = $ORGANIZATION"
echo "param BRANCH = $BRANCH"
echo "param USER_STORY = $USER_STORY"
echo "param PARENT_ID = $PARENT_ID"
echo "param COPADO_PROJECT = $COPADO_PROJECT"
CS_MAIN_BRANCH="main"
OUTPUT_JSON="output.json"
OUTPUT_CSV="violations.csv"
API_VERSION="65.0" # change if your org requires a different version
CSV_STRING=""
exitCode=0
SFDX_ACCESS_TOKEN="$CF_SF_SESSIONID" sf org login access-token --alias copadoOrg --instance-url "$CF_SF_ENDPOINT" --no-prompt

# Now pulls the Test ID from the job execution and queries for the user story
# if run from the Run Tests button 
echo "
if('$PARENT_ID' != ''){
  string recId='$PARENT_ID';

  copado__Test__c test = [
      SELECT copado__User_Story__c FROM copado__Test__c WHERE Id = :recId LIMIT 1
  ];

  System.debug('OUTPUT_VAR'+':'+test.copado__User_Story__c);
}
" > /tmp/userstory-run.apex


if [[ -z "$USER_STORY" && -n "$PARENT_ID" ]]
then  
  USER_STORY=$(sf apex run --file /tmp/userstory-run.apex --target-org copadoOrg --json | sed -n 's/.*OUTPUT_VAR:\(.*\)\\n.*/\1/p' | sed 's/\\n.*//')
fi

# Find the Project Name (if not present) based on the User Story Id
echo "
if('$PARENT_ID' != ''){
  string recId='$USER_STORY';

  copado__User_Story__c userStory = [
      SELECT copado__Project__r.Name FROM copado__User_Story__c WHERE Id = :recId LIMIT 1
  ];

  System.debug('OUTPUT_VAR'+':'+userStory.copado__Project__r.Name);
}
" > /tmp/project-run.apex


if  [[ -z "$COPADO_PROJECT" ]]
then  
  COPADO_PROJECT=$(sf apex run --file /tmp/project-run.apex --target-org copadoOrg --json | sed -n 's/.*OUTPUT_VAR:\(.*\)\\n.*/\1/p' | sed 's/\\n.*//')
fi


echo "****************************"
echo "****************************"
echo "User Story is: $USER_STORY"
echo "****************************"
echo "****************************"
echo "Copado Project is: $COPADO_PROJECT"
echo "****************************"
echo "****************************"

# Determine changed files in User Story
copado -p "finding changed files...."

echo "
if('$USER_STORY' != ''){
  string recID='$USER_STORY';
  List<String> filePaths = new List<String>();

  List<copado__User_Story_Metadata__c> components = [
      SELECT Name,copado__Metadata_API_Name__c,copado__Unique_ID__c,copado__Type__c
      FROM copado__User_Story_Metadata__c
      WHERE Copado__User_Story__c = :recId
  ];

  for (copado__User_Story_Metadata__c component : components) {
      if (component.copado__Unique_ID__c != null) {
          System.debug(component.copado__Metadata_API_Name__c);
          System.debug(component.copado__Type__c);

          filePaths.add('**/'+component.copado__Metadata_API_Name__c+'*');
      }
  }

  // Convert list to a comma-separated string
  string exclusions = String.join(filePaths, '*,');
  System.debug('OUTPUT_VAR'+':'+exclusions);
}
" > /tmp/files-run.apex

OUTPUT=$(sf apex run --file /tmp/files-run.apex --target-org copadoOrg --json)

CHANGED_FILES=$(echo "$OUTPUT" | sed -n 's/.*OUTPUT_VAR:\(.*\)\\n.*/\1/p' | sed 's/\\n.*//')

echo "****************************"
echo "****************************"
echo "Changed files include: $CHANGED_FILES"
echo "****************************"
echo "****************************"

copado -p "Cloning repo..."
copado-git-get $BRANCH

copado -p "Running codescan on User Story..."
sfdx codescan:run --token=$TOKEN --server=$SERVER --projectkey=$PROJECT_ID --organization=$ORGANIZATION -Dsonar.pullrequest.base=$CS_MAIN_BRANCH -Dsonar.pullrequest.branch="$COPADO_PROJECT" -Dsonar.pullrequest.key=$BRANCH -Dsonar.inclusions="$CHANGED_FILES" --json 2>&1 | tee /tmp/result.json \
    || exitCode=$?
echo "Codescan completed. exit code: $exitCode"
copado -u /tmp/result.json

copado -p "Creating Static Code Analysis Result record..."

cat > /tmp/create-parent.apex <<'APEX_EOF'
if('${USER_STORY}' != ''){
  String recID='${USER_STORY}';
  List<copado__User_Story__c> userStories = [
    SELECT Id FROM copado__User_Story__c WHERE Id = :recID OR Name = :recID LIMIT 1
  ];
  Id usid = userStories.isEmpty() ? null : userStories[0].Id;

  if (usid != null) {
    Id recTypeId = Schema.SObjectType.copado__Static_Code_Analysis_Result__c
      .getRecordTypeInfosByName().get('CodeScan').getRecordTypeId();

    copado__Static_Code_Analysis_Result__c scar = new copado__Static_Code_Analysis_Result__c(
      recordtypeId = recTypeId,
      copado__User_Story__c = usid,
      copado__Details__c = '${SERVER}/dashboard?id=${PROJECT_ID}&pullRequest=${BRANCH}'
    );
    insert scar;
    System.debug('OUTPUT_SCAR_ID:' + scar.Id);

    String parentId = '${PARENT_ID}';
    if(parentId != '') {
      List<copado__Result__c> results = [SELECT Id FROM copado__Result__c WHERE Id = :parentId LIMIT 1];
      if(!results.isEmpty()) {
        update new copado__Result__c(
          Id = results[0].Id,
          copado__Error_Message__c = 'CodeScan analysis started. Fetching and processing issues...',
          copado__Link__c = '${SERVER}/dashboard?id=${PROJECT_ID}&pullRequest=${BRANCH}'
        );
      }
    }
  }
}
APEX_EOF

sed "s|\${USER_STORY}|$USER_STORY|g; s|\${PARENT_ID}|$PARENT_ID|g; s|\${SERVER}|$SERVER|g; s|\${PROJECT_ID}|$PROJECT_ID|g; s|\${BRANCH}|$BRANCH|g" \
  /tmp/create-parent.apex > /tmp/create-parent-final.apex

PARENT_OUTPUT=$(sf apex run --file /tmp/create-parent-final.apex --target-org copadoOrg --json)
if [[ $? -ne 0 ]]; then
  echo "Failed to create Static Code Analysis Result parent record"
  exit 1
fi
SCAR_ID=$(echo "$PARENT_OUTPUT" | sed -n 's/.*OUTPUT_SCAR_ID:\([a-zA-Z0-9]*\).*/\1/p')
if [ -z "$SCAR_ID" ]; then
  echo "Failed to retrieve Static Code Analysis Result ID"
  echo "$PARENT_OUTPUT"
  exit 1
fi
echo "Created Static Code Analysis Result with ID: $SCAR_ID"

# FETCH ISSUES & BUILD CSV (streaming) - FAST + SAFE QUOTING
copado -p "Fetching issues and building CSV..."

echo "CSExtKey__c,copado__Rule__c,copado__Type__c,copado__Severity__c,copado__File__c,CSProject__c,copado__Line__c,copado__Message__c,copado__Static_Code_Analysis_Result__c,copado__Info_URL__c" > "$OUTPUT_CSV"

PAGE_SIZE=500
SEARCH_AFTER=""
HAS_MORE=true
PAGE_COUNT=0
TOTAL_ROWS=0

while [ "$HAS_MORE" = true ]; do
  PAGE_COUNT=$((PAGE_COUNT + 1))
  
  if [ -z "$SEARCH_AFTER" ]; then
    API_URL="$SERVER/api/issues/search?componentKeys=$PROJECT_ID&pullRequest=$BRANCH&statuses=OPEN&ps=$PAGE_SIZE"
  else
    API_URL="$SERVER/api/issues/search?componentKeys=$PROJECT_ID&pullRequest=$BRANCH&statuses=OPEN&ps=$PAGE_SIZE&searchAfter=$SEARCH_AFTER"
  fi

  TEMP_JSON="/tmp/codescan_page_${PAGE_COUNT}.json"
  curl -u "$TOKEN:" -s "$API_URL" -o "$TEMP_JSON"
  if [[ $? -ne 0 ]]; then
    echo "Failed to fetch API page $PAGE_COUNT"
    exit 1
  fi
  if ! jq empty "$TEMP_JSON" 2>/dev/null; then
    echo "Invalid JSON on page $PAGE_COUNT"
    cat "$TEMP_JSON"
    exit 1
  fi

  CURRENT_COUNT=$(jq '.issues | length' "$TEMP_JSON")
  if [ "$CURRENT_COUNT" -eq 0 ]; then
    echo "No more issues."
    HAS_MORE=false
    rm -f "$TEMP_JSON"
    break
  fi

  # Append rows to CSV using jq @csv (handles commas/quotes safely)
  jq -r \
    --arg scar "$SCAR_ID" \
    --arg server "$SERVER" \
    --arg project "$PROJECT_ID" \
    --arg branch "$BRANCH" \
    '
    .issues[] as $i |
    [
      ($i.key // ""),
      ($i.rule // ""),
      (($i.type // "") | gsub("_"; " ")),
      ($i.severity // ""),
      ($i.component // ""),
      ($i.project // ""),
      ((($i.line // 0) | tostring)),
      ($i.message // ""),
      $scar,
      ($server + "/project/issues?pullRequest=" + $branch + "&issues=" + ($i.key // "") + "&open=" + ($i.key // "") + "&id=" + $project)
    ] | @csv
    ' "$TEMP_JSON" >> "$OUTPUT_CSV"

  TOTAL_ROWS=$((TOTAL_ROWS + CURRENT_COUNT))

  SEARCH_AFTER=$(jq -r '.issues[-1].sort | if . != null then map(tostring) | join(",") else empty end' "$TEMP_JSON")
  if [ -z "$SEARCH_AFTER" ] || [ "$SEARCH_AFTER" = "null" ] || [ "$CURRENT_COUNT" -lt "$PAGE_SIZE" ]; then
    HAS_MORE=false
  fi

  rm -f "$TEMP_JSON"
done

echo "CSV built: $OUTPUT_CSV (rows: $TOTAL_ROWS)"

# BULK API 2.0 INSERT
copado -p "Bulk inserting violations (fast)..."

INSTANCE_URL="$CF_SF_ENDPOINT"
AUTH_HEADER="Authorization: Bearer $CF_SF_SESSIONID"

JOB_CREATE_RESP=$(curl -s -X POST \
  "$INSTANCE_URL/services/data/v${API_VERSION}/jobs/ingest" \
  -H "$AUTH_HEADER" \
  -H "Content-Type: application/json" \
  -d '{
    "object": "copado__Static_Code_Analysis_Violation__c",
    "contentType": "CSV",
    "operation": "insert",
    "lineEnding": "LF"
  }')

JOB_ID=$(echo "$JOB_CREATE_RESP" | jq -r '.id // empty')
if [ -z "$JOB_ID" ]; then
  echo "Failed to create Bulk job"
  echo "$JOB_CREATE_RESP"
  exit 1
fi
echo "Bulk Job created: $JOB_ID"

UPLOAD_RESP_CODE=$(curl -s -o /tmp/bulk_upload_resp.txt -w "%{http_code}" \
  -X PUT \
  "$INSTANCE_URL/services/data/v${API_VERSION}/jobs/ingest/$JOB_ID/batches" \
  -H "$AUTH_HEADER" \
  -H "Content-Type: text/csv" \
  --data-binary @"$OUTPUT_CSV")

if [ "$UPLOAD_RESP_CODE" -lt 200 ] || [ "$UPLOAD_RESP_CODE" -ge 300 ]; then
  echo "Bulk upload failed (HTTP $UPLOAD_RESP_CODE)"
  cat /tmp/bulk_upload_resp.txt
  exit 1
fi
echo "CSV uploaded to Bulk job"

CLOSE_RESP=$(curl -s -X PATCH \
  "$INSTANCE_URL/services/data/v${API_VERSION}/jobs/ingest/$JOB_ID" \
  -H "$AUTH_HEADER" \
  -H "Content-Type: application/json" \
  -d '{"state":"UploadComplete"}')

STATE=$(echo "$CLOSE_RESP" | jq -r '.state // empty')
echo "Bulk job state after close: $STATE"

# Poll until complete
ATTEMPTS=0
while true; do
  ATTEMPTS=$((ATTEMPTS + 1))
  JOB_STATUS=$(curl -s -X GET \
    "$INSTANCE_URL/services/data/v${API_VERSION}/jobs/ingest/$JOB_ID" \
    -H "$AUTH_HEADER")

  STATE=$(echo "$JOB_STATUS" | jq -r '.state // empty')
  echo "Bulk job state: $STATE"

  if [ "$STATE" = "JobComplete" ]; then
    break
  fi
  if [ "$STATE" = "Failed" ] || [ "$STATE" = "Aborted" ]; then
    echo "Bulk job failed: $JOB_STATUS"
    echo "Fetching failedResults..."
    curl -s -X GET \
      "$INSTANCE_URL/services/data/v${API_VERSION}/jobs/ingest/$JOB_ID/failedResults" \
      -H "$AUTH_HEADER" > /tmp/bulk_failedResults.csv || true
    echo "Saved: /tmp/bulk_failedResults.csv"
    exit 1
  fi

  if [ $ATTEMPTS -gt 200 ]; then
    echo "Bulk job polling exceeded limit"
    echo "$JOB_STATUS"
    exit 1
  fi

  sleep 3
done

# Optional: show counts
PROCESSED=$(echo "$JOB_STATUS" | jq -r '.numberRecordsProcessed // 0')
FAILED=$(echo "$JOB_STATUS" | jq -r '.numberRecordsFailed // 0')
echo "Bulk insert done. Processed=$PROCESSED Failed=$FAILED"

# UPLOAD FINAL CSV
copado -u "$OUTPUT_CSV" --name "$OUTPUT_CSV"

# Update Result record (if present)
if [ -n "$PARENT_ID" ] && [ "$PARENT_ID" != "" ]; then
  cat > /tmp/update-result.apex <<'APEX_EOF'
if('${PARENT_ID}' != ''){
  update new copado__Result__c(
    Id = '${PARENT_ID}',
    copado__Error_Message__c = 'CodeScan analysis completed. Successfully processed ${COUNT} violations.',
    copado__Link__c = '${SERVER}/dashboard?id=${PROJECT_ID}&pullRequest=${BRANCH}'
  );
}
APEX_EOF
  sed "s|\${PARENT_ID}|$PARENT_ID|g; s|\${COUNT}|$PROCESSED|g; s|\${SERVER}|$SERVER|g; s|\${PROJECT_ID}|$PROJECT_ID|g; s|\${BRANCH}|$BRANCH|g" \
    /tmp/update-result.apex > /tmp/update-result-final.apex
  sf apex run --file /tmp/update-result-final.apex --target-org copadoOrg --json > /dev/null 2>&1 || true
fi

export CF_SF_ENDPOINT="https://$(echo "$CF_SF_ENDPOINT" | sed -e 's/[^/]*\/\/\([^@]*@\)\?\([^:/]*\).*/\2/')"
echo "Normalized CF_SF_ENDPOINT: $CF_SF_ENDPOINT"

exit $exitCode
```

</details>

If the main branch of your repository is not **main**, please change the **CS\_MAIN\_BRANCH** variable on line 15.  This should match the branch name as it is shown in CodeScan.

Click **save**.

The configuration tab should show the callback type is **ApexClass** and the ApexClass is **EvaluateCodeScanResult.**

<figure><img src="../../../../.gitbook/assets/image (1547).png" alt=""><figcaption></figcaption></figure>

Navigate to the Parameters tab and click **Edit.**

Click **Add New Parameter** and add the following parameters:

**Name:** DataJson\
**Value:** {$Context.copado\_\_JobExecution\_\_r.copado\_\_DataJson\_\_c}

**Name**: BASE\_BRANCH\
**Value**: {$Context.copado\_\_JobExecution\_\_r.copado\_\_Pipeline\_\_r.copado\_\_Main\_Branch\_\_c}

**Name**: COPADO\_PROJECT\
**Value**: {$Context.copado\_\_JobExecution\_\_r.copado\_\_UserStoryCommit\_\_r.copado\_\_User\_Story\_\_r.copado\_\_Project\_\_r.Name}

**Name**: DEST\_BRANCH\
**Value**: {$Destination.Branch}

**Name:** PARENT\_ID\
**Value:** {$Context.copado\_\_JobExecution\_\_r.copado\_\_ParentRecord\_Id\_\_c}

Click **Save.** &#x20;

### Quality Gate Rule

The Quality Gate rule should show **After Commit** as a Trigger.  This is the default setup as described in the Copado documentation.

### User Story Page

We recommend adding the Static Code Analysis results related list to the User Story page to make them easier to access.

<figure><img src="../../../../.gitbook/assets/image (1550).png" alt=""><figcaption></figcaption></figure>

Violations will be stored as Static Code Analysis Violations.

<figure><img src="../../../../.gitbook/assets/image (1551).png" alt=""><figcaption></figcaption></figure>

### Using the "Run CodeScan" button or running functions directly from the User Story page

{% hint style="info" %}
These approaches are not recommended due to the fact that **it will not update the Test record Pass/Fail for the User Story** as it is not executing in Copado's Quality Integration Framework like the function above.

The supported use case above will scan every time code is committed in the User Story.  This means you will always have:

* The most up-to-date scan of your committed code in CodeScan
* The most up-to-date result of your committed code in Copado (Pass/Fail)
{% endhint %}

<br>
