# Setting the System Environment Variable

### Overview <a href="#overview" id="overview"></a>

You must renew your subscription by entering a new licence key if your subscription has expired and you can no longer access your CodeScan account.

A CodeScan license key can be passed on by setting the path and environment variables in user's machine.

{% hint style="info" %}
**Note:** Administrator privileges are required to set the system environment variables.
{% endhint %}

### Set the system environment variables in Windows machine <a href="#set-the-system-environment-variables-in-windows-machine" id="set-the-system-environment-variables-in-windows-machine"></a>

#### For Windows 11 <a href="#for-windows-11" id="for-windows-11"></a>

1. Press the **`Windows key+X`** to access the **`Power User Task`** menu.
2. In the **`Power User Task`** menu, select the **`System`** option.
3. In the **`System`** window, scroll to the bottom and click the **`About`** option.
4. In the **`System > About`** window, click the **`Advanced system settings`** link at the bottom of the **`Device specifications`** section.
5. In the **`System Properties`** window, click the **`Advanced`** tab, then click the **`Environment Variables`** button near the bottom of that tab.
6. In the **`Environment Variables`** window, click on **`New`** button in the **`System variables`** section.
7. Enter the following details:
   * **`Variable name`:** **codescanLicense**
   * **`Value:`** **\<License\_Key>**
8. Click **`OK`**.
9. Click **`OK`** again to close the **`Environment Variables`** screen.

#### For Windows 10 <a href="#for-windows-10" id="for-windows-10"></a>

1. Press the **`Windows key+X`** to access the **`Power User Task`** menu.
2. In the **`Power User Task`** menu, select the **`System`** option.
3. In the **`About`** window, click the **`Advanced system settings`** link under **Related settings** on the far-right side.
4. In the **`System Properties`** window, click the **`Advanced`** tab, then click the **`Environment Variables`** button near the bottom of that tab.
5. In the **`Environment Variables`** window, click on **`New`** button in the **`System variables`** section.
6. Enter the following details:
   * **`Variable name`:** **codescanLicense**
   * **`Value:`** **\<License\_Key>**
7. Click **`OK`.**
8. Click **`OK`** again to close the **`Environment Variables`** screen.

#### In MacOS <a href="#in-macos" id="in-macos"></a>

System environment variables are added to the `.bash_profile` file:

1. Find the path to **`.bash_profile`** by using:

```
~/.bash-profile
```

2. Open the **`.bash_profile`** file with a text editor of your choice.
3. Scroll down to the end of the **`.bash_profile`** file.
4. Use the **`export`** command to add new environment variables:

```
export codescanLicense=[License_Key]
```

5. Save any changes you made to the **`.bash_profile`** file.
6. Execute the new **`.bash_profile`** by either restarting the terminal window or using:

```
source ~/.bash-profile
```
