---
hidden: true
---

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

If the problem persists, please contact [support@autorabit.com](https://app.gitbook.com/u/U7KnccYpFWeXYvGf32TZthHRT3C3).
