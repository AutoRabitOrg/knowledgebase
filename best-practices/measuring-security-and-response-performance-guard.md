# Measuring Security & Response Performance (Guard)

<mark style="color:red;">Red metrics</mark> indicate the more important metrics to measure whether speed and efficiency are the goals.

To establish "Metrics that Matter" for assessing a customer's performance using AutoRabit Guard in securing their Salesforce environment, we can draw inspiration from Google's DORA Metrics. For Guard, the goal shifts from software delivery to security performance, emphasizing the detection, prevention, and resolution of Salesforce-specific vulnerabilities and risks. I propose a set of key metrics tailored to Guard's purpose, mirroring DORA's focus on actionable, measurable outcomes that reflect both efficiency and effectiveness in securing Salesforce environments.

### **Key Metrics that Matter for Guard**<sup>**™**</sup> <a href="#key-metrics-that-matter-for-guard-tm" id="key-metrics-that-matter-for-guard-tm"></a>

1. <mark style="color:red;">**Vulnerability Detection Frequency**</mark>

* **Definition**: Measures how often Guard identifies new vulnerabilities or misconfigurations in the Salesforce environment over a given time period (e.g., daily, weekly, monthly).
* **Purpose**: This metric reflects the tool's ability to proactively and regularly scan for issues, ensuring continuous visibility into the security posture. High frequency indicates robust monitoring of Salesforce-specific elements like Apex code, metadata, permissions, and sharing rules. [Audits](measuring-security-and-response-performance-guard.md)
* **Target**: Elite performers should aim for daily or on-demand detection aligned with Salesforce changes, while lower performers might detect issues monthly or reactively after incidents.
* **Improvement using Guard**: Increase scanning frequency by leveraging Guard’s real-time monitoring capabilities to catch configuration drift or permission changes as they occur.

2. <mark style="color:red;">**Mean Time to Detect (MTTD) Security Issues**</mark>

* **Definition**: The average time it takes Guard to identify a Salesforce-specific security issue (e.g., excessive permissions, sharing rule modifications, or metadata vulnerabilities) from the moment it is introduced.
* **Purpose**: This metric gauges the speed at which Guard provides actionable insights, critical for minimizing the window of exposure to potential exploits like privilege escalation or data exfiltration.
* **Target**: Elite performance achieves detection in under an hour, while slower performers take days or weeks, especially if relying on manual audits or generic tools.
* **Improvement using Guard**: Reduce MTTD by optimizing Guard’s Salesforce-aware scanning to focus on high-risk areas (e.g., profile permission changes) and integrating it into development workflows for early detection.

3. <mark style="color:red;">**Security Issue Resolution Time (SIRT)**</mark>

* **Definition**: The average time it takes to remediate a detected security issue (e.g., fixing a misconfiguration, revoking excessive permissions, or adjusting sharing rules) after Guard identifies it.
* **Purpose**: This metric assesses how quickly teams can respond to and resolve vulnerabilities, minimizing risk exposure and ensuring compliance.
* **Target**: Elite performers resolve issues in less than a day from provocation, while lower performers could take weeks, especially without automated remediation guidance.
* **Improvement using Guard**: Shorten SIRT by using Guard’s detailed reporting to prioritize critical issues and automate remediation steps where possible, addressing the technical gaps generic tools miss.

4. <mark style="color:red;">**Change Failure Rate (Security-Related)**</mark>

* **Definition**: The percentage of Salesforce configuration or development changes (e.g., new Apex code, metadata updates, or permission adjustments) that introduce a security vulnerability or compliance failure, as detected by Guard.
* **Purpose**: This metric evaluates the quality of changes in the Salesforce environment, highlighting how often they create exploitable attack vectors like privilege escalation or data exposure.
* **Target**: Elite performers maintain a failure rate of 0-15%, while lower performers could see rates exceeding 30%, reflecting inadequate monitoring of Salesforce-specific risks.
* **Improvement using Guard**: Lower the rate by using Guard to enforce pre-deployment checks, monitor low-code development, and validate metadata-driven customizations against security best practices.

**Why These Metrics Matter**

* **Throughput**: How quickly and frequently Guard detects vulnerabilities (Vulnerability Detection Frequency and MTTD), ensuring proactive security management in a dynamic, metadata-driven platform.
* **Stability**: How effectively Guard helps maintain a secure environment (SIRT and Change Failure Rate), reducing risks like configuration drift, excessive permissions, and regulatory exposure.

**Applying the Metrics**

* **Benchmarking**: Customers and AutoRabit CSMs can use these metrics to classify their security performance (e.g., Elite, High, Medium, Low) and compare against industry standards or internal goals.
* **Continuous Improvement**: Tracking these metrics over time helps teams identify bottlenecks (e.g., slow resolution times) and measure how well the customer can leverage Guard’s capabilities to close gaps.
* **Business Impact**: Improved metrics demonstrate reduced risk, enhanced compliance, and protection against Salesforce-specific threats, justifying investment in Guard.

By adopting these "Metrics that Matter," customers can quantify Guard’s impact on their Salesforce security, ensuring they address the unique challenges of admin-driven customization, constant release cycles, and platform-specific vulnerabilities—areas where Guard excels, and generic tools fall short.

#### **For the Security Nerds - Additional Metrics that Matter for Guard** <a href="#for-the-security-nerds-additional-metrics-that-matter-for-guard" id="for-the-security-nerds-additional-metrics-that-matter-for-guard"></a>

1. **Permission Exposure Score (PES)**

* **Definition**: A composite score (e.g., 0-100) reflecting the extent of excessive permissions or over-privileged profiles/users in the Salesforce environment, as detected by Guard’s monitoring of profile changes and sharing rules.
* **Purpose**: Quantifies the risk of privilege escalation and data exfiltration due to overly permissive access, a common Salesforce vulnerability generic tools miss. A lower score indicates a tighter, more secure configuration.
* **Target**: Elite performers might maintain a PES below 20, while higher scores (e.g., 50+) signal significant exposure needing immediate attention.
* **Improvement using Guard**: Use Guard to audit and adjust permissions regularly, focusing on least-privilege principles and detecting sharing rule modifications that expose sensitive data.\


2. **Configuration Drift Rate (CDR)**

* **Definition**: The percentage of Salesforce configurations (e.g., metadata, Apex code, sharing settings) that deviate from a secure baseline or compliance standard over a given period, as identified by Guard.
* **Purpose**: Measures the stability of the Salesforce environment against the constant changes from low-code development and release cycles, highlighting risks like misconfigurations that create attack vectors.
* **Target**: Elite performers keep CDR below 5%, while higher rates (e.g., 20%+) indicate uncontrolled drift and potential regulatory exposure.
* **Improvement using Guard**: Leverage Guard’s Salesforce-aware scanning to establish and enforce a secure baseline, alerting teams to unauthorized or risky changes in real time.

3. **Threat Detection Coverage (TDC)**

* **Definition**: The percentage of Salesforce-specific threat vectors (e.g., Apex vulnerabilities, metadata exploits, permission misconfigurations) that Guard actively monitors and detects out of all known or potential threats.
* **Purpose**: Assesses the comprehensiveness of Guard’s security monitoring, ensuring no critical blind spots remain in the Salesforce environment compared to generic tools lacking API integration.
* **Target**: High performers might achieve 90%+ coverage, while lower coverage (e.g., 50%) suggests gaps in monitoring key elements like custom code or sharing rules.
* **Improvement using Guard**: Expand TDC by fine-tuning Guard to include emerging Salesforce-specific threats and integrating it deeply into the platform’s ecosystem.\


4. **Mitigation Effectiveness Index (MEI)**

* **Definition**: The percentage of identified security issues (e.g., excessive permissions, configuration drift) that Guard successfully mitigates—either through automated fixes or actionable recommendations—without introducing new risks.
* **Purpose**: Evaluates how well Guard not only detects but also resolves Salesforce-specific issues, reducing the burden on security teams and minimizing residual risk.
* **Target**: Elite performers achieve an MEI of 85%+, while lower rates (e.g., 50%) indicate ineffective mitigation or reliance on manual processes.
* **Improvement using Guard**: Enhance MEI by utilizing Guard’s detailed insights and automation features to close vulnerabilities quickly and verify fixes.

#### **Want Even More Metrics?** <a href="#want-even-more-metrics" id="want-even-more-metrics"></a>

Beyond the original eight, here are two other potential Metrics that Matter to ensure a holistic view of security monitoring and mitigation with Guard:

1. **Compliance Adherence Rate (CAR)**

* **Definition**: The percentage of Salesforce configurations and processes that align with relevant regulatory standards (e.g., GDPR, HIPAA) as monitored by Guard.
* **Purpose**: Tracks the reduction of regulatory exposure, a key risk highlighted in the product info, ensuring the environment meets external requirements.
* **Target**: Aim for 95%+ adherence, with deviations flagged for immediate correction.
* **Why It Matters**: Persistent compliance control failures can lead to fines or reputational damage, and Guard’s Salesforce-specific capabilities can address this gap.

2. **Security Incident Avoidance Rate (SIAR)**

* **Definition**: The percentage of potential security incidents (e.g., data breaches, privilege abuse) prevented due to proactive detection and mitigation by Guard, based on historical incident patterns or simulations.
* **Purpose**: Quantifies Guard’s impact on avoiding real-world exploits, emphasizing its preventative value over reactive tools.
* **Target**: High performers might achieve 80%+ avoidance, reflecting strong preemptive security.
* **Why It Matters**: Preventing incidents like data exfiltration is a primary goal for Salesforce security, and this metric ties directly to business outcomes.

**Why These Metrics Are Unique**

Unlike DORA’s focus on software delivery speed and stability, these metrics prioritize security-specific outcomes in Salesforce:

* **PES** and **CDR** address platform-specific risks (permissions, drift) that generic tools can’t monitor effectively due to lacking Salesforce metadata awareness.
* **TDC** and **MEI** emphasize Guard’s ability to cover and resolve Salesforce-specific threats, shifting from DORA’s throughput/stability lens to a security efficacy lens.
* **CAR** and **SIAR** connect security performance to compliance and incident prevention, critical for Salesforce environments handling sensitive data.

**Are There Others We Should Be Concerned With?**

Yes, depending on the customer’s priorities, additional metrics could include:

* **User Behavior Anomaly Detection Rate**: Measures Guard’s ability to flag unusual admin or user actions (e.g., mass permission changes) that could signal insider threats.
* **Cost of Security Incidents Avoided**: Estimates the financial impact of risks mitigated by Guard, linking security to ROI.
* **False Positive Rate**: Tracks the accuracy of Guard’s alerts, ensuring teams aren’t overwhelmed by noise, which is vital for operational efficiency.

These metrics collectively provide a robust framework for evaluating Guard’s performance in securing Salesforce environments, focusing on visibility, risk mitigation, and compliance—key areas where it outshines generic tools. Customers can tailor these based on their specific security goals, such as regulatory focus or incident prevention.
