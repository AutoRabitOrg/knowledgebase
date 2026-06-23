# Schedule Configuration

## Configure Schedule

{% hint style="info" %}
* Repeatedly creating a schedule for the same organization and environment will simply overwrite the pre-existing schedule.
* Required Connected App scopes for each Job Type reference can be found here
{% endhint %}

1. Navigate to **`Schedules`** -> **`Schedules`** and click on **`Configure Schedule`**
2. Select appropriate job type
   1. **`Anypoint Mule Runtime Analysis`** - Job Type to scan application deployed in Runtime Manager
   2. **`Anypoint API Instance Analysis`** - Job Type to scan application deployed in API Manager
   3. **`Anypoint Exchange APIs Analysis`** - Job Type to scan RAML/OAS assets published to exchange
   4. **`API Health Check`** - Job Type to monitor APi Endpoints&#x20;
3. Select the Organizations and Environments to perform the scan&#x20;
4. Select the schedule/frequency at which the analysis should be performed<br>
5. Click on **`Submit`** to configure the schedule

### See Also

* Aggregated Dashboard
* Application Dashboard
* Agent Job Types
* Mule Projects
* API Applications
