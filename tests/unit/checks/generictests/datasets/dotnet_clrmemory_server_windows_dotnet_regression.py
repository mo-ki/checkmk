#!/usr/bin/env python3
# Copyright (C) 2019 tribe29 GmbH - License: GNU General Public License v2
# This file is part of Checkmk (https://checkmk.com). It is subject to the terms and
# conditions defined in the file COPYING, which is part of this source code package.

# yapf: disable
# type: ignore

checkname = 'dotnet_clrmemory'

info = [
    [
        u'AllocatedBytesPersec', u'Caption', u'Description', u'FinalizationSurvivors',
        u'Frequency_Object', u'Frequency_PerfTime', u'Frequency_Sys100NS', u'Gen0heapsize',
        u'Gen0PromotedBytesPerSec', u'Gen1heapsize', u'Gen1PromotedBytesPerSec', u'Gen2heapsize',
        u'LargeObjectHeapsize', u'Name', u'NumberBytesinallHeaps', u'NumberGCHandles',
        u'NumberGen0Collections', u'NumberGen1Collections', u'NumberGen2Collections',
        u'NumberInducedGC', u'NumberofPinnedObjects', u'NumberofSinkBlocksinuse',
        u'NumberTotalcommittedBytes', u'NumberTotalreservedBytes', u'PercentTimeinGC',
        u'PercentTimeinGC_Base', u'ProcessID', u'PromotedFinalizationMemoryfromGen0',
        u'PromotedMemoryfromGen0', u'PromotedMemoryfromGen1', u'Timestamp_Object',
        u'Timestamp_PerfTime', u'Timestamp_Sys100NS'
    ],
    [
        u'21380464834160', u'', u'', u'13821', u'0', u'14318180', u'10000000', u'2012417216',
        u'4762504', u'28497416', u'718488', u'257543384', u'239855984', u'_Global_', u'525896784',
        u'45499', u'894395', u'717878', u'531223', u'68441', u'2517', u'3222', u'2800212096',
        u'64290166912', u'78964360', u'-1', u'0', u'491512', u'4762504', u'718488', u'0',
        u'57866201615573', u'131407819020030000'
    ],
    [
        u'1034323144', u'', u'', u'421', u'0', u'14318180', u'10000000', u'13107200', u'0',
        u'1041864', u'0', u'12959776', u'8008032', u'powershell', u'22009672', u'3195', u'64', u'6',
        u'4', u'0', u'3', u'15', u'35868672', u'402644992', u'70028', u'863531387', u'3460', u'0',
        u'0', u'0', u'0', u'57866201615573', u'131407819020030000'
    ],
    [
        u'1256169848', u'', u'', u'403', u'0', u'14318180', u'10000000', u'13107200', u'0',
        u'845368', u'0', u'4340904', u'8393528', u'msftefd', u'13579800', u'1108', u'84', u'8',
        u'2', u'0', u'180', u'555', u'27209728', u'402644992', u'205', u'18132123', u'4964', u'0',
        u'0', u'0', u'0', u'57866201615573', u'131407819020030000'
    ],
    [
        u'40643607208', u'', u'', u'1176', u'0', u'14318180', u'10000000', u'171793984', u'1121296',
        u'1121488', u'1008', u'8512416', u'6165288', u'w3wp', u'15799192', u'1267', u'339', u'121',
        u'7', u'0', u'214', u'47', u'188348800', u'5368707456', u'6451', u'453642218', u'8544',
        u'40072', u'1121296', u'1008', u'0', u'57866201615573', u'131407819020030000'
    ],
    [
        u'28505439528', u'', u'', u'35', u'0', u'14318180', u'10000000', u'171793984', u'35560',
        u'6990272', u'0', u'82755208', u'2618360', u'w3wp#1', u'92363840', u'18005', u'209', u'3',
        u'2', u'0', u'0', u'233', u'370588032', u'5368707456', u'60', u'1098595346', u'5876',
        u'1120', u'35560', u'0', u'0', u'57866201615573', u'131407819020030000'
    ],
    [
        u'25377880160', u'', u'', u'610', u'0', u'14318180', u'10000000', u'6291456', u'188752',
        u'258032', u'0', u'12625184', u'8503648', u'SMEX_Master', u'21386864', u'2203', u'3922',
        u'759', u'42', u'0', u'10', u'79', u'27574272', u'402644992', u'348', u'26884726', u'4528',
        u'23800', u'188752', u'0', u'0', u'57866201615573', u'131407819020030000'
    ],
    [
        u'242127874192', u'', u'', u'1790', u'0', u'14318180', u'10000000', u'13107200', u'176160',
        u'360056', u'0', u'7061152', u'8857864', u'Microsoft.Exchange.Search.ExSearch', u'16279072',
        u'712', u'15616', u'7903', u'7532', u'0', u'174', u'51', u'33181696', u'402644992',
        u'115984', u'-343301640', u'4368', u'72240', u'176160', u'0', u'0', u'57866201615573',
        u'131407819020030000'
    ],
    [
        u'26405401888', u'', u'', u'62', u'0', u'14318180', u'10000000', u'13107200', u'123944',
        u'429784', u'0', u'3762392', u'640968', u'MSExchangeMailSubmission', u'4833144', u'656',
        u'2017', u'281', u'2', u'0', u'0', u'27', u'17838080', u'402644992', u'114', u'108452653',
        u'4256', u'1984', u'123944', u'0', u'0', u'57866201615573', u'131407819020030000'
    ],
    [
        u'41811669280', u'', u'', u'1417', u'0', u'14318180', u'10000000', u'171793984', u'106168',
        u'683872', u'0', u'4183576', u'532344', u'MSExchangeMailboxReplication', u'5399792', u'869',
        u'288', u'34', u'2', u'0', u'166', u'21', u'181623168', u'5368707456', u'374', u'825963764',
        u'4104', u'45336', u'106168', u'0', u'0', u'57866201615573', u'131407819020030000'
    ],
    [
        u'16261510680', u'', u'', u'0', u'0', u'14318180', u'10000000', u'13107200', u'808',
        u'67560', u'0', u'3716080', u'522704', u'MSExchangeMailboxAssistants', u'4306344', u'814',
        u'1243', u'31', u'1', u'0', u'1', u'16', u'17440768', u'402644992', u'41', u'183435328',
        u'4016', u'0', u'808', u'0', u'0', u'57866201615573', u'131407819020030000'
    ],
    [
        u'69115401592', u'', u'', u'0', u'0', u'14318180', u'10000000', u'6291456', u'336', u'4600',
        u'0', u'8067032', u'451712', u'MsExchangeFDS', u'8523344', u'540', u'10984', u'717', u'107',
        u'0', u'0', u'21', u'14839808', u'402644992', u'32', u'94034864', u'3908', u'0', u'336',
        u'0', u'0', u'57866201615573', u'131407819020030000'
    ],
    [
        u'50738223656', u'', u'', u'18', u'0', u'14318180', u'10000000', u'171793984', u'952',
        u'1538344', u'0', u'916448', u'324520', u'Microsoft.Exchange.EdgeSyncSvc', u'2779312',
        u'570', u'67317', u'67317', u'67317', u'67317', u'113', u'16', u'20654464', u'5368707456',
        u'102139', u'859523133', u'3752', u'576', u'952', u'0', u'0', u'57866201615573',
        u'131407819020030000'
    ],
    [
        u'14840512232', u'', u'', u'0', u'0', u'14318180', u'10000000', u'6291456', u'1264',
        u'3472', u'0', u'434048', u'228696', u'Microsoft.Exchange.AntispamUpdateSvc', u'666216',
        u'192', u'2358', u'366', u'23', u'0', u'0', u'10', u'6979584', u'402644992', u'16',
        u'95780910', u'3608', u'0', u'1264', u'0', u'0', u'57866201615573', u'131407819020030000'
    ],
    [
        u'19123272552', u'', u'', u'1038', u'0', u'14318180', u'10000000', u'171793984', u'38232',
        u'215688', u'0', u'3460464', u'193120', u'Microsoft.Exchange.AddressBook.Service',
        u'3869272', u'546', u'144', u'13', u'1', u'0', u'1', u'20', u'175999360', u'5368707456',
        u'177', u'1770804486', u'3284', u'33216', u'38232', u'0', u'0', u'57866201615573',
        u'131407819020030000'
    ],
    [
        u'3058406333280', u'', u'', u'112', u'0', u'14318180', u'10000000', u'13107200', u'0',
        u'7931664', u'0', u'15869384', u'5833944', u'MonitoringHost', u'29634992', u'1652',
        u'70407', u'27993', u'7758', u'1123', u'27', u'1177', u'156405760', u'402644992', u'175835',
        u'19646043', u'3060', u'0', u'0', u'0', u'0', u'57866201615573', u'131407819020030000'
    ],
    [
        u'447738985968', u'', u'', u'476', u'0', u'14318180', u'10000000', u'6291456', u'189240',
        u'191400', u'0', u'9368552', u'2119120', u'SMEX_SystemWatcher', u'11679072', u'2446',
        u'71158', u'21943', u'702', u'0', u'227', u'32', u'18190336', u'402644992', u'29427',
        u'864749559', u'3032', u'17372', u'189240', u'0', u'0', u'57866201615573',
        u'131407819020030000'
    ],
    [
        u'1582966894800', u'', u'', u'1755', u'0', u'14318180', u'10000000', u'171793984',
        u'845672', u'845864', u'184000', u'43915832', u'169687952', u'EdgeTransport', u'214449648',
        u'4137', u'16809', u'4630', u'1327', u'0', u'196', u'207', u'389077376', u'5368707456',
        u'615369', u'1836658321', u'2496', u'85264', u'845672', u'184000', u'0', u'57866201615573',
        u'131407819020030000'
    ],
    [
        u'248414065112', u'', u'', u'753', u'0', u'14318180', u'10000000', u'171793984', u'371528',
        u'371720', u'43384', u'13277960', u'7617504', u'MSExchangeTransportLogSearch', u'21267184',
        u'800', u'4038', u'1846', u'40', u'0', u'5', u'423', u'199731584', u'5368707456', u'92',
        u'33635996', u'2316', u'48192', u'371528', u'43384', u'0', u'57866201615573',
        u'131407819020030000'
    ],
    [
        u'14165996376', u'', u'', u'0', u'0', u'14318180', u'10000000', u'6291456', u'0',
        u'2565672', u'0', u'24', u'447256', u'MSExchangeTransport', u'3012952', u'480', u'2252',
        u'1011', u'23', u'1', u'169', u'12', u'15548416', u'402644992', u'235', u'100491032',
        u'2180', u'0', u'0', u'0', u'0', u'57866201615573', u'131407819020030000'
    ],
    [
        u'13976651744', u'', u'', u'0', u'0', u'14318180', u'10000000', u'171793984', u'520',
        u'1512', u'0', u'1452120', u'176968', u'MSExchangeThrottling', u'1630600', u'455', u'91',
        u'14', u'2', u'0', u'153', u'11', u'174422400', u'5368707456', u'181', u'-1825012662',
        u'2080', u'0', u'520', u'0', u'0', u'57866201615573', u'131407819020030000'
    ],
    [
        u'16394760256', u'', u'', u'578', u'0', u'14318180', u'10000000', u'171793984', u'24752',
        u'24944', u'489160', u'4562400', u'430120', u'Microsoft.Exchange.ServiceHost', u'5017464',
        u'984', u'175', u'6', u'1', u'0', u'170', u'101', u'182364544', u'5368707456', u'163',
        u'1419991972', u'1736', u'18748', u'24752', u'489160', u'0', u'57866201615573',
        u'131407819020030000'
    ],
    [
        u'37340719640', u'', u'', u'3176', u'0', u'14318180', u'10000000', u'171793984', u'1529360',
        u'1533104', u'800', u'8676480', u'560512', u'Microsoft.Exchange.RpcClientAccess.Service',
        u'10770096', u'1443', u'355', u'142', u'9', u'0', u'12', u'30', u'182610304', u'5368707456',
        u'427', u'402649328', u'2008', u'103568', u'1529360', u'800', u'0', u'57866201615573',
        u'131407819020030000'
    ],
    [
        u'4650095823504', u'', u'', u'1', u'0', u'14318180', u'10000000', u'6291456', u'6520',
        u'6544', u'136', u'5109608', u'6476080', u'msexchangerepl', u'11592232', u'1055', u'619841',
        u'582310', u'446273', u'0', u'223', u'94', u'25055232', u'402644992', u'207579', u'480900',
        u'1952', u'24', u'6520', u'136', u'0', u'57866201615573', u'131407819020030000'
    ],
    [
        u'14598452632', u'', u'', u'0', u'0', u'14318180', u'10000000', u'171793984', u'864',
        u'39448', u'0', u'2516320', u'439232', u'Microsoft.Exchange.ProtectedServiceHost',
        u'2995000', u'464', u'93', u'1', u'0', u'0', u'153', u'11', u'328391040', u'5368707456',
        u'28', u'-1876029354', u'1848', u'0', u'864', u'0', u'0', u'57866201615573',
        u'131407819020030000'
    ],
    [
        u'28892447808', u'', u'', u'0', u'0', u'14318180', u'10000000', u'6291456', u'576',
        u'1425144', u'0', u'24', u'626512', u'Microsoft.Exchange.Monitoring', u'2051680', u'906',
        u'4591', u'423', u'46', u'0', u'320', u'13', u'10268672', u'402644992', u'252', u'49256366',
        u'1740', u'0', u'576', u'0', u'0', u'57866201615573', u'131407819020030000'
    ]
]

discovery = {'': [(u'_Global_', 'dotnet_clrmemory_defaultlevels')]}

checks = {
    '': [
        (u'_Global_', {"upper": (10.0, 15.0)}, [
            (0, 'Time in GC: 1.84%', [
                ('percent', 1.8385322768796544, 10.0, 15.0, 0, 100),
            ]),
        ]),
    ],
}
