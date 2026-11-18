# Copado SFDX Integration CodeScan 2.0. Plugin

[Copado Labs CodeScan v2 User Manual](https://docs.google.com/document/d/1Mdv5iJuy4YNMWoZk8R1c2JTxJBsM4MbM14mYFy4W9xE/edit?tab=t.0#heading=h.5x0d5h95i329)

## Overview

The Copado Labs CodeScan v2 extension runs CodeScan scans from inside Copado SFDX (source format) pipelines, and the CodeScan quality gate decides whether the Copado quality gate passes.

A scan can be triggered from:

* **A User Story**, with the action _Run CodeScan From User Story_.
* **An Environment**, with the action _Run CodeScan From Environment_. Run it on your Production environment first to create the baseline.
* **A Copado Quality Gate**, with a Quality Gate Rule of type _CopadoLabsCodeScan_ that runs after a commit.

Every scan is mapped to a project in CodeScan. You choose how: let Copado create projects for you (default), keep one project per pipeline, or point all scans at a CodeScan project you control.&#x20;

This extension is a complete redesign of the former copado-codescan package (version 1.28 and earlier). If you still run the old package, read Migrating from copado-codescan before you install (the section in the Copado document).

## Choose how scans map to CodeScan projects

Decide this first, because it sets how your CodeScan projects will look. Every scan from Copado lands in a CodeScan project, and there are three ways to map it:

1. **Copado project (default).** Each Copado project gets its own corresponding project in CodeScan, created automatically.
2. **Pipeline project.** One project in CodeScan for the whole pipeline, named after the pipeline and created automatically. Feature branch scans land in it as pull requests under the main branch.
3. **Existing CodeScan project.** Works like Option 2, but the scans go to a project you already created in CodeScan, so you choose its name and key.

## Setup and migration

All settings, including the System Properties, the Quality Gate Rule and the record pages, are in Copado's user manual attached below. It also has the steps for migrating from the former copado-codescan package. Follow it for the installation and configuration.

[Copado Labs CodeScan v2 User Manual](https://docs.google.com/document/d/1Mdv5iJuy4YNMWoZk8R1c2JTxJBsM4MbM14mYFy4W9xE/edit?tab=t.0#heading=h.5x0d5h95i329)

