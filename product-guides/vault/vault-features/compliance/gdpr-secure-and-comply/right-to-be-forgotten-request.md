# Right to Be Forgotten Request

[Article 17 of the GDPR](https://gdpr-info.eu/art-17-gdpr/), the right to erasure, also known as the right to be forgotten or RTBF, enables individuals to request the deletion or removal of their personal data when there is no compelling reason for its continued processing.

**Vault:** Your files stored in Vault are easily searchable and, based on a user’s permission level in Vault, you can delete them.

You can initiate an RTBF request for your backed-up [Salesforce data](https://www.autorabit.com/blog/how-to-backup-salesforce-data/) to be deleted if it is no longer needed or if it has been misused.

### Procedure <a href="#procedure" id="procedure"></a>

1. Login to [Vault ](https://www.autorabit.com/products/vault-data-backup-recovery/)using your username and password.
2. Go to the **GDPR** module and select your [Salesforce Org](https://knowledgebase.autorabit.com/docs/salesforce-org-managements).
3. Click on **Create GDPR Request**.

<figure><img src="../../../../../.gitbook/assets/image (257).png" alt=""><figcaption></figcaption></figure>

4. In the **Create GDPR Request** dialog box, select Request type as **Forget**.
5. The label name is auto-generated, however, you can enter the label name of your choice.
6. Under the **Object Name**, select the component for which the records need to be erased.
7. Based on the primary object selected, enter its subsequent records (separated using semicolon).
8. You can even upload your own file that contains record details from your local machine. Select the **Upload File** option and click on **Choose File** to upload the file (in .csv format) from your local machine.
9. Make sure GDPR Forget has been implemented for the records you chose to erase/forget in Salesforce.
10. Click **Submit**.

<figure><img src="../../../../../.gitbook/assets/image (258).png" alt="" width="414"><figcaption></figcaption></figure>

11. You'll be redirected to the GDPR summary page where the status of your request can be seen.

<figure><img src="../../../../../.gitbook/assets/image (259).png" alt=""><figcaption></figcaption></figure>

### More Actions on GDPR Request Summary page <a href="#more-actions-on-gdpr-request-summary-page" id="more-actions-on-gdpr-request-summary-page"></a>

For each GDPR request, you can view the following under the **Actions** tab:

<figure><img src="../../../../../.gitbook/assets/image (260).png" alt=""><figcaption></figcaption></figure>

1. **Log Info:** View the detailed log report for each GDPR request
2. **Delete GDPR Request:** Delete the raised request if no longer required.
3. **Download GDPR Result**: Download the GDPR result in your local machine for your reference. The downloaded file is in **CSV** format.
