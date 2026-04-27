---
description: Understanding GitLeaks-Based Secret Detection Rules in CodeScan
---

# GitLeaks Rules

CodeScan has introduced a set of advanced rules powered by GitLeaks to strengthen security analysis by detecting hardcoded secrets within Salesforce codebases.

GitLeaks is a widely used tool for identifying sensitive information such as API keys, passwords, OAuth tokens, and private keys. CodeScan extends this capability to Salesforce-specific languages and components through the following rules:

#### **Supported Rules**

1. **GitLeaks Secret Detection in Apex Files** _(sf:ApexGitLeaksSecrets)_\
   This rule runs GitLeaks on Apex source files to detect hardcoded secrets such as API keys, passwords, OAuth tokens, and private keys. All standard and custom GitLeaks rules are applied, and detected issues are surfaced in CodeScan.
2. **GitLeaks Secret Detection in Salesforce Metadata Files** _(sfmeta:MetadataGitLeaksSecrets)_\
   GitLeaks Secret Detection in Salesforce Metadata Files: This rule runs GitLeaks on Salesforce Metadata files to detect hardcoded secrets such as API keys, passwords, OAuth tokens, and private keys. All standard and custom GitLeaks rules are applied, and detected issues are surfaced in CodeScan.
3. **GitLeaks Secret Detection in Visualforce & Lightning Files** _(vf:VFLightningGitLeaksSecrets)_\
   This rule runs GitLeaks on Visualforce source files to detect hardcoded secrets such as API keys, passwords, OAuth tokens, and private keys. All standard and custom GitLeaks rules are applied, and detected issues are surfaced in CodeScan.
4. **GitLeaks Secret Detection in JavaScript Files** _(cs-js:javascript-gitLeaks-secrets)_\
   This rule runs GitLeaks on Javascript files to detect hardcoded secrets such as API keys, passwords, OAuth tokens, and private keys. All standard and custom GitLeaks rules are applied, and detected issues are surfaced in CodeScan.

#### **How It Works**

* Each rule executes GitLeaks scanning on the respective file types.
* These rules are not enabled by default; users must activate them in the Quality Profile for the specific language.
* Identified issues are surfaced directly within CodeScan for review and remediation.

#### **Availability**

These GitLeaks-based detection rules are currently available on **AUS and US instances**.
