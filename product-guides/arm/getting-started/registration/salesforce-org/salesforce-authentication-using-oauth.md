# Salesforce Authentication using OAuth

The Salesforce platform implements the OAuth 2.0 Authorization Framework, so users can authorize applications to access Force.com resources. When configuring ARM and Salesforce source, you must know the **Client\_ID** and **Client\_Secret** token values for the Salesforce organization you want to index.&#x20;

{% hint style="warning" %}
I**mportant Note**: The following article is only applicable to **self-hosted** and **dedicated** instances. It is **NOT** applicable to Cloud users.

For shared cloud customers, ARM has a preconfigured connected app via Salesforce; therefore, client\_id and client\_secret fields are not exposed in the user interface. For more information, please refer to the link: [Adding a Salesforce Org connection via OAuth](https://knowledgebase.autorabit.com/arm/docs/salesforce-org).
{% endhint %}

## To get the Salesforce Client\_ID and Client\_Secret values

1. Log in to Salesforce as an administrator.
2. In the drop-down list of the account (in the upper-right corner), select **Setup**.
3. In the navigation menu on the left, under App Setup, expand Create, then click **Apps**.
4. On the Connected Apps page, click the **New** button.
5. On the New Connected App page, fill in the following required fields under **Basic Information**:&#x20;
   1. Enter meaningful names in the **Connected App Name** and **API Name** boxes.&#x20;
   2. Enter your email in the **Contact Email** box to receive messages from this application.
6. Go to API (Enable OAuth Settings) and select '**Enable OAuth Settings**.'&#x20;
   1.  In the Callback URL field, enter _https://\<ARM access URL>/oauth/\_callback_&#x20;

       Example: https://preview.autorabit.com/oauth/\_callback\
       Depending on which OAuth flow you use, this is typically the URL that a user's browser is redirected to after successful authentication.
   2. In the **Available OAuth Scopes** list, select the following items:&#x20;
      1. Access and manage your data (API)&#x20;
      2. Full access (full)&#x20;
      3. Perform requests on your behalf at any time (refresh\_token, offline\_access)&#x20;
      4. Click **Add** for each to appear in the Selected OAuth Scopes list.
7. Click the **Save** button to save the new Connected App.
8. In the Connected Apps list, find the App you just created and click **Manage**.&#x20;
   1. On the page that opens, click the **Edit** button.&#x20;
   2. Under OAuth policies, select '**All users may self-authorize in the Permitted Users list**,' then click the **Save** button.
9. Return to the Connected Apps list and click the **app** you created.
10. In the page that appears for your new connected app, in the API (Enable OAuth Settings) section:
    1. Copy the **Consumer Key** value and paste it into a secure reference document of your choice. The Consumer Key is the _client\_id_.&#x20;
    2. Next to Consumer secret, click **Click to reveal**, copy the value that appears, and paste it into your secure reference document. The Consumer secret is the _client\_secret_.
11. Open the _oauth.properties_ file in the _.rabit/org/oauth.properties_ directory and update the _client\_id_ and _client\_secret_ token during on-premises installation.

    <pre class="language-actionscript"><code class="lang-actionscript"><strong>clientId=&#x3C;Consumer Key>
    </strong><strong>clientSecret=&#x3C;Consumer Secret>
    </strong>redirecturl=&#x3C;AutoRABIT application access URL>/oauth/_callback
    hosturl==&#x3C;AutoRABIT application access URL>
    </code></pre>
