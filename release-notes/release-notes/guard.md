# Guard Release Notes

## Guard 25.1.1 Release

**Release Date: 21 March 2025**

### New Features

**Multi-Factor Authentication (MFA) for Guard:** MFA is now implemented for Guard.

**User Lockout After Failed Login Attempts:** Users will be locked out after three consecutive failed login attempts and notified via email.

**New Settings Page:** The Admin section has been moved to the profile menu for improved navigation. Users can access Settings from the dropdown menu, which includes Salesforce Orgs and User Management.

**Criteria-Based Policies for Permissions:** Users can now create criteria-based policies for permission-specific policies, extending the existing capability for permission set policies.

### Enhancements

**Removal of Clickjack Protection Setting from Risk Assessment:** The Enable clickjack protection for Setup pages setting has been removed from Risk Assessment due to Salesforce limitations.

**Rebranding of SPM to Guard in Emails:** All customer-facing emails now display "Guard" instead of "SPM."

**Identification of Sandbox Type Upon Login:** Guard now determines and stores the sandbox type for usage tracking when a sandbox org is registered.

**Move Management Console to Settings Page:** The Management Console is now integrated into the Settings page, and the Delete User button has been relocated to the User Detail page.
