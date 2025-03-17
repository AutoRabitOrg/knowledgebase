---
description: Understanding Backup Behavior
---

# Understanding Backup Behavior

## Understanding **Backup Behavior** for Polymorphic Fields, Special Objects, and Ignored Objects

As part of the backup process, certain fields and objects are handled differently to ensure data integrity and system efficiency. The following changes outline how these elements are handled:

1. **Polymorphic Fields**
   * When a backup is performed, **polymorphic fields are not included**.
   * Since these fields reference multiple object types dynamically, excluding them helps maintain data consistency.
2. **Special Objects**
   * When a backup is performed, **special objects are not included** in the backup.
   * These objects are **not** displayed in the schema, as they are excluded due to system limitations or unique structural constraints.
3. **Ignored Objects**
   * **Ignored objects are included** in the backup.
   * These objects **are visible** in the schema, ensuring transparency in the backup process.
