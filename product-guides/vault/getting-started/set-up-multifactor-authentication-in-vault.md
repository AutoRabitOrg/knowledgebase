# Set Up Multifactor Authentication in Vault

### What is Multi-factor authentication? <a href="#what-is-multifactor-authentication" id="what-is-multifactor-authentication"></a>

**Multi-factor authentication (MFA)** is a powerful, secure authentication method with two steps (or factors) to prove users’ identities when they log in. The first factor is information known to users, like usernames and passwords. The second is a verification method the user has in their possession, like an authenticator app or a security key. So multi-factor authorization makes it a lot harder for fraudsters to get access to your Vault data.

### Enabling MFA for your account <a href="#enabling-mfa-for-your-account" id="enabling-mfa-for-your-account"></a>

As an administrator of your account, you can enable multifactor authentication (MFA) for every account member (global level) or at the user level.

Enabling MFA in your account at a global level affects all members of the account. This means that the users must enroll for MFA at their next login.

Point to Note:

Enabling MFA does not affect users already logged in, as the enforcement of MFA on the account takes effect only at new logins.

Enabling MFA will mandate users to register their mobile devices for generating and validating tokens using authenticator apps like Google Authenticator or Salesforce Authenticator app.

1. In the **Vault** application, go to **`Manage Users > Users`**.
2.  Enable multifactor authentication (MFA) for every member in the account using the **`MFA toggle`** button located in the header or, look for the user from the list and enable the MFA by sliding the **`MFA toggle`** button to the right side.\


    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-AJJ0D9JM.png" alt=""><figcaption></figcaption></figure>

### Reset MFA <a href="#reset-mfa" id="reset-mfa"></a>

You can reach out to your administrator to reset your MFA, if you have lost your phone or changed your device, .

1. The administrator will reset MFA from the **`Manage Users > Users`** screen.
2.  Click on the **`Reset`** icon (next to where the MFA toggle button is displayed).\


    <figure><img src="https://cdn.document360.io/8711f4e7-c040-4616-aac9-d947f87e4619/Images/Documentation/image-W6W7MV33.png" alt=""><figcaption></figcaption></figure>
3. This will enable the user to register his device again with a new bar code on the authenticator app when he tries to log in.
