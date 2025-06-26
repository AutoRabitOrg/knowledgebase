# Errors

AutoRABIT APIs follow standard HTTP response codes to signal the outcome of API requests. Understanding these codes helps in diagnosing issues and improving the stability of your integrations.

- **2xx** — Successful operations
- **4xx** — Client-side errors (e.g., invalid inputs, missing data)
- **5xx** — Server-side errors (typically rare)

## HTTP Status Code Summary <a href="#http-status-code-summary" id="http-status-code-summary"></a>

| Error Code                        | Description                                                                                      |
| -------------------------------- | ------------------------------------------------------------------------------------------------ |
| **200 - OK**                     | The request succeeded as expected.                                                               |
| **400 - Bad Request**            | The request was invalid—commonly due to missing or malformed parameters.                         |
| **401 - Unauthorized**           | No valid API key was provided.                                                                  |
| **402 - Request Failed**         | The request was well-formed, but the operation failed.                                           |
| **403 - Forbidden**              | The API key lacks permissions to perform the action.                                             |
| **404 - Not Found**              | The requested resource could not be found.                                                       |
| **409 - Conflict**               | The request conflicts with another operation (e.g., duplicate submission using the same token).  |
| **429 - Too Many Requests**      | The rate limit has been exceeded. Implement exponential backoff.                                 |
| **500, 502, 503, 504 - Server Errors** | Internal AutoRABIT server issues. These errors are rare and usually temporary.               |
