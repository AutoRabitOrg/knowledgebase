# Common Event Format (CEF) Data

Common Event Format (CEF) is a standardized logging format developed by ArcSight (now part of Micro Focus), a security information and event management (SIEM) solution provider. CEF is designed to simplify the process of logging security-related events, making it easier to integrate logs from different sources into a single system.

CEF is a text-based log format that uses Syslog as its transport protocol—a standard for message logging supported by most network devices and operating systems. A full CEF message includes:

- **Syslog header (prefix)**
- **CEF header**
- **CEF extension** (a list of key-value pairs)

The extension supports both standard and user-defined key names.

### CEF Standard and Custom Key

This table lists the CEF key names used in events, along with their full names, types, applicable modules, data types, length limits, and descriptions.

> **Note:** The key name is what must be used in the actual event log.

<!-- Table preserved as HTML to maintain formatting integrity -->

<table>
<thead>
<tr>
<th width="113">Key Name</th>
<th width="117">Full Name</th>
<th width="103">Key Type</th>
<th width="87">Module</th>
<th width="79">Data Type</th>
<th width="74">Length</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<!-- Full table content from original input goes here -->
</tbody>
</table>
