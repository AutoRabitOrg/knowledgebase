# External Unique ID Validation

### Introduction

Now users no longer have to worry about the possibility of '**External Unique ID**’ being assigned to non-unique fields.

### Feature Overview

1. As part of this feature, a validation will be performed to verify whether the ‘**lookup key**’ is available in the destination Org.
2. A verification will be performed to confirm whether users have access to the ‘**External ID**’.
3. If the external unique ID is changed to a ‘**non-unique field**’ (example: Name), then a notification will appear when users click on the ‘**Create Dataset & Deploy**’ or ‘**Create Dataset Commit & Deploy**’ button.

### Step-by-Step Guide

1. Select the required values from the dropdown available on the ‘**Feature Deployment**’ section.
2.  If the ‘**external ID**’ is not available, then the following notification as highlighted will be displayed in the popup, when users click on ‘**Create Dataset & Deploy**’, as displayed in the following screenshot.

    <figure><img src="../../../../../../.gitbook/assets/ExternalID Unique Validation (1).png" alt=""><figcaption></figcaption></figure>
