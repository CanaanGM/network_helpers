using `netdiscover` you can find the ips and macs for all devices just to validate ur work (be sudo tho)


```bash
netdiscover -r 192.168.1.1/24 -i wlan1
```

>look up the [scapy docs](https://scapy.readthedocs.io/en/latest/api/) 
>tip: create a virtual env, install scapy there and dive into the code there
