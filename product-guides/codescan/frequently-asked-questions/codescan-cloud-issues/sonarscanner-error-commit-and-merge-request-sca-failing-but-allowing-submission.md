# SonarScanner Error - Commit & Merge Request SCA Failing but Allowing Submission

## Commit and Merge request SCA is failing with the following error but is allowing submission.

ERROR: Error during SonarScanner execution

ERROR: Language of file force-app/main/default/permissionsets/abc\_filename.permissionset-metaxml' can not be decided as the file matches patterns of both sonar.lang.patterns.mule: \*\*/\*abcd,\*\*/\*xml and sonar.lanq.patterns.sfmeta: \*\*/\*profile-meta.xml.\*\*/\*permissionset-meta.xml.\*\*/\*settings-meta.xml.\*\*/\*abject-metaxml.z\*/\*field-meta.xmll\*s/\*fiow-meta.xml.\*\*/\*sharingrules-meta.xml.\*\*/\*workflow-meta.xml\*\*/\*profilesessionsetting-meta.xml \*\*/\*profilepasswordpolicy-meta.xml.\*\*/\*.profile，\*\*/\*.permissionset，\*\*/\*.settings.\*\*/\*.object.\*\*/\*.flow，\*\*/\*.sharingrules，\*\*/\*warkflow\*\*/\*.profilesessionsetting，\*\*/\*.profilepassvordpolicy

<figure><img src="../../../../.gitbook/assets/image (6).png" alt=""><figcaption></figcaption></figure>

### Environment configuration checklist

Configured the Mule setting (Key: sonar.mule.file.suffixes) with values ".abcd" and ".xml," which are causing errors. Need to navigate to the project where this error occurs in CodeScan?

Go to Project Settings > General Settings, and search for "mule" in the search box. Remove ".xml".

<figure><img src="../../../../.gitbook/assets/image (1) (1) (1) (1) (2).png" alt=""><figcaption></figcaption></figure>

By adjusting these settings in CodeScan, the SCA will not fail
