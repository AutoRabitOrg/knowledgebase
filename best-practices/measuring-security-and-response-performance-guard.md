# Measuring Security & Response Performance (Guard)

<mark style="color:red;">Red metrics</mark> indicate the more important metrics to measure whether speed and efficiency are the goals.

To establish "Metrics that Matter" for assessing a customer's performance using AutoRabit Guard in securing their Salesforce environment, we can draw inspiration from Google's DORA Metrics. For Guard, the goal shifts from software delivery to security performance, emphasizing the detection, prevention, and resolution of Salesforce-specific vulnerabilities and risks. I propose a set of key metrics tailored to Guard's purpose, mirroring DORA's focus on actionable, measurable outcomes that reflect both efficiency and effectiveness in securing Salesforce environments.&#x20;

### **Key Metrics that Matter for Guard**<sup>**™**</sup>   <a href="#key-metrics-that-matter-for-guard-tm" id="key-metrics-that-matter-for-guard-tm"></a>

1. <mark style="color:red;">**Vulnerability Detection Frequency**</mark>  &#x20;

* **Definition**: Measures how often Guard identifies new vulnerabilities or misconfigurations in the Salesforce environment over a given time period (e.g., daily, weekly, monthly). &#x20;
* **Purpose**: This metric reflects the tool's ability to proactively and regularly scan for issues, ensuring continuous visibility into the security posture. High frequency indicates robust monitoring of Salesforce-specific elements like Apex code, metadata, permissions, and sharing rules.  [Audits](https://app.gitbook.com/o/vIHQCTOOUDcNoPic3AQi/s/9vAxMuDrkUkB4OXlH9CL/~/changes/2585/best-practices/measuring-security-and-response-performance-guard/~/audits)
* **Target**: Elite performers should aim for daily or on-demand detection aligned with Salesforce changes, while lower performers might detect issues monthly or reactively after incidents. &#x20;
* **Improvement using Guard**: Increase scanning frequency by leveraging Guard’s real-time monitoring capabilities to catch configuration drift or permission changes as they occur. &#x20;

2. <mark style="color:red;">**Mean Time to Detect (MTTD) Security Issues**</mark>  &#x20;

* **Definition**: The average time it takes Guard to identify a Salesforce-specific security issue (e.g., excessive permissions, sharing rule modifications, or metadata vulnerabilities) from the moment it is introduced. &#x20;
* **Purpose**: This metric gauges the speed at which Guard provides actionable insights, critical for minimizing the window of exposure to potential exploits like privilege escalation or data exfiltration. &#x20;
* **Target**: Elite performance achieves detection in under an hour, while slower performers take days or weeks, especially if relying on manual audits or generic tools. &#x20;
* **Improvement using Guard**: Reduce MTTD by optimizing Guard’s Salesforce-aware scanning to focus on high-risk areas (e.g., profile permission changes) and integrating it into development workflows for early detection. &#x20;

3. <mark style="color:red;">**Security Issue Resolution Time (SIRT)**</mark>  &#x20;

* **Definition**: The average time it takes to remediate a detected security issue (e.g., fixing a misconfiguration, revoking excessive permissions, or adjusting sharing rules) after Guard identifies it. &#x20;
* **Purpose**: This metric assesses how quickly teams can respond to and resolve vulnerabilities, minimizing risk exposure and ensuring compliance. &#x20;
* **Target**: Elite performers resolve issues in less than a day from provocation, while lower performers could take weeks, especially without automated remediation guidance. &#x20;
* **Improvement using Guard**: Shorten SIRT by using Guard’s detailed reporting to prioritize critical issues and automate remediation steps where possible, addressing the technical gaps generic tools miss. &#x20;

4. <mark style="color:red;">**Change Failure Rate (Security-Related)**</mark>  &#x20;

* **Definition**: The percentage of Salesforce configuration or development changes (e.g., new Apex code, metadata updates, or permission adjustments) that introduce a security vulnerability or compliance failure, as detected by Guard. &#x20;
* **Purpose**: This metric evaluates the quality of changes in the Salesforce environment, highlighting how often they create exploitable attack vectors like privilege escalation or data exposure. &#x20;
* **Target**: Elite performers maintain a failure rate of 0-15%, while lower performers could see rates exceeding 30%, reflecting inadequate monitoring of Salesforce-specific risks. &#x20;
* **Improvement using Guard**: Lower the rate by using Guard to enforce pre-deployment checks, monitor low-code development, and validate metadata-driven customizations against security best practices. &#x20;

**Why These Metrics Matter** &#x20;

* **Throughput**: How quickly and frequently Guard detects vulnerabilities (Vulnerability Detection Frequency and MTTD), ensuring proactive security management in a dynamic, metadata-driven platform. &#x20;
* **Stability**: How effectively Guard helps maintain a secure environment (SIRT and Change Failure Rate), reducing risks like configuration drift, excessive permissions, and regulatory exposure. &#x20;

**Applying the Metrics** &#x20;

* **Benchmarking**: Customers and AutoRabit CSMs can use these metrics to classify their security performance (e.g., Elite, High, Medium, Low) and compare against industry standards or internal goals. &#x20;
* **Continuous Improvement**: Tracking these metrics over time helps teams identify bottlenecks (e.g., slow resolution times) and measure how well the customer can leverage Guard’s capabilities to close gaps. &#x20;
* **Business Impact**: Improved metrics demonstrate reduced risk, enhanced compliance, and protection against Salesforce-specific threats, justifying investment in Guard. &#x20;

By adopting these "Metrics that Matter," customers can quantify Guard’s impact on their Salesforce security, ensuring they address the unique challenges of admin-driven customization, constant release cycles, and platform-specific vulnerabilities—areas where Guard excels, and generic tools fall short. &#x20;

&#x20;

#### **For the Security Nerds - Additional Metrics that Matter for Guard**  <a href="#for-the-security-nerds-additional-metrics-that-matter-for-guard" id="for-the-security-nerds-additional-metrics-that-matter-for-guard"></a>

1. **Permission Exposure Score (PES)** &#x20;

* **Definition**: A composite score (e.g., 0-100) reflecting the extent of excessive permissions or over-privileged profiles/users in the Salesforce environment, as detected by Guard’s monitoring of profile changes and sharing rules. &#x20;
* **Purpose**: Quantifies the risk of privilege escalation and data exfiltration due to overly permissive access, a common Salesforce vulnerability generic tools miss. A lower score indicates a tighter, more secure configuration. &#x20;
* **Target**: Elite performers might maintain a PES below 20, while higher scores (e.g., 50+) signal significant exposure needing immediate attention. &#x20;
* **Improvement using Guard**: Use Guard to audit and adjust permissions regularly, focusing on least-privilege principles and detecting sharing rule modifications that expose sensitive data.  \
  &#x20;

2. **Configuration Drift Rate (CDR)** &#x20;

* **Definition**: The percentage of Salesforce configurations (e.g., metadata, Apex code, sharing settings) that deviate from a secure baseline or compliance standard over a given period, as identified by Guard. &#x20;
* **Purpose**: Measures the stability of the Salesforce environment against the constant changes from low-code development and release cycles, highlighting risks like misconfigurations that create attack vectors. &#x20;
* **Target**: Elite performers keep CDR below 5%, while higher rates (e.g., 20%+) indicate uncontrolled drift and potential regulatory exposure. &#x20;
* **Improvement using Guard**: Leverage Guard’s Salesforce-aware scanning to establish and enforce a secure baseline, alerting teams to unauthorized or risky changes in real time.  \
  \


3. **Threat Detection Coverage (TDC)** &#x20;

* **Definition**: The percentage of Salesforce-specific threat vectors (e.g., Apex vulnerabilities, metadata exploits, permission misconfigurations) that Guard actively monitors and detects out of all known or potential threats. &#x20;
* **Purpose**: Assesses the comprehensiveness of Guard’s security monitoring, ensuring no critical blind spots remain in the Salesforce environment compared to generic tools lacking API integration. &#x20;
* **Target**: High performers might achieve 90%+ coverage, while lower coverage (e.g., 50%) suggests gaps in monitoring key elements like custom code or sharing rules. &#x20;
* **Improvement using Guard**: Expand TDC by fine-tuning Guard to include emerging Salesforce-specific threats and integrating it deeply into the platform’s ecosystem.\
  &#x20;&#x20;

4. **Mitigation Effectiveness Index (MEI)** &#x20;

* **Definition**: The percentage of identified security issues (e.g., excessive permissions, configuration drift) that Guard successfully mitigates—either through automated fixes or actionable recommendations—without introducing new risks. &#x20;
* **Purpose**: Evaluates how well Guard not only detects but also resolves Salesforce-specific issues, reducing the burden on security teams and minimizing residual risk. &#x20;
* **Target**: Elite performers achieve an MEI of 85%+, while lower rates (e.g., 50%) indicate ineffective mitigation or reliance on manual processes. &#x20;
* **Improvement using Guard**: Enhance MEI by utilizing Guard’s detailed insights and automation features to close vulnerabilities quickly and verify fixes. &#x20;

&#x20;

#### **Want Even More Metrics?**   <a href="#want-even-more-metrics" id="want-even-more-metrics"></a>

Beyond the original eight, here are two other potential Metrics that Matter to ensure a holistic view of security monitoring and mitigation with Guard: &#x20;

1. **Compliance Adherence Rate (CAR)** &#x20;

* **Definition**: The percentage of Salesforce configurations and processes that align with relevant regulatory standards (e.g., GDPR, HIPAA) as monitored by Guard. &#x20;
* **Purpose**: Tracks the reduction of regulatory exposure, a key risk highlighted in the product info, ensuring the environment meets external requirements. &#x20;
* **Target**: Aim for 95%+ adherence, with deviations flagged for immediate correction. &#x20;
* **Why It Matters**: Persistent compliance control failures can lead to fines or reputational damage, and Guard’s Salesforce-specific capabilities can address this gap.  \
  \


2. **Security Incident Avoidance Rate (SIAR)** &#x20;

* **Definition**: The percentage of potential security incidents (e.g., data breaches, privilege abuse) prevented due to proactive detection and mitigation by Guard, based on historical incident patterns or simulations. &#x20;
* **Purpose**: Quantifies Guard’s impact on avoiding real-world exploits, emphasizing its preventative value over reactive tools. &#x20;
* **Target**: High performers might achieve 80%+ avoidance, reflecting strong preemptive security. &#x20;
* **Why It Matters**: Preventing incidents like data exfiltration is a primary goal for Salesforce security, and this metric ties directly to business outcomes. &#x20;

\
**Why These Metrics Are Unique** &#x20;

Unlike DORA’s focus on software delivery speed and stability, these metrics prioritize security-specific outcomes in Salesforce: &#x20;

* **PES** and **CDR** address platform-specific risks (permissions, drift) that generic tools can’t monitor effectively due to lacking Salesforce metadata awareness. &#x20;
* **TDC** and **MEI** emphasize Guard’s ability to cover and resolve Salesforce-specific threats, shifting from DORA’s throughput/stability lens to a security efficacy lens. &#x20;
* **CAR** and **SIAR** connect security performance to compliance and incident prevention, critical for Salesforce environments handling sensitive data. &#x20;

\
**Are There Others We Should Be Concerned With?** &#x20;

Yes, depending on the customer’s priorities, additional metrics could include: &#x20;

* **User Behavior Anomaly Detection Rate**: Measures Guard’s ability to flag unusual admin or user actions (e.g., mass permission changes) that could signal insider threats. &#x20;
* **Cost of Security Incidents Avoided**: Estimates the financial impact of risks mitigated by Guard, linking security to ROI. &#x20;
* **False Positive Rate**: Tracks the accuracy of Guard’s alerts, ensuring teams aren’t overwhelmed by noise, which is vital for operational efficiency. &#x20;

These metrics collectively provide a robust framework for evaluating Guard’s performance in securing Salesforce environments, focusing on visibility, risk mitigation, and compliance—key areas where it outshines generic tools. Customers can tailor these based on their specific security goals, such as regulatory focus or incident prevention.&#x20;

\
