# Anypoint Teams Synchronization

## Anypoint Teams Sync

This section provides a detailed guide on how to synchronize users and permissions from Anypoint Teams to IZ Suite. It outlines the necessary steps to ensure seamless integration and efficient user management. By following these instructions, administrators can effectively sync/map user data along with permissions to align with IZ Suite’s roles. The process aims to streamline and enhance security by maintaining up-to-date user and access controls.

### Enable Anypoint Teams Sync

1. Login to IZ Suite Web application
2. Navigate to **`Settings`** -> **`Global Settings`**
3. Search for **`Anypoint Team Sync`** and click on **`Edit`** action
4. Update the value to **`true`** and click on Submit.&#x20;

### Schedule - Anypoint Teams Sync

1. Navigate to **`Schedules`** -> **`Schedules`**
2. Filter **`Anypoint Sync`** Job Type
3. There would be a recurring schedules created by default as part of the initial setup which runs every 12 hours once.
4. Optional - To update the default recurring schedule -
   1. Click on **`Configure Schedule`** and select **`Anypoint Sync`** job type
   2. Select `Scan on a recurring/regular basis` and select the schedule at which the Teams Sync should be performed
   3. Or select `Just one time scan` to just run the schedule once
5. Navigate to **`Schedules`** -> **`Jobs`** to check the run logs of the created schedule

### Map Anypoint Permissions to IZ Suite Permissions

1. Navigate to **`Settings`** -> **`Global Settings`**
2. Search for **`Anypoint Teams Role Mapping`** and click on **`Edit`** action
3. The mapping is defined using JSON. Below table describes the default/built-in mapping between **`Anypoint Teams`** and **`IZ Suite`** Permissions
4. The JSON can be updated based on the specific requirements of the organization

| Anypoint Team Permission Name                   | Anypoint Team Permission Key                       | IZ Suite Permission Key .13+                        |
| ----------------------------------------------- | -------------------------------------------------- | --------------------------------------------------- |
| **`Exchange Administrator`** .13+               | bc402b36-438d-430d-88c1-b2a14726a863               | **`view_dashboard`**                                |
| **`view_falcon_eye_api_application`**           | **`delete_falcon_eye_api_application`**            | **`edit_falcon_eye_api_application`**               |
| **`create_falcon_eye_api_application`**         | **`view_falcon_eye_api_application_dashboard`**    | **`view_falcon_eye_api_application_issues`**        |
| **`view_falcon_scan_api_application`**          | **`delete_falcon_scan_api_application`**           | **`edit_falcon_scan_api_application`**              |
| **`create_falcon_scan_api_application`**        | **`view_falcon_scan_api_application_dashboard`**   | **`view_falcon_scan_api_application_issues`** .13+  |
| **`Exchange Contributor`** .13+                 | d5b3fd8a-abe9-48de-a4e1-01040ca99b2e               | **`view_dashboard`**                                |
| **`view_falcon_eye_api_application`**           | **`delete_falcon_eye_api_application`**            | **`edit_falcon_eye_api_application`**               |
| **`create_falcon_eye_api_application`**         | **`view_falcon_eye_api_application_dashboard`**    | **`view_falcon_eye_api_application_issues`**        |
| **`view_falcon_scan_api_application`**          | **`delete_falcon_scan_api_application`**           | **`edit_falcon_scan_api_application`**              |
| **`create_falcon_scan_api_application`**        | **`view_falcon_scan_api_application_dashboard`**   | **`view_falcon_scan_api_application_issues`** .7+   |
| **`Exchange Viewer`** .7+                       | 98f87b9d-3e41-49cc-a171-f2580a742049               | **`view_dashboard`**                                |
| **`view_falcon_eye_api_application`**           | **`view_falcon_eye_api_application_dashboard`**    | **`view_falcon_eye_api_application_issues`**        |
| **`view_falcon_scan_api_application`**          | **`view_falcon_scan_api_application_dashboard`**   | **`view_falcon_scan_api_application_issues`** .13+  |
| **`Exchange Creator`** .13+                     | a772188d-d161-4e0c-bf5b-7cb021b7cd2f               | **`view_dashboard`**                                |
| **`view_falcon_eye_api_application`**           | **`delete_falcon_eye_api_application`**            | **`edit_falcon_eye_api_application`**               |
| **`create_falcon_eye_api_application`**         | **`view_falcon_eye_api_application_dashboard`**    | **`view_falcon_eye_api_application_issues`**        |
| **`view_falcon_scan_api_application`**          | **`delete_falcon_scan_api_application`**           | **`edit_falcon_scan_api_application`**              |
| **`create_falcon_scan_api_application`**        | **`view_falcon_scan_api_application_dashboard`**   | **`view_falcon_scan_api_application_issues`** .13+  |
| **`Delete Applications`** .13+                  | 4b3b5050-2f33-4740-9b63-dccc421b9f92               | **`view_dashboard`**                                |
| **`view_falcon_scan_mule_application`**         | **`view_falcon_scan_mule_application_dashboard`**  | **`view_falcon_scan_mule_application_issues`**      |
| **`delete_falcon_scan_mule_application`**       | **`edit_falcon_scan_mule_application`**            | **`create_falcon_scan_mule_application`**           |
| **`view_falcon_eye_mule_application`**          | **`view_falcon_eye_mule_application_dashboard`**   | **`view_falcon_eye_mule_application_issues`**       |
| **`delete_falcon_eye_mule_application`**        | **`edit_falcon_eye_mule_application`**             | **`create_falcon_eye_mule_application`** .7+        |
| **`Download Application`** .7+                  | 4e2a978e-0c79-4131-bebf-a653fd8ba039               | **`view_dashboard`**                                |
| **`view_falcon_scan_mule_application`**         | **`view_falcon_scan_mule_application_dashboard`**  | **`view_falcon_scan_mule_application_issues`**      |
| **`view_falcon_eye_mule_application`**          | **`view_falcon_eye_mule_application_dashboard`**   | **`view_falcon_eye_mule_application_issues`** .13+  |
| **`Manage Application Data`** .13+              | 51de3390-9bfe-4bcc-a790-6016b820ba92               | **`view_dashboard`**                                |
| **`view_falcon_scan_mule_application`**         | **`view_falcon_scan_mule_application_dashboard`**  | **`view_falcon_scan_mule_application_issues`**      |
| **`delete_falcon_scan_mule_application`**       | **`edit_falcon_scan_mule_application`**            | **`create_falcon_scan_mule_application`**           |
| **`view_falcon_eye_mule_application`**          | **`view_falcon_eye_mule_application_dashboard`**   | **`view_falcon_eye_mule_application_issues`**       |
| **`delete_falcon_eye_mule_application`**        | **`edit_falcon_eye_mule_application`**             | **`create_falcon_eye_mule_application`** .13+       |
| **`Manage Runtime Fabric`** .13+                | 3b8fefa5-f939-44f3-ae19-d154b89de45d               | **`view_dashboard`**                                |
| **`view_falcon_scan_mule_application`**         | **`view_falcon_scan_mule_application_dashboard`**  | **`view_falcon_scan_mule_application_issues`**      |
| **`delete_falcon_scan_mule_application`**       | **`edit_falcon_scan_mule_application`**            | **`create_falcon_scan_mule_application`**           |
| **`view_falcon_eye_mule_application`**          | **`view_falcon_eye_mule_application_dashboard`**   | **`view_falcon_eye_mule_application_issues`**       |
| **`delete_falcon_eye_mule_application`**        | **`edit_falcon_eye_mule_application`**             | **`create_falcon_eye_mule_application`** .7+        |
| **`Read Applications`** .7+                     | 674c9f7a-ee81-44d7-b25f-eb938d8e69b1               | **`view_dashboard`**                                |
| **`view_falcon_scan_mule_application`**         | **`view_falcon_scan_mule_application_dashboard`**  | **`view_falcon_scan_mule_application_issues`**      |
| **`view_falcon_eye_mule_application`**          | **`view_falcon_eye_mule_application_dashboard`**   | **`view_falcon_eye_mule_application_issues`** .13+  |
| **`Manage Servers`** .13+                       | 53823f29-6e57-4c42-acdb-e42a881a888f               | **`view_dashboard`**                                |
| **`view_falcon_scan_mule_application`**         | **`view_falcon_scan_mule_application_dashboard`**  | **`view_falcon_scan_mule_application_issues`**      |
| **`delete_falcon_scan_mule_application`**       | **`edit_falcon_scan_mule_application`**            | **`create_falcon_scan_mule_application`**           |
| **`view_falcon_eye_mule_application`**          | **`view_falcon_eye_mule_application_dashboard`**   | **`view_falcon_eye_mule_application_issues`**       |
| **`delete_falcon_eye_mule_application`**        | **`edit_falcon_eye_mule_application`**             | **`create_falcon_eye_mule_application`** .13+       |
| **`Manage Application Flows`** .13+             | 6c017fac-1311-11eb-adc1-0242ac120002               | **`view_dashboard`**                                |
| **`view_falcon_scan_mule_application`**         | **`view_falcon_scan_mule_application_dashboard`**  | **`view_falcon_scan_mule_application_issues`**      |
| **`delete_falcon_scan_mule_application`**       | **`edit_falcon_scan_mule_application`**            | **`create_falcon_scan_mule_application`**           |
| **`view_falcon_eye_mule_application`**          | **`view_falcon_eye_mule_application_dashboard`**   | **`view_falcon_eye_mule_application_issues`**       |
| **`delete_falcon_eye_mule_application`**        | **`edit_falcon_eye_mule_application`**             | **`create_falcon_eye_mule_application`** .7+        |
| **`Read Servers`** .7+                          | 8b7caaba-e94a-11e4-b02c-1681e6b88ec1               | **`view_dashboard`**                                |
| **`view_falcon_scan_mule_application`**         | **`view_falcon_scan_mule_application_dashboard`**  | **`view_falcon_scan_mule_application_issues`**      |
| **`view_falcon_eye_mule_application`**          | **`view_falcon_eye_mule_application_dashboard`**   | **`view_falcon_eye_mule_application_issues`** .13+  |
| **`Create Applications`** .13+                  | 3c91e5ca-fe58-441f-b6ab-a2be0a684bbf               | **`view_dashboard`**                                |
| **`view_falcon_scan_mule_application`**         | **`view_falcon_scan_mule_application_dashboard`**  | **`view_falcon_scan_mule_application_issues`**      |
| **`delete_falcon_scan_mule_application`**       | **`edit_falcon_scan_mule_application`**            | **`create_falcon_scan_mule_application`**           |
| **`view_falcon_eye_mule_application`**          | **`view_falcon_eye_mule_application_dashboard`**   | **`view_falcon_eye_mule_application_issues`**       |
| **`delete_falcon_eye_mule_application`**        | **`edit_falcon_eye_mule_application`**             | **`create_falcon_eye_mule_application`** .7+        |
| **`API Manager Environment Administrator`** .7+ | f14b0d23-a267-4014-9563-29d46a26295b               | **`view_dashboard`**                                |
| **`view_falcon_eye_apimgr_application`**        | **`delete_falcon_eye_apimgr_application`**         | **`edit_falcon_eye_apimgr_application`**            |
| **`create_falcon_eye_apimgr_application`**      | **`view_falcon_eye_apimgr_application_dashboard`** | **`view_falcon_eye_apimgr_application_issues`** .7+ |
| **`Deploy API Proxies`** .7+                    | 67ff49cb-6774-49de-92aa-95e0dd525b3d               | **`view_dashboard`**                                |
| **`view_falcon_eye_apimgr_application`**        | **`delete_falcon_eye_apimgr_application`**         | **`edit_falcon_eye_apimgr_application`**            |
| **`create_falcon_eye_apimgr_application`**      | **`view_falcon_eye_apimgr_application_dashboard`** | **`view_falcon_eye_apimgr_application_issues`** .7+ |
| **`Manage API Alerts`** .7+                     | c4662f0f-31fc-4791-9493-97a6e7ea261a               | **`view_dashboard`**                                |
| **`view_falcon_eye_apimgr_application`**        | **`delete_falcon_eye_apimgr_application`**         | **`edit_falcon_eye_apimgr_application`**            |
| **`create_falcon_eye_apimgr_application`**      | **`view_falcon_eye_apimgr_application_dashboard`** | **`view_falcon_eye_apimgr_application_issues`** .7+ |
| **`Manage APIs Configuration`** .7+             | 2ee11112-51ca-47a8-b4ae-a6bb6e7e5573               | **`view_dashboard`**                                |
| **`view_falcon_eye_apimgr_application`**        | **`delete_falcon_eye_apimgr_application`**         | **`edit_falcon_eye_apimgr_application`**            |
| **`create_falcon_eye_apimgr_application`**      | **`view_falcon_eye_apimgr_application_dashboard`** | **`view_falcon_eye_apimgr_application_issues`** .7+ |
| **`Manage Contracts`** .7+                      | be26fe60-0cc9-4b9a-bf20-5b12a6aa34e1               | **`view_dashboard`**                                |
| **`view_falcon_eye_apimgr_application`**        | **`delete_falcon_eye_apimgr_application`**         | **`edit_falcon_eye_apimgr_application`**            |
| **`create_falcon_eye_apimgr_application`**      | **`view_falcon_eye_apimgr_application_dashboard`** | **`view_falcon_eye_apimgr_application_issues`** .7+ |
| **`Manage Policies`** .7+                       | 456f139c-39e2-48c4-80b5-5205cb6b8ae2               | **`view_dashboard`**                                |
| **`view_falcon_eye_apimgr_application`**        | **`delete_falcon_eye_apimgr_application`**         | **`edit_falcon_eye_apimgr_application`**            |
| **`create_falcon_eye_apimgr_application`**      | **`view_falcon_eye_apimgr_application_dashboard`** | **`view_falcon_eye_apimgr_application_issues`** .4+ |
| **`View API Alerts`** .4+                       | 5a46e86c-7a28-424b-84a9-20021b1ec626               | **`view_dashboard`**                                |
| **`view_falcon_eye_apimgr_application`**        | **`view_falcon_eye_apimgr_application_dashboard`** | **`view_falcon_eye_apimgr_application_issues`** .4+ |
| **`View APIs Configuration`** .4+               | 8856c1b1-37cf-4f12-a02d-f36ce1a96a93               | **`view_dashboard`**                                |
| **`view_falcon_eye_apimgr_application`**        | **`view_falcon_eye_apimgr_application_dashboard`** | **`view_falcon_eye_apimgr_application_issues`**     |

### See Also

* [Aggregated Dashboard](dashboard.md)
* [Application Dashboard](applications/application-dashboard.md)
* [Agent Job Types](../agent/agent-job-types.md)
* [Mule Projects](applications/mule-applications.md)
* [API Applications](applications/api-applications.md)
