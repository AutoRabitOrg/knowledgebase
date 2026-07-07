# Destination\_ORG

## Reviewing destination org connection status and org details from the Vault Dashboard

## Starting Context

The flow begins after the source org and destination org are registered and authenticated in Vault. The Dashboard displays the connected org indicators at the top of the page, along with the available Vault actions and usage summaries.

{% hint style="info" %}
**Note:** The values displayed for the destination org depend on the connected Salesforce environment and remain specific to the selected org.
{% endhint %}

## Destination ORG Status on the Dashboard

The Dashboard shows both Source Org and Destination Org connection indicators near the page header. The Destination ORG indicator confirms that the destination Salesforce org is connected and ready for Vault workflows. The Re-Authenticate action remains available beside the org indicator to refresh the connection when required.

The rest of the Dashboard continues to show key Vault areas, including Backup Configs, Backup Jobs, Restore Jobs, Replicate Jobs, storage usage, and Recommended Actions. These sections provide the next operational paths after org registration is complete.

![](<../../.gitbook/assets/Unknown image (236)>)

## Review Destination Org Details

Selecting the Destination ORG indicator opens the Destination org details dialog. The dialog displays the registered destination org information in a read-only view, including Org name, Username, Org ID, API version, Instance URL, Environment type, Platform, Org edition, Auth type, and Registered details.

This information helps confirm that Vault is connected to the intended destination org before backup, restore, replication, or related data operations proceed. The displayed values reflect the authenticated Salesforce destination org and are not edited from this dialog.

![](<../../.gitbook/assets/Unknown image (237)>)

## Close the Details Dialog

The Close action dismisses the Destination org details dialog and returns to the Dashboard. The connected destination org status remains visible in the header, and the Dashboard remains available for the next Vault workflow.

## System Behavior

* Vault displays the Destination ORG indicator only after the destination org is connected.
* The Destination org details dialog provides read-only information about the registered destination org.
* Re-Authenticate remains available when the org connection must be refreshed.
* Closing the dialog does not change org registration, authentication, or Dashboard state.

## Final Result

After the destination org details are reviewed, the Dashboard confirms that the destination org remains connected and ready for downstream Vault operations. The flow ends with the Dashboard available for backup, restore, replication, or other configured actions.
