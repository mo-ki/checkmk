#!/usr/bin/env python3
# Copyright (C) 2019 tribe29 GmbH - License: GNU General Public License v2
# This file is part of Checkmk (https://checkmk.com). It is subject to the terms and
# conditions defined in the file COPYING, which is part of this source code package.

# yapf: disable
# type: ignore

checkname = 'cisco_secure'

info = [[[u'16777216', u'fc1/1', u'1'], [u'16781312', u'fc1/2',
                                         u'1'], [u'16785408', u'fc1/3', u'2'],
         [u'16789504', u'fc1/4', u'2'], [u'16793600', u'fc1/5',
                                         u'2'], [u'16797696', u'fc1/6', u'2'],
         [u'83886080', u'mgmt0', u'2'], [u'151060481', u'Vlan1', u'2'],
         [u'369098754', u'port-channel3', u'1'], [u'369100040', u'port-channel1289', u'1'],
         [u'369100041', u'port-channel1290', u'1'], [u'369100042', u'port-channel1291', u'1'],
         [u'436232192', u'Ethernet1/7', u'2'], [u'436236288', u'Ethernet1/8', u'2'],
         [u'436240384', u'Ethernet1/9', u'2'], [u'436244480', u'Ethernet1/10', u'2'],
         [u'436248576', u'Ethernet1/11', u'2'], [u'436252672', u'Ethernet1/12', u'2'],
         [u'436256768', u'Ethernet1/13', u'2'], [u'436260864', u'Ethernet1/14', u'2'],
         [u'436264960', u'Ethernet1/15', u'1'], [u'436269056', u'Ethernet1/16', u'1'],
         [u'436273152', u'Ethernet1/17', u'1'], [u'436277248', u'Ethernet1/18', u'1'],
         [u'436281344', u'Ethernet1/19', u'2'], [u'436285440', u'Ethernet1/20', u'2'],
         [u'436289536', u'Ethernet1/21', u'2'], [u'436293632', u'Ethernet1/22', u'2'],
         [u'436297728', u'Ethernet1/23', u'2'], [u'436301824', u'Ethernet1/24', u'2'],
         [u'436305920', u'Ethernet1/25', u'2'], [u'436310016', u'Ethernet1/26', u'2'],
         [u'436314112', u'Ethernet1/27', u'2'], [u'436318208', u'Ethernet1/28', u'2'],
         [u'436322304', u'Ethernet1/29', u'2'], [u'436326400', u'Ethernet1/30', u'2'],
         [u'436330496', u'Ethernet1/31', u'2'], [u'436334592', u'Ethernet1/32', u'2'],
         [u'436338688', u'Ethernet1/33', u'2'], [u'436342784', u'Ethernet1/34', u'2'],
         [u'436346880', u'Ethernet1/35', u'2'], [u'436350976', u'Ethernet1/36', u'2'],
         [u'436355072', u'Ethernet1/37', u'2'], [u'436359168', u'Ethernet1/38', u'2'],
         [u'436363264', u'Ethernet1/39', u'2'], [u'436367360', u'Ethernet1/40', u'2'],
         [u'469773120', u'Vethernet693', u'1'], [u'469773184', u'Vethernet697', u'1'],
         [u'469773248', u'Vethernet701', u'1'], [u'469904224', u'Vethernet8887', u'1'],
         [u'469904288', u'Vethernet8891', u'1'], [u'469904352', u'Vethernet8895', u'1'],
         [u'503317174', u'vfc695', u'1'], [u'503317178', u'vfc699', u'1'],
         [u'503317182', u'vfc703', u'1'], [u'520093760', u'Ethernet1/1/2', u'2'],
         [u'520093824', u'Ethernet1/1/3', u'1'], [u'520093888', u'Ethernet1/1/4', u'2'],
         [u'520093952', u'Ethernet1/1/5', u'1'], [u'520094016', u'Ethernet1/1/6', u'2'],
         [u'520094080', u'Ethernet1/1/7', u'1'], [u'520094144', u'Ethernet1/1/8', u'2'],
         [u'520094208', u'Ethernet1/1/9', u'1'], [u'520094272', u'Ethernet1/1/10', u'2'],
         [u'520094336', u'Ethernet1/1/11', u'1'], [u'520094400', u'Ethernet1/1/12', u'2'],
         [u'520094464', u'Ethernet1/1/13', u'2'], [u'520094528', u'Ethernet1/1/14', u'2'],
         [u'520094592', u'Ethernet1/1/15', u'2'], [u'520094656', u'Ethernet1/1/16', u'2'],
         [u'520094720', u'Ethernet1/1/17', u'2'], [u'520094784', u'Ethernet1/1/18', u'2'],
         [u'520094848', u'Ethernet1/1/19', u'2'], [u'520094912', u'Ethernet1/1/20', u'2'],
         [u'520094976', u'Ethernet1/1/21', u'2'], [u'520095040', u'Ethernet1/1/22', u'2'],
         [u'520095104', u'Ethernet1/1/23', u'2'], [u'520095168', u'Ethernet1/1/24', u'2'],
         [u'520095232', u'Ethernet1/1/25', u'2'], [u'520095296', u'Ethernet1/1/26', u'2'],
         [u'520095360', u'Ethernet1/1/27', u'2'], [u'520095424', u'Ethernet1/1/28', u'2'],
         [u'520095488', u'Ethernet1/1/29', u'2'], [u'520095552', u'Ethernet1/1/30', u'2'],
         [u'520095616', u'Ethernet1/1/31', u'2'], [u'520095680', u'Ethernet1/1/32', u'2'],
         [u'520095744', u'Ethernet1/1/33', u'1']],
        [[u'469773120', u'', u'', u'0', u''], [u'469773184', u'', u'', u'0', u''],
         [u'469773248', u'', u'3', u'0', u''], [u'520093760', u'', u'3', u'0', u''],
         [u'520093888', u'2', u'3', u'0', u''], [u'520094016', u'2', u'3', u'0', u''],
         [u'520094144', u'2', u'3', u'0', u''], [u'520094272', u'2', u'3', u'0', u''],
         [u'520094400', u'2', u'3', u'0', u''], [u'520094784', u'2', u'3', u'0', u''],
         [u'520094912', u'2', u'3', u'0', u'']]]

discovery = {'': [(None, None)]}

checks = {
    '': [(None, {}, [
        (3, u'Port Vethernet693: unknown (violation count: 0, last MAC: ) unknown enabled state',
         []),
        (3, u'Port Vethernet697: unknown (violation count: 0, last MAC: ) unknown enabled state',
         []),
        (3,
         u'Port Vethernet701: shutdown due to security violation (violation count: 0, last MAC: ) unknown enabled state',
         []),
        (3,
         u'Port Ethernet1/1/2: shutdown due to security violation (violation count: 0, last MAC: ) unknown enabled state',
         []),
        (2,
         u'Port Ethernet1/1/4: shutdown due to security violation (violation count: 0, last MAC: )',
         []),
        (2,
         u'Port Ethernet1/1/6: shutdown due to security violation (violation count: 0, last MAC: )',
         []),
        (2,
         u'Port Ethernet1/1/8: shutdown due to security violation (violation count: 0, last MAC: )',
         []),
        (2,
         u'Port Ethernet1/1/10: shutdown due to security violation (violation count: 0, last MAC: )',
         []),
        (2,
         u'Port Ethernet1/1/12: shutdown due to security violation (violation count: 0, last MAC: )',
         []),
        (2,
         u'Port Ethernet1/1/18: shutdown due to security violation (violation count: 0, last MAC: )',
         []),
        (2,
         u'Port Ethernet1/1/20: shutdown due to security violation (violation count: 0, last MAC: )',
         [])
    ])]
}
