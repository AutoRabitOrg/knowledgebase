# Error: "Invalid meta-xml name: lwc/xxx/xxx.css-meta.xml, should end with js-meta.xml"

### Description

The deployment is getting failed with the following error: **"Invalid meta-xml name: lwc/xxx/xxx.css-meta.xml, should end with js-meta.xml."**

### Cause

This error usually occurs due to behavior in the Salesforce CLI 7.83 version. When retrieving the lwc components, it retrieves .css-meta.xml rather than .js-meta.xml file which results in deployment to get failed.

### Resolution

Try renaming the .css-meta.xml file to .js-meta.xml and running the deployment again.
