# TFS

Integrating a **Team Foundation Server (TFS)** repository with AutoRABIT (ARM) lets you automate commits, merges, and CI/CD pipelines against code stored in your on-premises or Azure DevOps–hosted TFS project.

The steps below show an Org Admin how to register a TFS repo so ARM can authenticate, index metadata, and launch jobs.

***

## Registering TFS Repository in ARM <a href="#registering-tfs-repository-in-arm" id="registering-tfs-repository-in-arm"></a>

1. Log in to **ARM**.
2.  Hover over **`Admin`** and choose **`VC Repos`**.<br>

    <figure><img src="../../../../../.gitbook/assets/Screenshot 2025-08-16 at 8.27.09 PM.png" alt="" width="232"><figcaption></figcaption></figure>
3. Click **Register Repository**.
4. On the **Register Repository** page, select **TFS** as the **Version Control System**.
5. **Repository Label** – enter a friendly name that will appear in ARM.
6. **Repository URL** – paste the full TFS URL (e.g., `https://tfs.mycorp.com/tfs/Collection/Project`).
7. **Credentials** – choose stored credentials or click **+** to add new ones.
8.  Click **Test Connection**. A success message confirms ARM can authenticate.<br>

    <figure><img src="../../../../../.gitbook/assets/image (18) (1) (2).png" alt="" width="375"><figcaption></figcaption></figure>
9. Click **Save** to finish. The repository now appears in the VC Repos list.

{% hint style="info" %}
**nCino projects**\
Tick **Enable nCino** if the repo contains nCino objects. ARM marks such repositories with the nCino logo so you can spot them quickly.
{% endhint %}
