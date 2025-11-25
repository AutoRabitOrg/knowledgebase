# Run Destructive Changes

This template will allow you to mass-delete certain metadata in [AutoRABIT](https://www.autorabit.com/). Destructive Change is an .xml file that contains information about metadata you want to delete. List the elements you are trying to get rid of, save the file, run a standard script, and your job is done.

To create this template, follow the steps below:

1. In the **Create Migration Template** screen, select the checkbox: **Run Destructive Changes.**
2. Next, upload the destructive manifest XML file. Click **Choose File** and upload the required XML file from your local system.
3. Click **Save**.&#x20;
4. Once the template is successfully created, you'll be redirected to the **Environment Provisioning History** screen.
5. Click on the **Run** button to run the current template on your destination org.
6. Select your **destination org** from the dropdown and enter the **email address(es)** to receive an email notification whenever the template is run.
7. To use the current template as the post-deployment during [CI/CD](https://www.autorabit.com/blog/avoid-these-common-salesforce-ci-cd-mistakes/), select the **Run Destructive Changes** checkbox under the **Post-Deployment Steps** section. This is optional.
8. Click **Run**. For a detailed summary report of the operation carried out, please check the **View History** page.
