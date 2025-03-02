---
title: Router cant change DNS issue
created: 2025-03-02
updated: 2025-03-02T14:44
---

# scenario:
- wifi uses 4g lte signal from mobile sim card plan.
- after reboot after 1 months of power off, the signal seems to have decreased significantly. symptoms include
    - slower connection
    - slower speed test
    - cannot log into monkeytype
      - when disabling dns in firefox monkeytype works again.
    - Im also further having issues with all network connectivity inside wsl.
      - dhcp dns address (same as router config ip address) is visible inside wsl2 instead and result in destination net unreachable
      - this sub problem is resolved in [[WSL ip pinging issues.md]].
    - cant log in to copilot sessions

- this seems to be a router issue?
    - reasons:
        1. mobile phone hotspot with other sim allow log in to monkeytype stablely. before this month mobile signal is worse than 4g router.
        2. insertion of mobile phone hotspot sim into router have same performance issue. 

- this could also be an ISP issue.
  - got suggested that could be caused by recent storm. perhaps changing isp is enough?
  - currently both the home internet sim and phone sim are essentially from the same ISP (different brand)

# failed attempts
- try to configure router dns
  - home router does not have dedicated dns section to set to cloudflare.
- changing /etc/resolv.conf to nameserver 1.1.1.1 or 8.8.8.8 
  - does not work and result in temporary unresolution?
  - https://askubuntu.com/questions/1192347/temporary-failure-in-name-resolution-on-wsl

- factory reset
- downgrade firmware
- change ip
- change dhcp setting
- change dns
  - all failed for home router.
  - online chat with customer support deemed faulty product. await replacement process.
- get replacement router of same model 
  - (same model does not work)

# ongoing attempts
- get replacement router of different model 
- get replacement sim for the current home internet sim 
  - (currently this sim hotspot in phone works, dont work in router).
- order temporary substitute sim from different ISP for a month 
  - (only activate when the first 2 method doesnt work, can still put old sim in mobile phone temporarily for hotspot) 
  - (pause old sim or cancel depend on how things goes)

# resources
related knowledge on signal performance:

- https://wiki.teltonika-networks.com/view/RSRP_and_RSRQ
- https://support.cel-fi.com/hc/en-us/articles/1260805036129-Understanding-LTE-Signal-Strength-Values

dns and #NAT knowledge

- https://www.reddit.com/r/HomeNetworking/comments/qkxsdr/router_providing_dhcp_but_not_dns_configuration/
- https://askubuntu.com/questions/1364984/dns-not-working-on-wsl
- https://gist.github.com/coltenkrauter/608cfe02319ce60facd76373249b8ca6
- https://medium.com/@smitgabani/advanced-wsl-configuration-2b4888332fff
- https://github.com/microsoft/WSL/issues/4285
- https://learn.microsoft.com/en-us/windows/wsl/networking
- https://learn.microsoft.com/en-us/windows/wsl/wsl-config
- https://learn.microsoft.com/en-us/windows/wsl/wsl-config#wslconfig






