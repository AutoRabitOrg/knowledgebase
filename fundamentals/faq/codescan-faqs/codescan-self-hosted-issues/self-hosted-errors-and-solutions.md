# Self-Hosted Errors and Solutions

## CodeScan Self-Hosted (On-Premises)

## Errors and Solutions

### Why is my CodeScan update binding getting failed?

If the CodeScan update binding is getting failed, try disabling the VPN and antivirus, then try updating the binding again.

**If the binding successfully updates,** the error occurred due to antivirus blocking CodeScan. Add CodeScan to the list of allowed sites for the antivirus in use.

**If the binding still fails**, raise a [Support Ticket](https://support.autorabit.com/portal/en/home), including the **analyzer logs** and **verbose logs** in the attachment.

### Why did I get the following error during initialization of VM: Could not reserve enough space for xxxKB object heap?

If you are experiencing this error when running a scan, the issue may be with your Java version. **32-bit Java versions** have a lower limit to their heap size. This limit can be as low as **1.6GB** on Windows operating systems.

If you are running a **64-bit** operating system, you will need to upgrade to a **64-bit version of Java**.

You can check whether your Java version is **32** or **64-bit** by using the command: _**java -d64 -version**_ in your command prompt or terminal. If you have a **32-bit version of Java** installed, you will get the message:

```
Error: This Java instance does not support a 64-bit JVM.
```

To correct this error, please install the proper Java version.

### Why am I getting the error: java.lang.OutOfMemoryError: GC overhead limit exceeded?

This error can be solved by manually adding a parameter to your Ant environment path variable.

**In Windows:**

```
set ANT_OPTS=%ANT_OPTS% -Xmx2048M
```

**In Linux/OS X:**

```
export ANT_OPTS=$ANT_OPTS -Xmx2048M
```

If the problem persists, please contact [support@autorabit.com](mailto:itservice@autorabit.com).

### Why am I getting the error: Jenkins: java.lang.OutOfMemoryError: Java heap space?

This error can be solved by manually adding a parameter to dedicate memory to the build process.

1. In your Jenkins project, click **Configure**.
2. Scroll down to the **Build** section of the page to the Build Step titled **Invoke Ant** with the fields:
   * **Ant Version**: [CodeScan](https://www.codescan.io/) Bundled Ant
   * **Targets**: sonar
3. Click on **Advanced**.
4. In the **Java Options** field, add the parameter -**Xmx2000m**. This will assign **2000mb** of memory to you build.

If after increasing the heap space, you get the error:

{% code overflow="wrap" %}
```
Error occurred during initialization of VM Could not reserve enough space for xxxxxxKB object heap
```
{% endcode %}

This usually happens because the JVM you’re running is 32-bit, which can’t allocate very large contiguous memory blocks; install and run a 64-bit Java version (or lower the `-Xmx` value) to resolve the issue.

### Why am I getting a PKIX Path Building failed error?

**Error Code:**

```
javax.net.ssl.SSLHandshakeException: 
sun.security.validator.ValidatorException: 
PKIX path building failed: 
sun.security.provider.certpath.SunCertPathBuilderException: 
unable to find valid certification path to requested target.
```

This error occurs when the Java environment does not trust the certificate of the server running your SonarQube™ instance.

To correct this issue, you need to install the server certificate to the Java key.

1. In your browser, to the left of the URL, there is a lock icon (![](https://knowledgebase.autorabit.com/~gitbook/image?url=https%3A%2F%2F1912836914-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F9vAxMuDrkUkB4OXlH9CL%252Fuploads%252F4DlQ8zznQx1sY1L0PXJn%252Fimage.png%3Falt%3Dmedia%26token%3D92c84356-531e-4975-aa19-1bb827f245a4\&width=300\&dpr=4\&quality=100\&sign=feefb4d8\&sv=2)). Click on this icon and a window will pop up.&#x20;
2. From the window, select **Connection is secure**.

<figure><img src="https://knowledgebase.autorabit.com/~gitbook/image?url=https%3A%2F%2F1912836914-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F9vAxMuDrkUkB4OXlH9CL%252Fuploads%252FHyL8Xq5eKjxeGlD3mSC3%252Fimage.png%3Falt%3Dmedia%26token%3D5a1eb181-d254-478f-9602-64a8cc7241cc&#x26;width=768&#x26;dpr=4&#x26;quality=100&#x26;sign=db602ed9&#x26;sv=2" alt=""><figcaption></figcaption></figure>

3. Next, select the second option: **`Certificate is valid`**.

![](https://knowledgebase.autorabit.com/~gitbook/image?url=https%3A%2F%2F1912836914-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F9vAxMuDrkUkB4OXlH9CL%252Fuploads%252Fi8nO8q5LB43e92nfTXpS%252Fimage.png%3Falt%3Dmedia%26token%3D800a8a69-d937-4c5a-b7a7-1121b69e66cf\&width=768\&dpr=4\&quality=100\&sign=40e35397\&sv=2)

4. Go to the **Details** tab and click on **Export**.

![](https://knowledgebase.autorabit.com/~gitbook/image?url=https%3A%2F%2F1912836914-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F9vAxMuDrkUkB4OXlH9CL%252Fuploads%252Fa9ALPUunDZSAC3e8POJh%252Fimage.png%3Falt%3Dmedia%26token%3D47cfcb9d-047c-47e3-818f-4997746e1b4f\&width=768\&dpr=4\&quality=100\&sign=b0a6e876\&sv=2)

5. Rename the certificate (e.g., _**codescan-certificate**_), then choose a location and save the certificate.

![](https://knowledgebase.autorabit.com/~gitbook/image?url=https%3A%2F%2F1912836914-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F9vAxMuDrkUkB4OXlH9CL%252Fuploads%252F8NEL9QIEhuhbeqVTGkXN%252Fimage.png%3Falt%3Dmedia%26token%3D5bd46583-8e4f-4033-986d-c5a8b08aaae5\&width=768\&dpr=4\&quality=100\&sign=56c00d9c\&sv=2)

6. The next process is to install the certificate in the **cacerts** file of the jdk installed in the system using the command line.

**Command:**

> keytool -import **-alias** _{alias-name for the certificate}_ **-keystore** _“{path for the cacerts file}”_ **-file** _{path where we have save the certificate}_

**Example:**

> keytool -import **-alias** _codescan-certificate_ **-keystore** _"C:\Program Files\Java\jdk-11.0.9\lib\security\cacerts"_ **-file** _c:/tmp/codescan-certificate.crt_

When adding the certificate, password is required. The password is **`changeit`.**

**Note:**

If adding the certificate as a trusted certificate to the Java Keystore still results in the **PKIX path building failed** error, delete the currently installed certificate from the Java Keystore, export a new certificate, and then attempt a new installation of the certificate.

**Command to list all of the certificates from the Java Keystore:** keytool -list -v **-keystore** _“{path for the cacerts file}”_ > /tmp/certs\_list.txt

**Example:** keytool -list -v **-keystore** _“c:\Program Files\Java\jdk-11.0.13\lib\security\cacerts”_ > /tmp/certs\_list.txt **Command to delete the certificate:** keytool -delete -noprompt **-alias** _{alias-name for the certificate}_ **-keystore** _“{path for the cacerts file}”_

**Example:** keytool -delete -noprompt **-alias** _codescan-certificate_ **-keystore** _“c:\Program Files\Java\jdk-11.0.13\lib\security\cacerts”_[\
](https://knowledgebase.autorabit.com/fundamentals/faq/codescan-faqs/codescan-self-hosted-issues/java.lang.outofmemoryerror-gc-overhead-limit-exceeded)
