# SVN

Connecting an SVN (Subversion) repository to AutoRABIT (ARM) lets you automate commits, merges, and CI pipelines against code stored in that repo.\
The steps below walk an Org Admin through **registering** an SVN repository so ARM can authenticate, cache metadata, and trigger jobs.

***

## Registering SVN Repository in ARM <a href="#registering-svn-repository-in-arm" id="registering-svn-repository-in-arm"></a>

1. Log in to **ARM**.
2.  Hover over **`Admin`** and choose **`VC Repos`**.\
    \


    <figure><img src="../../../../../.gitbook/assets/Screenshot 2025-08-16 at 8.27.09 PM.png" alt="" width="232"><figcaption></figcaption></figure>
3. Click **Register Repository**.
4. On the **Register Repository** page:
   * Set **Version Control System** to **SVN**.
   * **Repository Label** – a friendly name that appears in ARM.
   * **Repository URL** – the full SVN URL (e.g., `https://svn.mycorp.com/repos/project`).
   * **Credentials** – select stored credentials or click **+** to add new ones.
5.  Click **Test Connection**. A success message confirms ARM can authenticate.\


    <figure><img src="../../../../../.gitbook/assets/image (17).png" alt="" width="375"><figcaption></figcaption></figure>
6. Click **Save** to finish. The repository now appears in the VC Repos list.

{% hint style="info" %}
**nCino projects**\
If your repository contains nCino objects, tick **Enable nCino** while registering. ARM marks such repos with the nCino logo so you can spot them quickly.
{% endhint %}
