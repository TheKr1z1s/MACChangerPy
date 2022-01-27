#!/usr/bin/env python
import subprocess
import  optparse

parser = optparse.OptionParser()

parser.add_option("-i","--interface",dest="interface",help="Interface to change its MAC address")
parser.add_option("-m","--mac",dest="new_mac",help="New MAC address")

(options, arguments) = parser.parse_args()

print("\nHello see your configurations and interface ethernet for release the changes: ")
subprocess.call("ifconfig")

interface = options.interface
new_mac = options.new_mac

subprocess.call(["ifdown", interface])
subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
subprocess.call(["ifup", interface])

print("\nYour MAC address has changed to: " + new_mac + " on the interface " + interface)