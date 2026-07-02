# Scan External Repositories

## Configuring External Repositories Sync

### Configuring Bitbucket as an External Source

1. Create an OAuth consumer App in Bitbucket with the following details -
   1. Callback URL - https://\<FALCON\_SUITE\_INSTANCE\_URL>/oauth/bitbucket/callback
   2. URL - https://\<FALCON\_SUITE\_INSTANCE\_URL>
   3. Permissions - Account (Read), Repositories (Read)
2. Navigate to **`Global Settings`** -> **`Settings`** -> **`BitBucket Repo Sync Settings`** and click on edit. Other settings apart from the below-mentioned keys can be left blank.

### BitBucket Repo Sync Settings

| Settings Name                      | Description                                                                                                      |
| ---------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| **`OAUTH_CLIENT_ID`**              | OAuth Consumer Client Id. Used for authenticating the REST API to get repositories.                              |
| **`OAUTH_CLIENT_SECRET`**          | OAuth Consumer Client Secret. Used for authenticating the REST API to get repositories.                          |
| **`PROJECT_NAME_INCLUDE_PATTERN`** | Repository name matching this pattern will only be synced. By default all the repositories will be scanned.      |
| **`PROJECT_NAME_EXCLUDE_PATTERN`** | Repository name matching this pattern will only be ignored. By default none of the repositories will be ignored. |
| **`SCAN_ALL_APPLICATION`**         | Should all the repositories matching the Include / Exclude Pattern be scanned.                                   |
| **`SCAN_ALL_BRANCHES`**            | Should all the branches of the repository be scanned.                                                            |

### Configuring GitHub as an External Source

1. Navigate to **`Global Settings`** -> **`Settings`** -> **`GitHub Repo Sync Settings`** and click on edit. Other settings apart from the below-mentioned keys can be left blank.

### GitHub Repo Sync Settings

| Settings Name                      | Description                                                                                                      |
| ---------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| **`OAUTH_CLIENT_ID`**              | OAuth Consumer Client Id. Used for authenticating the REST API to get repositories.                              |
| **`OAUTH_CLIENT_SECRET`**          | OAuth Consumer Client Secret. Used for authenticating the REST API to get repositories.                          |
| **`PROJECT_NAME_INCLUDE_PATTERN`** | Repository name matching this pattern will only be synced. By default all the repositories will be scanned.      |
| **`PROJECT_NAME_EXCLUDE_PATTERN`** | Repository name matching this pattern will only be ignored. By default none of the repositories will be ignored. |
| **`SCAN_ALL_APPLICATION`**         | Should all the repositories matching the Include / Exclude Pattern be scanned.                                   |
| **`SCAN_ALL_BRANCHES`**            | Should all the branches of the repository be scanned.                                                            |
| **`API_TOKEN_SCOPE`**              | Scopes to be requested while generating the OAuth token                                                          |

### Configuring Anypoint Design Center as an External Source

1. Navigate to **`Global Settings`** -> **`Settings`** -> **`Design Center Project Sync Settings`** and click on edit
2. NOTE: The connected app should have **`Design Center Viewer`** permission for the required organizations

### Design Center Project Sync Settings

| Settings Name                      | Description                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| ---------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **`ANYPOINT_CLIENT_ID`**           | Anypoint **`Connected App`** client id                                                                                                                                                                                                                                                                                                                                                                                                                |
| **`ANYPOINT_CLIENT_SECRET`**       | Anypoint **`Connected App`** client secret                                                                                                                                                                                                                                                                                                                                                                                                            |
| **`OWNER_ID`**                     | The owner ID is your user’s unique identifier (UUID). It can be obtained by the organization owner (or any user with Admin privilege) accessing to the Anypoint Platform’s Users page. For more details on how to obtain a given user ID, please refer to the [API Design Center documentation](https://anypoint.mulesoft.com/exchange/portals/anypoint-platform/f1e97bc6-315a-4490-82a7-23abe036327a.anypoint-platform/api-designer-experience-api/) |
| **`SCAN_ALL_APPLICATION`**         | Should all the repositories matching the Include / Exclude Pattern be scanned.                                                                                                                                                                                                                                                                                                                                                                        |
| **`SCAN_ALL_BRANCHES`**            | Should all the branches of the repository be scanned.                                                                                                                                                                                                                                                                                                                                                                                                 |
| **`PROJECT_NAME_INCLUDE_PATTERN`** | Repository name matching this pattern will only be synced. By default all the repositories will be scanned.                                                                                                                                                                                                                                                                                                                                           |
| **`PROJECT_NAME_EXCLUDE_PATTERN`** | Repository name matching this pattern will only be ignored. By default none of the repositories will be ignored.                                                                                                                                                                                                                                                                                                                                      |

### See Also

* [On The Fly Results](../anypoint-studio/source-code-analysis/anypoint-studio-analysis.md)
* [Source Code Analysis - Auto Fix Issues](../../../../iz-analyzer/autofix/autofix-anypoint-studio.md)
