# CodeScan License Issues (IDE)

Depending on permissions in your SonarQube instance, the following issue can occur when running the analysis:

\[Warn  - 12:10:58] XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX&#x20;

\[Warn  - 12:10:58] CodeScan License has not been set

\[Warn  - 12:10:58] XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

\[Error - 12:10:58] CodeScan is NOT licensed. Please contact [support@code-scan.com](mailto:support@code-scan.com) to purchase or renew your license

\


The issue is that the license is a variable that needs to be checked by [CodeScan](https://www.codescan.io/) when it runs and the user that created the token needs certain permissions for the plugin to access the license variable.\
So this can be solved by allowing access to the variable or providing the license early. Here are the options:

Enable the Execute Analysis permission on the Global level to read the CodeScan license key configured on the organization level for each member/group that is using [VS Code](https://www.autorabit.com/ide-extension/).

#### OR <a href="#or" id="or"></a>

Add an environment variable called **codescanLicense** containing the license on the user's machine. The plugin checks for this before calling out.

#### OR for VS Code <a href="#or-for-vs-code" id="or-for-vs-code"></a>

In VSCode settings.json, add the following setting:\
"codescan.analyzerProperties": {\
"sf.license.secured": "**\<license-goes-here>** "\
&#x20;},

#### OR for IntelliJ <a href="#or-for-intellij" id="or-for-intellij"></a>

Under **Settings > Tools > CodeScan > Project Settings**, click the **Analysis Properties** tab. Add **sf.license.secured** with your license as the value.

If you do not have your license available, please contact [support@codescan.io](mailto::support@codescan.io)
