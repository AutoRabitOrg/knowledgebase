# Custom Dashboard Filters

## Configuring Dashboard Filters

Dashboard filters are preconfigured by default as part of the builtin setup. In addition to these, custom filters can be defined and managed through the dashboard filter settings.

### Configuring Custom Dashboard Filters

* Navigate to **`Global Settings`** -> **`Settings`**
* Search for **`Dashboard Filters`** and click Edit
* Modify an existing filter or add a new one by selecting **`Add Entry`**
* Save the changes to make the new or updated filters available for use in dashboards

### Dashboard Filter Structure

| Field | Description       | Example |
| ----- | ----------------- | ------- |
| key   | Unique Filter key |         |

```json
{
    "key": "applicationStatus"
}
```

\| type | Type of filter. Possible values **`select_multi`**, **`select`**, **`search`** | |

```json
{
      "type": "select_multi"
}
```

\| name | Name of filter to be displayed | |

```json
{
    "name": "Application Status"
}
```

\| placeholder | Placeholder to be displayed when no search option is selected | |

```json
{
    "placeholder": "Select Application Status",
}
```

\| filterKeys | Name of the column to be used to filter data. The value of the field should be same as filter key. | |

```json
{
  "filterKeys": ["applicationStatus"],
}
```

\| options | Dropdown values which to be displayed for the filter. Applicable for **`select_multi`** and **`select`** option types. | |

```json
{
  "options": [
    { "value": "RUNNING", "label": "RUNNING" }
  ]
}
```

* NOTE: The name of the filter **`key`** should be same as the value of the **`filterKeys`**

Complete example:

```json
{
  "key": "appStatus",
  "type": "select_multi",
  "name": "Application Status",
  "display": "modal",
  "placeholder": "Select Application Status",
  "filterKeys": ["appStatus"],
  "options": [
    { "value": "RUNNING", "label": "RUNNING" },
    { "value": "STARTED", "label": "STARTED" }
  ]
}
```

### See Also

* [Create Agent](../agent/create-agent.md)
* [Update Agent](../agent/update-agent.md)
