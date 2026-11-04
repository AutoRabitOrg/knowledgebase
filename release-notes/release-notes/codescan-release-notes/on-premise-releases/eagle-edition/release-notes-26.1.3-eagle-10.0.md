# Release Notes 26.1.3 Eagle 10.0

**Release Date: 10 August 2026**

### Summary&#x20;

CodeScan Self-hosted 26.1.3 is comprised of the following 1 component:&#x20;

* 0 New Features&#x20;
* 0 Application Enhancements
* 0 New Rules&#x20;
* 0 Rule Enhancements&#x20;
* 0 Rule Deprecations&#x20;
* 1 Fix&#x20;

Component details are listed in their corresponding sections within this document.&#x20;

### &#x20;Fixes

#### 1. Enhanced Detection of Unused Formal Parameters in Dynamic SOQL Queries

Enhanced the _sf:UnusedFormalParameter_ rule to analyze SOQL condition strings that are first assigned to local variables before being passed to dynamic SOQL methods, so that unused formal parameters referenced in dynamically constructed queries are detected consistently regardless of how the query string is built.

Previously, the rule only analyzed SOQL string literals passed directly as method arguments. It did not resolve the value of local string variables before they were passed into methods such as _setCondition()_ or ultimately executed through _Database.query(query.toSOQL())_. As a result, unused formal parameters referenced in these queries were not detected.

The following rule behavior has been updated:

1. Local variable resolution: the rule now traces `String` variable assignments — including concatenation (`+=`) and re-assignment — and resolves their values before analyzing parameter references.
2. Supported dynamic SOQL APIs: detection applies consistently across `Database.query()`, `Database.getQueryLocator()`, and `setCondition()`.
3. Direct string literal handling: existing detection of unused parameters in SOQL literals passed directly to dynamic SOQL methods remains unchanged.

The updated rule correctly handles scenarios including:

* Parameters used in variables passed to `setCondition()` — no false violation.
* Parameters absent from query strings built via local variables — violation flagged.
* Query strings built incrementally with `+=` concatenation — unreferenced parameters flagged.
* Variables re-assigned to static strings after referencing a parameter — no false violation.
* Parameters used inside conditional (`if`/`else`) query construction — no false positive.
* Multiple unused parameters in a single method signature — all unreferenced parameters flagged.

**Outcome**

* Provides more comprehensive unused parameter detection across real-world Apex coding patterns.
* Eliminates false negatives caused by indirect query string construction.
* Preserves all existing behavior with no regressions.
