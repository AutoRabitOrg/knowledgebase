# Security-Related Rules

## CodeScan Rules Related to Security

You can search for security-related rules using tags such as:

**Example**: sans-top25-insecure, sans-top25-porous, phishing, owasp-m4, owasp-a8, owasp-a6, owasp-a1, owasp-a2, owasp-m5, owasp-a5, owasp-m3, owasp-a7, owasp-a10, owasp-a4, owasp-a3, owasp-m2, owasp-a9, owasp-m1…

<figure><img src="../../../.gitbook/assets/image (1568).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../.gitbook/assets/image (1571).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../.gitbook/assets/image (1572).png" alt=""><figcaption></figcaption></figure>

Note: Tags are a way to categorize rules and issues.

### Types of Security Rules

CodeScan features four types of rules: **Bug** (reliability domain), **Code Smell** (maintainability), and **Vulnerability and Hotspot** (security domain). Given the importance of security, let's explore key concepts and how security rules differ from others.

* **Security-injection rules:** These rules address vulnerabilities arising when user-controlled inputs are not validated or sanitized. This can lead to dangerous flows from sources (user inputs) to sinks (sensitive functions). CodeScan employs taint analysis technology to detect issues.
* **Security-configuration rules:** These rules highlight security issues caused by incorrect parameters or the absence of essential checks when calling sensitive functions. Unlike injection rules, these problems are often encountered during execution without complex attacks.

### **Viewing Security Categories in CodeScan**

You can find the security category in the rules filter and related rules in the right-side panel, as shown in the images below.

<figure><img src="../../../.gitbook/assets/image (1573).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../.gitbook/assets/image (1574).png" alt=""><figcaption></figcaption></figure>

These security issues are divided into two categories: vulnerabilities and hotspots (see the main differences on the [Security Hotspots](https://knowledgebase.autorabit.com/product-guides/codescan/issues/security-hotspots) page).

Security hotspots represent code locations that should be reviewed but are not necessarily real vulnerabilities.

For example, most injection rules are considered vulnerabilities. If an SQL injection is found, it is certain that a fix (input validation) is required, making it a vulnerability.

On the other hand, the absence of an HttpOnly flag when creating a cookie could be problematic, but it might not always be. Since it is not always possible to implement the HttpOnly flag, determining the true level of risk requires review by a developer. Therefore, this is categorized as a hotspot.

With hotspots, we aim to help you understand information security risks, threats, impacts, root causes of security issues, and the selection of relevant software protections. In short, we want to educate developers and assist you in creating secure, ethical, and privacy-friendly applications.
