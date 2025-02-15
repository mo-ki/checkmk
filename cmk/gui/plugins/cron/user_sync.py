#!/usr/bin/env python3
# Copyright (C) 2019 tribe29 GmbH - License: GNU General Public License v2
# This file is part of Checkmk (https://checkmk.com). It is subject to the terms and
# conditions defined in the file COPYING, which is part of this source code package.

import cmk.gui.userdb as userdb
from cmk.gui.cron import register_job

register_job(userdb.execute_userdb_job)
register_job(userdb.execute_user_profile_cleanup_job)
