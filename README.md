# Jamaddr Python Package

This package Created by Jamison Emilio and packaged by Todd Albiston

## Description:
Python Package adds functions to convert IP address or subnet masks to bits and bits back to IP address.


```python
from jamaddr import JamAddr
ipbits = JamAddr.ip_to_bits("192.168.0.23")
ipbits
```

returns = '11000000101010000000000000010111'

```python
from jamaddr import JamAddr
bitsip = JamAddr.bits_to_ip("11000000101010000000000000010111")
bitsip
```

returns = '192.168.0.23'
