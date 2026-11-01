# Analyze and Fix in Anypoint Studio

Once the plugin is connected to IZ Suite, it analyzes your Mule and API projects as you build them. Issues are found as soon as you configure a component, so you can fix them before they reach your repository.

{% hint style="info" %}
Install the plugin, connect it and sync metadata first. See [Anypoint Studio Plugin](anypoint-studio-plugin.md).
{% endhint %}

## When the Analysis Runs

The plugin analyzes the whole project of the file you are editing.

| Event                                           | What happens                                                                                      |
| ----------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| You open or switch to a file of another project | The plugin analyzes that project.                                                                 |
| You save a change                               | The plugin analyzes the current project again.                                                    |
| You click **Reload OnTheFly Results**           | The plugin analyzes the current project again.                                                    |
| You click **Sync Rules From Server**            | The plugin downloads the rules of your quality profiles again, then analyzes the current project. |

The plugin analyzes a project only when your IDE key is valid and still has allowance for a new project, and the project name is allowed by the IDE settings in IZ Suite. Otherwise **On The Fly Results** shows the reason instead of issues. See [IDE Extensions](./#control-which-projects-developers-can-analyze).

## Read the Results

### On The Fly Results

1. Click **Window** → **Show View** → **Other...**.
2. Expand the plugin's category and select **On The Fly Results**.
3. Click **Open**.

Open a Mule configuration file or API specification of your project. The view lists the issues of the whole project.

| Column                | Description                                                                          |
| --------------------- | ------------------------------------------------------------------------------------ |
| **Error Description** | The rule the code breaks.                                                            |
| **Severity**          | The rule's severity, with its icon.                                                  |
| **Line**              | The line of the issue.                                                               |
| **Auto Fix**          | **Fix** and **Preview** when the rule has an automatic fix and autofix is turned on. |
| **Resource**          | The file.                                                                            |
| **Path**              | The file's path in the project.                                                      |

Double-click an issue to open the **Rule Description** view: the rule name, severity, type and description, with compliant and non-compliant examples where the rule has them.

The view's toolbar and menu have:

| Action                      | What it does                                                                                                                                             |
| --------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Group By File**           | Groups the issues by file.                                                                                                                               |
| **Group By Component**      | Groups the issues by component type.                                                                                                                     |
| **Group By Severity**       | Groups the issues by severity.                                                                                                                           |
| **Reload OnTheFly Results** | Analyzes the current project again.                                                                                                                      |
| **Sync Rules From Server**  | Downloads the rules again from IZ Suite and re-analyzes. Use it after your team changes rules or profiles.                                               |
| **Start/Stop Analysis**     | Stops or restarts the automatic analysis on save and on switching projects. Stop it while you make a large change, and start it again when you are done. |
| **Auto Fix Logs**           | Opens the **Auto Fix Logs** view.                                                                                                                        |
| **View Announcements**      | Shows product announcements.                                                                                                                             |

### Problems View

The plugin also adds a marker for each issue, so issues appear in Anypoint Studio's **Problems** view and beside the line in the editor.

| Rule severity            | Shown in Problems as |
| ------------------------ | -------------------- |
| Blocker, Critical, Major | Error                |
| Minor                    | Warning              |
| Info                     | Info                 |

## Fix Issues with Autofix

Turn autofix on once:

1. Open **Window** → **Preferences** → **IZ Preferences**.
2. Under **Additional Settings**, select **Enable Auto Fix**.
3. Click **Apply and Close**.

Then, for an issue whose rule has an automatic fix:

1. Click **Preview** in the **Auto Fix** column. A dialog lists each change the fix would make. Your files are not changed.
2. Click **Fix** to apply the change.

After a fix, the plugin analyzes the project again, so the results reflect the change. A fix can change more than one file, for example the Mule configuration and a property file.

{% hint style="warning" %}
Commit or back up your work before you apply fixes, so you can review the change in your version control and undo it if needed.
{% endhint %}

### Autofix Logs

Every fix you apply is logged in the project, in `target/izanalyzer/autofix-log.csv`. Click **Auto Fix Logs** in the results toolbar, or open **Window** → **Show View** → **Other...** → **Auto Fix Logs**, to read the log as a table. **Refresh Logs** reloads it and **Clear Logs** deletes it.

## Your Results in IZ Suite

The plugin publishes a summary of each project you analyze to IZ Suite: the issue counts by severity and type, not your code. Open **Administration** → **My Account** → **IDE projects**, click **Scanned projects** on your key, and click **Review results** on a project. The first analysis of a project uses one project of your key's allowance; **Token Usage** in the plugin's preferences shows how many you have used.

<figure><img src="../../../../.gitbook/assets/.gitbookassetsgs-ide-keys-review (1).png" alt="Review results drawer with the latest published scan counts and recent scans"><figcaption><p>Results published from the IDE</p></figcaption></figure>

## Next steps

* [Rules Playground](rules-playground.md): write a custom rule and try it on your project.
* [IDE Projects](https://knowledgebase.autorabit.com/product-guides/integral-zone/iz-suite/my-account/ide-projects): review the projects you analyzed.
* [Anypoint Studio Plugin](anypoint-studio-plugin.md): connection, profiles and preferences.
