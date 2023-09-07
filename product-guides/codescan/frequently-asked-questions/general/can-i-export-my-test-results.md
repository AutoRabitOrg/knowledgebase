# Can I export my test results?

Yes, you can. You can use our **.CSV export tools** to export to a **.CSV file**.

To export results for CodeScan Cloud or [CodeScan Self-Hosted](https://www.codescan.io/products/self-hosted/), you can use our npm tool. Click [here](https://www.npmjs.com/package/codescan-export) to find out more.

You can use our CSV plugin if you want a self-hosted GUI tool. See below for details.

### Installation <a href="#installation" id="installation"></a>

Note:

The .CSV plugin requires a SonarQube™ (**6.5+**) installation.

* First, download the **.CSV export plugin** from [here](https://github.com/VillageChief/sonarqube-csv-export-plugin/releases/tag/v0.4.0). It’s available as a ready-to-go **.JAR file** or an archive of source code (**.ZIP** and **.TAR.GZ**) .
* Copy the **.JAR file** into your SonarQube™ plugins folder at “(your SonarQube™ directory)/extensions/plugins/“.

Start your SonarQube™ server and run a scan on one or more projects. When the scan is finished, click on the **More** drop-down menu at the top of the screen. Click on **CSV Issue Export** and you’ll be given a list of filters and all projects currently in SonarQube™.\
![image.png](https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image\(368\).png)

Choose the filters you require and click the project name to download the **.CSV report** for that project with the selected filters. Open the file with a spreadsheet editor to view your project's issues.\


<figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image(369).png" alt=""><figcaption></figcaption></figure>

\
