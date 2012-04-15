#!/usr/bin/env python
import sys, time, subprocess, operator

if len(sys.argv) != 2:
    print "NEEDED: File to write statistics to"
    sys.exit()

statisticsFile = sys.argv[1]
usedApps = {}
maxIdleTime = 300.0
writeEvery = 300
updateEvery = 1

def loadStatistics():
    f = open(statisticsFile, 'r')
    dic = {}
    for line in f:
        split = line.rstrip().partition(":")
        if split[0] != "":
            key = split[0] + "\n"
        else:
            key = split[0]
        dic[key] = int(split[2].rstrip())
    f.close()
    return dic

def writeStatistics():
    sort = sorted(usedApps.iteritems(), key=operator.itemgetter(1), reverse=True)
    f = open(statisticsFile, 'w')
    for i, j in sort:
        if i.endswith("\n"):
            i = i[:-1]
        f.write(i + ":" + str(j) + "\n")
    f.close()

i = 0
usedApps = loadStatistics()

while True:
    activeAppCMD = """arch -i386 osascript \
            -e 'tell application "System Events"' \
            -e 'set app_name to name of the first process whose frontmost is true' \
            -e 'end tell' """

    idleTimeCMD = """ioreg -c IOHIDSystem | perl -ane 'if (/Idle/) {$idle=(pop @F)/1000000000; print $idle,"\n"; last}'"""

    idleTime = float(subprocess.Popen(idleTimeCMD, shell=True, stdout=subprocess.PIPE).stdout.read())
    if idleTime < maxIdleTime:
        activeApp = str(subprocess.Popen(activeAppCMD, shell=True, stdout=subprocess.PIPE).stdout.read())
        if activeApp not in usedApps:
            usedApps[activeApp] = 0
        usedApps[activeApp] += updateEvery

    i+=1
    time.sleep(updateEvery)
    if i % writeEvery == 0:
        writeStatistics()
