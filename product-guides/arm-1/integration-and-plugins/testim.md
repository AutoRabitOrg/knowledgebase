# TestIm

## **Integrate Testim with ARM CI Jobs - New UI**

### **Overview**

You can integrate **Testim** with ARM CI Jobs to automate test execution as part of your deployment pipeline. This integration enables:

* Automated execution of Testim tests during CI jobs
* Automatic rollback of deployments when test execution fails
* Email notifications with execution results
* Full visibility into logs, reports, and job history

This helps ensure **safer deployments**, **faster failure recovery**, and **immediate visibility into test outcomes**.

***

### **Prerequisites**

Ensure the following before configuration:

* Active **Testim account**
* Test cases, suites, or plans created in Testim
* **Application Token** generated from Testim (project level)
* Required permissions to create and execute CI jobs in ARM

### **Step 1: Configure Testim Credentials**

1. Navigate to **Plugins → Test Types**
2. Enable **Testim**

<figure><img src="../../../.gitbook/assets/image (2497).png" alt=""><figcaption></figcaption></figure>

3. Click **Edit (✏️)** or add a new configuration
4. In the **Create Credential** window:
   * **Name**: Enter a unique identifier
   * **Type**: Select _Application Token_
   * **Token**: Enter the Testim token (generated at project level)

<figure><img src="../../../.gitbook/assets/image (2498).png" alt="" width="375"><figcaption></figcaption></figure>

5. Save the configuration

> Note: Ensure the correct Testim environment (host URL, if applicable) is configured as part of your setup.

### **Step 2: Create a CI Job**

1. Go to **CI Jobs → Create CI Job**
2. Configure the **Build** and **Deploy** stages as required
3. Navigate to the **Tests** stage

<figure><img src="../../../.gitbook/assets/image (2499).png" alt=""><figcaption></figcaption></figure>

### **Step 3: Configure Testim in Test Stage**

#### **Select Test Source**

* Choose **Testim** under _Fetch test cases from_

#### **Provide Execution Details**

* **Branch Name**: Select the Testim branch
* **Execution Type**:
  * **Suite**
  * **Label**
  * **Plan**

#### **Based on Execution Type**

**Suite / Label**

* Suite or Label Name
* **Grid Name** _(manual entry required)_
* **Base URL** _(optional override for execution environment)_

**Plan**

* Plan Name _(manual entry required)_
* **Grid Name**

#### **Optional: Run Parameters**

* Add key-value pairs if required for execution

### **Step 4: Enable Automatic Rollback**

* Select **✔ Rollback if test cases fail**

#### **Rollback Behavior**

* Rollback is triggered when:
  * The **overall Testim execution status is Failed**
  * This applies even if **one or more test cases fail**
* When triggered:
  * All deployed components are rolled back
  * Rollback takes precedence over other backup mechanisms (if configured)

> ⚠️ Important:\
> To prevent unintended ALM updates when failures occur, ensure the **Rollback option is also enabled at the main CI Job level**.

### **Step 5: Configure Email Notifications**

ARM uses the **existing notification system** to send execution updates.

#### **Notifications include:**

* Job name and environment
* Execution status (Success/Failed)
* Number of tests passed and failed
* Rollback status (if triggered)
* Link to detailed execution logs and reports

Emails are automatically sent after:

* Test execution completes
* Rollback is triggered (if applicable)

### **Step 6: Execute and Monitor CI Job**

1. Save the CI Job
2. Trigger execution
3. Monitor progress under **CI Job Run History**

### **Execution Flow**

1. Deployment is executed
2. Testim tests are triggered
3. ARM polls for execution results periodically
4. Final status is determined:
   * **Success** → Job continues
   * **Failure** → Rollback triggered (if enabled)
5. Notification email is sent

### **Result Handling and Visibility**

After execution, users can view:

* Execution summary
* Test results (pass/fail count)
* Failed test details
* Rollback status
* Execution logs
* Direct link to Testim report

All actions are recorded in **CI Job execution history** for traceability.

### **Validation Behavior**

* Invalid **Plan Name**:
  * Displays validation error
  * Prevents job execution
* Grid Name:
  * Must be entered manually
  * No validation API available (see limitations)

### **Important Behavior Notes**

* Test execution is considered **Failed** when:
  * The overall Testim run status is failed
* Rollback is based on:
  * Execution status, not individual test thresholds
* Test execution:
  * Cannot be aborted once started
* Base URL:
  * Allows overriding the execution environment independently of Testim configuration

### **Limitations & Known Issues**

#### 1. Grid Name Validation

* No API available to validate Grid Name
* Invalid values:
  * Cause execution failure
  * May not always reflect correct failure status in UI

#### 2. Status Icon Issue

* When failure occurs due to invalid Grid Name:
  * Logs capture the failure
  * ❌ UI status icon may not display as “Failed”

#### 3. Rollback & ALM Status Mismatch

* Components rollback successfully
* ❌ ALM status is **not reverted automatically**

**Workaround:**

* Enable rollback at the **main CI Job level** to prevent incorrect ALM updates

#### 4. Rollback Option Visibility (UI Issue)

* Rollback option may appear in **test-only (CA) job tiles**
* This is incorrect since no deployment occurs

#### 5. Execution Control

* Test execution:
  * ❌ Cannot be aborted once started

#### 6. Polling Delay

* Execution results are polled at intervals
* This may introduce slight delays in status updates

### **Best Practices**

* Always verify:
  * Grid Name
  * Plan/Suite Name
* Enable rollback at:
  * Test stage
  * Main CI Job level
* Configure email notifications for visibility
* Review execution logs for troubleshooting
* Use Base URL carefully when overriding environments

### **Summary**

With Testim integration in ARM:

* Test execution is fully automated
* Failures trigger immediate rollback
* Stakeholders receive real-time updates
* Deployment risks are minimized

This enables **reliable, automated, and auditable CI workflows**.
