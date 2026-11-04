---
description: How various elements are counted within CodeScan
---

# CodeScan Blocks, Lines, and Field Inquiries

### **What is a 'Block' of Code in CodeScan?**&#x20;

A 'block' in CodeScan refers to a defined segment of code that can be scanned in one operation. Specifically, a block consists of up to 40,000 lines of code. This metric is used to quantify and manage the code analysis process effectively.

### **How is a 'Line' of Code Defined in CodeScan?**&#x20;

In CodeScan, a 'line' of code is defined as any physical line in the codebase that contains at least one non-whitespace character and is not part of a comment. This definition ensures a consistent and accurate measurement of the actual code being analyzed, excluding whitespaces and comments.

### **How are Lines Counted in Queries with Multiple Fields?**&#x20;

When analyzing code containing queries with multiple fields, each field placed on a separate line is counted individually. For instance, if a query is structured with five fields, each on its own line, this will be counted as five lines in total. This granularity helps in providing a precise assessment of the code structure and volume.

### What Is the Difference Between a Line and a Line of Code?

CodeScan has two ways of counting the "Lines" in a project.

1. Lines
2. Lines of Code

The Lines of Code may not increase in a project, but the number of Lines may increase due to the addition of the Profiles and Permission Sets to the Salesforce project.

XML settings count as lines but not as Code.  To see this, you can use a custom view in the activity graph: [https://app.codescan.io/project/activity?custom\_metrics=duplicated\_lines\_density%2Clines%2Cncloc\&graph=custom\&id=NDR-Main](https://app.codescan.io/project/activity?custom_metrics=duplicated_lines_density%2Clines%2Cncloc\&graph=custom\&id=NDR-Main)

### **Are Empty Lines or Lines with Only Whitespace Included in the Line Count?**&#x20;

No, lines that consist solely of whitespace or are part of comments are not included in the line count in CodeScan.&#x20;

### What Blocks of Code are Billable?

Only non-commented lines of code for Apex, Aura Lightning, and Visual Force languages are billable. JavaScript, HTML, CSS, and Salesforce Metadata languages are not considered.

### Where can I find the current Lines of Code Consumed?

When adding or removing lines of code, the count of Lines of Code Consumed immediately updates in the billing section of the CodeScan UI.

