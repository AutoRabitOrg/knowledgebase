# Error occurred during initialization of VM Could not reserve enough space for xxxKB object heap

If you are experiencing this error when running a scan, the issue may be with your Java version. **32bit Java versions** have a lower limit to their heap size. This limit can be as low as **1.6GB** on Windows operating systems.

If you are running a **64bit** operating system you will need to upgrade to a **64bit version of Java**.

You can check whether your Java version is **32** or **64bit** by using the command: _**java -d64 -version**_ in your command prompt or terminal. If you have a **32bit version of Java** installed you will get the message:

```
Error: This Java instance does not support a 64-bit JVM.
```

```
Please install the desired version.
```
