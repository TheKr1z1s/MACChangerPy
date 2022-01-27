#!/usr/bin/env python
#Created by N3S7S

import subprocess
import  optparse

parser = optparse.OptionParser()

parser.add_option("-i","--interface",dest="interface",help="Interface to change its MAC address")
parser.add_option("-m","--mac",dest="new_mac",help="New MAC address")

(options, arguments) = parser.parse_args()

print("\nHello see your configurations and interface ethernet for release the changes: \n\n")
subprocess.call(["ip", "a"])

interface = options.interface
new_mac = options.new_mac

subprocess.call(["ip", "link", "set", interface, "down"])
subprocess.call(["ip", "link", "set", "dev", interface, "address", new_mac])
subprocess.call(["ip", "link", "set", interface, "up"])

print("\nYour MAC address has changed to: " + new_mac + " on the interface " + interface)
