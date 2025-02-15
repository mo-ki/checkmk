#!/usr/bin/env python3
# Copyright (C) 2019 tribe29 GmbH - License: GNU General Public License v2
# This file is part of Checkmk (https://checkmk.com). It is subject to the terms and
# conditions defined in the file COPYING, which is part of this source code package.

# yapf: disable
# type: ignore



checkname = u'scaleio_mdm'


info = [[u'Cluster:'],
        [u'Name: tuc',
         u' Mode: 5_node',
         u' State: Normal',
         u' Active: 5/5',
         u' Replicas: 3/3'],
        [u'Virtual IPs: 192.168.50.21', u' 192.168.51.21', u' 123.456.78.99'],
        [u'Master MDM:'],
        [u'Name: Manager1', u' ID: 0x0000000000000001'],
        [u'IPs: 192.168.50.1',
         u' 192.168.51.1',
         u' Management IPs: 123.456.78.91',
         u' Port: 9011',
         u' Virtual IP interfaces: eth1',
         u' eth2',
         u' eth0'],
        [u'Version: 2.5.0'],
        [u'Slave MDMs:'],
        [u'Name: Manager2', u' ID: 0x0000000000000002'],
        [u'IPs: 192.168.50.2',
         u' 192.168.51.2',
         u' Management IPs: 123.456.78.92',
         u' Port: 9011',
         u' Virtual IP interfaces: eth1',
         u' eth2',
         u' eth0'],
        [u'Status: Normal', u' Version: 2.5.0'],
        [u'Name: Manager3', u' ID: 0x0000000000000003'],
        [u'IPs: 192.168.50.3',
         u' 192.168.51.3',
         u' Management IPs: 123.456.78.93',
         u' Port: 9011',
         u' Virtual IP interfaces: eth1',
         u' eth2',
         u' eth0'],
        [u'Status: Degraded', u' Version: 2.5.0'],
        [u'Name: Manager4', u' ID: 0x0000000000000004'],
        [u'IPs: 192.168.50.4',
         u' 192.168.51.4',
         u' Management IPs: 123.456.78.94',
         u' Port: 9011',
         u' Virtual IP interfaces: eth1',
         u' eth2',
         u' eth0'],
        [u'Status: Not synchronized', u' Version: 2.5.0'],
        [u'Name: Manager5', u' ID: 0x0000000000000005'],
        [u'IPs: 192.168.50.5',
         u' 192.168.51.5',
         u' Management IPs: 123.456.78.95',
         u' Port: 9011',
         u' Virtual IP interfaces: eth1',
         u' eth2',
         u' eth0'],
        [u'Status: Error', u' Version: 2.5.0'],
        [u'Name: Manager6', u' ID: 0x0000000000000006'],
        [u'IPs: 192.168.50.6',
         u' 192.168.51.6',
         u' Management IPs: 123.456.78.96',
         u' Port: 9011',
         u' Virtual IP interfaces: eth1',
         u' eth2',
         u' eth0'],
        [u'Status: Disconnected', u' Version: 2.5.0'],
        [u'Standby MDMs:'],
        [u'Name: Standby1', u' ID: 0x00000000000007', u' Manager'],
        [u'IPs: 192.168.50.7',
         u' 192.168.51.7',
         u' Management IPs: 123.456.78.97',
         u' Port: 9011',
         u' Virtual IP interfaces: eth1',
         u' eth2',
         u' eth0'],
        [u'Tie-Breakers:'],
        [u'Name: TB1', u' ID: 0xtb00000000000008'],
        [u'IPs: 192.168.50.3', u' 192.168.51.3', u' Port: 9011'],
        [u'Status: Normal', u' Version: 2.5.0']]


discovery = {'': [(None, {})]}


checks = {'': [(None,
                {},
                [(0, u'Mode: 5_node, State: Normal', []),
                 (0, u'Active: 5/5, Replicas: 3/3', []),
                 (0, u'Master MDM: Manager1', []),
                 (2,
                  u'Slave MDMs: Manager2, Manager3, Manager4, Manager5, Manager6',
                  []),
                 (0, u'Tie-Breakers: TB1', []),
                 (0, u'Standby MDMs: Standby1', [])])]}
