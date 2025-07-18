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
echo $branchesAndFileIdJson
echo $git_json
originBranch=$(jq -r '.originBranch' <<< $branchesAndFileIdJson)
BRANCH="$originBranch"
echo "param branchesAndFileIdJson =  $branchesAndFileIdJson"
echo "param originBranch = $originBranch"
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

if [ -f /tmp/result.json ]
then
  # Fetch the issues from the API
  copado -p "Fetching issues..."

  # Fetch JSON data from the API
  echo $(curl -u $TOKEN: -s "$SERVER/api/issues/search?componentKeys=$PROJECT_ID&pullRequest=$BRANCH&statuses=OPEN" -o $OUTPUT_JSON)

  # Check if the curl command was successful
  if [[ $? -ne 0 ]]
  then
    echo "Failed to fetch data from the API"
    exit 1
  fi

  # Create a CSV
  copado -p "Creating CSV..."
fi

rows=$(node <<EOF
const fs = require('fs');

// Read the JSON file
const data = JSON.parse(fs.readFileSync('$OUTPUT_JSON', 'utf8'));
if (data.current) {
  console.error("No scan has been performed.");
} else {

  // Extract the issues array
  const issues = data.issues;

  // Create CSV headers
  const headers = ['CSExtKey__c', 'copado__Rule__c', 'copado__Type__c', 'copado__Severity__c', 'copado__File__c', 'CSProject__c', 'copado__Line__c' ];

  // Create CSV rows
  const rows = issues.map(issue => {
      const { key, rule, type, severity, component, project, line} = issue;
      
      return [
          key, 
          rule,
          type,
          severity, 
          component, 
          project, 
          line,
      ].join(',');
  });
  // Combine headers and rows
  const csv = [headers.join(','), ...rows].join('\n');
  // Write the CSV file
  fs.writeFileSync('$OUTPUT_CSV', csv);
  // Output rows as JSON
  console.log(JSON.stringify(rows));
}
EOF
)

# Check if the Node.js script was successful
if [[ $? -ne 0 ]]
then
  echo "Failed to convert JSON to CSV"
  exit 1
fi

if [[ "$rows" != '' ]]
then
  # Convert JSON rows to CSV string
  CSV_STRING=$(jq -r 'join("#")' <<< "$rows")

  # Escape special characters in CSV_STRING for Apex
  CSV_STRING=$(echo "$CSV_STRING" | sed 's/\\/\\\\/g; s/"/\\"/g')
  echo "CSV_STRING: $CSV_STRING"

  # Check if the CSV file exists and upload it 
  if [ -f "$OUTPUT_CSV" ]; then
    copado -u $OUTPUT_CSV --name $OUTPUT_CSV 
    echo "Script completed successfully. CSV file is located at $OUTPUT_CSV"
  else
    copado -u $OUTPUT_JSON
    echo "CSV creation was unsuccessful. JSON file is located at $OUTPUT_JSON"
  fi

  # Import issues as Salesforce records
  copado -p "Importing issues..."
fi
# Create and run Apex script
echo "
if('$USER_STORY' != ''){
  string recID='$USER_STORY';
  List<copado__User_Story__c> userStories = [SELECT Id FROM copado__User_Story__c WHERE Id = :recID LIMIT 1];
  Id usid = userStories.isEmpty() ? null : userStories[0].Id;

  if (usid != null) {
    //***************************
    // Get the Result record ID from the parent record
    string parentId = '$PARENT_ID';
    Id resultId;
    if(parentId != '') {
      List<copado__Result__c> results = [SELECT Id FROM copado__Result__c WHERE Id = :parentId LIMIT 1];
      if(!results.isEmpty()) {
        resultId = results[0].Id;
      }
    }
    //*************************^^^

    // Proceed with creating Static Code Analysis Result
    Id recTypeId = Schema.SObjectType.copado__Static_Code_Analysis_Result__c.getRecordTypeInfosByName().get('CodeScan').getRecordTypeId();
    copado__Static_Code_Analysis_Result__c scar = new copado__Static_Code_Analysis_Result__c(recordtypeId=recTypeId,copado__User_Story__c=usid,copado__Details__c='$SERVER/dashboard?id=$PROJECT_ID&pullRequest=$BRANCH');
    insert scar;
    id scarid = scar.id;   

    //***************************
    // Update the Result record with error message and external result link if it exists
    if(resultId != null) {
      copado__Result__c result = new copado__Result__c(
        Id = resultId,
        copado__Error_Message__c = 'CodeScan analysis completed. See details in Static Code Analysis Result.',
        copado__Link__c = '$SERVER/dashboard?id=$PROJECT_ID&pullRequest=$BRANCH'
      );
      update result;
    }
    //*************************^^^

    List<copado__Static_Code_Analysis_Violation__c> SCAV = new List<copado__Static_Code_Analysis_Violation__c>();
    
    String csvAsString = '$CSV_STRING';
    System.debug('CSV as string:'+csvAsString);

    if(csvAsString != ''){
        String[] csvFileLines = csvAsString.split('#');
        System.debug(csvFileLines.size());

        for(Integer i=0; i<csvFileLines.size(); i++){
            String[] csvRecordData = csvFileLines[i].split(',');
            String issueLink='$SERVER/project/issues?pullRequest=$BRANCH&issues='+csvRecordData[0]+'&open='+csvRecordData[0]+'&id=$PROJECT_ID';
            
            copado__Static_Code_Analysis_Violation__c viol= new copado__Static_Code_Analysis_Violation__c(
                CSExtKey__c = csvRecordData[0],             
                copado__Rule__c = csvRecordData[1],
                copado__Type__c = csvRecordData[2],
                copado__Severity__c = csvRecordData[3],   
                copado__File__c = csvRecordData[4],                                                                            
                CSProject__c = csvRecordData[5],
                copado__Line__c = Integer.valueOf(csvRecordData[6].removeEnd('\n')), 
                copado__Static_Code_Analysis_Result__c = scarid,
                copado__Info_URL__c = issueLink
            );
            SCAV.add(viol);   
        }
    insert SCAV;
    } else {
        System.debug('No Issues in CSV');
    }
  } else {
    System.debug('Could not find User Story with name: ' + recID);
  }

} else {
  System.debug('Not a User Story, check issues in CodeScan'); 
}
" > /tmp/run.apex

# Fix URLs
export CF_SF_ENDPOINT="https://$(echo $CF_SF_ENDPOINT | sed -e 's/[^/]*\/\/\([^@]*@\)\?\([^:/]*\).*/\2/')"

copado -p "Inserting parent..."
sf apex run --file /tmp/run.apex --target-org copadoOrg --json
if [[ $? -ne 0 ]]
then
  echo "The Apex Script failed to add violations."
  exit 1
fi

exit $exitCode
```

</details>

If the main branch of your repository is not **main**, please change the **CS\_MAIN\_BRANCH** variable on line 15.  This should match the branch name as it is shown in CodeScan.

Click **save**.

The configuration tab should show the callback type is **ApexClass** and the ApexClass is **EvaluateCodeScanResult.**

<figure><img src="../../../../.gitbook/assets/image (1547).png" alt=""><figcaption></figcaption></figure>

Navigate to the Parameters tab and click **Edit.**

Click **Add New Parameter** and add the following parameters:

**Name:** USER\_STORY\
**Value:** {$Context.copado\_\_JobExecution\_\_r.copado\_\_UserStoryCommit\_\_r.copado\_\_User\_Story\_\_c}

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

### Using the "Run CodeScan" button on the User Story page

{% hint style="info" %}
The Run CodeScan button allows you to run the scan directly from a User Story without committing and will reflect the results in a Static Code Analysis Results object attached to the User Story. &#x20;

I**t will not update the Test record Pass/Fail for the User Story** as it is not executing in Copado's Quality Integration Framework like the function above.
{% endhint %}

To add and use the Run CodeScan Action on the User Story page, some additions must be made to the Run CodeScan function.\
\
First, under the script tab, click the lower edit button and replace the script with the following:

<details>

<summary>Expand to view script</summary>

```
BRANCH="feature/$USER_STORY"
echo "param TOKEN = $TOKEN"
echo "param SERVER = $SERVER"
echo "param PROJECT_ID = $PROJECT_ID"
echo "param ORGANIZATION = $ORGANIZATION"
echo "param BRANCH = $BRANCH"
echo "param USER_STORY = $USER_STORY"   
echo "param BASE_BRANCH = $BASE_BRANCH"
echo "param COPADO_PROJECT = $COPADO_PROJECT"
OUTPUT_JSON="output.json"
OUTPUT_CSV="violations.csv"
CSV_STRING=""
exitCode=0
NEW_PROJECT="true"

# Check if the project has been scanned before
curl -u $TOKEN: -s "$SERVER/api/ce/component?component=$PROJECT_ID" -o $OUTPUT_JSON || exitCode=$?
# Check if the curl command was successful
if [[ $? -ne 0 ]]
then
  echo "Failed to fetch data from the API"
  exit 1
fi


# Set New Project based on response
NEW_PROJECT=$(node <<EOF
  const fs = require('fs');
  try {
    // Read the JSON file and parse it
    const data = JSON.parse(fs.readFileSync('$OUTPUT_JSON', 'utf8'));
    // Check if there is an "errors" field indicating an error
    if (data.errors) {
      console.error("Project does not exist or there is an error in the response:" + JSON.stringify(data));
      console.log("true");
    } else if ('current' in data) {
      console.log("false");  // Project has been scanned before
    } else {
      console.log("true");   // New project, not scanned before
    }
  } catch (error) {
    console.error("ERROR: ", error);
    process.exit(1);
  }
EOF
)

# Need to determine changed files in User Story

# Check for branch type and scan
if [[ "$BRANCH" =~ .+/US-[0-9]+ ]]
then
  API_URL="$SERVER/api/issues/search?componentKeys=$PROJECT_ID&pullRequest=$BRANCH&statuses=OPEN"
  if [[ "$NEW_PROJECT" = true ]]
  then
    copado-git-get $BASE_BRANCH
    copado -p "Running codescan on Main Branch for first run..."
    sfdx codescan:run --token=$TOKEN --server=$SERVER --projectkey=$PROJECT_ID --organization=$ORGANIZATION --json 2>&1 | tee /tmp/result.json \
        || exitCode=$?
    echo "Codescan completed. exit code: $exitCode"
  fi
  copado -p "Cloning repo..."
  copado-git-get $BRANCH
  ls -a
  copado -p "Running codescan on User Story..."
  sfdx codescan:run --token=$TOKEN --server=$SERVER --projectkey=$PROJECT_ID --organization=$ORGANIZATION -Dsonar.pullrequest.base=$BASE_BRANCH -Dsonar.pullrequest.branch="$COPADO_PROJECT" -Dsonar.pullrequest.key="$BRANCH" --json 2>&1 | tee /tmp/result.json \
      || exitCode=$?
  echo "Codescan completed. exit code: $exitCode"
  copado -u /tmp/result.json
else
  echo "No scan needed."
fi

if [ -f /tmp/result.json ]
then
  # Fetch the issues from the API
  copado -p "Fetching issues..."

  # Fetch JSON data from the API
  echo $(curl -u $TOKEN: -s $API_URL -o $OUTPUT_JSON)

  # Check if the curl command was successful
  if [[ $? -ne 0 ]]
  then
    echo "Failed to fetch data from the API"
    exit 1
  fi

  # Create a CSV
  copado -p "Creating CSV..."
fi

rows=$(node <<EOF
const fs = require('fs');

// Read the JSON file
const data = JSON.parse(fs.readFileSync('$OUTPUT_JSON', 'utf8'));
if (data.current) {
  console.error("No scan has been performed.");
} else {

  // Extract the issues array
  const issues = data.issues;

  // Create CSV headers
  const headers = ['CSExtKey__c', 'copado__Rule__c', 'copado__Type__c', 'copado__Severity__c', 'copado__File__c', 'CSProject__c', 'copado__Line__c' ];

  // Create CSV rows
  const rows = issues.map(issue => {
      const { key, rule, type, severity, component, project, line} = issue;
      
      return [
          key, 
          rule,
          type,
          severity, 
          component, 
          project, 
          line,
      ].join(',');
  });
  // Combine headers and rows
  const csv = [headers.join(','), ...rows].join('\n');
  // Write the CSV file
  fs.writeFileSync('$OUTPUT_CSV', csv);
  // Output rows as JSON
  console.log(JSON.stringify(rows));
}
EOF
)

# Check if the Node.js script was successful
if [[ $? -ne 0 ]]
then
  echo "Failed to convert JSON to CSV"
  exit 1
fi

if [[ "$rows" != '' ]]
then
  # Convert JSON rows to CSV string
  CSV_STRING=$(jq -r 'join("#")' <<< "$rows")

  # Escape special characters in CSV_STRING for Apex
  CSV_STRING=$(echo "$CSV_STRING" | sed 's/\\/\\\\/g; s/"/\\"/g')
  echo "CSV_STRING: $CSV_STRING"

  # Check if the CSV file exists and upload it 
  if [ -f "$OUTPUT_CSV" ]; then
    copado -u $OUTPUT_CSV --name $OUTPUT_CSV 
    echo "Script completed successfully. CSV file is located at $OUTPUT_CSV"
  else
    copado -u $OUTPUT_JSON
    echo "CSV creation was unsuccessful. JSON file is located at $OUTPUT_JSON"
  fi

  # Import issues as Salesforce records
  copado -p "Importing issues..."
fi
# Create and run Apex script
echo "
if('$USER_STORY' != ''){
  string recID='$USER_STORY';
  List<copado__User_Story__c> userStories = [SELECT Id FROM copado__User_Story__c WHERE Name = :recID LIMIT 1];
  Id usid = userStories.isEmpty() ? null : userStories[0].Id;

  if (usid != null) {
    // Proceed with creating Static Code Analysis Result
    Id recTypeId = Schema.SObjectType.copado__Static_Code_Analysis_Result__c.getRecordTypeInfosByName().get('CodeScan').getRecordTypeId();
    copado__Static_Code_Analysis_Result__c scar = new copado__Static_Code_Analysis_Result__c(recordtypeId=recTypeId,copado__User_Story__c=usid);
    insert scar;
    id scarid = scar.id;   

    List<copado__Static_Code_Analysis_Violation__c> SCAV = new List<copado__Static_Code_Analysis_Violation__c>();
    
    String csvAsString = '$CSV_STRING';
    System.debug('CSV as string:'+csvAsString);

    if(csvAsString != ''){
        String[] csvFileLines = csvAsString.split('#');
        System.debug(csvFileLines.size());

        for(Integer i=0; i<csvFileLines.size(); i++){
            String[] csvRecordData = csvFileLines[i].split(',');
            String issueLink='$SERVER/project/issues?pullRequest=$BRANCH&issues='+csvRecordData[0]+'&open='+csvRecordData[0]+'&id=$PROJECT_ID';
            
            copado__Static_Code_Analysis_Violation__c viol= new copado__Static_Code_Analysis_Violation__c(
                CSExtKey__c = csvRecordData[0],             
                copado__Rule__c = csvRecordData[1],
                copado__Type__c = csvRecordData[2],
                copado__Severity__c = csvRecordData[3],   
                copado__File__c = csvRecordData[4],                                                                            
                CSProject__c = csvRecordData[5],
                copado__Line__c = Integer.valueOf(csvRecordData[6].removeEnd('\n')), 
                copado__Static_Code_Analysis_Result__c = scarid,
                copado__Info_URL__c = issueLink
            );
            SCAV.add(viol);   
        }
    insert SCAV;
    } else {
        System.debug('No Issues in CSV');
    }
  } else {
    System.debug('Could not find User Story with name: ' + recID);
  }

} else {
  System.debug('Not a User Story, check issues in CodeScan'); 
}
" > /tmp/run.apex

# Fix URLs
export CF_SF_ENDPOINT="https://$(echo $CF_SF_ENDPOINT | sed -e 's/[^/]*\/\/\([^@]*@\)\?\([^:/]*\).*/\2/')"

copado -p "Inserting parent..."
SFDX_ACCESS_TOKEN="$CF_SF_SESSIONID" sf org login access-token --alias copadoOrg --instance-url "$CF_SF_ENDPOINT" --no-prompt
sf apex run --file /tmp/run.apex --target-org copadoOrg --json
if [[ $? -ne 0 ]]
then
  echo "The Apex Script failed to add violations."
  exit 1
fi
exit $exitCode
```

</details>

Navigate to the Parameters tab and click **Edit.**

Click **Add New Parameter** and add the following parameters:

**Name:** USER\_STORY\
**Value:** {$Context}

**Name**: BASE\_BRANCH\
**Value**: {$Pipeline.copado\_\_Main\_Branch\_\_c}

**Name**: COPADO\_PROJECT\
**Value**: {$Job.ExecutionParent.copado\_\_Project\_\_r.Name}\
