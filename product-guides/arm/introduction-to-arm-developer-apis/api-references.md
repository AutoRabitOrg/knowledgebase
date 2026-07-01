---
description: Comprehensive reference for integrating with AutoRABIT API endpoints
---

# API References

### Endpoint Overview <a href="#endpoint-overview" id="endpoint-overview"></a>

AutoRABIT API endpoints are listed below.

> **Continuous (CI) Jobs**\
> Retrieve the CI build / job details, trigger new job, and view different CI job reports.

> [/api/cijobs/v1/listjobs](https://documenter.getpostman.com/view/7212585/UVkvHBtD#5ed09b17-074c-4b86-b691-63f34fb39465)\
> [/api/cijobs/v1/history](https://documenter.getpostman.com/view/7212585/UVkvHBtD#7233ece7-4d94-4a69-b67d-84552f0e6815)\
> [/api/cijobs/v1/latestresults](https://documenter.getpostman.com/view/7212585/UVkvHBtD#b4ab95ee-09b1-4bdf-9c45-fc7e67312234)\
> [/api/cijobs/v1/pollstatus](https://documenter.getpostman.com/view/7212585/UVkvHBtD#685b51cb-ec61-4825-8152-bf6cf3bc51bc)\
> [/api/cijobs/v1/rollbackhistory](https://documenter.getpostman.com/view/7212585/UVkvHBtD#d5276c89-e10a-4d7e-b606-0c906fd36cb8)\
> [/api/cijobs/v1/rollbackdetails](https://documenter.getpostman.com/view/7212585/UVkvHBtD#2c6fdb6b-ba7d-484a-8863-9cf36d3464ac)\
> [/api/cijobs/v1/triggerbuild](https://documenter.getpostman.com/view/7212585/UVkvHBtD#2c7dc202-0437-4e02-bc9c-1dfc8ffc1b0d)\
> [/api/cijobs/v1/update/baselinerevision](https://documenter.getpostman.com/view/7212585/UVkvHBtD#14450888-d0bc-4f00-b400-f38a90282186)\
> [/api/cijobs/v1/triggerquickdeploy](https://documenter.getpostman.com/view/7212585/UVkvHBtD#888f1c91-bb51-4d8a-ae22-92a3415040fc)\
> [/api/cijobs/v1/triggerrollback](https://documenter.getpostman.com/view/7212585/UVkvHBtD#d68c63cd-15bf-4a54-b77a-b5582ef03989)\
> [/api/cijobs/v1/abort](https://documenter.getpostman.com/view/7212585/UVkvHBtD#a2afe9f3-7946-44cd-add0-11a0f34ac6a7)

## Deployment APIs

The Deployment APIs allow external applications to retrieve deployment information, execution details, deployment components, Jira stories, logs, and test coverage reports.<br>

[/api/deployments/v1/listdeployments](https://documenter.getpostman.com/view/46841090/2sBY4HSNpN#1650a778-8a7d-4d5c-8c9d-14e7cd1747c6)\
[/api/deployments/v1/deploymentdetails](https://documenter.getpostman.com/view/46841090/2sBY4HSNpN#25ddfae2-5dfa-4698-827f-3929f844269f)\
[/api/deployments/v1/deploymentcomponents](https://documenter.getpostman.com/view/46841090/2sBY4HSNpN#815cf38a-5c96-4db6-bd75-a833789457db)\
[/api/deployments/v1/deploymentstories](https://documenter.getpostman.com/view/46841090/2sBY4HSNpN#459491d5-27ec-4006-a5b8-365e43543d24)\
[/api/deployments/v1/promotionlog](https://documenter.getpostman.com/view/46841090/2sBY4HSNpN#3098e19f-9d04-4771-a38a-fe820b354578)\
[/api/deployments/v1/testcoveragereport](https://documenter.getpostman.com/view/46841090/2sBY4HSNpN#7b01d81c-47bf-4f22-9e46-5a799773c6af)



> **Note:** All Deployment APIs require a valid API token in the `token` request header. Generate an API token from **Administration → API Token Manager**.

Looking for nCino Developer API References? Follow the link [here](https://knowledgebase.autorabit.com/product-guides/arm/arm-features/ncino/developer-apis/api-references).
