# Invalid meta-xml name: lwc/xxx/xxx.css-meta.xml, should end with js-meta.xml

## Error message: Invalid meta-xml name: lwc/xxx/xxx.css-meta.xml, should end with js-meta.xml

When a deployment fails, this error usually occurs due to behavior in the Salesforce CLI 7.83 version. When retrieving the LWC components, it retrieves .css-meta.xml rather than .js-meta.xml file, which results in the deployment failing. Try renaming the .css-meta.xml file to .js-meta.xml and running the deployment again. Salesforce stopped maintaining SFDX v7 in April 2023 and no longer provides updates, bug fixes, or technical support.&#x20;
