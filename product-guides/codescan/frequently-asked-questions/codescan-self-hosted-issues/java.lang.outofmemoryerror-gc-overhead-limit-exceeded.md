# java.lang.OutOfMemoryError: GC overhead limit exceeded

This error can be solved by manually adding a parameter to your Ant environment path variable.

**In Windows:**

```
set ANT_OPTS=%ANT_OPTS% -Xmx2048M
```

**In Linux/OS X:**

```
export ANT_OPTS=$ANT_OPTS -Xmx2048M
```

If the problem persists, please contact [support@codescan.io](https://support@codescan.io/)

***
