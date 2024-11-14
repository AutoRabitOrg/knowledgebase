# Copado MDAPI Integration

**Copado** is a release management tool for the Salesforce platform. Copado users can now integrate [CodeScan](https://www.codescan.io/) in their deployments to achieve error-free and secure releases.

If you have been wondering on how to integrate your [CodeScan](https://www.codescan.io/) account with Copado, we have a step-by-step guide to help you, and you will be on your way to performing static analysis using CodeScan with Copado.

Click [here](https://docs.copado.com/article/ehy5j4f8e5-code-scan-sca-settings) to access the documentation required to follow step by step procedure on how to integrate it.

Once the integration is completed, whenever you run a [static code analysis](https://www.codescan.io/blog/static-code-analysis-tools-for-salesforce/) from a User Story or an Org Credential record associated to an environment inside this pipeline, it will take these SCA settings and will create a new [Static Code Analysis Results](https://docs.copado.com/article/e5b2qany3u-code-scan-sca-results) record with the scan details and a link to the CodeScan results.
