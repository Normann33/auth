#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import socket
import traceback

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
red = bcolors.FAIL + bcolors.BOLD
green = bcolors.OKGREEN + bcolors.BOLD
blue = bcolors.OKBLUE

res = socket.gethostbyaddr

try:
    user = sys.argv[1]
except:
    print("Usage: auth.py [username] or ALL for all users]")
    exit()

def resolve(x):
    try:
        host = res(x)
        return host[0]
    except:
        return x


print("*"*100)
print ("\t" +red +user +bcolors.ENDC)
print("*"*100)
with open ('/var/log/auth', 'r', encoding='latin-1') as f:
    try:
        for line in f:
            if user in line and user != "ALL" and "cmd=" in line:
                line = line.split()
                cmd = [s for s in line if "cmd=" in s]
                x = line.index(cmd[0])
                print (line[0], line[1], line[2], green +resolve(line[5]) +bcolors.ENDC, blue +(' '.join(line[x:][:-1])).replace("cmd=", "") +bcolors.ENDC)
            elif user == "ALL" and "cmd=" in line:
                line = line.split()
                cmd = [s for s in line if "cmd=" in s]
                x = line.index(cmd[0])
                print(line[0], line[1], line[2], green +resolve(line[5]) +bcolors.ENDC, red +line[6], blue +(' '.join(line[x:][:-1])).replace("cmd=", "") +bcolors.ENDC)
    except Exception:
       traceback.print_exc()
