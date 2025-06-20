# Viewing Project Activity

**Activity Tab**: Navigate to a Project, and in the project navigation bar, you should be able to see **Activity.**

The **Activity** tab in CodeScan, available under a project, allows you to visualize the evolution of code quality over time. It displays a history of analyses, including changes in metrics and events related to those analyses. The activity tab can show graphs of selected metrics against each other, providing insights into trends and project code quality changes.&#x20;

<figure><img src="../../../.gitbook/assets/image (1711).png" alt=""><figcaption><p>Activity Tab</p></figcaption></figure>

Graphs on the **Activity** page help you understand the evolution of up to three measures of your choice against each other. Graph mouseovers show the measure values and events associated with particular analyses. Users can see whether the code quality is improving or deteriorating and take proactive measures accordingly. Users can check various measures under the “Activity tab.”

You will have **four types of Graph** representation:

1: Issues: This graph representation shows the overall history of issues (Bugs, Vulnerabilities, Code Smells).

2: Coverage: This graph representation shows the history of Code Coverage. It will show the Lines to cover, Covered lines, and the % of Coverage.

3: Duplication: This graph representation shows the history of duplicated lines. It will show the lines of code in the project, duplicated lines, and the % of duplicated lines.

4: Custom type: This will allow you to design and view the graphical representation based on your selected metric. In Custom type, you can have a maximum of two graphs, and only three metrics of the same type can be displayed on one graph.

<figure><img src="../../../.gitbook/assets/image (1709).png" alt=""><figcaption><p>Custom Graphs</p></figcaption></figure>

**There are two types of filters: The Event filter and the Date Range filter**

**Event filter:** You can filter the scan list by event type

1: Version: The project's version changed

2: Quality Gate: The status of the quality gate changed.

3: Quality Profile: The quality profiles used to analyze the project changed - either the profile was edited, or a different profile was used to analyze the project

4: CodeScan Upgrade: This will show the analysis data based on CodeScan upgrades.

5: Other: An event was manually created on a snapshot; these events typically represent events that are manually created or related to project configuration changes, rather than automated processes.&#x20;

<figure><img src="../../../.gitbook/assets/image (1708).png" alt=""><figcaption><p>Event Filters</p></figcaption></figure>

**Date Range filter:**

This Date Range filter is helpful when you want to see the graph for a specific period. After selecting the date range, the events that fall within it will be displayed on the left, and the graph will change accordingly.

<figure><img src="../../../.gitbook/assets/image (1707).png" alt=""><figcaption><p>Date Range Filter</p></figcaption></figure>
