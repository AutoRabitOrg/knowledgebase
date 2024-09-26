# Dataloader Configuration

### Dataloader Configuration: Overview <a href="#dataloader-configuration-overview" id="dataloader-configuration-overview"></a>

Dataloader plays an essential role in data migration from source sandbox to destination sandbox. However, in this data migration process, the chances of duplicate records being created always exist. To avoid this, ARM has developed a new feature that allows synchronizing data between the org with the help of ARM external ID. Now, the user can use data synchronization to connect the source and destination on the objects for which data migration is required.

### Creating a new Dataloader Configuration <a href="#creating-a-new-dataloader-configuration" id="creating-a-new-dataloader-configuration"></a>

1. Log in to your ARM account.
2. Hover your mouse over the [**`Dataloader`**](dataloader-configuration.md#dataloader-configuration-overview) module and select **`Dataloader Configuration`**.

<figure><img src="../../../../.gitbook/assets/image (1106).png" alt="" width="341"><figcaption></figcaption></figure>

3. Click on **`New Configuration`**.

<figure><img src="../../../../.gitbook/assets/image (1107).png" alt=""><figcaption></figcaption></figure>

4. On the next screen, give the process a **`Name`**.
5. Select the **`Source org`** and the **`Destination org`**.
6. Click on **`Login and Fetch Objects`**. This lists all the objects that are available in your source org.

<figure><img src="../../../../.gitbook/assets/image (1108).png" alt=""><figcaption></figcaption></figure>

7. Select the objects from the lists along with their respective **`Fields`**. You can use the **`search`** filter to find specific objects faster.

<figure><img src="../../../../.gitbook/assets/image (1109).png" alt=""><figcaption></figcaption></figure>

8. Click **`Save`** to save and initiate the job later or **`Save and Run`** to save and run the job simultaneously.

<figure><img src="../../../../.gitbook/assets/image (1110).png" alt=""><figcaption></figcaption></figure>

9. The **`Job Details`** section lists the objects you opted for earlier and the unique field sets for each object. The number of successful or failed record IDs is updated; you can view the detailed destination record IDs using the **`Search`**(![](<../../../../.gitbook/assets/image (1111).png>)) icon. You can download the successful/failed record IDs in your local system using the **`Download`** (![](<../../../../.gitbook/assets/image (1112).png>)) icon.

<figure><img src="../../../../.gitbook/assets/image (1113).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/image (1114).png" alt=""><figcaption></figcaption></figure>

#### More Options: <a href="#more-options" id="more-options"></a>

<figure><img src="../../../../.gitbook/assets/image (1115).png" alt=""><figcaption></figcaption></figure>

1. **`Edit:`** Allows users to modify the process details according to their requirements.
2. **`Delete:`** Deletes a process.
3. **`Clone:`** Creates a copy (clone) of the selected process.
4. **`Log:`** Provides information about the execution of a process.
