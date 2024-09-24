# Security Hotspots

## **What is a Security Hotspot?**

A security hotspot identifies a piece of code that is sensitive to security issues and requires developer review. Upon reviewing the hotspot, you will determine whether there is an actual threat or if a fix is needed to secure the code.

## **Is it a Vulnerability or a Hotspot?**

The main difference between a hotspot and a vulnerability is the need for review before deciding on a fix:

* **Hotspot:** A hotspot points out a security-sensitive piece of code. While it may not immediately impact the overall security of the application, it requires a developer's review to decide if a fix is necessary.
* **Vulnerability:** A vulnerability directly identifies a security issue that affects the application's security and needs to be addressed immediately.

## **Why are security hotspots important?**

While the need to address individual hotspots depends on the specific context, security hotspots are crucial for enhancing an application's robustness. Addressing more hotspots generally leads to more secure code, which better withstands potential attacks. Reviewing security hotspots allows you to:

1. **Understand the Risk:** By evaluating hotspots, you gain insight into when and why a fix is needed to mitigate information security risks, including threats and potential impacts.
2. **Identify Protections:** Reviewing hotspots helps you recognize how to avoid writing vulnerable code, assess which protections are already in place, and identify which fixes still need to be applied.
3. **Assess Impacts:** Hotspots guide you in applying fixes to enhance your code's security based on its overall impact on the application's security. The hotspots page typically includes recommended secure coding practices to aid you during the review process.

## **Status**

Throughout its lifecycle, a security hotspot can have one of the following statuses:

* **To Review:** This is the default status assigned to new security hotspots by CodeScan. It indicates that a security hotspot has been identified and requires review.
* **Acknowledged:** This status means a developer has reviewed the security hotspot and a resolution is pending. This could be because a fix is in progress or additional time is needed to determine the appropriate action.
* **Fixed:** This status is used when a developer has reviewed the security hotspot and applied a fix to address the issue.
* **Safe:** This status indicates that a developer has reviewed the security hotspot and determined that no changes are necessary. This might be because other, more relevant protections are already in place.
* **Exception**: This status indicates that the code has been reviewed and does not pose a risk currently. Further review is needed at a later date.
