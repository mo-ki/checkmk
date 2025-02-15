#!/usr/bin/env python3
# Copyright (C) 2019 tribe29 GmbH - License: GNU General Public License v2
# This file is part of Checkmk (https://checkmk.com). It is subject to the terms and
# conditions defined in the file COPYING, which is part of this source code package.

# yapf: disable
# type: ignore



checkname = 'ibm_svc_portsas'


info = [[u'0',
         u'1',
         u'6Gb',
         u'1',
         u'node1',
         u'500507680305D3C0',
         u'online',
         u'',
         u'host',
         u'host_controller',
         u'0',
         u'1'],
        [u'1',
         u'2',
         u'6Gb',
         u'1',
         u'node1',
         u'500507680309D3C0',
         u'online',
         u'',
         u'host',
         u'host_controller',
         u'0',
         u'2'],
        [u'2',
         u'3',
         u'6Gb',
         u'1',
         u'node1',
         u'50050768030DD3C0',
         u'online',
         u'',
         u'host',
         u'host_controller',
         u'0',
         u'3'],
        [u'3',
         u'4',
         u'6Gb',
         u'1',
         u'node1',
         u'500507680311D3C0',
         u'offline',
         u'500507680474F03F',
         u'none',
         u'enclosure',
         u'0',
         u'4'],
        [u'4',
         u'5',
         u'N/A',
         u'1',
         u'node1',
         u'500507680315D3C0',
         u'offline_unconfigured',
         u'',
         u'none',
         u'host_controller',
         u'1',
         u'1'],
        [u'5',
         u'6',
         u'N/A',
         u'1',
         u'node1',
         u'500507680319D3C0',
         u'offline_unconfigured',
         u'',
         u'none',
         u'host_controller',
         u'1',
         u'2'],
        [u'6',
         u'7',
         u'N/A',
         u'1',
         u'node1',
         u'50050768031DD3C0',
         u'offline_unconfigured',
         u'',
         u'none',
         u'host_controller',
         u'1',
         u'3'],
        [u'7',
         u'8',
         u'N/A',
         u'1',
         u'node1',
         u'500507680321D3C0',
         u'offline_unconfigured',
         u'',
         u'none',
         u'host_controller',
         u'1',
         u'4'],
        [u'8',
         u'1',
         u'6Gb',
         u'2',
         u'node2',
         u'500507680305D3C1',
         u'online',
         u'',
         u'host',
         u'host_controller',
         u'0',
         u'1'],
        [u'9',
         u'2',
         u'6Gb',
         u'2',
         u'node2',
         u'500507680309D3C1',
         u'online',
         u'',
         u'host',
         u'host_controller',
         u'0',
         u'2'],
        [u'10',
         u'3',
         u'6Gb',
         u'2',
         u'node2',
         u'50050768030DD3C1',
         u'online',
         u'',
         u'host',
         u'host_controller',
         u'0',
         u'3'],
        [u'11',
         u'4',
         u'6Gb',
         u'2',
         u'node2',
         u'500507680311D3C1',
         u'offline',
         u'500507680474F07F',
         u'none',
         u'enclosure',
         u'0',
         u'4'],
        [u'12',
         u'5',
         u'N/A',
         u'2',
         u'node2',
         u'500507680315D3C1',
         u'offline_unconfigured',
         u'',
         u'none',
         u'host_controller',
         u'1',
         u'1'],
        [u'13',
         u'6',
         u'N/A',
         u'2',
         u'node2',
         u'500507680319D3C1',
         u'offline_unconfigured',
         u'',
         u'none',
         u'host_controller',
         u'1',
         u'2'],
        [u'14',
         u'7',
         u'N/A',
         u'2',
         u'node2',
         u'50050768031DD3C1',
         u'offline_unconfigured',
         u'',
         u'none',
         u'host_controller',
         u'1',
         u'3'],
        [u'15',
         u'8',
         u'N/A',
         u'2',
         u'node2',
         u'500507680321D3C1',
         u'offline_unconfigured',
         u'',
         u'none',
         u'host_controller',
         u'1',
         u'4']]


discovery = {'': [(u'Node 1 Slot 0 Port 1', {'current_state': u'online'}),
                  (u'Node 1 Slot 0 Port 2', {'current_state': u'online'}),
                  (u'Node 1 Slot 0 Port 3', {'current_state': u'online'}),
                  (u'Node 1 Slot 0 Port 4', {'current_state': u'offline'}),
                  (u'Node 2 Slot 0 Port 1', {'current_state': u'online'}),
                  (u'Node 2 Slot 0 Port 2', {'current_state': u'online'}),
                  (u'Node 2 Slot 0 Port 3', {'current_state': u'online'}),
                  (u'Node 2 Slot 0 Port 4', {'current_state': u'offline'})]}


checks = {'': [(u'Node 1 Slot 0 Port 1',
                {'current_state': u'online'},
                [(0, u'Status: online, Speed: 6Gb, Type: host_controller', [])]),
               (u'Node 1 Slot 0 Port 2',
                {'current_state': u'online'},
                [(0, u'Status: online, Speed: 6Gb, Type: host_controller', [])]),
               (u'Node 1 Slot 0 Port 3',
                {'current_state': u'online'},
                [(0, u'Status: online, Speed: 6Gb, Type: host_controller', [])]),
               (u'Node 1 Slot 0 Port 4',
                {'current_state': u'offline'},
                [(0, u'Status: offline, Speed: 6Gb, Type: enclosure', [])]),
               (u'Node 2 Slot 0 Port 1',
                {'current_state': u'online'},
                [(0, u'Status: online, Speed: 6Gb, Type: host_controller', [])]),
               (u'Node 2 Slot 0 Port 2',
                {'current_state': u'online'},
                [(0, u'Status: online, Speed: 6Gb, Type: host_controller', [])]),
               (u'Node 2 Slot 0 Port 3',
                {'current_state': u'online'},
                [(0, u'Status: online, Speed: 6Gb, Type: host_controller', [])]),
               (u'Node 2 Slot 0 Port 4',
                {'current_state': u'offline'},
                [(0, u'Status: offline, Speed: 6Gb, Type: enclosure', [])])]}
