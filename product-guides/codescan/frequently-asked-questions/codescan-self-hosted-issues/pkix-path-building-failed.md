# PKIX Path Building Failed

**Error Code:**

```
javax.net.ssl.SSLHandshakeException: 
sun.security.validator.ValidatorException: 
PKIX path building failed: 
sun.security.provider.certpath.SunCertPathBuilderException: 
unable to find valid certification path to requested target.
```

**Reason:**\
This error occurs when the Java environment does not trust the certificate of the server running your SonarQube instance.

**Solution:**\
Install the server certificate to the Java key.

**Steps:**

1. In your browser, to the left of the URL, there is a lock icon (![image.png](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-ICO24JDZ.png)).
2. Click on this icon and a window will pop up. From the window, select **Connection is secure**.\
   ![image.png](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-5THK9CAG.png)
3. Select the second option, i.e., **`Certificate is valid`**.\
   ![image.png](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-XKDJCMFI.png)
4. Go to the **Details** tab and click on **Export**.\
   ![image.png](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-CZDQLKG3.png)
5. Rename the certificate (e.g., _**codescan-certificate**_), then choose a location and save the certificate.\
   ![image.png](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-IBFUK217.png)
6.  The next process is to install the certificate in the **cacerts** file of the jdk installed in the system using the command line.

    **Command:**

    > keytool -import **-alias** _{alias-name for the certificate}_ **-keystore** _“{path for the cacerts file}”_ **-file** _{path where we have save the certificate}_

    \
    **Example:**

    > keytool -import **-alias** _codescan-certificate_ **-keystore** _"C:\Program Files\Java\jdk-11.0.9\lib\security\cacerts"_ **-file** _c:/tmp/codescan-certificate.crt_

>

When adding the certificate, password is required. The password is **`changeit`.**

Point to Note:

If adding the certificate as a trusted certificate to the Java Keystore still results in the **PKIX path building failed** error, we suggest you delete the currently installed certificate from the Java Keystore, export a new certificate, and then attempt a new installation of the certificate.

**Command to list all of the certificates from the Java Keystore:**\
keytool -list -v **-keystore** _“{path for the cacerts file}”_ > /tmp/certs\_list.txt

**Example:** keytool -list -v **-keystore** _“c:\Program Files\Java\jdk-11.0.13\lib\security\cacerts”_ > /tmp/certs\_list.txt\
\
\
**Command to delete the certificate:**\
keytool -delete -noprompt **-alias** _{alias-name for the certificate}_ **-keystore** _“{path for the cacerts file}”_

**Example:** keytool -delete -noprompt **-alias** _codescan-certificate_ **-keystore** _“c:\Program Files\Java\jdk-11.0.13\lib\security\cacerts”_

