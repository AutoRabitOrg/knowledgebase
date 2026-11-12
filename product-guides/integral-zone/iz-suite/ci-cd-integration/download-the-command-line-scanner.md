# Download the Command-Line Scanner

The command-line scanner runs Code Analysis scans from your build machine or CI/CD pipeline and sends the results to IZ Suite. Download the zip for your operating system and processor. Each zip includes its own Java runtime, so nothing else needs to be installed.

{% hint style="info" %}
Use the scanner version that matches your IZ Suite release. The pipeline steps that **Administration** → **Setup** → **Scan in your CI/CD pipeline** generates download the right version for you.
{% endhint %}

## Version 26.4.2

| Operating system      | Download                                                                                                                               |
| --------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| Linux (x64)           | [iz-scan-cli-26.4.2-linux.zip](https://iz-releases.s3.amazonaws.com/iz-scan-cli/26.4.2/iz-scan-cli-26.4.2-linux.zip)                   |
| Linux (ARM64)         | [iz-scan-cli-26.4.2-linux-aarch64.zip](https://iz-releases.s3.amazonaws.com/iz-scan-cli/26.4.2/iz-scan-cli-26.4.2-linux-aarch64.zip)   |
| macOS (Intel)         | [iz-scan-cli-26.4.2-macosx.zip](https://iz-releases.s3.amazonaws.com/iz-scan-cli/26.4.2/iz-scan-cli-26.4.2-macosx.zip)                 |
| macOS (Apple silicon) | [iz-scan-cli-26.4.2-macosx-aarch64.zip](https://iz-releases.s3.amazonaws.com/iz-scan-cli/26.4.2/iz-scan-cli-26.4.2-macosx-aarch64.zip) |
| Windows (x64)         | [iz-scan-cli-26.4.2-windows.zip](https://iz-releases.s3.amazonaws.com/iz-scan-cli/26.4.2/iz-scan-cli-26.4.2-windows.zip)               |

## Version 26.4.1

| Operating system      | Download                                                                                                                               |
| --------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| Linux (x64)           | [iz-scan-cli-26.4.1-linux.zip](https://iz-releases.s3.amazonaws.com/iz-scan-cli/26.4.1/iz-scan-cli-26.4.1-linux.zip)                   |
| Linux (ARM64)         | [iz-scan-cli-26.4.1-linux-aarch64.zip](https://iz-releases.s3.amazonaws.com/iz-scan-cli/26.4.1/iz-scan-cli-26.4.1-linux-aarch64.zip)   |
| macOS (Intel)         | [iz-scan-cli-26.4.1-macosx.zip](https://iz-releases.s3.amazonaws.com/iz-scan-cli/26.4.1/iz-scan-cli-26.4.1-macosx.zip)                 |
| macOS (Apple silicon) | [iz-scan-cli-26.4.1-macosx-aarch64.zip](https://iz-releases.s3.amazonaws.com/iz-scan-cli/26.4.1/iz-scan-cli-26.4.1-macosx-aarch64.zip) |
| Windows (x64)         | [iz-scan-cli-26.4.1-windows.zip](https://iz-releases.s3.amazonaws.com/iz-scan-cli/26.4.1/iz-scan-cli-26.4.1-windows.zip)               |

## Version 26.3.1

| Operating system      | Download                                                                                                                               |
| --------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| Linux (x64)           | [iz-scan-cli-26.3.1-linux.zip](https://iz-releases.s3.amazonaws.com/iz-scan-cli/26.3.1/iz-scan-cli-26.3.1-linux.zip)                   |
| Linux (ARM64)         | [iz-scan-cli-26.3.1-linux-aarch64.zip](https://iz-releases.s3.amazonaws.com/iz-scan-cli/26.3.1/iz-scan-cli-26.3.1-linux-aarch64.zip)   |
| macOS (Intel)         | [iz-scan-cli-26.3.1-macosx.zip](https://iz-releases.s3.amazonaws.com/iz-scan-cli/26.3.1/iz-scan-cli-26.3.1-macosx.zip)                 |
| macOS (Apple silicon) | [iz-scan-cli-26.3.1-macosx-aarch64.zip](https://iz-releases.s3.amazonaws.com/iz-scan-cli/26.3.1/iz-scan-cli-26.3.1-macosx-aarch64.zip) |
| Windows (x64)         | [iz-scan-cli-26.3.1-windows.zip](https://iz-releases.s3.amazonaws.com/iz-scan-cli/26.3.1/iz-scan-cli-26.3.1-windows.zip)               |

## Install the Scanner

1. Download the zip for your operating system.
2. Unzip it. It unpacks to a folder named like the zip, for example `iz-scan-cli-26.4.2-linux/`.
3. Run `bin/iz-scan-cli` (`bin\iz-scan-cli.bat` on Windows) from that folder. See [Command-Line Scanner](command-line-scanner.md) for the options.

To download from a script, use the same address with your version and file name:

```bash
export IZ_CLI_VERSION=26.4.2
curl -fsSLo iz.zip "https://iz-releases.s3.amazonaws.com/iz-scan-cli/$IZ_CLI_VERSION/iz-scan-cli-$IZ_CLI_VERSION-linux.zip" && unzip -oq iz.zip
```

## Next Steps

* [Command-Line Scanner](command-line-scanner.md): run a scan and read its results.
* [Pipeline Examples](pipeline-examples.md): add the scanner to your pipeline.
* [Access Tokens](pipeline-access-tokens.md): create the token the scanner signs in with.
