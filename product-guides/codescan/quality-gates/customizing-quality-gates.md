# Customizing Quality Gates

Quality Gates return a **Pass** or **Fail** (sometimes referred to as **Go/No-Go** rules) rating for analysis, depending on the selected criteria.

To create a new Quality Gate, follow the steps below:

1.  Navigate to your organization's page and select the **Quality Gates** tab.<br>

    <figure><img src="../../../.gitbook/assets/image (1712).png" alt=""><figcaption><p>Quality Gates tab</p></figcaption></figure>
2. **Copy** an existing Quality Gate to use as a template or select **Create** to design it from scratch.&#x20;
3.  Give it a unique name and select **Save**.<br>

    <figure><img src="../../../.gitbook/assets/image (1713).png" alt="" width="375"><figcaption><p>Create Quality Gate</p></figcaption></figure>
4. To add desired conditions with their Warning and Error thresholds, click on **Add Condition**.&#x20;

<figure><img src="../../../.gitbook/assets/QG Add Condition 9.9 (4).png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
Note: To customize a Quality Gate that is already in use, click on **Unlock editing** first, as shown below.
{% endhint %}

<figure><img src="../../../.gitbook/assets/QG Unlock edit 10.0.png" alt=""><figcaption></figcaption></figure>

5.  Conditions on **New Code** and **Old Code** must be added separately.<br>

    <figure><img src="../../../.gitbook/assets/QG Condition 10.1.png" alt="" width="375"><figcaption></figcaption></figure>
6. To assign Quality Gates to specific projects, use the **Project Settings > Quality Gates** menu for your project and select the one you would like to use.

<figure><img src="../../../.gitbook/assets/QGate 9.8.png" alt="" width="563"><figcaption></figcaption></figure>

7. A default **Quality Gate** can be set at the org level. Select **Set as Default.**

<figure><img src="../../../.gitbook/assets/QG Default 10.2.png" alt=""><figcaption></figcaption></figure>

Then it will be assigned automatically to every new project, except those for which you specify a different gate. (See step 6.)

{% hint style="info" %}
**NOTE:** BUILT-IN Quality Gates are standard and can’t be edited. But you can always **Copy** and customize as needed. (See step 2.)
{% endhint %}

{% hint style="info" %}
**NOTE**: Changing the severity to '**Info**' will not block the Quality Gates.
{% endhint %}
