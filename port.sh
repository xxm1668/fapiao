#!/bin/bash
pro='tcp'
NAT_Host='11.10.10.3'
NAT_Port=8000
Dst_Host='172.16.19.81'
Dst_Port=8000
iptables -t nat -A PREROUTING  -m $pro -p $pro --dport $NAT_Port -j DNAT --to-destination $Dst_Host:$Dst_Port
iptables -t nat -A POSTROUTING -m $pro -p $pro --dport $Dst_Port -d $Dst_Host -j SNAT --to-source $NAT_Host