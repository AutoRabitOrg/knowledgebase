# Backup Config

This guide explains the process for creating a backup configuration in AutoRABIT Vault. The flow starts from the Dashboard, continues through object selection and configuration options, and ends with the saved backup configuration available from the Backup Config List.

| **Feature Area**    | Backup                                                                 |
| ------------------- | ---------------------------------------------------------------------- |
| **Workflow**        | Backup configuration creation                                          |
| **Primary Outcome** | A saved backup configuration is created for the selected objects.      |
| **Applies To**      | AutoRABIT Vault Free Trial and applicable AutoRABIT Vault environments |

## Before Starting

A source org and destination org must be connected before the backup configuration is created. The Dashboard shows the current connection status, available limits, storage usage, and recommended actions. When the environment is ready, the Backup Configs card provides access to configuration creation.

![](<../../.gitbook/assets/Unknown image (238)>)

## Open the Backup Configuration List

The Backup Configs card opens the Backup Config List. When no configuration exists, the list displays an empty state and provides the Create Config action. This starts the backup configuration workflow.

![](<../../.gitbook/assets/Unknown image (239)>)

## Select Objects for Backup

The Create Backup workflow opens at Select Objects. The object list displays available Salesforce objects with a search option for locating required objects. Objects selected in this step define the scope of the backup configuration.

After the required objects are selected, Next moves the workflow to Options. Cancel exits the creation flow without saving the configuration.

![](<../../.gitbook/assets/Unknown image (240)>)

## Configure Backup Options

The Options step captures the configuration details. Config Label identifies the backup configuration, while Description provides supporting context for the configuration purpose. The Exclude Deleted Records From the backup option controls whether deleted records are excluded from the backup scope.

Next remains unavailable until the required configuration details are entered. Back returns to the object selection step without completing the configuration.

![](<../../.gitbook/assets/Unknown image (241)>)

Once the required values are provided, Next becomes available. The configuration can then proceed to Review & Run.

![](<../../.gitbook/assets/Unknown image (242)>)

## Review and Save the Backup Configuration

The Review & Run step summarizes the selected objects and configuration settings before saving. The review includes the selected objects, Config Label, Description, and the current value of Exclude Deleted Records. This step provides a final confirmation point before the configuration is created.

Save Backup Config saves the configuration. During the save operation, the button displays a processing state to indicate that the request is being submitted.

![](<../../.gitbook/assets/Unknown image (243)>)

![](<../../.gitbook/assets/Unknown image (244)>)

## Confirm Configuration Creation

After the configuration is saved, AutoRABIT Vault returns to the Dashboard. The Backup Configs count updates to reflect the new configuration. Related dashboard indicators and recommended actions update based on the current environment state.

![](<../../.gitbook/assets/Unknown image (245)>)

Opening the Backup Config List displays the newly created configuration. The list includes the Configuration Name, Config Type, Last Config Status, and available actions. The status confirms whether the configuration creation completed successfully.

![](<../../.gitbook/assets/Unknown image (246)>)

## Result

The backup configuration is saved and available for future backup activity. The configuration can be reviewed or edited from the Backup Config List based on the available actions.
