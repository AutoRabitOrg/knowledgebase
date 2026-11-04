# Retention Policy

## What is a data retention policy? <a href="#what-is-a-data-retention-policy" id="what-is-a-data-retention-policy"></a>

Data retention policies dictate what data should be stored or archived, where that should happen, and for how long. Historical data that becomes irrelevant after a certain period will be cleared from the ARM database weekly. This way, the ARM application performs faster, primary storage remains uncluttered, and at the same time, the organization remains compliant.

## How can I change the data retention policy? <a href="#how-to-change-data-retention-policy" id="how-to-change-data-retention-policy"></a>

Administrators can determine the age of still-relevant data for the company and then change the retention policy under the **Admin > My Account > Retention Policy** page.

## Can the data retention policy be disabled? <a href="#can-the-data-retention-policy-be-disabled" id="can-the-data-retention-policy-be-disabled"></a>

No, Administrators cannot disable the data retention policy. Data retention policies greatly enhance data scan performance by removing outdated and duplicated data.

## How can I access the data that has been cleared? <a href="#how-can-i-access-the-data-that-has-been-cleared" id="how-can-i-access-the-data-that-has-been-cleared"></a>

To access any historical data that has already been cleaned up, contact us at **support@autorabit.com**, and we will provide the data in a CSV file format.

For **on-premises customers**, the historic data is moved to the alt path in the **.rabit** folder (_**.rabit/dataretention/{org-name}**_).

## Can the cleared data be restored to the application? <a href="#can-the-cleared-data-be-restored-to-the-application" id="can-the-cleared-data-be-restored-to-the-application"></a>

No. Deleted data **cannot be restored** to ARM under any circumstances.

## Data from which pages are affected by this policy? <a href="#data-from-which-pages-is-affected-by-this-policy" id="data-from-which-pages-is-affected-by-this-policy"></a>

The following pages have historic data that is affected by the retention policy:

* Deployment history
* CI Job history
* Org Sync history
* EZ-Commits
  * EZ-Commits history
  * Prevalidation commits history
  * Reverted commits history
  * Merges history
  * Prevalidation merge history
* Merge Requests history
* External Pull Requests page
* Branching baseline page
* Change Labels page
  * Commit Labels
  * Release Labels
  * ALM Labels

## I did not select the period for data retention. Will I lose everything? <a href="#i-did-not-select-the-period-for-data-retention-will-i-lose-everything" id="i-did-not-select-the-period-for-data-retention-will-i-lose-everything"></a>

You will not lose data if you do not manually set the retention period. The retention period is set to 12 months by default. When ARM version 22.3 is released, data older than 12 months is cleaned up. If you did not alter the settings, you will still have access to up to 12 months of old data.

## What if I decrease the retention period from 12 months to 3 or 6 months? <a href="#what-if-i-change-the-retention-period-from-12-months-to-3-or-6-months" id="what-if-i-change-the-retention-period-from-12-months-to-3-or-6-months"></a>

If you decrease the retention period from 12 months to 3 or 6 months, then at the time of the next cleanup, data older than 3 or 6 months (whichever you have selected) will be cleaned up from the application, and the rest will be retained.

## What if I increase the retention period from 3 to 6 months or 6 to 12 months? <a href="#what-if-i-change-the-retention-period-from-3-months-to-6-or-12-months-or-from-6-months-to-12-months" id="what-if-i-change-the-retention-period-from-3-months-to-6-or-12-months-or-from-6-months-to-12-months"></a>

If you increase the retention period from 3 months to 6 or 12 months, then data from the last 3 months will remain as it is, but data older than that will not be restored. Instead, for the next 3 or 9 months, no data will be deleted when the cleanup happens.\
\
**For example:** If your retention period is set as three months, and you change it to 6 months on 1 April, then data from 1 January to 31 March is already retained. From 1 April to 30 June, the cleanup will still happen weekly as scheduled, but no data will be deleted because nothing is older than six months. After the 30 June, some data will be more than six months old. This six-month-old data will be deleted at the next cleanup.

Similarly, if you change it from 6 months to 12 months, the above logic applies, i.e., no data will be deleted during cleanup for the next six months until the oldest data is 12 months or more.
