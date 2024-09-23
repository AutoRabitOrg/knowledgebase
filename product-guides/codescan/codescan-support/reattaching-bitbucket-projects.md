# Reattaching Bitbucket Projects

We have made some changes to make our Bitbucket project webhooks more secure.  To take advantage of this change, Bitbucket projects that were created in CodeScan will need to be reattached. &#x20;

This will not erase the history of your project, it will only re-connect the CodeScan project with the Bitbucket repository.

{% hint style="info" %}
This only affects projects created in CodeScan with our internal integration.

This **DOES NOT** include:

* Projects created from Bitbucket pipelines&#x20;
* Projects being cloned from Bitbucket and scanned from a separate CI platform&#x20;
{% endhint %}

Follow these steps to reattach your project analysis:

1. Open your Bitbucket project
2. Navigate to **Project Settings > Project Analysis**
3. Click **Delete Analysis**

<figure><img src="https://knowledgebase.autorabit.com/~gitbook/image?url=https%3A%2F%2F1912836914-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F9vAxMuDrkUkB4OXlH9CL%252Fuploads%252FVHZkjz1ZwMnN2M1yKWH1%252Fimage.png%3Falt%3Dmedia%26token%3D9bd14e0f-f243-497f-8278-addd4a5332fe&#x26;width=768&#x26;dpr=4&#x26;quality=100&#x26;sign=62cafe6d&#x26;sv=1" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
**Important! DO NOT** select the checkbox to '**Delete the Project also?'** if you want to keep the current project and its history:

![](https://knowledgebase.autorabit.com/\~gitbook/image?url=https%3A%2F%2F1912836914-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F9vAxMuDrkUkB4OXlH9CL%252Fuploads%252FT9x5wKokEeJl9EVROsWp%252Fimage.png%3Falt%3Dmedia%26token%3Dc8c35fc2-a285-4928-be5e-b53d9bb2516f\&width=768\&dpr=4\&quality=100\&sign=ef0fa505\&sv=1)
{% endhint %}

4. Click **"Attach Analysis Project"** and choose Bitbucket

<figure><img src="https://knowledgebase.autorabit.com/~gitbook/image?url=https%3A%2F%2F1912836914-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F9vAxMuDrkUkB4OXlH9CL%252Fuploads%252FkMD8jvNvSntFehn4CTKF%252Fimage.png%3Falt%3Dmedia%26token%3D3f6418d3-dcd8-4d6d-8db0-096689ec6dad&#x26;width=768&#x26;dpr=4&#x26;quality=100&#x26;sign=2c68ea99&#x26;sv=1" alt=""><figcaption></figcaption></figure>

5. &#x20;Authenticate with Bitbucket and choose your repository

![](https://knowledgebase.autorabit.com/\~gitbook/image?url=https%3A%2F%2F1912836914-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F9vAxMuDrkUkB4OXlH9CL%252Fuploads%252FecrzFoDeeZxtKyFmhdGs%252Fimage.png%3Falt%3Dmedia%26token%3Dadf6ffb3-ce85-4685-bd26-44cc4a88e69a\&width=768\&dpr=4\&quality=100\&sign=e4427d36\&sv=1)

1. Click **"Run Manual Analysis"**; it should succeed.
