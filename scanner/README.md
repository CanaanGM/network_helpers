using `netdiscover` you can find the ips and macs for all devices just to validate ur work (be sudo tho)


```bash
netdiscover -r 192.168.1.1/24 -i wlan1
```
> Docs used
- resource for this [ARP_Ping](https://scapy.readthedocs.io/en/latest/usage.html#arp-ping)
- [ARP_class](https://scapy.readthedocs.io/en/latest/api/scapy.layers.l2.html)
- [Ether_Class](https://scapy.readthedocs.io/en/latest/api/scapy.layers.l2.html#scapy.layers.l2.Ether.fields_desc)
- [scapy docs](https://scapy.readthedocs.io/en/latest/api/) 
>tip: create a virtual env, install scapy there and dive into the code there

todo: 
- [ ] error handling xD
- [ ] find a way to gather more info, can use a { "IP" : [ device, info, and, stuff ] }
- [ ] use a [lib](https://stackoverflow.com/questions/9535954/printing-lists-as-tabular-data) to pretty print