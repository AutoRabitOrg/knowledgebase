# Selective Deployments Using Pre-Prepared Artifacts

Deploy selective changes to production in AutoRABIT using pre-prepared artifacts, a feature designed to streamline deployment by eliminating additional Git operations. This allows developers to deploy only the necessary components, reducing deployment time and the risk of errors associated with manual Git processes.  &#x20;

**The current deployment strategy for Release Labels in AutoRABIT includes distinct processes for full and selective deployments:**&#x20;

* **Full Deployments:** Deploy all changes based on a pre-prepared artifact. This approach minimizes time by avoiding repetitive package preparation steps.&#x20;
* **Selective Deployments:** Require re-preparing the package using additional Git operations, rather than using an existing artifact. This process increases deployment time and introduces the potential for errors during manual Git interaction.&#x20;

### **Solution Overview**&#x20;

To optimize the selective deployment process, AutoRABIT now utilizes the pre-prepared artifact for component selection, removing the need for additional Git operations. Instead of re-creating the package, developers perform component selection operations directly on the existing artifact, simplifying the workflow and improving deployment speed.&#x20;

AutoRABIT enables selective deployments by leveraging pre-prepared artifacts instead of re-running Git operations. This method allows developers to deploy only the selected components, enhancing both deployment speed and reliability.&#x20;

#### **Key Features:**&#x20;

* Artifact-Based Component Selection: Developers can now deploy specific components from the pre-prepared artifact, eliminating the need for repeated Git processes.&#x20;
* Elimination of Additional Git Operations: By relying on the existing artifact, AutoRABIT avoids unnecessary Git interactions, making the selective deployment process faster and less complex. &#x20;

### **Steps for Selective Deployments Using Pre-Prepared Artifacts**&#x20;

1. **Prepare the Deployment Artifact:** Create the deployment artifact as usual in AutoRABIT. This artifact contains all components necessary for deployment.&#x20;
2. **Select Desired Components:** During deployment, specify only the components required for the selective deployment. AutoRABIT will use the prepared artifact and only deploy the selected components.&#x20;
3. **Deploy to Production:** Proceed with the deployment. AutoRABIT will deploy the chosen components without additional Git operations, minimizing both deployment time and error risk.&#x20;

### **Outcomes**&#x20;

* **Increased Efficiency:** Selective deployments using pre-prepared artifacts reduce deployment times by eliminating redundant Git steps.&#x20;
* **Reduced Error Risk:** This method minimizes manual Git interactions, reducing the potential for deployment errors.&#x20;
* Enh**anced Release Management:** The streamlined process improves the overall efficiency of release management for selective changes. &#x20;

#### **Conclusion**&#x20;

By enabling selective deployments through pre-prepared artifacts, AutoRABIT provides a more efficient and reliable deployment process. Developers can now deploy specific changes without additional Git operations, resulting in faster, less error-prone production deployments. For further information or assistance with selective deployments, please reach out to AutoRABIT Support.&#x20;
