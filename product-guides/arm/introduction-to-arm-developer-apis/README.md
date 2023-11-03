---
description: Introduction
---

# Developer APIs

ARM provides a comprehensive set of APIs for developer/product\_manager to integrate ARM with their platform.

The ARM API is organized around [REST](https://en.wikipedia.org/wiki/Representational\_state\_transfer). Our API has predictable resource-oriented URLs, accepts [form-encoded](https://en.wikipedia.org/wiki/POST\_\(HTTP\)#Use\_for\_submitting\_web\_forms) request bodies, returns [JSON-encoded](https://www.json.org/json-en.html) responses, and uses standard HTTP response codes, authentication, and verbs.

For all APIs as `<BASE-ORG-URL>` please use the URL of the [ARM](https://www.autorabit.com/products/automated-release-management/) organization instance where you want to integrate your data.

**For example:** if you are using **https://pilot.autorabit.com**, your `<BASE-ORG-URL>` will be **pilot.autorabit.com**\


### **To get started, you need to:**

1. **Obtaining your access token**: To interact with the API, you need to have a unique, personal access token, which is used to authenticate yourself within the API.
2. Configure your **projects** within AutoRABIT before using the API.
