# Configure a Webhook in Microsoft Azure

In the world of Azure, a Webhook is a trigger. There are several systems in Azure that can be triggered, including:

* Runbooks in Azure Automation
* Web jobs in Web Apps or Service Fabric that allow a website to have a background task
* Functions, another Service Fabric feature but is a server-less method of running a task or small workflow

One of the scenarios that you will be most familiar with is runbooks in [Azure Automation](../../../integration-and-plugins/azure-devops.md). Automation allows us to create a runbook, which will perform some task, such as powering up one or more virtual machines. That runbook can be triggered or started in many ways, one of the methods is triggering via a webhook.

We can create a webhook in the Azure Portal or a runbook. This webhook generates a URI, a uniform resource identifier that looks like a URL. We can use this URI in any external system to start the runbook via HTTP POST action.

For example:\
_A developer writes an application that is running in Azure or anywhere with Internet access and when something happens, the URI is posted. Azure Automation will respond by executing the associated runbook._

### &#x20;<a href="#a-create-a-webhook-connection" id="a-create-a-webhook-connection"></a>

\
