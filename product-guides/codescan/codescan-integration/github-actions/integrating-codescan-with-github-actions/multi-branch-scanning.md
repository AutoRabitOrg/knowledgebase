# Multi-Branch Scanning

## Introduction

This document explains how to set up GitHub Actions workflows to perform CodeScan static analysis on a repository, including a baseline scan for the main branch and multi-branch scanning. Due to limitations in CodeScan/Sonar, special steps are required to manage the master/main branch creation.

## YAML Files Overview

<table><thead><tr><th valign="bottom">YAML</th><th valign="bottom">Purpose</th><th valign="bottom">Notes</th></tr></thead><tbody><tr><td valign="bottom">First YAML Option 1</td><td valign="bottom">Baseline scan on main branch (flexible push/PR)</td><td valign="bottom">Uses <code>ubuntu-latest</code>; scans changed files only; generates <code>SARIF</code>.</td></tr><tr><td valign="bottom">First YAML Option 2</td><td valign="bottom">Baseline scan on main branch (restricted to main)</td><td valign="bottom">Uses <code>ubuntu-latest</code>; fails on red quality gate; requires secrets for login.</td></tr><tr><td valign="bottom">Second YAML</td><td valign="bottom">Multi-branch scan</td><td valign="bottom">Runs on any branch; push = standard branch analysis; PR = comparison analysis.</td></tr></tbody></table>

## First YAML – Baseline Scan Options

### Option 1

name: CI\
env:\
&#x20; SONAR\_SCANNER\_VERSION: 5.0.1.3006\
on:\
&#x20; push:\
&#x20;   branches:\
&#x20;     \- '\*'\
&#x20;   paths-ignore:\
&#x20;     \- src/test/java/\*\*\
&#x20;     \- target/\*\*\
&#x20; pull\_request:\
&#x20;   branches:\
&#x20;     \- '\*'\
&#x20;   paths-ignore:\
&#x20;     \- src/test/java/\*\*\
&#x20;     \- target/\*\*\
jobs:\
&#x20; build:\
&#x20;   runs-on: ubuntu-latest\
&#x20;   steps:\
&#x20;     \- name: Checkout repository\
&#x20;       uses: actions/checkout@v4\
&#x20;     \- name: Cache files\
&#x20;       uses: actions/cache@v4\
&#x20;       with:\
&#x20;         path: |\
&#x20;           \~/.sonar\
&#x20;         key: $\{{ runner.os \}}-sonar\
&#x20;         restore-keys: $\{{ runner.os \}}-sonar\
&#x20;     \- name: Run Codescan On Push\
&#x20;       if: github.event\_name == 'push'\
&#x20;       uses: codescan-io/codescan-scanner-action@1.6\
&#x20;       with:\
&#x20;         scanChangedFilesOnly: true\
&#x20;         organization: 'Enter organization key here'\
&#x20;         projectKey: 'Enter project key here'\
&#x20;         codeScanUrl: 'Enter your instance URL'\
&#x20;         login: $\{{ secrets.codescan\_token \}}\
&#x20;         generateSarifFile: true\
&#x20;     \- name: Run Codescan On PR\
&#x20;       if: github.event\_name == 'pull\_request'\
&#x20;       uses: codescan-io/codescan-scanner-action@1.6\
&#x20;       with:\
&#x20;         scanChangedFilesOnly: true\
&#x20;         organization: 'Enter organization key here'\
&#x20;         projectKey: 'Enter project key here'\
&#x20;         codeScanUrl: 'Enter your instance URL'\
&#x20;         login: $\{{ secrets.codescan\_token \}}\
&#x20;         generateSarifFile: true\
&#x20;         args: |\
&#x20;           sonar.pullrequest.branch=$\{{github.head\_ref\}}\
&#x20;           sonar.pullrequest.base=$\{{github.base\_ref\}}\
&#x20;           sonar.pullrequest.key=$\{{github.event.number\}}\
&#x20;     \- name: Upload SARIF file\
&#x20;       uses: github/codeql-action/upload-sarif@v3\
&#x20;       with:\
&#x20;         sarif\_file: codescan.sarif\
&#x20;     \- name: Archive code coverage results\
&#x20;       uses: actions/upload-artifact@v4\
&#x20;       with:\
&#x20;         name: codescan.sarif\
&#x20;         path: codescan.sarif

***

### Option 2

name: CI\
on:\
&#x20; push:\
&#x20;   branches: \[main]\
&#x20; pull\_request:\
&#x20;   branches: \[main]\
env:\
&#x20; SONAR\_SCANNER\_VERSION: 5.0.1.3006\
jobs:\
&#x20; build:\
&#x20;   runs-on: ubuntu-latest\
&#x20;   steps:\
&#x20;     \- name: Checkout repository\
&#x20;       uses: actions/checkout@v4\
&#x20;     \- name: Cache files\
&#x20;       uses: actions/cache@v4\
&#x20;       with:\
&#x20;         path: |\
&#x20;           \~/.sonar\
&#x20;         key: $\{{ runner.os \}}-sonar\
&#x20;         restore-keys: $\{{ runner.os \}}-sonar\
&#x20;     \- name: Run Codescan On Push\
&#x20;       if: github.event\_name == 'push'\
&#x20;       uses: codescan-io/codescan-scanner-action@1.6\
&#x20;       with:\
&#x20;         organization: 'Enter organization key here'\
&#x20;         projectKey: 'Enter project key here'\
&#x20;         codeScanUrl: 'Enter your instance URL'\
&#x20;         login: $\{{ secrets.codescan\_token \}}\
&#x20;         generateSarifFile: true\
&#x20;         failOnRedQualityGate: true\
&#x20;     \- name: Run Codescan On PR\
&#x20;       if: github.event\_name == 'pull\_request'\
&#x20;       uses: codescan-io/codescan-scanner-action@1.6\
&#x20;       with:\
&#x20;         organization: 'Enter organization key here'\
&#x20;         projectKey: 'Enter project key here'\
&#x20;         codeScanUrl: 'Enter your instance URL'\
&#x20;         login: $\{{ secrets.codescan\_token \}}\
&#x20;         scanChangedFilesOnly: true\
&#x20;         generateSarifFile: true\
&#x20;         failOnRedQualityGate: true\
&#x20;         args: |\
&#x20;           sonar.pullrequest.branch=$\{{github.head\_ref\}}\
&#x20;           sonar.pullrequest.base=$\{{github.base\_ref\}}\
&#x20;           sonar.pullrequest.key=$\{{github.event.number\}}\
&#x20;     \- name: Upload SARIF file\
&#x20;       uses: github/codeql-action/upload-sarif@v3\
&#x20;       with:\
&#x20;         sarif\_file: codescan.sarif\
&#x20;     \- name: Archive code coverage results\
&#x20;       uses: actions/upload-artifact@v4\
&#x20;       with:\
&#x20;         name: codescan.sarif\
&#x20;         path: codescan.sarif

***

## Handling Master/Main Branch Issue

* After the first scan, a master branch may exist in CodeScan.
* When switching to the second YAML, pushing to main may create an extra main branch.

Steps to resolve:

1. Delete the newly created main branch in CodeScan.
2. Rename the master branch to main.
3. Confirm the baseline analysis is associated with the main.

***

## Second YAML – Multi-Branch Scan

name: CI\
env:\
&#x20; SONAR\_SCANNER\_VERSION: 5.0.1.3006\
&#x20; SONAR\_SOURCES: force-app\
on:\
&#x20; push:\
&#x20;   branches:\
&#x20;     \- '\*'\
&#x20;   paths-ignore:\
&#x20;     \- src/test/java/\*\*\
&#x20;     \- target/\*\*\
&#x20; pull\_request:\
&#x20;   branches:\
&#x20;     \- '\*'\
&#x20;   paths-ignore:\
&#x20;     \- src/test/java/\*\*\
&#x20;     \- target/\*\*\
jobs:\
&#x20; build:\
&#x20;   runs-on: macos-latest\
&#x20;   steps:\
&#x20;     \- name: Checkout repository\
&#x20;       uses: actions/checkout@v4\
&#x20;       with:\
&#x20;         fetch-depth: 0\
&#x20;     \- name: Cache files\
&#x20;       uses: actions/cache@v4\
&#x20;       with:\
&#x20;         path: |\
&#x20;           \~/.sonar\
&#x20;         key: $\{{ runner.os \}}-sonar\
&#x20;         restore-keys: $\{{ runner.os \}}-sonar\
&#x20;     \- name: Run Codescan On Push\
&#x20;       if: github.event\_name == 'push'\
&#x20;       uses: codescan-io/codescan-scanner-action@1.6\
&#x20;       with:\
&#x20;         scanChangedFilesOnly: true\
&#x20;         organization: 'Enter organization key here'\
&#x20;         projectKey: 'Enter project key here'\
&#x20;         codeScanUrl: 'Enter your instance URL'\
&#x20;         login: $\{{ secrets.codescan\_token \}}\
&#x20;         generateSarifFile: true\
&#x20;         args: |\
&#x20;           sonar.branch.name=$\{{ github.ref\_name \}}\
&#x20;           sonar.sources=$\{{ env.SONAR\_SOURCES \}}\
&#x20;           sonar.exclusions=target/\*\*,src/test/java/\*\*\
&#x20;     \- name: Run Codescan On PR\
&#x20;       if: github.event\_name == 'pull\_request'\
&#x20;       uses: codescan-io/codescan-scanner-action@1.6\
&#x20;       with:\
&#x20;         scanChangedFilesOnly: true\
&#x20;         organization: 'Enter organization key here'\
&#x20;         projectKey: 'Enter project key here'\
&#x20;         codeScanUrl: 'Enter your instance URL'\
&#x20;         login: $\{{ secrets.codescan\_token \}}\
&#x20;         generateSarifFile: true\
&#x20;         args: |\
&#x20;           sonar.pullrequest.key=$\{{ github.event.pull\_request.number \}}\
&#x20;           sonar.pullrequest.branch=$\{{ github.head\_ref \}}\
&#x20;           sonar.pullrequest.base=$\{{ github.base\_ref \}}\
&#x20;           sonar.sources=$\{{ env.SONAR\_SOURCES \}}\
&#x20;           sonar.exclusions=target/\*\*,src/test/java/\*\*\
&#x20;     \- name: Upload SARIF file\
&#x20;       uses: github/codeql-action/upload-sarif@v3\
&#x20;       with:\
&#x20;         sarif\_file: codescan.sarif\
&#x20;     \- name: Archive code coverage results\
&#x20;       uses: actions/upload-artifact@v4\
&#x20;       with:\
&#x20;         name: codescan.sarif

***

## Step-by-Step Workflow

1. Initial Baseline Scan

* Add first YAML (Option 1 or 2) to scan main branch.
* Push and verify baseline scan on CodeScan.

2. Branch Adjustment

* Replace YAML with second YAML
* Delete extra main branch in CodeScan if created.
* Rename master to main.

3. Multi-Branch Scanning.

* Push to other branches to enable scanning.
* Verify SARIF upload and analysis in GitHub.

***

## Notes & Considerations

* Sonar/CodeScan limitations require the baseline to be on main/master first.
* Always fetch full history for PR analysis (fetch-depth: 0).
* SONAR\_SOURCES: force-app Incase folder structure is other than DX
* SONAR\_SOURCES: src (or) .(. here represents the ROOT FOLDER)
* Specifying Root Folder, CodeScan always scans the Root folder mentioned and files within it.
* In scenarios where the customer has multiple root folders, using (.) will make sure every root folder in the repo is scanned.&#x20;

***
