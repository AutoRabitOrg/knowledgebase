# Authentication

AutoRABIT APIs use API keys for secure authentication. All authentication is handled through **HTTP Basic Auth**, where the API key is provided as the username. No password is required.

Your API key grants significant access—treat it like a password. **Do not expose your API key** in public code repositories, client-side applications, or other insecure locations, such as GitHub.

> **ℹ️ API Token Header Usage**
>
> <mark style="color:$primary;">Generate your API key from the AutoRABIT platform. For cURL or other HTTP clients, include it in the header as:</mark>
>
> ```
> header -- "token: api-key"
> ```
>
> <mark style="color:$primary;">This header is required for all authenticated API requests.</mark>

