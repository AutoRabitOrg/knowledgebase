# SSL Certificates

## How are SSL Certificate validity enforced?

The certificate validity is set by CodeScan; however, if there is a firewall (e.g., Zscaler), then it’s determined by Zscaler.\
\
You can bypass the SSL security for [app.codescan.io](http://app.codescan.io/) or whichever instance url you are using to avoid the issue of the SSL certificate expiring and the need to keep adding them to the environment variables every time.
