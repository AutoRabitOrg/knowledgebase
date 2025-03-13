# Release Notes 24.3.3

## **ARM Release Notes 24.3.3**

**22 September 2024**

**The following fix was implemented to enhance security performance as indicated below:**

1. A security enhancement introduced with the 24.3.2 build to improve XSS schema validation across all APIs unintentionally caused Single Sign-On (SSO) requests using the application/x-www-form-urlencoded media type to be rejected. A fix implemented excluding this media type from the validation process for SSO successfully resolved the issue, and login functionality is fully restored.
