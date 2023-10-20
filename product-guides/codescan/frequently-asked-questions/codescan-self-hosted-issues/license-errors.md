# License Errors

### License Expired Errors <a href="#license-expired-errors" id="license-expired-errors"></a>

You must renew your subscription by entering a new licence key if your subscription has expired and you can no longer access your CodeScan account. For your subscription extension and the proper licence key, reach out to our support team.

However, if the system throws the below error message after you enter a new licence key, you need to identify where the expired licence key is being passed on and update it with the new licence key.

```
XXXXXXXXXXXXXXXXXXXXXX

License is not valid
License expired on <date_of_expiry>
Code: 6

XXXXXXXXXXXXXXXXXXXXX
```

\


A CodeScan license key can be entered via the following ways:

* [**Sonarqube UI**](https://docs.sonarqube.org/9.6/instance-administration/license-administration/)
* **Command Line parameter** \[-Dsf.license.secured]
* In the **sonar.properties**, **codescan.properties** or **sfdx-project.json** inside the **project** folder considered for analysis
* In the **Sonarqube-{version} installation** folder\
  **Example:** _sonarqube-1.0.12345/conf/sonar.properties_
* [**System environment variable**](https://knowledgebase.autorabit.com/codescan/docs/setting-the-system-environment-variable)**:** Add an environment variable called **codescanLicense** containing the license on the user's machine.
  * **Variable name:** _codescanLicense_
  * **Value:** _\<License\_Key>_

***

### Proxy Errors <a href="#proxy-errors" id="proxy-errors"></a>

The most common problem with licensing problems are when your network has a proxy. This can cause licensing problems including:

```

101: Couldn’t fetch license for unlicensed project

104: Couldn’t fetch license: No response given

```

**Couldn't fetch license for unlicensed product** is sometimes coupled with something similar to:

>

{% code overflow="wrap" %}
```
JsonSyntaxException: com.google.gson.stream.MalformedJsonException: Expected EOF near <!DOCTYPE html PUBLIC "-//W3C//DTD

```
{% endcode %}

\
\
This is the proxy replying with an HTML error page when a JSON object is expected.

See [**here**](https://knowledgebase.autorabit.com/codescan/docs/setting-up-codescan-for-use-with-a-proxy) for instructions on how to set up CodeScan on a network with a proxy.

***

### Version Errors <a href="#version-errors" id="version-errors"></a>

Licensing version problems can occur with older versions of CodeScan. When this occurs, you will see the following error:

```
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

License is not valid:

License is not for this product

Code: 7

XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX 

```

This can be avoided by updating to the latest version of CodeScan.

If this is not an option, contact [Support](https://www.codescan.io/contact/) for assistance and we will provide you with the appropriate license version.

***

### Line Count Problems <a href="#line-count-problems" id="line-count-problems"></a>

Licensing problems can occur when you are operating outside the Terms of Service.

```

XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

License is not valid:

Lines exceed your license (6878 > 1000)

Code: 103

XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
```

This can be avoided by increasing your license limit or reducing the lines of code you are scanning. More information: [CodeScan License Issues (IDE)](https://knowledgebase.autorabit.com/codescan/docs/codescan-license-issues-ide)

Please reach out to [CodeScan Support](https://www.codescan.io/contact/) for any queries about your license.
