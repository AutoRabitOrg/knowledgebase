# Release Notes 24.0

## Release Notes 24.0.2

**26 June 2024**

The latest Flow Center release includes various new features and enhancements to improve the user experience.&#x20;

### **New Features**

#### DORA Metric Correlation in Widgets&#x20;

Each widget in FlowCenter Insights is now linked to a maximum of two DORA metrics. The valid DORA metrics are Deployment Frequency, Lead Time for Changes, Change Failure Rate, Mean Time to Recovery, and Reliability. Users can view the relationship between widgets and DORA metrics in the detailed view of each widget. Additionally, a "Learn more about DORA" link has been added for further information on DORA metrics.&#x20;

#### User Management Console Access for Tenant Managers&#x20;

Tenant managers now have access to a "User Management" link in the UI. Clicking this link directs users to the management console. Non-tenant management users will not see this link. From here, users can be created and/or edited.&#x20;

#### Rolled-Back Deployments Widget&#x20;

A new widget named "Rolled Back Deployments" has been added. This widget exclusively shows the number of deployments that were rolled back. &#x20;

#### Export Top 25 Failing Apex Tests&#x20;

Users can now export data for the "Top 25 failing Apex tests" directly to an Excel file. This export includes all deployments with test failures within the past 30 days, regardless of the dashboard timeframe.&#x20;

#### Export for Top 25 Failing Metadata and Metadata Types&#x20;

The "Top 25 Failing Metadata" and "Top 25 Failing Metadata Types" widgets now have an export feature. When users click the detailed view of these widgets, the Export button is available. This export includes all deployments with metadata failures within the past 30 days, regardless of the dashboard timeframe.&#x20;

### Enhancements

#### "Last 60 Days" Time Frame Option&#x20;

The "Last 60 Days" option is now available in the Time Frame field when creating or editing dashboards. This option is selected by default when creating new dashboards. &#x20;

#### Dashboard Last Refreshed Date Display&#x20;

The dashboard now displays the last refreshed date and time, indicating when the integration with ARM last ran. The date is shown in UTC and updates based on the viewer's current time, with formats such as "Today at 3:30 PM UTC," "Yesterday at 3:30 PM UTC," and "2 days ago at 3:30 PM UTC." This helps users understand the currency of the data and addresses common questions about data visibility and dashboard updates.&#x20;

#### Improved "Understand This Report" Section&#x20;

The "Understand This Report" section has been enhanced for a better user experience. The background colors and icons now match the updated design. This section is opened by default and remains open unless manually closed by the user. User preferences for this section's visibility are remembered across login sessions through a browser cookie, ensuring that once reopened, it stays open until closed again.&#x20;

#### Enhanced Deployment Frequency Widget&#x20;

The Deployment Summary widget has been renamed to "Deployment Frequency" to better align with the Deployment Frequency DORA metric. Additionally, deployment statuses have been consolidated into two categories: "Failed" (includes partially successful, validation failed, aborted, and other) and "Succeeded" (everything else). These statuses are visually distinguished by red and green colors, respectively.&#x20;

#### Widget Subtitles&#x20;

Each widget now features a subtitle positioned under the DORA metrics pills. This allows for shorter widget names while providing additional context about the widget.&#x20;

#### Improved Widget Tooltips&#x20;

The tooltips for widgets displaying combined data from multiple organizations now show a detailed breakdown of the data by organization. On hover, users can see the name of the area, the breakdown of data from each organization, and the total. This enhancement ensures consistent ordering of organizations across all widgets in a single dashboard and maintains text readability regardless of the background color.&#x20;



## Release Notes 24.0.1 (Pilot)

Flow Center is your Salesforce DevOps command and control center, presenting an oversight dashboard CIOs and CISOs can use to gain a high-level overview of projects as well as detailed drill-down components for team members and project managers. This tool enables you to view your projects, insights, dashboards, and pipelines in one comprehensive solution, streamlining operations and offering an integrated platform to simplify decision-making. From giving team members a holistic overview of projects to presenting CIOs and CISOs with data insights, the dashboards allow teams to visualize both in-depth, component-level details as well as the overall progress of each release in your pipeline.

### Notes on the Flow Center Pilot

This Pilot release of Flow Center is intentionally thin on functionality. Our goal is to introduce and get early feedback on the concepts and organization before making a fuller set of capabilities available.
