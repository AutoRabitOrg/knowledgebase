# Register AutoRABIT Agent

{% hint style="info" %}
**Important Note:** This article is for the **Super Administrator** in particular. The actions discussed in this article are not available to general users or org admins.
{% endhint %}

ARM supports a single agent for parallel streaming the Build, Deploy, and Test interface. ARM was primarily dependent on two server agents, i.e., RBA (Rabit Build Agent) and RTA (Rabit Test Agent) for parallel streaming. With the increase in user subscriptions with us, our customers are triggering multiple parallel builds and deployments that are getting delayed. This was having a severe impact on the user experience point with us. Therefore, the user can associate Agent with their Salesforce org or pool multiple agents for a Salesforce org in our current release.

### Register an Agent <a href="#register-an-agent" id="register-an-agent"></a>

1. Log in to ARM using the super admin credentials.
2. Go to **`Admin`** > **`Pool Mgmt.`**

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1623821547615.png" alt=""><figcaption></figcaption></figure>

3. Click on **`Register Agent`**.

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1623821613239.png" alt=""><figcaption></figcaption></figure>

4. In the **`New Agent Registration`** screen, you must fill in the details below to register an agent in ARM.\


<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1667376363542.png" alt="" width="375"><figcaption></figcaption></figure>

* **`Pool Name:`** Select the pool name from the dropdown field or assign a name for your agent using the **`+`** icon.
* **`Agent Name:`** Enter a name for your agent here.
* **`Agent Description:`** Add any relevant description for your agent. This is optional.
* **`Operating System (OS):`** Select the operating system from the dropdown, i.e., Windows, Linux, or Mac, for which the agent will be assigned.
* **`Credentials:`** Select the user's credential here. If you are new to ARM and your credentials are unavailable, you can create a new one using the **`+`** icon.
* **`Host Name:`** Enter the hostname. This will identify a computer on a network or a domain on the Internet.  \
  _**For example, www.google.com**_ (hostname for Google's webserver)Important Note:Hostnames can also be expressed via an IP address, a unique sequence of numbers representing an individual host. A website can be accessed by entering an IP address or hostname. For example, you can access Google by entering the text [**www.google.com**](https://www.google.com/) or the IP address **216.58.208.46** into the Internet browser's address bar.
* **`Port:`** Specify the port number for the above hostname. A semicolon separates the port from its corresponding address/hostname (;).\
  _**Example:** For **216.58.208.46;1364** as an **agent URL**, **216.58.208.46** is the hostname, and **1364** is the port._
* **`Agent URL:`** Enter the agent URL in this field. This is a combination of both hostname and port. Before you proceed, ensure the agent entered is successfully authenticated. To verify, click on **`Test Connection`** (![](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1623822543109.png)). You may need to check your agent URL if the application throws an error.



<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1623822742015.png" alt=""><figcaption></figcaption></figure>



* **`Parallel Processes Limit:`** Specify the limit to which the agent will run the processes in parallel. Setting the process limit to three means you can trigger and run three builds in parallel. The remaining builds triggered will remain in the queue.
* **`External commits Parallel Processes Limit:`** Similar to parallel processes limit, specify the limit here to which the agent will the external commits (commits triggered outside AutoRABIT) parallelly.
* **`Thread Pool Count(between 8 and 256):`** Enter the number of threads you want to run to complete a build or an external commit task. This field will only accept numbers from **8-256**.\
  Important Notes:&#x20;
  * If you do not enter the thread pool count, the default value is set to **30**.
  * If you enter a value less than **8**, it will automatically change to **8**.&#x20;
  * Similarly, if you enter a value greater than **256**, it will automatically change to **256**.&#x20;
* **`Shared Orgs:`** Select from the list of orgs that will get associated with the current agent.

1. Once you fill in all the details, click **`Save`** to complete the agent registration process.
2. The newly created agent will be available on the **`Pool Management`** homepage. Whenever the builds get triggered for your shared orgs, the list of the jobs running gets displayed beside your agent name. If you click on the agent, it will furnish you with a detailed agent summary report.

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1623822798307.png" alt=""><figcaption></figcaption></figure>

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1667376561278.png" alt=""><figcaption></figcaption></figure>

#### Agent Summary <a href="#agent-summary" id="agent-summary"></a>

The **`Agent Summary`** tab will have the information you have filled in while registering your agent. It's a detailed report for your agent. If required, you can update the agent details, such as Agent URL, Port, Thread Pool Count, etc., using the **`Edit Agent`** button and authenticate the agent connection using the **`Test Connection`** button.

Important Note**Thread Pool Count** is displayed in the **Agent Summary** report only if the value is manually entered on the **New Agent Registration** or the **Edit Agent Registration** screen. If the user does not enter the thread pool count, the default value will be set to **30** and not displayed on the **Agent Summary** tab.

#### Process Summary  <a href="#process-summary" id="process-summary"></a>

This tab will list down the details of the job that are currently in the processing state.

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1623777118005.png" alt=""><figcaption></figcaption></figure>

### Queued Jobs <a href="#queued-jobs" id="queued-jobs"></a>

All jobs in the waiting state are displayed in this tab.

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1623777089786.png" alt=""><figcaption></figcaption></figure>
