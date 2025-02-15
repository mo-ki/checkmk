#!/usr/bin/env python3
# Copyright (C) 2019 tribe29 GmbH - License: GNU General Public License v2
# This file is part of Checkmk (https://checkmk.com). It is subject to the terms and
# conditions defined in the file COPYING, which is part of this source code package.

# yapf: disable
# type: ignore

checkname = 'cisco_secure'

info = [[[u'83886080', u'mgmt0', u'2'], [u'101191680', u'sup-fc0', u'1'],
         [u'151060481', u'Vlan1', u'2'], [u'369098752', u'port-channel1', u'1'],
         [u'369098753', u'port-channel2', u'1'], [u'369099904', u'port-channel1153', u'1'],
         [u'369099905', u'port-channel1154', u'1'], [u'369100049', u'port-channel1298', u'1'],
         [u'369100054', u'port-channel1303', u'1'], [u'369100057', u'port-channel1306', u'1'],
         [u'369100059', u'port-channel1308', u'1'], [u'369100062', u'port-channel1311', u'1'],
         [u'369100068', u'port-channel1317', u'1'], [u'369100071', u'port-channel1320', u'2'],
         [u'369100077', u'port-channel1326', u'2'], [u'369100081', u'port-channel1330', u'1'],
         [u'369100085', u'port-channel1334', u'2'], [u'369100087', u'port-channel1336', u'1'],
         [u'369100091', u'port-channel1340', u'1'], [u'369100093', u'port-channel1342', u'1'],
         [u'369100097', u'port-channel1346', u'1'], [u'369100099', u'port-channel1348', u'1'],
         [u'369100101', u'port-channel1350', u'1'], [u'436207616', u'Ethernet1/1', u'1'],
         [u'436211712', u'Ethernet1/2', u'1'], [u'436215808', u'Ethernet1/3', u'1'],
         [u'436219904', u'Ethernet1/4', u'1'], [u'436224000', u'Ethernet1/5', u'1'],
         [u'436228096', u'Ethernet1/6', u'1'], [u'436232192', u'Ethernet1/7', u'1'],
         [u'436236288', u'Ethernet1/8', u'1'], [u'436240384', u'Ethernet1/9', u'2'],
         [u'436244480', u'Ethernet1/10', u'2'], [u'436248576', u'Ethernet1/11', u'2'],
         [u'436252672', u'Ethernet1/12', u'2'], [u'436256768', u'Ethernet1/13', u'2'],
         [u'436260864', u'Ethernet1/14', u'2'], [u'436264960', u'Ethernet1/15', u'2'],
         [u'436269056', u'Ethernet1/16', u'2'], [u'436273152', u'Ethernet1/17', u'1'],
         [u'436277248', u'Ethernet1/18', u'1'], [u'436281344', u'Ethernet1/19', u'2'],
         [u'436285440', u'Ethernet1/20', u'2'], [u'436289536', u'Ethernet1/21', u'1'],
         [u'436293632', u'Ethernet1/22', u'1'], [u'436297728', u'Ethernet1/23', u'2'],
         [u'436301824', u'Ethernet1/24', u'2'], [u'436305920', u'Ethernet1/25', u'2'],
         [u'436310016', u'Ethernet1/26', u'2'], [u'436314112', u'Ethernet1/27', u'2'],
         [u'436318208', u'Ethernet1/28', u'2'], [u'436322304', u'Ethernet1/29', u'2'],
         [u'436326400', u'Ethernet1/30', u'2'], [u'436330496', u'Ethernet1/31', u'2'],
         [u'436334592', u'Ethernet1/32', u'2'], [u'469775264', u'Vethernet827', u'1'],
         [u'469775296', u'Vethernet829', u'1'], [u'469775392', u'Vethernet835', u'1'],
         [u'469775424', u'Vethernet837', u'1'], [u'469775696', u'Vethernet854', u'1'],
         [u'469775760', u'Vethernet858', u'1'], [u'469776528', u'Vethernet906', u'1'],
         [u'469776608', u'Vethernet911', u'1'], [u'469776640', u'Vethernet913', u'1'],
         [u'469776720', u'Vethernet918', u'2'], [u'469777888', u'Vethernet991', u'1'],
         [u'469777920', u'Vethernet993', u'1'], [u'469778192', u'Vethernet1010', u'1'],
         [u'469778208', u'Vethernet1011', u'1'], [u'469778240', u'Vethernet1013', u'1'],
         [u'469778480', u'Vethernet1028', u'1'], [u'469778496', u'Vethernet1029', u'1'],
         [u'469778528', u'Vethernet1031', u'1'], [u'469778576', u'Vethernet1034', u'1'],
         [u'469778592', u'Vethernet1035', u'1'], [u'469778624', u'Vethernet1037', u'1'],
         [u'469778672', u'Vethernet1040', u'1'], [u'469778688', u'Vethernet1041', u'1'],
         [u'469778720', u'Vethernet1043', u'1'], [u'469778976', u'Vethernet1059', u'1'],
         [u'469779008', u'Vethernet1061', u'1'], [u'469779056', u'Vethernet1064', u'1'],
         [u'469779072', u'Vethernet1065', u'1'], [u'469779104', u'Vethernet1067', u'1'],
         [u'469779312', u'Vethernet1080', u'1'], [u'469779456', u'Vethernet1089', u'1'],
         [u'469779488', u'Vethernet1091', u'1'], [u'469779536', u'Vethernet1094', u'1'],
         [u'469779552', u'Vethernet1095', u'1'], [u'469779584', u'Vethernet1097', u'1'],
         [u'469780176', u'Vethernet1134', u'1'], [u'469780288', u'Vethernet1141', u'1'],
         [u'469780320', u'Vethernet1143', u'1'], [u'469780368', u'Vethernet1146', u'1'],
         [u'469780384', u'Vethernet1147', u'1'], [u'469780416', u'Vethernet1149', u'1'],
         [u'469780496', u'Vethernet1154', u'1'], [u'469906432', u'Vethernet9025', u'1'],
         [u'469906560', u'Vethernet9033', u'1'], [u'469906816', u'Vethernet9049', u'1'],
         [u'469906880', u'Vethernet9053', u'1'], [u'469907648', u'Vethernet9101', u'1'],
         [u'469907776', u'Vethernet9109', u'1'], [u'469907840', u'Vethernet9113', u'2'],
         [u'469909056', u'Vethernet9189', u'1'], [u'469910208', u'Vethernet9261', u'1'],
         [u'469910432', u'Vethernet9275', u'1'], [u'469910688', u'Vethernet9291', u'1'],
         [u'469911296', u'Vethernet9329', u'1'], [u'469911520', u'Vethernet9343', u'1'],
         [u'469911616', u'Vethernet9349', u'1'], [u'503317202', u'vfc723', u'1'],
         [u'503317312', u'vfc833', u'1'], [u'503317320', u'vfc841', u'1'],
         [u'503317336', u'vfc857', u'1'], [u'503317340', u'vfc861', u'1'],
         [u'503317388', u'vfc909', u'1'], [u'503317396', u'vfc917', u'1'],
         [u'503317400', u'vfc921', u'2'], [u'503317476', u'vfc997', u'1'],
         [u'503317548', u'vfc1069', u'1'], [u'503317562', u'vfc1083', u'1'],
         [u'503317578', u'vfc1099', u'1'], [u'503317616', u'vfc1137', u'1'],
         [u'503317630', u'vfc1151', u'1'], [u'503317636', u'vfc1157', u'1'],
         [u'520093696', u'Ethernet1/1/1', u'1'], [u'520093760', u'Ethernet1/1/2', u'2'],
         [u'520093824', u'Ethernet1/1/3', u'1'], [u'520093888', u'Ethernet1/1/4', u'2'],
         [u'520093952', u'Ethernet1/1/5', u'1'], [u'520094016', u'Ethernet1/1/6', u'2'],
         [u'520094080', u'Ethernet1/1/7', u'1'], [u'520094144', u'Ethernet1/1/8', u'2'],
         [u'520094208', u'Ethernet1/1/9', u'1'], [u'520094272', u'Ethernet1/1/10', u'2'],
         [u'520094336', u'Ethernet1/1/11', u'1'], [u'520094400', u'Ethernet1/1/12', u'2'],
         [u'520094464', u'Ethernet1/1/13', u'1'], [u'520094528', u'Ethernet1/1/14', u'2'],
         [u'520094592', u'Ethernet1/1/15', u'1'], [u'520094656', u'Ethernet1/1/16', u'2'],
         [u'520094720', u'Ethernet1/1/17', u'1'], [u'520094784', u'Ethernet1/1/18', u'2'],
         [u'520094848', u'Ethernet1/1/19', u'1'], [u'520094912', u'Ethernet1/1/20', u'2'],
         [u'520094976', u'Ethernet1/1/21', u'1'], [u'520095040', u'Ethernet1/1/22', u'2'],
         [u'520095104', u'Ethernet1/1/23', u'1'], [u'520095168', u'Ethernet1/1/24', u'2'],
         [u'520095232', u'Ethernet1/1/25', u'1'], [u'520095296', u'Ethernet1/1/26', u'2'],
         [u'520095360', u'Ethernet1/1/27', u'1'], [u'520095424', u'Ethernet1/1/28', u'2'],
         [u'520095488', u'Ethernet1/1/29', u'1'], [u'520095552', u'Ethernet1/1/30', u'2'],
         [u'520095616', u'Ethernet1/1/31', u'1'], [u'520095680', u'Ethernet1/1/32', u'2'],
         [u'520095744', u'Ethernet1/1/33', u'1'], [u'520159232', u'Ethernet2/1/1', u'1'],
         [u'520159296', u'Ethernet2/1/2', u'2'], [u'520159360', u'Ethernet2/1/3', u'1'],
         [u'520159424', u'Ethernet2/1/4', u'2'], [u'520159488', u'Ethernet2/1/5', u'1'],
         [u'520159552', u'Ethernet2/1/6', u'2'], [u'520159616', u'Ethernet2/1/7', u'1'],
         [u'520159680', u'Ethernet2/1/8', u'2'], [u'520159744', u'Ethernet2/1/9', u'1'],
         [u'520159808', u'Ethernet2/1/10', u'2'], [u'520159872', u'Ethernet2/1/11', u'1'],
         [u'520159936', u'Ethernet2/1/12', u'2'], [u'520160000', u'Ethernet2/1/13', u'1'],
         [u'520160064', u'Ethernet2/1/14', u'2'], [u'520160128', u'Ethernet2/1/15', u'1'],
         [u'520160192', u'Ethernet2/1/16', u'2'], [u'520160256', u'Ethernet2/1/17', u'2'],
         [u'520160320', u'Ethernet2/1/18', u'2'], [u'520160384', u'Ethernet2/1/19', u'2'],
         [u'520160448', u'Ethernet2/1/20', u'2'], [u'520160512', u'Ethernet2/1/21', u'2'],
         [u'520160576', u'Ethernet2/1/22', u'2'], [u'520160640', u'Ethernet2/1/23', u'2'],
         [u'520160704', u'Ethernet2/1/24', u'2'], [u'520160768', u'Ethernet2/1/25', u'1'],
         [u'520160832', u'Ethernet2/1/26', u'2'], [u'520160896', u'Ethernet2/1/27', u'1'],
         [u'520160960', u'Ethernet2/1/28', u'2'], [u'520161024', u'Ethernet2/1/29', u'2'],
         [u'520161088', u'Ethernet2/1/30', u'2'], [u'520161152', u'Ethernet2/1/31', u'2'],
         [u'520161216', u'Ethernet2/1/32', u'2'], [u'520161280', u'Ethernet2/1/33', u'1']],
        [[u'469775392', u'', u'3', u'', u''], [u'469775424', u'', u'3', u'', u''],
         [u'469775696', u'', u'3', u'', u''], [u'469775760', u'', u'3', u'', u''],
         [u'469776528', u'', u'3', u'', u''], [u'469776608', u'2', u'3', u'0', u''],
         [u'469776640', u'2', u'3', u'0', u''], [u'469776720', u'2', u'3', u'0', u''],
         [u'469777888', u'2', u'3', u'0', u''], [u'469777920', u'2', u'3', u'0', u''],
         [u'469778192', u'2', u'3', u'0', u''], [u'469778208', u'2', u'3', u'0', u''],
         [u'469778240', u'2', u'3', u'0', u''], [u'469778480', u'2', u'3', u'0', u''],
         [u'469778496', u'2', u'3', u'0', u''], [u'469778528', u'2', u'3', u'0', u''],
         [u'469778576', u'2', u'3', u'0', u''], [u'469778592', u'2', u'3', u'0', u''],
         [u'469778624', u'2', u'3', u'0', u''], [u'469778672', u'2', u'3', u'0', u''],
         [u'469778688', u'2', u'3', u'0', u''], [u'469778720', u'2', u'3', u'0', u''],
         [u'469778976', u'2', u'3', u'0', u''], [u'469779008', u'2', u'3', u'0', u''],
         [u'469779056', u'2', u'3', u'0', u''], [u'469779072', u'2', u'3', u'0', u''],
         [u'469779104', u'2', u'3', u'0', u''], [u'469779312', u'2', u'3', u'0', u''],
         [u'469779456', u'2', u'3', u'0', u''], [u'469779488', u'2', u'3', u'0', u''],
         [u'469779536', u'2', u'3', u'0', u''], [u'469779552', u'2', u'3', u'0', u''],
         [u'469779584', u'2', u'3', u'0', u''], [u'469780176', u'2', u'3', u'0', u''],
         [u'469780288', u'2', u'3', u'0', u''], [u'469780320', u'2', u'3', u'0', u''],
         [u'469780368', u'2', u'3', u'0', u''], [u'469780384', u'2', u'3', u'0', u''],
         [u'469780416', u'2', u'3', u'0', u''], [u'469780496', u'2', u'3', u'0', u''],
         [u'520093760', u'2', u'3', u'0', u''], [u'520093888', u'2', u'3', u'0', u''],
         [u'520094016', u'2', u'3', u'0', u''], [u'520094144', u'2', u'3', u'0', u''],
         [u'520094272', u'2', u'3', u'0', u''], [u'520094400', u'2', u'3', u'0', u''],
         [u'520094528', u'2', u'3', u'0', u''], [u'520094656', u'2', u'3', u'0', u''],
         [u'520094784', u'2', u'3', u'0', u''], [u'520094912', u'2', u'3', u'0', u''],
         [u'520095040', u'2', u'3', u'0', u''], [u'520095168', u'2', u'3', u'0', u''],
         [u'520095296', u'2', u'3', u'0', u''], [u'520095424', u'2', u'3', u'0', u''],
         [u'520095552', u'2', u'3', u'0', u''], [u'520095680', u'2', u'3', u'0', u''],
         [u'520159296', u'2', u'3', u'0', u''], [u'520159424', u'2', u'3', u'0', u''],
         [u'520159552', u'2', u'3', u'0', u''], [u'520159680', u'2', u'3', u'0', u''],
         [u'520159808', u'2', u'3', u'0', u''], [u'520159936', u'2', u'3', u'0', u''],
         [u'520160064', u'2', u'3', u'0', u''], [u'520160192', u'2', u'3', u'0', u''],
         [u'520160320', u'2', u'3', u'0', u''], [u'520160448', u'2', u'3', u'0', u''],
         [u'520160576', u'2', u'3', u'0', u''], [u'520160704', u'2', u'3', u'0', u''],
         [u'520160832', u'2', u'3', u'0', u''], [u'520160960', u'2', u'3', u'0', u''],
         [u'520161088', u'2', u'3', u'0', u''], [u'520161216', u'2', u'3', u'0', u'']]]

discovery = {'': [(None, None)]}

checks = {
    '': [(None, {}, [
        (3,
         u'Port Vethernet835: shutdown due to security violation (violation count: 0, last MAC: ) unknown enabled state',
         []),
        (3,
         u'Port Vethernet837: shutdown due to security violation (violation count: 0, last MAC: ) unknown enabled state',
         []),
        (3,
         u'Port Vethernet854: shutdown due to security violation (violation count: 0, last MAC: ) unknown enabled state',
         []),
        (3,
         u'Port Vethernet858: shutdown due to security violation (violation count: 0, last MAC: ) unknown enabled state',
         []),
        (3,
         u'Port Vethernet906: shutdown due to security violation (violation count: 0, last MAC: ) unknown enabled state',
         []),
        (2,
         u'Port Vethernet911: shutdown due to security violation (violation count: 0, last MAC: )',
         []),
        (2,
         u'Port Vethernet913: shutdown due to security violation (violation count: 0, last MAC: )',
         []),
        (2,
         u'Port Vethernet918: shutdown due to security violation (violation count: 0, last MAC: )',
         []),
        (2,
         u'Port Vethernet991: shutdown due to security violation (violation count: 0, last MAC: )',
         []),
        (2,
         u'Port Vethernet993: shutdown due to security violation (violation count: 0, last MAC: )',
         []),
        (2,
         u'Port Vethernet1010: shutdown due to security violation (violation count: 0, last MAC: )',
         []),
        (2,
         u'Port Vethernet1011: shutdown due to security violation (violation count: 0, last MAC: )',
         []),
        (2,
         u'Port Vethernet1013: shutdown due to security violation (violation count: 0, last MAC: )',
         []),
        (2,
         u'Port Vethernet1028: shutdown due to security violation (violation count: 0, last MAC: )',
         []),
        (2,
         u'Port Vethernet1029: shutdown due to security violation (violation count: 0, last MAC: )',
         []),
        (2,
         u'Port Vethernet1031: shutdown due to security violation (violation count: 0, last MAC: )',
         []),
        (2,
         u'Port Vethernet1034: shutdown due to security violation (violation count: 0, last MAC: )',
         []),
        (2,
         u'Port Vethernet1035: shutdown due to security violation (violation count: 0, last MAC: )',
         []),
        (2,
         u'Port Vethernet1037: shutdown due to security violation (violation count: 0, last MAC: )',
         []),
        (2,
         u'Port Vethernet1040: shutdown due to security violation (violation count: 0, last MAC: )',
         []),
        (2,
         u'Port Vethernet1041: shutdown due to security violation (violation count: 0, last MAC: )',
         []),
        (2,
         u'Port Vethernet1043: shutdown due to security violation (violation count: 0, last MAC: )',
         []),
        (2,
         u'Port Vethernet1059: shutdown due to security violation (violation count: 0, last MAC: )',
         []),
        (2,
         u'Port Vethernet1061: shutdown due to security violation (violation count: 0, last MAC: )',
         []),
        (2,
         u'Port Vethernet1064: shutdown due to security violation (violation count: 0, last MAC: )',
         []),
        (2,
         u'Port Vethernet1065: shutdown due to security violation (violation count: 0, last MAC: )',
         []),
        (2,
         u'Port Vethernet1067: shutdown due to security violation (violation count: 0, last MAC: )',
         []),
        (2,
         u'Port Vethernet1080: shutdown due to security violation (violation count: 0, last MAC: )',
         []),
        (2,
         u'Port Vethernet1089: shutdown due to security violation (violation count: 0, last MAC: )',
         []),
        (2,
         u'Port Vethernet1091: shutdown due to security violation (violation count: 0, last MAC: )',
         []),
        (2,
         u'Port Vethernet1094: shutdown due to security violation (violation count: 0, last MAC: )',
         []),
        (2,
         u'Port Vethernet1095: shutdown due to security violation (violation count: 0, last MAC: )',
         []),
        (2,
         u'Port Vethernet1097: shutdown due to security violation (violation count: 0, last MAC: )',
         []),
        (2,
         u'Port Vethernet1134: shutdown due to security violation (violation count: 0, last MAC: )',
         []),
        (2,
         u'Port Vethernet1141: shutdown due to security violation (violation count: 0, last MAC: )',
         []),
        (2,
         u'Port Vethernet1143: shutdown due to security violation (violation count: 0, last MAC: )',
         []),
        (2,
         u'Port Vethernet1146: shutdown due to security violation (violation count: 0, last MAC: )',
         []),
        (2,
         u'Port Vethernet1147: shutdown due to security violation (violation count: 0, last MAC: )',
         []),
        (2,
         u'Port Vethernet1149: shutdown due to security violation (violation count: 0, last MAC: )',
         []),
        (2,
         u'Port Vethernet1154: shutdown due to security violation (violation count: 0, last MAC: )',
         []),
        (2,
         u'Port Ethernet1/1/2: shutdown due to security violation (violation count: 0, last MAC: )',
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
         u'Port Ethernet1/1/14: shutdown due to security violation (violation count: 0, last MAC: )',
         []),
        (2,
         u'Port Ethernet1/1/16: shutdown due to security violation (violation count: 0, last MAC: )',
         []),
        (2,
         u'Port Ethernet1/1/18: shutdown due to security violation (violation count: 0, last MAC: )',
         []),
        (2,
         u'Port Ethernet1/1/20: shutdown due to security violation (violation count: 0, last MAC: )',
         []),
        (2,
         u'Port Ethernet1/1/22: shutdown due to security violation (violation count: 0, last MAC: )',
         []),
        (2,
         u'Port Ethernet1/1/24: shutdown due to security violation (violation count: 0, last MAC: )',
         []),
        (2,
         u'Port Ethernet1/1/26: shutdown due to security violation (violation count: 0, last MAC: )',
         []),
        (2,
         u'Port Ethernet1/1/28: shutdown due to security violation (violation count: 0, last MAC: )',
         []),
        (2,
         u'Port Ethernet1/1/30: shutdown due to security violation (violation count: 0, last MAC: )',
         []),
        (2,
         u'Port Ethernet1/1/32: shutdown due to security violation (violation count: 0, last MAC: )',
         []),
        (2,
         u'Port Ethernet2/1/2: shutdown due to security violation (violation count: 0, last MAC: )',
         []),
        (2,
         u'Port Ethernet2/1/4: shutdown due to security violation (violation count: 0, last MAC: )',
         []),
        (2,
         u'Port Ethernet2/1/6: shutdown due to security violation (violation count: 0, last MAC: )',
         []),
        (2,
         u'Port Ethernet2/1/8: shutdown due to security violation (violation count: 0, last MAC: )',
         []),
        (2,
         u'Port Ethernet2/1/10: shutdown due to security violation (violation count: 0, last MAC: )',
         []),
        (2,
         u'Port Ethernet2/1/12: shutdown due to security violation (violation count: 0, last MAC: )',
         []),
        (2,
         u'Port Ethernet2/1/14: shutdown due to security violation (violation count: 0, last MAC: )',
         []),
        (2,
         u'Port Ethernet2/1/16: shutdown due to security violation (violation count: 0, last MAC: )',
         []),
        (2,
         u'Port Ethernet2/1/18: shutdown due to security violation (violation count: 0, last MAC: )',
         []),
        (2,
         u'Port Ethernet2/1/20: shutdown due to security violation (violation count: 0, last MAC: )',
         []),
        (2,
         u'Port Ethernet2/1/22: shutdown due to security violation (violation count: 0, last MAC: )',
         []),
        (2,
         u'Port Ethernet2/1/24: shutdown due to security violation (violation count: 0, last MAC: )',
         []),
        (2,
         u'Port Ethernet2/1/26: shutdown due to security violation (violation count: 0, last MAC: )',
         []),
        (2,
         u'Port Ethernet2/1/28: shutdown due to security violation (violation count: 0, last MAC: )',
         []),
        (2,
         u'Port Ethernet2/1/30: shutdown due to security violation (violation count: 0, last MAC: )',
         []),
        (2,
         u'Port Ethernet2/1/32: shutdown due to security violation (violation count: 0, last MAC: )',
         [])
    ])]
}
