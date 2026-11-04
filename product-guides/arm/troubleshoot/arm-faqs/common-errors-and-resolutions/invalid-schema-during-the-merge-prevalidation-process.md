# Invalid Schema during the Merge Prevalidation Process

## Error message: Invalid Schema during the Merge Prevalidation Process

This issue will occur if there are any special characters like the one below and if the string (length=7) is considered a GIT conflict (it is a GIT behavior), it will not perform the Merge.

Special Characters: '>' ; '<' ; '|' ; '=' &#x20;

We recommend limiting the above four special characters to fewer than 7 to avoid such problems.

For example, in the Class file, if you observe this **">>>>>>>"** character string (length=7), then update it to less than 7 in the branch itself and rerun the Merge operation.
