# Authentication

AutoRABIT API uses API keys to authenticate requests. Authentication to the API is performed via HTTP Basic Auth. Provide your API key as the basic auth username value. You do not need to provide a password.

Your API keys carry many privileges, so be sure to keep them secure! Do not share your secret API keys in publicly accessible areas such as [GitHub](arm-features/automation-and-ci/enabling-github-checks.md), client-side code, and so forth.

{% hint style="info" %}
Generate an API Key from the AutoRABIT platform and provide it in the header such as **header -- "token: api-key"** for cURL for all the requests requiring this authentication.
{% endhint %}
