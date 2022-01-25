# MACChangerPy
It's a small project for MAC address change, for ethical hacking purposes, don't use it for bad purposes, any infringement will be your responsibility.

"With big powers come big responsabilities"

Mode of use:

python3 main.py --help                                  
Usage: main.py [options]

Options:
  -h, --help            show this help message and exit
  -i INTERFACE, --interface=INTERFACE
                        Interface to change its MAC address
  -m NEW_MAC, --mac=NEW_MAC
                        New MAC address
                                      
                                      
Example:

use comand su to be a superuser, after this, use this command:

python3 main.py -i eth0 -m 00:00:00:00:00:00
