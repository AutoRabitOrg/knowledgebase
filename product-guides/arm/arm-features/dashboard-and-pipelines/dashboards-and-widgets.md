# Dashboards & Widgets

### Dashboards: Overview <a href="#dashboards-overview" id="dashboards-overview"></a>

The Dashboard is an important feature of ARM that enables you to display multiple performance analytics, reporting, and other widgets on a single screen. ARM includes predefined widgets that can be customized and displayed on the classic Dashboards page. These widgets are shown in their own pane, and display graphs, tables, and/or text. Users can choose their own widgets to populate their Dashboard. Widgets are also expandable to view the raw data that comprises the visualization.\


<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1654513711085.png" alt=""><figcaption></figcaption></figure>

### Adding Filters to the Dashboard <a href="#adding-filters-to-the-dashboard" id="adding-filters-to-the-dashboard"></a>

Filters can be added to the Dashboard so users can narrow the Dashboard’s results to the data they are interested in viewing. To get started, click on the **Filter (**![](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1654513753542.png)**) icon** available at the top right of the screen. This will bring up the **Filters** window.\


<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1654513884932.png" alt=""><figcaption></figcaption></figure>

![](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1654514204780.png)

Next, in the **FILTER OPTIONS** window, select the field(s) by which to filter the data:

1.  **Date Range:** You can select a date range to show only the Dashboard results contained in that range.\


    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1654514282479.png" alt="" width="375"><figcaption></figcaption></figure>
2.  **Salesforce Org:** Filters the results by **Salesforce Org.**\


    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1654514337012.png" alt="" width="375"><figcaption></figcaption></figure>
3.  **Version Control Type,** **Repo, and Branch**: Filters the commits by Version Control Repository and the branch.\


    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1654515841566.png" alt="" width="563"><figcaption></figcaption></figure>

### Use Dashboards to: <a href="#use-dashboards-to" id="use-dashboards-to"></a>

1. Monitor the day-to-day activities being carried out in your Salesforce Org.
2. Access the information you use frequently.
3. View the top developers actively working on your project.
4. Quickly find and preview widgets, then add them to the Dashboard from the **Add Widget** pane.

### Widgets Available <a href="#widgets-available" id="widgets-available"></a>

The following widgets are now available:

#### A. CI Maturity <a href="#a-ci-maturity" id="a-ci-maturity"></a>

_**Build Monitor**_

The **Build Monitor** widget provides a highly visible view of the build status of the selected CI job. Here the builds are categorized as **Good**, **Bad**, or **Unstable**.\


<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1654520735870.png" alt="" width="375"><figcaption></figcaption></figure>

On expanding the widget, you can find the build status (measured as a percentage), along with the build-initiated date.

![](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1654520984285.png)

_**On-Commit Builds**_

Displays the report of your CI pipeline based on the commits happening on your remote repository.\


<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1654521213225.png" alt=""><figcaption></figcaption></figure>

Clicking on the link on your job will take you to the **CI Job Result** page, where you can track the status of your deployment validation, apex tests, code coverage, etc.\


<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1654521295690.png" alt=""><figcaption></figcaption></figure>

_**CI Builds Over Time**_

Displays the number of build cycles triggered over time for the selected Salesforce Org.\


<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1654521403536.png" alt=""><figcaption></figcaption></figure>

_**Rollback History**_

Lists the rollback summary carried out through the CI and the Deployment modules. When the widget is expanded, you can see more information, such as the rollback-initiated date, status, etc. Also, you can download the report in CSV format.\


<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1654521523857.png" alt=""><figcaption></figcaption></figure>

_**Last 7, 14, and 30 days Build Summary**_

Displays the build summary for your CI job triggered over the last 7, 14, and 30 days.\


<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1654521664093.png" alt="" width="375"><figcaption></figcaption></figure>

_**Code Coverage trend per CI Job**_

Displays CI jobs with permitted code coverage along with the code coverage percentage for the target org.\


<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1654521772934.png" alt=""><figcaption></figcaption></figure>

#### B. Developer Productivity <a href="#b-developer-productivity" id="b-developer-productivity"></a>

_**User Commit Feed**_

Displays the developer's list of those who may commit on your chosen local repository, along with other details like the date the commit was initiated, the iteration, and the commit comments.\


<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1654521924205.png" alt=""><figcaption></figcaption></figure>

_**Metadata Member Changes By Month**_

Displays the number of metadata members, modified files, and the commits that occurred each month.\


<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1654522027580.png" alt=""><figcaption></figcaption></figure>

_**Top Ten Branches By Category**_

Lists the top 10 branches used by developers for the commit process (merge, internal, or external commits).

![](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1654522114662.png)

_**Top Ten Dev By Category**_

List the top 10 developers who contributed the most for the date selected.

![](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1654522169513.png)

_**Commit Frequency per Day**_

Displays the number of commits that occurred each day.\


<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1654522227579.png" alt=""><figcaption></figcaption></figure>

#### C. State of Sandbox <a href="#c-state-of-sandbox" id="c-state-of-sandbox"></a>

_**Deployment Feed**_

Displays the summary report for each deployment of your selected Salesforce Org.

<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1654522356333.png" alt=""><figcaption></figcaption></figure>

### Adding Widgets to Dashboard <a href="#adding-widgets-to-dashboard" id="adding-widgets-to-dashboard"></a>

Widgets are the UI elements that make up Dashboards. You add widgets to your Dashboard to gain visibility of the status and trends occurring as you develop your software project.

1.  To add widgets to the Dashboard, click on the **+ ADD WIDGETS** call-to-action button.\


    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1654527271763.png" alt=""><figcaption></figcaption></figure>
2. Select the widget(s) you wish to view on the **Dashboard** page.
3.  When you're finished with your selection, click on the **Add To Dashboard** button to add the widgets to the **Dashboard** page.\


    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1654527481621.png" alt=""><figcaption></figcaption></figure>
4.  Use the![](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1654527507609.png) icon to expand the widgets and view the raw data that comprises the visualization.\


    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-1654520735870.png" alt="" width="375"><figcaption></figcaption></figure>
