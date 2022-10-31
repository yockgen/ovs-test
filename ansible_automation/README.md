## An Ansible Playbook example on Docker Container with Open vSwitch as network bridge automation    

This example is assumed that user has been:
1. Installed Ansible engine 
2. SSH setup on all hosts    

Tutorial could be found on https://docs.ansible.com/ansible/latest/getting_started/index.html

### Verifying Ansible is proper configured        
```
ansible -i /etc/ansible/hosts all -m ping    
```

### Run OvS Container Playbook
The playbook is expected the host directory all shell scripts files (the *.sh files in this project) will be located inside /data/ovs-test, if this not the case, please change the main.yaml "path" variable accordingly:
```
ansible-playbook main.yaml
```

### Expected Result

```
yockgenm@kbl01:/data/imsa$ ansible-playbook main.yaml

PLAY [Ubuntu OvS configuration and validation] **********************************************************************************************************************************************

TASK [Gathering Facts] **********************************************************************************************************************************************************************
[DEPRECATION WARNING]: Distribution ubuntu 22.04 on host 192.168.1.161 should use /usr/bin/python3, but is using /usr/bin/python for backward compatibility with prior Ansible releases. A
future Ansible release will default to using the discovered platform python for this host. See https://docs.ansible.com/ansible-core/2.11/reference_appendices/interpreter_discovery.html
for more information. This feature will be removed in version 2.12. Deprecation warnings can be disabled by setting deprecation_warnings=False in ansible.cfg.
ok: [192.168.1.161]

TASK [Install Open vSwitch] *****************************************************************************************************************************************************************
ok: [192.168.1.161]

TASK [Install Docker] ***********************************************************************************************************************************************************************
ok: [192.168.1.161]

TASK [Run container] ************************************************************************************************************************************************************************
changed: [192.168.1.161]

TASK [debug] ********************************************************************************************************************************************************************************
ok: [192.168.1.161] => {
    "msg": [
        "Clear previous running container",
        "eccd06415a29",
        "532ea46a84b5",
        "a7fc7d0fc57c",
        "20f6f0d872d9",
        "714e97cf6d15",
        "92a793322f75",
        "3372bcba61f3",
        "a8602e300076",
        "e57deb6de7f1",
        "2b189eb51a62",
        "722eff48c814",
        "0a3b7fedc787",
        "53d75edc2489",
        "d90c41949313",
        "6e1a37438087",
        "d7e103ed4284",
        "5644be70a911",
        "96515eedc111",
        "989b928e8d94",
        "8639b31d10ff",
        "bfb57c30d1a4",
        "d5c0681b55e2",
        "b74783b5f2ad",
        "7ae22c6e3044",
        "0a31940af539",
        "79df96b12672",
        "b6b36c976e3b",
        "e0d2934a9beb",
        "2d72eb785099",
        "85197f5084e4",
        "771fc47e266c",
        "eeee8dfe525a",
        "293eee43cc56",
        "57de3387d686",
        "Run 1st container - yockgen01",
        "deb4f9eb9dc8737d65c8e58c0ff9fbc222a638bdd05b6de2e06bc8bb7f90746b",
        "Run 2nd container - yockgen02",
        "8fcba7d8b40020fe52e2eb4005bcab539f80885d09ab374310edcbe204a32756"
    ]
}

TASK [Verify test container] ****************************************************************************************************************************************************************
changed: [192.168.1.161]

TASK [debug] ********************************************************************************************************************************************************************************
ok: [192.168.1.161] => {
    "msg": [
        "8fcba7d8b400   alpine                 \"sh -c 'while sleep …\"   1 second ago    Up Less than a second             yockgen02",
        "deb4f9eb9dc8   alpine                 \"sh -c 'while sleep …\"   2 seconds ago   Up 1 second                       yockgen01"
    ]
}

TASK [Configure ovs] ************************************************************************************************************************************************************************
changed: [192.168.1.161]

TASK [debug] ********************************************************************************************************************************************************************************
ok: [192.168.1.161] => {
    "msg": [
        "1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN qlen 1000",
        "    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00",
        "    inet 127.0.0.1/8 scope host lo",
        "       valid_lft forever preferred_lft forever",
        "2: gre0@NONE: <NOARP> mtu 1476 qdisc noop state DOWN qlen 1000",
        "    link/gre 0.0.0.0 brd 0.0.0.0",
        "3: gretap0@NONE: <BROADCAST,MULTICAST> mtu 1462 qdisc noop state DOWN qlen 1000",
        "    link/ether 00:00:00:00:00:00 brd ff:ff:ff:ff:ff:ff",
        "4: erspan0@NONE: <BROADCAST,MULTICAST> mtu 1450 qdisc noop state DOWN qlen 1000",
        "    link/ether 00:00:00:00:00:00 brd ff:ff:ff:ff:ff:ff",
        "5: tunl0@NONE: <NOARP> mtu 1480 qdisc noop state DOWN qlen 1000",
        "    link/ipip 0.0.0.0 brd 0.0.0.0",
        "76: eth0@if77: <BROADCAST,MULTICAST,UP,LOWER_UP,M-DOWN> mtu 1500 qdisc noqueue state UP ",
        "    link/ether 02:42:ac:11:00:02 brd ff:ff:ff:ff:ff:ff",
        "    inet 172.17.0.2/16 brd 172.17.255.255 scope global eth0",
        "       valid_lft forever preferred_lft forever",
        "85: eth1@if86: <BROADCAST,MULTICAST,UP,LOWER_UP,M-DOWN> mtu 1500 qdisc noqueue state UP qlen 1000",
        "    link/ether 92:8b:8e:69:86:93 brd ff:ff:ff:ff:ff:ff",
        "    inet 173.16.1.10/24 scope global eth1",
        "       valid_lft forever preferred_lft forever",
        "1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN qlen 1000",
        "    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00",
        "    inet 127.0.0.1/8 scope host lo",
        "       valid_lft forever preferred_lft forever",
        "2: gre0@NONE: <NOARP> mtu 1476 qdisc noop state DOWN qlen 1000",
        "    link/gre 0.0.0.0 brd 0.0.0.0",
        "3: gretap0@NONE: <BROADCAST,MULTICAST> mtu 1462 qdisc noop state DOWN qlen 1000",
        "    link/ether 00:00:00:00:00:00 brd ff:ff:ff:ff:ff:ff",
        "4: erspan0@NONE: <BROADCAST,MULTICAST> mtu 1450 qdisc noop state DOWN qlen 1000",
        "    link/ether 00:00:00:00:00:00 brd ff:ff:ff:ff:ff:ff",
        "5: tunl0@NONE: <NOARP> mtu 1480 qdisc noop state DOWN qlen 1000",
        "    link/ipip 0.0.0.0 brd 0.0.0.0",
        "78: eth0@if79: <BROADCAST,MULTICAST,UP,LOWER_UP,M-DOWN> mtu 1500 qdisc noqueue state UP ",
        "    link/ether 02:42:ac:11:00:03 brd ff:ff:ff:ff:ff:ff",
        "    inet 172.17.0.3/16 brd 172.17.255.255 scope global eth0",
        "       valid_lft forever preferred_lft forever",
        "89: eth1@if90: <BROADCAST,MULTICAST,UP,LOWER_UP,M-DOWN> mtu 1500 qdisc noqueue state UP qlen 1000",
        "    link/ether a2:fd:74:83:cd:96 brd ff:ff:ff:ff:ff:ff",
        "    inet 173.16.1.11/24 scope global eth1",
        "       valid_lft forever preferred_lft forever"
    ]
}

TASK [Connection Testing] *******************************************************************************************************************************************************************
changed: [192.168.1.161]

TASK [debug] ********************************************************************************************************************************************************************************
ok: [192.168.1.161] => {
    "msg": [
        "PING 173.16.1.11 (173.16.1.11): 56 data bytes",
        "64 bytes from 173.16.1.11: seq=0 ttl=64 time=0.308 ms",
        "64 bytes from 173.16.1.11: seq=1 ttl=64 time=0.071 ms",
        "64 bytes from 173.16.1.11: seq=2 ttl=64 time=0.057 ms",
        "64 bytes from 173.16.1.11: seq=3 ttl=64 time=0.065 ms",
        "64 bytes from 173.16.1.11: seq=4 ttl=64 time=0.144 ms",
        "64 bytes from 173.16.1.11: seq=5 ttl=64 time=0.111 ms",
        "64 bytes from 173.16.1.11: seq=6 ttl=64 time=0.140 ms",
        "64 bytes from 173.16.1.11: seq=7 ttl=64 time=0.103 ms",
        "64 bytes from 173.16.1.11: seq=8 ttl=64 time=0.107 ms",
        "64 bytes from 173.16.1.11: seq=9 ttl=64 time=0.153 ms",
        "",
        "--- 173.16.1.11 ping statistics ---",
        "10 packets transmitted, 10 packets received, 0% packet loss",
        "round-trip min/avg/max = 0.057/0.125/0.308 ms",
        "PING 173.16.1.10 (173.16.1.10): 56 data bytes",
        "64 bytes from 173.16.1.10: seq=0 ttl=64 time=0.059 ms",
        "64 bytes from 173.16.1.10: seq=1 ttl=64 time=0.145 ms",
        "64 bytes from 173.16.1.10: seq=2 ttl=64 time=0.140 ms",
        "64 bytes from 173.16.1.10: seq=3 ttl=64 time=0.193 ms",
        "64 bytes from 173.16.1.10: seq=4 ttl=64 time=0.061 ms",
        "64 bytes from 173.16.1.10: seq=5 ttl=64 time=0.169 ms",
        "64 bytes from 173.16.1.10: seq=6 ttl=64 time=0.162 ms",
        "64 bytes from 173.16.1.10: seq=7 ttl=64 time=0.063 ms",
        "64 bytes from 173.16.1.10: seq=8 ttl=64 time=0.198 ms",
        "64 bytes from 173.16.1.10: seq=9 ttl=64 time=0.136 ms",
        "",
        "--- 173.16.1.10 ping statistics ---",
        "10 packets transmitted, 10 packets received, 0% packet loss",
        "round-trip min/avg/max = 0.059/0.132/0.198 ms"
    ]
}

PLAY RECAP **********************************************************************************************************************************************************************************
192.168.1.161              : ok=11   changed=4    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0

```

