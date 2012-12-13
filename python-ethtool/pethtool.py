import ethtool

# Get info about all devices
devices = ethtool.get_interfaces_info(ethtool.get_devices()) 

# Retrieve and print info
for dev in devices:
   print "** Device: %s" % dev.device
   print "MAC addr: %s" % dev.mac_address
   print "IPv4: %s/%s   Brd: %s" % (dev.ipv4_address, dev.ipv4_netmask, dev.ipv4_broadcast)
   for ip6 in dev.get_ipv6_addresses():
        print "IPv6: [%s] %s/%i" % (ip6.scope, ip6.address, ip6.netmask)
   print
