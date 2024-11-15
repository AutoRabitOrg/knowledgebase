# Copado MDAPI Integration

**Copado** is a release management tool for the Salesforce platform. Copado users can now integrate [CodeScan](https://www.codescan.io/) in their deployments to achieve error-free and secure releases.

For step-by-step instructions on how to integrate your [CodeScan](https://www.codescan.io/) account with Copado, click [here](https://docs.copado.com/article/ehy5j4f8e5-code-scan-sca-settings) and follow the documentation.

Once the integration has been completed, whenever you run a [static code analysis](https://www.codescan.io/blog/static-code-analysis-tools-for-salesforce/) (SCA) from a User Story or an Org Credential record associated with an environment inside this pipeline, it will apply these SCA settings and create a new [Static Code Analysis Results](https://docs.copado.com/article/e5b2qany3u-code-scan-sca-results) record with the scan details and a link to the CodeScan results.

It is important to note that when a scan is triggered from Copado, it scans for Apex components, Aura definition bundles, and a few metadata components. However, not all metadata supported by CodeScan is scanned.
