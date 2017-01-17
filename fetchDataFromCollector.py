#!/usr/bin/env python

import os, sys
from datetime import date, datetime, timedelta
import csv, threading, logging, operator, rrdtool, syslog, time, zipfile, math
import Globals, sys
from Products.ZenUtils.ZenScriptBase import ZenScriptBase

# Variables for the whole script
report_for = "Ent"
start_time = time.time()
logging.basicConfig(level=logging.DEBUG)

cwd = "/opt/report/test"
collectors = ['sjdc-1', 'udc2-1', 'sjc1-1', 'iad1-1', 'muc1-1', 'fra1-1', 'localhost', 'sjc1-1300', 'sjc1-2', 'sjc1-3', 'sjdc-2']


def rsync_rrds(collector):
    syslog.syslog("Starting rsync proc on %s."%collector)
    logging.info("Starting rsync proc on %s."%collector)
    mkdir_cmd = "mkdir -p %s/data/%s/Devices"%(cwd, collector)
    cmd = "rsync -av zenoss@%s:/opt/zenoss/perf/Devices/* %s/data/%s/Devices"%(collector, cwd, collector)
    (dummy, stdout_and_stderr) = os.popen4(mkdir_cmd)
    (dummy, stdout_and_stderr) = os.popen4(cmd)
    result = stdout_and_stderr.read()

    syslog.syslog("Done rsync proc on %s..."%collector)
    logging.info("Done rsync proc on %s..."%collector)

    return 

# Sync RRD files
syslog.syslog("Starting rsync threads.")
logging.info("Starting rsync threads.")
threads = []

for collector in collectors:
    t = threading.Thread(target=rsync_rrds, args=(collector,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

syslog.syslog("Done rsync'ing rrd files")
logging.info("Done rsync'ing rrd files")

runtime = int(time.time() - start_time)

syslog.syslog("Done fetching data after %s seconds"%runtime)
logging.info("Done fetching data after %s seconds"%runtime)

