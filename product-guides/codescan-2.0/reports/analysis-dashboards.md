---
description: Track trends across your projects and your development activity.
---

# Analysis Dashboards

CodeScan has two dashboards. Both can be filtered by period (default: the last 90 days) and by repository.&#x20;

## Projects Dashboard

Shows the health of your code over time:

| Metric                            | What it tells you                                                                                                        |
| --------------------------------- | ------------------------------------------------------------------------------------------------------------------------ |
| Open findings over time           | Whether your backlog is growing or shrinking                                                                             |
| Introduced versus resolved        | Whether new problems are being added faster than old ones are fixed                                                      |
| Severity mix                      | Where your open findings sit by severity                                                                                 |
| Reference Branch Score (0 to 100) | An overall score for the reference branch <mark style="color:red;">**\[TO CONFIRM: how the score is calculated]**</mark> |
| Findings per 1,000 lines          | Finding density, comparable across projects of different sizes                                                           |
| Estimated test coverage           | From the coverage estimate or measured coverage                                                                          |
| Scan freshness                    | How recently each project was scanned                                                                                    |
| Top offending rules               | The rules with the most findings: candidates for training or for tuning                                                  |
| Practice deviation                | Where the code departs from policies set with [Policy as Intent](/broken/pages/2ce8f855435a7814a0336a9b9d81e6f96aac8bae) |
| Test quality                      | Test-quality scores over time                                                                                            |

## Development Dashboard

Shows development activity: commits, lines added and removed, test ratio, rework ratio, commit cadence, effort mix, test cases written per developer, and AI scan credit usage per user.

{% hint style="info" %}
**Note:** Use per-developer figures to guide team conversations, such as in sprint reviews, not as targets for individuals.
{% endhint %}

## Who Can See Dashboards

<mark style="background-color:yellow;">**Tenant manager**</mark> and <mark style="background-color:yellow;">**ACA admin**</mark> can see dashboards. <mark style="background-color:yellow;">**Support engineer**</mark> sees a read-only view. See [Users, Roles and Permissions](/broken/pages/2b94a4b9e4d4b52f8e2c7fefd702c1c7f6bbfa17).

## Related Articles

* [Reports and Export](/broken/pages/d79824437e9592a26c869ea6db870d920ed0fc6b)
* [Test Quality and Coverage](/broken/pages/f484f0589f327b3eba12ab568dbef7d6834b50f6)
