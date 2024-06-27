# IP Whitelist

### When and Why would you need to Whitelist the AutoRABIT IP Address? <a href="#when-and-why-would-you-need-to-whitelist-the-autorabit-ip-address" id="when-and-why-would-you-need-to-whitelist-the-autorabit-ip-address"></a>

IP whitelisting adheres to the Zero Trust model's principle of '**deny all and permit some**'. So by default, all unknown entities are denied access to network resources by default. Because the Customer network by default blocks all traffic, AutoRABIT is unable to access the services on GIT in order to proceed with salesforce release management.

Application whitelists help in the protection of your system against malware, spam, ransomware, and other threats. Only approved apps can run thanks to application whitelists. Anything that is not whitelisted is deemed unsafe and is blocked.

In order to facilitate the connectivity of AutoRABIT with your VCS, you need to whitelist the specific IP address allocated to your AutoRABIT instance.

When a customer instance is behind a firewall, one of the methods for configuring connectivity is required. You can either whitelist AutoRABIT instance IPs in your Git network or set up the required VPN Tunnel. Any of these connections can be assisted by AutoRABIT.
