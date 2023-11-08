# Salesforce API Version Mismatch for the CI Build and Custom Deployment

#### Salesforce API Version Mismatch for the CI Build and for the Custom Deployment. <a href="#salesforce-api-version-mismatch-for-the-ci-build-and-for-the-custom-deployment" id="salesforce-api-version-mismatch-for-the-ci-build-and-for-the-custom-deployment"></a>

To troubleshoot, run the following command to see the **default** API version for the SFDX:

```
sfdx config:get apiVersion --json
```

Next, run the below command to **change** the SFDX API version. _For example_, changing the API Version to 51.0:

```
sfdx config:set apiVersion=51.0 --global
```

Finally, run the command to see the **configured** API version:

```
sfdx config:get apiVersion --json
```



\
