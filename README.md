# Jamaddr Python Package

This package Created by Jamison Emilio and packaged by Todd Albiston

## Description:
Python Package adds functions to convert IP address or subnet masks to bits and bits back to IP address.


```python
from jamaddr import JamAddr
ipbits = JamAddr.ip_to_bits("192.168.0.23")
ipbits

returns = '11000000101010000000000000010111'
```

```python
from jamaddr import JamAddr
bitsip = JamAddr.bits_to_ip("11000000101010000000000000010111")
bitsip

returns = '192.168.0.23'
```

Of course you could also enter a subnet mask to convert to bits then do the same with it corresponding IP to then
work out what the network ID or Broadcast IPs would be or use your imagination on what other use cases could be.

```python
from jamaddr import JamAddr

def network_id(ip_cidr):

    ip, cidr = ip_cidr.split('/')
    ip_bits = JamAddr.ip_to_bits(ip)[:int(cidr)] + '0' * (32 - int(cidr))
    return '{}/{}'.format(JamAddr.bits_to_ip(ip_bits), cidr)

networkID = network_id("192.168.0.23/28")
print(networkID)

returns = 192.168.0.16/28
```

This example above is already included as a function in this package so you could just do the following, but you get the point. 

```python
from jamaddr import JamAddr

networkID = JamAddr.network_id("192.168.0.23/28")
print(networkID)

returns = 192.168.0.16/28
```