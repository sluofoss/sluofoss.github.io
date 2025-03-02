---
created: 2025-02-26T00:52
updated: 2025-03-02T15:38
title: WSL ip pinging issues
---
# Context
## symptoms
- cant use wget to download files
- ping inside  powershell and cmd works fine.
- ping any ip inside wsl2 
	- tried 
		- 8.8.8.8
		- www.google.com
		- 1.1.1.1
		- 8.8.4.4
	- gets redirected to the router page
	- From 192.168.1.1 icmp_seq=1 Destination Net Unreachable
- this issue only arised after windows update some time in Feb 2025.
# attempt fixes
- https://github.com/microsoft/WSL/issues/4171#issuecomment-929858850
	- see this in windows defender with advanced security - inbound rules
	- ![[Pasted image 20250226005602.png]]
	- this did not work
- try to upgrade to windows 11 (worked on laptop when having issues with vpn)
	- windows 11 is more resource intensive and killed other applications (wsl) much more often due to lack of RAM
	- this would be less of an issue on desktop with 32GB
	- need to permanently disable this somehow.
		- considering adding task scheduler to delay update by 35 days with trigger on
			- startup
			- daily
		- [How to Pause Windows Updates Longer Than 5 Weeks (Up to 20 Years) - YouTube](https://www.youtube.com/watch?v=zNBQx7o7WsI)
		- ![[Pasted image 20250226232416.png]]
	

# Why reality sucks 
windows is still the only least effort option for both window+linux dev (wsl)
	- desktop BI tools like power bi, tableau, qlik sense are only avail on window and/or mac