# TAF Workflow

### Prerequisite <a href="#prerequisite" id="prerequisite"></a>

1. AutoRABIT TAF expert team provides basic training to QA team members on the best practices using Selenium recorder to record the test scripts as part of the initial roll-out.
2. QA team will register the Sandboxes scoped for testing with AutoRABIT and test for the initial login to be successful since Salesforce asks for a security token at the time of the first login from a new IP address.

### Workflow <a href="#workflow" id="workflow"></a>

1. The QA team member records a test scenario and uploads it to AutoRABIT.
2. AutoRABIT TAF will run the uploaded test scripts in scheduled batches. It will try to playback the recorded script.
3. **If the playback is successful**:
   * An email notification is sent from AutoRABIT to the QA team member for review of the automated test case along with the data set that is entered at the time of testing.
   * The QA team member can attach the test case to multiple environments/data sets.
   * The QA team member checks-in on the changes to the version control from AutoRABIT UI.
4. **If the playback is unsuccessful**:
   * AutoRABIT team will review the reasons. If there is an error with the way the script is recorded, the TAF team expert will let the client QA team member know of the improvements to be done. If there is an error due to any browser issue / Lightning framework changes with the new release or a gap with AutoRABIT TAF playback libraries, the AutoRABIT TAF team will resolve the issue, upload the transformed test case with successful playback to AutoRABIT.
