# What ActiveAppTracker provides
* Overview of how much time you spend at which application
* Every second(default) your active Application on the Mac is determined via AppleScript
* Every 5 minutes(default) the app writes simple statistics into the statistics file

* Daemon behavior:
	- Once started, it runs in background and will be started on system boot automatically
	- Restarts automatically when killed

# How to install
Copy the sample .plist file into the Systems LaunchDaemons folder

* *sudo cp activeAppTracker.plist /Library/LaunchDaemons/activeAppTracker.plist*

* Adjust the /Library/LaunchDaemons/activeAppTracker.plist to match your paths for  
	(1) the program  
	(2) the statistics file

### Start it with:
- *sudo launchctl load /Library/LaunchDaemons/activeAppTracker.plist*

### Stop it with:
- *sudo launchctl unload /Library/LaunchDaemons/activeAppTracker.plist*
