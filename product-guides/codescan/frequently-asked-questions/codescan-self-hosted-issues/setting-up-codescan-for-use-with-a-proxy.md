# Setting up CodeScan for use with a Proxy

To configure CodeScan for use in a network with a proxy you will need to set the following settings in your **antbuild.properties** file (version **3.6-RC3+**) or as parameters of your Jenkins job.

**http.proxyHost, http.proxyPort** and optionally **http.proxyUser** and **http.proxyPassword**

Older versions require you to set the above parameters and the following parameters in -**DANT\_OPTS**:

**https.proxyHost**, **https.proxyPort** and optionally **https.proxyUser** and **https.proxyPassword**

Also, if your SonarQube™ server is not localhost and your proxy doesn’t resolve internally, you’ll need to add the SonarQube™ server host to **http.nonProxyHosts** to ensure that contacting the SonarQube™ server doesn’t go through the proxy. The value in **http.nonProxyHosts** MUST match the **sonar.host.url** value in the **antbuild.xml** file (minus the port number) or it will not connect.

For example, **antbuild.xml**

<figure><img src="../../../../.gitbook/assets/image (438).png" alt=""><figcaption></figcaption></figure>

and **antbuild.properties**

<figure><img src="../../../../.gitbook/assets/image (439).png" alt=""><figcaption></figcaption></figure>
