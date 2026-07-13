# Anomaly Detection

## Vault Anomaly Detection User Guide

## Purpose

Vault Anomaly Detection monitors configured Salesforce data objects and metadata types for unusual changes. The feature helps identify unexpected activity, review affected records, compare snapshots, and roll back selected data changes where required. The workflow begins with configuration, continues through dashboard monitoring and anomaly review, and ends with rollback or comparison result tracking.

## Workflow Covered

* Configure anomaly detection for data and metadata.
* Select notification and exclusion settings.
* Monitor active or paused detection status from the dashboard.
* Review anomaly details and compare detected records.
* Submit rollback jobs and review rollback outcomes.
* Use job history, compare labels, export, and field-selection controls.
* Pause, stop, or restart anomaly detection.

Anomaly Detection is configured from the Anomaly Detection workspace. The configuration defines the source org, monitored data objects, monitored metadata types, threshold percentages, notification recipients, and excluded change owners. Once the configuration is saved, Vault begins evaluating the selected scope based on the scheduled detection cycle.

![](<../../.gitbook/assets/Unknown image (268)>)

&#x20;                                                _Anomaly Detection landing page before configuration_

![](<../../.gitbook/assets/Unknown image (269)>)

&#x20;                                                _Config Creation window with Data threshold settings_

![](<../../.gitbook/assets/Unknown image (270)>)

&#x20;                                                _Data object selection for anomaly monitoring_

![](<../../.gitbook/assets/Unknown image (271)>)

&#x20;                                                _Config Creation window with Metadata threshold settings_

![](<../../.gitbook/assets/Unknown image (272)>)

&#x20;                                                _Metadata type selection for anomaly monitoring_

![](<../../.gitbook/assets/Unknown image (273)>)

&#x20;                                                _Email Notifications and External Changes of Users options_

![](<../../.gitbook/assets/Unknown image (274)>)

&#x20;                                                _User Details selection for excluding internal application users_

![](<../../.gitbook/assets/Unknown image (275)>)

&#x20;                                                _External Changes of Users option after selecting Vault users_

![](<../../.gitbook/assets/Unknown image (276)>)

&#x20;                                                _Salesforce User Details selection for excluding Salesforce users_

## Monitoring the Dashboard

After configuration is saved, the dashboard displays the detection status, source org, date range, and anomaly summary cards for Data and Metadata. The status indicator shows whether anomaly detection is active or paused. The dashboard presents detected data changes by severity so the investigation can continue from a summarized view into detailed records.

![](<../../.gitbook/assets/Unknown image (277)>)

&#x20;                                                _Anomaly Detection dashboard after configuration is saved_

![](<../../.gitbook/assets/Unknown image (278)>)

&#x20;                                                _Active anomaly detection status on the dashboard_

![](<../../.gitbook/assets/Unknown image (279)>)

&#x20;                                                _Data anomaly summary chart for the selected object_

![](<../../.gitbook/assets/Unknown image (280)>)

&#x20;                                                _Data anomaly summary chart with severity filter_

## Reviewing Data Anomaly Details

The Data anomaly details view lists detected records for the selected source org, object, and detection period. Records can be reviewed in the table, selected for rollback, or compared for deeper field-level analysis. The system presents available actions based on the selected records and the current result state.

![](<../../.gitbook/assets/Unknown image (281)>)

&#x20;                                                _Anomaly Details page with detected records_

![](<../../.gitbook/assets/Unknown image (282)>)

&#x20;                                                _Record selection for rollback action_

![](<../../.gitbook/assets/Unknown image (283)>)

&#x20;                                                _Rollback prerequisite and behavior information_

Rollback is initiated from the anomaly details or result views after eligible records are selected. Vault presents a rollback summary before submission, including rollback options and the selected record count. Once confirmed, a rollback job is created and tracked from the Anomaly Rollback section until completion.

![](<../../.gitbook/assets/Unknown image (284)>)

&#x20;                                           _Rollback Summary window with selected records and rollback preferences_

![](<../../.gitbook/assets/Unknown image (285)>)

&#x20;                                                _Rollback job submitted confirmation_

![](<../../.gitbook/assets/Unknown image (286)>)

&#x20;                                                _Anomaly Rollback job list_

![](<../../.gitbook/assets/Unknown image (287)>)

&#x20;                                                _Rollback job actions and progress tracking_

![](<../../.gitbook/assets/Unknown image (288)>)

&#x20;                                                _Rollback result details with Follow Records tab_

![](<../../.gitbook/assets/Unknown image (289)>)

&#x20;                                                _Rollback result details with Outcome Records tab_

![](<../../.gitbook/assets/Unknown image (290)>)

&#x20;                                                _Completed rollback status in the rollback job list_

Comparison results are accessed from Anomaly Detection Job History. The results view shows detected changes by compare label and object. Field-level changes are highlighted in the results table, and detailed record comparison is available through the View Record action. Export and field-selection options support focused review of the result set.

![](<../../.gitbook/assets/Unknown image (291)>)

&#x20;                                                _Return to the Anomaly Detection dashboard after rollback review_

![](<../../.gitbook/assets/Unknown image (292)>)

&#x20;                                                _Anomaly Details page with records selected for comparison_

![](<../../.gitbook/assets/Unknown image (293)>)

&#x20;                                                _Comparison job submitted confirmation_

![](<../../.gitbook/assets/Unknown image (294)>)

&#x20;                                                _Anomaly Detection Job History list_

![](<../../.gitbook/assets/Unknown image (295)>)

&#x20;                                                _Job history action for viewing comparison results_

![](<../../.gitbook/assets/Unknown image (296)>)

&#x20;                                                _Anomaly Detection Results page with comparison records_

![](<../../.gitbook/assets/Unknown image (297)>)

&#x20;                                                _View Record action in the comparison results table_

![](<../../.gitbook/assets/Unknown image (298)>)

&#x20;                                                _View Record window showing field-level snapshot comparison_

![](<../../.gitbook/assets/Unknown image (299)>)

&#x20;                                                _Export option in Anomaly Detection Results_

![](<../../.gitbook/assets/Unknown image (300)>)

&#x20;                                                _Export window with available export scope options_

![](<../../.gitbook/assets/Unknown image (301)>)

&#x20;                                                _Choose Fields option in Anomaly Detection Results_

![](<../../.gitbook/assets/Unknown image (302)>)

&#x20;                                                _Fields selection window for result display_

![](<../../.gitbook/assets/Unknown image (303)>)

&#x20;                                                _Records selected for rollback from Anomaly Detection Results_

![](<../../.gitbook/assets/Unknown image (304)>)

&#x20;                                                _Rollback action from Anomaly Detection Results_

![](<../../.gitbook/assets/Unknown image (305)>)

&#x20;                                                _Rollback fields selection window_

![](<../../.gitbook/assets/Unknown image (306)>)

&#x20;                                                _Rollback job submitted from comparison results_

Anomaly Detection Job History maintains the comparison and rollback activity initiated from the anomaly workflow. Each job entry provides status, timing, and action controls. Compare label actions open detailed field-level status information for the selected compare run.

![](<../../.gitbook/assets/Unknown image (307)>)

&#x20;                                                _Job History list after rollback submission from results_

![](<../../.gitbook/assets/Unknown image (308)>)

&#x20;                                                _Job History action for compare label review_

![](<../../.gitbook/assets/Unknown image (309)>)

&#x20;                                                _Compare Label window showing field-level status_

![](<../../.gitbook/assets/Unknown image (310)>)

&#x20;                                                _ob History action for detailed compare label review_

![](<../../.gitbook/assets/Unknown image (309)>)

&#x20;                                                _Compare Label window with scrollable field status list_

## Pausing, Stopping, and Restarting Detection

Anomaly detection can be temporarily paused until a selected date or permanently turned off. A confirmation message appears before permanent changes are applied. When detection is restarted, the dashboard returns to an active monitoring state and allows the detection date range to be selected again.

![](<../../.gitbook/assets/Unknown image (311)>)

&#x20;                                                _Date picker for changing the dashboard date range_

![](<../../.gitbook/assets/Unknown image (312)>)

&#x20;                                                _Pause anomaly detection date selection on the dashboard_

![](<../../.gitbook/assets/Unknown image (313)>)

&#x20;                                                _Save action for pausing anomaly detection until a selected date_

![](<../../.gitbook/assets/Unknown image (314)>)

&#x20;                                                _Active status after date-based anomaly detection control_

![](<../../.gitbook/assets/Unknown image (315)>)

&#x20;                                                _Turn off anomaly detection permanently option_

![](<../../.gitbook/assets/Unknown image (316)>)

&#x20;                                                _Confirmation window for turning off anomaly detection permanently_

![](<../../.gitbook/assets/Unknown image (317)>)

&#x20;                                                _Stopped anomaly detection status after permanent turn off_

![](<../../.gitbook/assets/Unknown image (318)>)

&#x20;                                                _Confirmation window for restarting anomaly detection_

![](<../../.gitbook/assets/Unknown image (319)>)

&#x20;                                                _Date picker available after anomaly detection is restarted_

## Result

After the workflow is completed, Vault maintains the anomaly configuration, displays the current monitoring state on the dashboard, stores comparison jobs in job history, and tracks rollback jobs separately. This provides a controlled path to identify suspicious changes, verify field-level differences, and restore selected data where required.
