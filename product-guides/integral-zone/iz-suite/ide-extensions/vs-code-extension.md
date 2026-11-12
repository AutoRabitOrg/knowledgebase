# VS Code Extension

The IZ extension for Visual Studio Code analyzes your projects while you code, with the quality profiles and rules from your IZ Suite workspace. This page covers installing it, connecting it to IZ Suite and the settings it adds to VS Code. To work with the results, see [Analyze and Fix in VS Code](analyze-and-fix-in-vs-code.md).

## Prerequisites

| You need               | Details                                                                                                                                                                     |
| ---------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Visual Studio Code** | On Windows, macOS or Linux.                                                                                                                                                 |
| **Java**               | Java 11 or later. The extension runs its analysis in a Java process on your computer.                                                                                       |
| **IZ Suite address**   | The address you use to sign in, for example `https://izsuite.example.com`.                                                                                                  |
| **Security token**     | Generate one in **Administration** → **My Account** → **Security credentials**. See [Security Credentials](../administration/my-account/security-credentials.md).           |
| **IDE key**            | Assigned to you by an administrator. Copy it from **Administration** → **My Account** → **IDE projects**. See [IDE Projects](../administration/my-account/ide-projects.md). |
| **Network access**     | From your computer to your IZ Suite address and to the IZ key service, `https://license.integralzone.com`.                                                                  |

<figure><img src="../../../../.gitbook/assets/v2-account-ide-projects (1).png" alt="Your IDE keys in My Account, where you copy the key for the extension"><figcaption></figcaption></figure>

### How the Extension Finds Java

When VS Code starts, the extension looks for Java 11 or later in this order:

1. The `java` command on your `PATH`.
2. The folder set in the `falconscan.ls.java.home` setting (see Settings).
3. The `JAVA_HOME` environment variable.

If none of them gives Java 11 or later, the extension shows a warning with two choices:

* Click **Install** to let the extension download Java 11 (Eclipse Temurin) for its own use. It downloads the build for your operating system and processor, sets `falconscan.ls.java.home` to it and asks you to restart VS Code. If the download fails, an error says why.
* Or install Java 11 or later yourself, or set `falconscan.ls.java.home` to the Java home folder (the folder that contains `bin`), then restart VS Code.

## Install the Extension

{% tabs %}
{% tab title="From the Marketplace" %}
1. In VS Code, open the **Extensions** view (`Ctrl+Shift+X`, or `Cmd+Shift+X` on macOS).
2. Search for `IntegralZone.falcon-scan`, the extension's identifier. The extension is listed as **IZ Scan**; the publisher is **IntegralZone**.
3. Click **Install**.
4. Restart VS Code.

You can also install it from a terminal:

```bash
code --install-extension IntegralZone.falcon-scan
```
{% endtab %}

{% tab title="From a VSIX File" %}
Use this when your VS Code cannot reach the Marketplace, for example a VS Code that runs on a server and opens in your browser.

1. Open `https://marketplace.visualstudio.com/items?itemName=IntegralZone.falcon-scan` on a computer with internet access.
2. Click **Download Extension** to save the `.vsix` file, and copy it to where your VS Code can open it.
3. In VS Code, open the **Extensions** view, click the **...** menu at the top of the view and choose **Install from VSIX...**.
4. Select the `.vsix` file.
5. Restart VS Code.

The machine that runs VS Code still needs Java 11 or later and network access to IZ Suite.
{% endtab %}
{% endtabs %}

When the extension starts, VS Code shows **Extension initialized successfully!**. If it shows **Failed to initialize the extension**, check the Java prerequisite.

To update the extension, update it from the **Extensions** view like any other extension. To remove it, click **Uninstall** on the extension in the **Extensions** view and restart VS Code.

## Connect to IZ Suite

1. Click the **IZ Scan** icon in the Activity Bar. The extension's side bar opens with three views: **Connection**, **Profile Rules \[In Use]** and **Support & Documentation**.
2. In **Connection**, click **IZ Suite Connection**.
3.  Fill in the connection form. All three fields are required.

    | Field               | Description                                                       |
    | ------------------- | ----------------------------------------------------------------- |
    | **Server URL**      | Your IZ Suite address, for example `https://izsuite.example.com`. |
    | **Security Token**  | Your security token. Click **View** to show what you typed.       |
    | **Developer Token** | Your IDE key. Click **View** to show what you typed.              |
4. Click **Save Connection**.

The extension checks that the server is reachable, that the security token is valid and that the IZ key service recognizes the IDE key. It then downloads the IDE settings, the language settings and the list of languages your licence allows, and lists their quality profiles. If something fails, the form shows the error.

{% hint style="danger" %}
The extension saves the tokens in your VS Code user settings, in plain text. Do not share your settings file, and use a security token that carries only the roles the extension needs.
{% endhint %}

To change the connection later, click the connection (your server URL) at the top of the **Connection** view, change the fields and click **Save Connection** again.

## Choose the Quality Profiles

After you connect, the **Connection** view shows your server URL, and under it each language available to you. Expand a language to see its quality profiles:

| Label          | Meaning                                                                                             |
| -------------- | --------------------------------------------------------------------------------------------------- |
| **\[Default]** | The language's default quality profile in IZ Suite. The extension uses it until you choose another. |
| **\[Active]**  | The profile the extension uses for this language.                                                   |

To use another profile, hover over it and click the check icon (**Activate / Apply Profile**). The extension reloads the profile's rules into **Profile Rules \[In Use]**. Click a rule there to read its description.

Which profiles are listed depends on the **Show All Quality Profiles** IDE setting in IZ Suite. See [IDE Extensions](./).

## Settings

The extension stores its configuration in your VS Code user settings. The connection form and the **Connection** view write them for you; edit them by hand only when told to. Open them with **Preferences: Open User Settings (JSON)** in the Command Palette.

| Setting                                | What it holds                                                                                                                                                                                                   |
| -------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `falconscan.connection`                | The connection: `serverURL`, `securityToken`, `developerToken`, the `connectionType`, `allowedLanguages` (the languages available to you) and other values the extension fills in when you save the connection. |
| `falconscan.muleQualityProfile`        | The `key` of the active Mule quality profile.                                                                                                                                                                   |
| `falconscan.apiQualityProfile`         | The `key` of the active API quality profile.                                                                                                                                                                    |
| `falconscan.kubernetesQualityProfile`  | The `key` of the active Kubernetes quality profile.                                                                                                                                                             |
| `falconscan.logicappQualityProfile`    | The `key` of the active Azure Logic Apps quality profile.                                                                                                                                                       |
| `falconscan.apimgmtQualityProfile`     | The `key` of the active Azure API Management quality profile.                                                                                                                                                   |
| `falconscan.functionappQualityProfile` | The `key` of the active Azure Function App quality profile.                                                                                                                                                     |
| `falconscan.csharpQualityProfile`      | The `key` of the active C# quality profile.                                                                                                                                                                     |
| `falconscan.pythonQualityProfile`      | The `key` of the active Python quality profile.                                                                                                                                                                 |
| `falconscan.pysparkQualityProfile`     | The `key` of the active PySpark quality profile.                                                                                                                                                                |
| `falconscan.javaQualityProfile`        | The `key` of the active Java quality profile.                                                                                                                                                                   |
| `falconscan.lambdaQualityProfile`      | The `key` of the active AWS Lambda quality profile.                                                                                                                                                             |
| `falconscan.cfnQualityProfile`         | The `key` of the active AWS CloudFormation quality profile.                                                                                                                                                     |
| `falconscan.ls.java.home`              | The Java home folder the extension uses when `java` on your `PATH` is missing or older than Java 11.                                                                                                            |

For example, to point the extension at a specific Java installation:

```json
{
  "falconscan.ls.java.home": "/Library/Java/JavaVirtualMachines/temurin-17.jdk/Contents/Home"
}
```

## Language Server

The analysis runs in a language server, a Java process that the extension starts when it activates (when you open its views or run one of its commands) and stops when VS Code closes. It reads your project files locally, so your code stays on your computer. It keeps the downloaded profiles and rules in a cache, which **Sync Rules from Server** refreshes. It publishes issues to VS Code's **Problems** panel and to the extension's results view.

The language server also talks to IZ Suite in the background: it publishes the summary of the projects you analyzed (see [IDE Extensions](./)) and checks your IDE key.

## Next Steps

* [Analyze and Fix in VS Code](analyze-and-fix-in-vs-code.md): read the results, fix issues and control the analysis.
* [Custom Rule Editor](rules-playground.md): write and publish a custom rule from VS Code.
* [IDE Projects](../administration/my-account/ide-projects.md): copy your IDE key and see the projects you analyzed.
* [IDE Extensions](./): how the extensions work with IZ Suite.
