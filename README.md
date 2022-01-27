# MACChangerPy
It's a small project for MAC address change, for ethical hacking purposes, don't use it for bad purposes, any infringement will be your responsibility.

"With big powers come big responsabilities"

## Mode of use:
With this command, you see all parameters of utilization in this program.

```
python3 main.py --help                                  
```
### Options:
```
  -h, --help show this help message and exit
  -i INTERFACE, --interface=INTERFACE Interface to change its MAC address
  -m NEW_MAC, --mac=NEW_MAC New MAC address
                                      
```                                      
#### Example:

use comand su to be a superuser, after this, use this command:
```
python3 main.py -i eth0 -m 00:00:00:00:00:00
```

## Updates

#### _v0.1_

  The "ifconfig" command is deprecated, changed the command to "ip" for more compatibility with other distros.
