# PKIX Path Building Failed

**Error Code:**

```
javax.net.ssl.SSLHandshakeException: 
sun.security.validator.ValidatorException: 
PKIX path building failed: 
sun.security.provider.certpath.SunCertPathBuilderException: 
unable to find valid certification path to requested target.
```

**Reason:** This error occurs when the Java environment does not trust the certificate of the server running your SonarQube™ instance.

**Solution:** Install the server certificate to the Java key.

**Steps:**

1. In your browser, to the left of the URL, there is a lock icon (![](<../../../../.gitbook/assets/image (437).png>)).
2. Click on this icon and a window will pop up. From the window, select **Connection is secure**.

<figure><img src="../../../../.gitbook/assets/image (433).png" alt=""><figcaption></figcaption></figure>

3. Select the second option, i.e., **`Certificate is valid`**.

<figure><img src="../../../../.gitbook/assets/image (434).png" alt=""><figcaption></figcaption></figure>

4. Go to the **Details** tab and click on **Export**.

<figure><img src="../../../../.gitbook/assets/image (435).png" alt="" width="452"><figcaption></figcaption></figure>

5. Rename the certificate (e.g., _**codescan-certificate**_), then choose a location and save the certificate.

<figure><img src="../../../../.gitbook/assets/image (436).png" alt="" width="540"><figcaption></figcaption></figure>

6. The next process is to install the certificate in the **cacerts** file of the jdk installed in the system using the command line.

**Command:**

> keytool -import **-alias** _{alias-name for the certificate}_ **-keystore** _“{path for the cacerts file}”_ **-file** _{path where we have save the certificate}_

\
**Example:**

> keytool -import **-alias** _codescan-certificate_ **-keystore** _"C:\Program Files\Java\jdk-11.0.9\lib\security\cacerts"_ **-file** _c:/tmp/codescan-certificate.crt_

When adding the certificate, password is required. The password is **`changeit`.**

{% hint style="info" %}
**Point to Note:**

If adding the certificate as a trusted certificate to the Java Keystore still results in the **PKIX path building failed** error, we suggest you delete the currently installed certificate from the Java Keystore, export a new certificate, and then attempt a new installation of the certificate.
{% endhint %}

**Command to list all of the certificates from the Java Keystore:**\
keytool -list -v **-keystore** _“{path for the cacerts file}”_ > /tmp/certs\_list.txt

**Example:** keytool -list -v **-keystore** _“c:\Program Files\Java\jdk-11.0.13\lib\security\cacerts”_ > /tmp/certs\_list.txt\
\
**Command to delete the certificate:**\
keytool -delete -noprompt **-alias** _{alias-name for the certificate}_ **-keystore** _“{path for the cacerts file}”_

**Example:** keytool -delete -noprompt **-alias** _codescan-certificate_ **-keystore** _“c:\Program Files\Java\jdk-11.0.13\lib\security\cacerts”_
