---
hidden: true
---

# Anomaly Detection\_OLD Changed on 19 Aug 2026

## AutoRABIT Vault Anomaly Detection User Guide

## Purpose

AutoRABIT Vault Anomaly Detection monitors configured Salesforce data objects and metadata types for unusual changes. The feature helps identify unexpected activity, review affected records, compare snapshots, and roll back selected data changes where required. The workflow begins with configuration, continues through dashboard monitoring and anomaly review, and ends with rollback or comparison result tracking.

## Workflow Covered

* Configure anomaly detection for data and metadata.
* Select notification and exclusion settings.
* Monitor active or paused detection status from the dashboard.
* Review anomaly details and compare detected records.
* Submit rollback jobs and review rollback outcomes.
* Use job history, compare labels, export, and field-selection controls.
* Pause, stop, or restart anomaly detection.

Anomaly Detection is configured from the Anomaly Detection workspace. The configuration defines the source org, monitored data objects, monitored metadata types, threshold percentages, notification recipients, and excluded change owners. Once the configuration is saved, AutoRABIT Vault begins evaluating the selected scope based on the scheduled detection cycle.

<figure><img src="/broken/files/nwZGLr17Lc4yfpslNLKC" alt=""><figcaption></figcaption></figure>

&#x20;                                                _Anomaly Detection landing page before configuration_

<figure><img src="/broken/files/t8b7VrqnfP4FM4KIOnml" alt=""><figcaption></figcaption></figure>

&#x20;                                                _Config Creation window with Data threshold settings_

<figure><img src="../../../.gitbook/assets/3 (29).png" alt=""><figcaption></figcaption></figure>

&#x20;                                                _Data object selection for anomaly monitoring_

<figure><img src="../../../.gitbook/assets/4 (25).png" alt=""><figcaption></figcaption></figure>

&#x20;                                                _Config Creation window with Metadata threshold settings_

<figure><img src="../../../.gitbook/assets/5 (25).png" alt=""><figcaption></figcaption></figure>



&#x20;                                                _Metadata type selection for anomaly monitoring_

![](<../../../.gitbook/assets/Unknown image (422)>)

&#x20;                                                _Email Notifications and External Changes of Users options_

![](<../../../.gitbook/assets/Unknown image (423)>)

&#x20;                              _User Details selection for excluding internal application users_

![](<../../../.gitbook/assets/Unknown image (424)>)

&#x20;                       _External Changes of Users option after selecting AutoRABIT Vault users_

![](<../../../.gitbook/assets/Unknown image (425)>)

&#x20;                                                _Salesforce User Details selection for excluding Salesforce users_

## Monitoring the Dashboard

After configuration is saved, the dashboard displays the detection status, source org, date range, and anomaly summary cards for Data and Metadata. The status indicator shows whether anomaly detection is active or paused. The dashboard presents detected data changes by severity so the investigation can continue from a summarized view into detailed records.

![](<../../../.gitbook/assets/Unknown image (426)>)

&#x20;                                                _Anomaly Detection dashboard after configuration is saved_

![](<../../../.gitbook/assets/Unknown image (427)>)

&#x20;                                                _Active anomaly detection status on the dashboard_

![](<../../../.gitbook/assets/Unknown image (428)>)

&#x20;                                                _Data anomaly summary chart for the selected object_

![](<../../../.gitbook/assets/Unknown image (429)>)

&#x20;                                                _Data anomaly summary chart with severity filter_

## Reviewing Data Anomaly Details

The Data anomaly details view lists detected records for the selected source org, object, and detection period. Records can be reviewed in the table, selected for rollback, or compared for deeper field-level analysis. The system presents available actions based on the selected records and the current result state.

![](<../../../.gitbook/assets/Unknown image (430)>)

&#x20;                                                _Anomaly Details page with detected records_

![](<../../../.gitbook/assets/Unknown image (431)>)

&#x20;                                                _Record selection for rollback action_

![](<../../../.gitbook/assets/Unknown image (432)>)

&#x20;                                                _Rollback prerequisite and behavior information_

Rollback is initiated from the anomaly details or result views after eligible records are selected. AutoRABIT Vault presents a rollback summary before submission, including rollback options and the selected record count. Once confirmed, a rollback job is created and tracked from the Anomaly Rollback section until completion.

![](<../../../.gitbook/assets/Unknown image (433)>)

&#x20;                                           _Rollback Summary window with selected records and rollback preferences_

![](<../../../.gitbook/assets/Unknown image (434)>)

&#x20;                                                _Rollback job submitted confirmation_

![](<../../../.gitbook/assets/Unknown image (435)>)

&#x20;                                                _Anomaly Rollback job list_

![](<../../../.gitbook/assets/Unknown image (436)>)

&#x20;                                                _Rollback job actions and progress tracking_

![](<../../../.gitbook/assets/Unknown image (437)>)

&#x20;                                                _Rollback result details with Follow Records tab_

![](<../../../.gitbook/assets/Unknown image (438)>)

&#x20;                                                _Rollback result details with Outcome Records tab_

![](<../../../.gitbook/assets/Unknown image (439)>)

&#x20;                                                _Completed rollback status in the rollback job list_

Comparison results are accessed from Anomaly Detection Job History. The results view shows detected changes by compare label and object. Field-level changes are highlighted in the results table, and detailed record comparison is available through the View Record action. Export and field-selection options support focused review of the result set.

![](<../../../.gitbook/assets/Unknown image (440)>)

&#x20;                                                _Return to the Anomaly Detection dashboard after rollback review_

![](<../../../.gitbook/assets/Unknown image (441)>)

&#x20;                                                _Anomaly Details page with records selected for comparison_

![](<../../../.gitbook/assets/Unknown image (442)>)

&#x20;                                                _Comparison job submitted confirmation_

![](<../../../.gitbook/assets/Unknown image (443)>)

&#x20;                                                _Anomaly Detection Job History list_

![](<../../../.gitbook/assets/Unknown image (444)>)

&#x20;                                                _Job history action for viewing comparison results_

![](<../../../.gitbook/assets/Unknown image (445)>)

&#x20;                                                _Anomaly Detection Results page with comparison records_

![](<../../../.gitbook/assets/Unknown image (446)>)

&#x20;                                                _View Record action in the comparison results table_

![](<../../../.gitbook/assets/Unknown image (447)>)

&#x20;                                                _View Record window showing field-level snapshot comparison_

![](<../../../.gitbook/assets/Unknown image (448)>)

&#x20;                                                _Export option in Anomaly Detection Results_

![](<../../../.gitbook/assets/Unknown image (449)>)

&#x20;                                                _Export window with available export scope options_

![](<../../../.gitbook/assets/Unknown image (450)>)

&#x20;                                                _Choose Fields option in Anomaly Detection Results_

![](<../../../.gitbook/assets/Unknown image (451)>)

&#x20;                                                _Fields selection window for result display_

![](<../../../.gitbook/assets/Unknown image (452)>)

&#x20;                                                _Records selected for rollback from Anomaly Detection Results_

![](<../../../.gitbook/assets/Unknown image (453)>)

&#x20;                                                _Rollback action from Anomaly Detection Results_

![](<../../../.gitbook/assets/Unknown image (454)>)

&#x20;                                                _Rollback fields selection window_

![](<../../../.gitbook/assets/Unknown image (455)>)

&#x20;                                                _Rollback job submitted from comparison results_

Anomaly Detection Job History maintains the comparison and rollback activity initiated from the anomaly workflow. Each job entry provides status, timing, and action controls. Compare label actions open detailed field-level status information for the selected compare run.

![](<../../../.gitbook/assets/Unknown image (456)>)

&#x20;                                                _Job History list after rollback submission from results_

![](<../../../.gitbook/assets/Unknown image (457)>)

&#x20;                                                _Job History action for compare label review_

![](<../../../.gitbook/assets/Unknown image (458)>)

&#x20;                                                _Compare Label window showing field-level status_

![](<../../../.gitbook/assets/Unknown image (459)>)

&#x20;                                                _Job History action for detailed compare label review_

![](<../../../.gitbook/assets/Unknown image (458)>)

&#x20;                                                _Compare Label window with scrollable field status list_

## Pausing, Stopping, and Restarting Detection

Anomaly detection can be temporarily paused until a selected date or permanently turned off. A confirmation message appears before permanent changes are applied. When detection is restarted, the dashboard returns to an active monitoring state and allows the detection date range to be selected again.

![](<../../../.gitbook/assets/Unknown image (460)>)

&#x20;                                                _Date picker for changing the dashboard date range_

![](<../../../.gitbook/assets/Unknown image (461)>)

&#x20;                                                _Pause anomaly detection date selection on the dashboard_

![](<../../../.gitbook/assets/Unknown image (462)>)

&#x20;                                                _Save action for pausing anomaly detection until a selected date_

![](<../../../.gitbook/assets/Unknown image (463)>)

&#x20;                                                _Active status after date-based anomaly detection control_

![](<../../../.gitbook/assets/Unknown image (464)>)

&#x20;                                                _Turn off anomaly detection permanently option_

![](<../../../.gitbook/assets/Unknown image (465)>)

&#x20;                                                _Confirmation window for turning off anomaly detection permanently_

![](<../../../.gitbook/assets/Unknown image (466)>)

&#x20;                                                _Stopped anomaly detection status after permanent turn off_

![](<../../../.gitbook/assets/Unknown image (467)>)

&#x20;                                                _Confirmation window for restarting anomaly detection_

![](<../../../.gitbook/assets/Unknown image (468)>)

&#x20;                                                _Date picker available after anomaly detection is restarted_

## Result

After the workflow is completed, AutoRABIT Vault maintains the anomaly configuration, displays the current monitoring state on the dashboard, stores comparison jobs in job history, and tracks rollback jobs separately. This provides a controlled path to identify suspicious changes, verify field-level differences, and restore selected data where required.
