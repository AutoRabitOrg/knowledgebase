# Errors

AutoRABIT APIs follow standard HTTP response codes to signal the outcome of API requests. Understanding these codes helps in diagnosing issues and improving the stability of your integrations.

* **2xx** — Successful operations
* **4xx** — Client-side errors (e.g., invalid inputs, missing data)
* **5xx** — Server-side errors (typically rare)

## HTTP Status Code Summary <a href="#http-status-code-summary" id="http-status-code-summary"></a>

<table><thead><tr><th width="223">Error Code</th><th>Description</th></tr></thead><tbody><tr><td><strong>200 - OK</strong></td><td>The request succeeded as expected.</td></tr><tr><td><strong>400 - Bad Request</strong></td><td>The request was invalid—commonly due to missing or malformed parameters.</td></tr><tr><td><strong>401 - Unauthorized</strong></td><td>No valid API key was provided.</td></tr><tr><td><strong>402 - Request Failed</strong></td><td>The request was well-formed, but the operation failed.</td></tr><tr><td><strong>403 - Forbidden</strong></td><td>The API key lacks permissions to perform the action.</td></tr><tr><td><strong>404 - Not Found</strong></td><td>The requested resource could not be found.</td></tr><tr><td><strong>409 - Conflict</strong></td><td>The request conflicts with another operation (e.g., duplicate submission using the same token).</td></tr><tr><td><strong>429 - Too Many Requests</strong></td><td>The rate limit has been exceeded. Implement exponential backoff.</td></tr><tr><td><strong>500, 502, 503, 504 - Server Errors</strong></td><td>Internal AutoRABIT server issues. These errors are rare and usually temporary.</td></tr></tbody></table>
