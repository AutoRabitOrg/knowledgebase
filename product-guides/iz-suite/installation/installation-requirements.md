# Installation Requirements

## IZ Suite Installation Requirements

This document outlines the hardware and software requirements required for installing the **`IZ Suite`** application. Below are the recommended requirements. However, specific sizing may vary based on different factors.

### Hardware Requirements

| Software         | Requirement |
| ---------------- | ----------- |
| **`RAM`**        | 4GB of RAM  |
| **`Processor`**  | 2 cores     |
| **`Disk Space`** | 20GB        |

### Software Requirements

| Software       | Requirement                        |
| -------------- | ---------------------------------- |
| **`Docker`**   | v20.x or greater                   |
| **`Database`** | PostgreSQL version 12.x or greater |

{% hint style="warning" %}
* On Linux-based machines, it is recommended for high-load systems to ensure that ulimit settings are properly configured (e.g., 65535 or unlimited) based on the number of applications running on the instance.
* Some versions lack backward compatibility, but users can contact Integral Zone support for assistance with migration as needed.
{% endhint %}

### See Also

* [Single Server Installation](../../integral-zone/iz-suite/installation/modes/single-server-installation.md)
* [Cluster Mode](../../integral-zone/iz-suite/installation/modes/cluster-installation.md)
