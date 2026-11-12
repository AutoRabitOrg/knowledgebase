# Anypoint Studio Plugin

The IZ plugin for Anypoint Studio analyzes your Mule, API and Kubernetes projects while you build them, with the quality profiles and rules from your IZ Suite workspace. This page covers installing the plugin and connecting it to IZ Suite. To work with the results, see [Analyze and Fix in Anypoint Studio](analyze-and-fix-in-anypoint-studio.md).

## Prerequisites

| You need             | Details                                                                                                                                                                                                                |
| -------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Anypoint Studio**  | Running on Java 11 or later.                                                                                                                                                                                           |
| **IZ Suite address** | The address you use to sign in, for example `https://izsuite.example.com`.                                                                                                                                             |
| **Security token**   | Generate one in **Administration** → **My Account** → **Security credentials**. See [Security Credentials](../administration/my-account/security-credentials.md).                                                      |
| **IDE key**          | Assigned to you by an administrator. Copy it from **Administration** → **My Account** → **IDE projects**. See [IDE Projects](../administration/my-account/ide-projects.md).                                            |
| **Network access**   | From your computer to the update site `https://plugins.integralzone.com/v5`, your IZ Suite address the IZ key service, `https://license.integralzone.com`, and `https://iz-releases.s3.amazonaws.com` (version check). |

## Install the Plugin

1. In Anypoint Studio, click **Help** → **Install New Software...**.
2. In **Work with**, enter `https://plugins.integralzone.com/v5` and press Enter.
3. Select the **IZ Scan Analysis** feature. The update site has one feature.
4. Click **Next**, review the items to install, and click **Next** again.
5. Accept the licence agreement and click **Finish**.
6. If Anypoint Studio asks whether you trust the content, confirm it.
7. Restart Anypoint Studio when asked.

## Update the Plugin

1. Click **Help** → **Install New Software...**.
2. In **Work with**, enter `https://plugins.integralzone.com/v5` and press Enter.
3. Select **IZ Scan Analysis**, click **Next** and follow the steps.
4. Restart Anypoint Studio.

If you already have the latest version, the wizard says **All items are installed**.

{% hint style="info" %}
The plugin checks regularly whether its version is still supported. When it is not, it asks you to install the latest version.
{% endhint %}

## Remove the Plugin

1. Click **Help** → **Install New Software...**.
2. Click the **already installed** link.
3. On **Installed Software**, select the plugin and click **Uninstall...**.
4. Follow the steps, then restart Anypoint Studio.

## Connect to IZ Suite

Open the plugin's preferences: **Window** → **Preferences** → **IZ Preferences**. On macOS, the preferences are under the **Anypoint Studio** menu.

<figure><img src="../../../../.gitbook/assets/v2-account-ide-projects (2).png" alt="Your IDE keys in My Account, where you copy the key for the plugin"><figcaption></figcaption></figure>

1.  Under **Connection Details**, fill in the fields:

    | Field               | Description                                                                                                                     |
    | ------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
    | **Plugin Type**     | The kind of server. Choose **IZ Scan**, the IZ Suite connection. The other option, **IZ Analyzer**, is for IZ Analyzer servers. |
    | **Service URL**     | Your IZ Suite address, for example `https://izsuite.example.com`.                                                               |
    | **Security Token**  | Your security token. Click **View** to show what you typed, **Hide** to mask it again.                                          |
    | **Developer Token** | Your IDE key. **View** and **Hide** work the same way.                                                                          |
2. Click **Test Connection**. The plugin checks that the address is reachable and the security token is valid, and says **Connection successful to** your address.
3. Click **Sync Metadata**. The plugin checks your IDE key, downloads the IDE settings, the quality profiles of each language available to you, and their rules. When it finishes, it lists how many rules it downloaded per language.
4. Under **Quality Profiles**, choose the profile to use for each language (see below).
5. Click **Apply and Close**.

All four connection fields are required: **Test Connection** and **Sync Metadata** say **Fill in all the fields** when one is empty.

{% hint style="warning" %}
Sync metadata again whenever you change the connection or your quality profile choices, or when the plugin asks you to. The plugin also re-reads the IDE settings and rules from IZ Suite when you click **Sync Rules From Server** in **On The Fly Results**, and on its own every six hours.
{% endhint %}

## Preferences Reference

### Quality Profiles

After **Sync Metadata**, this section has one list per language available to you, showing each profile as its name and key. The plugin selects the profile you used last, or the first one. When you choose another profile, the plugin downloads its rules straight away and says **Downloaded** _N_ **rules for** the language.

Anypoint Studio lists every quality profile of the language.

### Additional Settings

| Setting               | Description                                                                                                                                              |
| --------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Enable Auto Fix**   | Turns on the **Fix** and **Preview** buttons in **On The Fly Results**. See [Analyze and Fix in Anypoint Studio](analyze-and-fix-in-anypoint-studio.md). |
| **Enable Clean Code** | Applies only to IZ Analyzer connections. Leave it off for IZ Suite.                                                                                      |
| **CLI Scanner Path**  | Applies only to IZ Analyzer connections. Leave it empty for IZ Suite.                                                                                    |

### Token Usage

| Field                          | Description                                                                                                                                                                                                               |
| ------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Total Projects Allowed**     | The number of projects your IDE key can analyze.                                                                                                                                                                          |
| **Total Projects Scanned**     | The projects analyzed with your key so far.                                                                                                                                                                               |
| **View Scanned Projects List** | Saves the list of projects analyzed with your key to a file named `scanned_projects.json` (one project path per line) in the current project's folder (or your temporary folder when no project is open) and shows where. |

To see the results the plugin published, open **Administration** → **My Account** → **IDE projects** in IZ Suite. See [IDE Projects](../administration/my-account/ide-projects.md).

## Next Steps

* [Analyze and Fix in Anypoint Studio](analyze-and-fix-in-anypoint-studio.md): read the results and fix issues.
* [Custom Rule Editor](rules-playground.md): write and publish a custom rule from Anypoint Studio.
* [IDE Extensions](./): how the plugin works with IZ Suite.
