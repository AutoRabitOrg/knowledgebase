# IZ Eye Scan Patterns

## IZ Eye | Pattern Matcher

The following section describes the pattern configurations to be used to filter (include / exclude) certain applications from being scanned from IZ Eye. By default all applications will be scanned by **`IZ Eye`**.

Examples:

1. Scan Assets in Exchange which are tagged as "PRODUCTION"
2. Scan Applications in Runtime Manager which follow a certain naming convention or which are updated after a certain date

### Anypoint Mule Applications Pattern Matcher:

Anypoint Mule Applications pattern matcher settings can be updated in the **`Global Settings`** -> **`Settings`** -> Search for **`Anypoint Mule Applications Pattern Matcher`**

Mule applications can be filtered using following attributes -

1. Application Name
2. Last Updated Time of the Application

**Pattern Configuration** -

| Attribute Name   | Pattern Configuration |
| ---------------- | --------------------- |
| Application Name |                       |

```json
{
    "name": {
      "includePattern": [".*"],
      "excludePattern": [] 
    }
}
```

\| Last Updated Time of the Application | |

```json
{
    "lastUpdated": {
      "type": "compare",
      "operator": ">",
      "value": 0
    }
}
```

### Anypoint Exchange APIs Pattern Matcher:

Anypoint Exchange APIs pattern matcher settings can be updated in the **`Global Settings`** -> **`Settings`** -> Search for **`Anypoint Exchange APIs Pattern Matcher`**

Anypoint Exchange APIs can be filtered using following attributes -

1. API Name / Asset Id
2. Tags attached to the Asset
3. Categories attached to the Asset
4. Last Updated Time of the Asset
5. API Visibility
6. API Status
7. Custom Fields

**Pattern Configuration** -

| Attribute Name      | Pattern Configuration |
| ------------------- | --------------------- |
| API Name / Asset Id |                       |

```json
{
    "name": {
      "includePattern": [".*"],
      "excludePattern": [] 
    }
}
```

\| Tags attached to the Asset | |

```json
{
    "tags": {
      "includePattern": ["sapi","papi"],
      "excludePattern": [] 
    }
}
```

\| Categories attached to the Asset | |

```json
{
    "categories": {
      "includePattern": ["Category Name=Value"],
      "excludePattern": [] 
    }
}
```

\| API Visibility | |

```json
{
    "isPublic": {
      "includePattern": ["true"],
      "excludePattern": [] 
    }
}
```

\| API Status | |

```json
{
    "status": {
      "includePattern": ["Published"],
      "excludePattern": [] 
    }
}
```

\| Custom Fields | |

```json
{
    "customFields": {
      "includePattern": ["Custom Field Display Name=Value"],
      "excludePattern": [] 
    }
}
```

\| Last Updated Time of the Asset | |

```json
{
    "lastUpdated": {
      "type": "compare",
      "operator": ">",
      "value": 0
    }
}
```

### Anypoint API Instance Pattern Matcher:

Anypoint API Instance pattern matcher settings can be updated in the **`Global Settings`** -> **`Settings`** -> Search for **`Anypoint API Instance Pattern Matcher`**

Anypoint API Instances can be filtered using following attributes -

1. API Instance Name / Asset Id
2. Tags attached to the Instance
3. Last Updated Time of the Instance
4. API Instance Visibility
5. API Instance Status
6. API Instance Deprecation Status
7. API Instance Stage

**Pattern Configuration** -

| Attribute Name               | Pattern Configuration |
| ---------------------------- | --------------------- |
| API Instance Name / Asset Id |                       |

```json
{
    "name": {
      "includePattern": [".*"],
      "excludePattern": [] 
    }
}
```

\| Tags attached to the Instance | |

```json
{
    "tags": {
      "includePattern": ["sapi","papi"],
      "excludePattern": [] 
    }
}
```

\| API Instance Deprecation Status | |

```json
{
    "deprecated": {
      "includePattern": [".*"],
      "excludePattern": [] 
    }
}
```

\| API Instance Visibility | |

```json
{
    "isPublic": {
      "includePattern": ["true"],
      "excludePattern": [] 
    }
}
```

\| API Instance Status | |

```json
{
    "status": {
      "includePattern": ["Published"],
      "excludePattern": [] 
    }
}
```

\| Last Updated Time of the Instance | |

```json
{
    "lastUpdated": {
      "type": "compare",
      "operator": ">",
      "value": 0
    }
}
```

### See Also

* [Create Agent](../agent/create-agent.md)
* [Update Agent](../agent/update-agent.md)
