#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 20:29:11 2019

@author: jdwood
"""

import sys
#import mysql.connector
#from bs4 import BeautifulSoup
import glob
#import yaml
from pprint import pprint

class isHTMLfile(object):
    @staticmethod
    def check(filename):
        if filename[-4:]==".htm":
            return True
        if filename[-5:]==".html":
            return True
        return False

arguments=sys.argv[1:]
count_args=len(arguments)
if count_args == 0:
    print("spell2csv needs to have a directory argument")
    sys.exit(1)

for argument in arguments:
    if os.path.isfile(argument) and isHTMLfile(argument)

target_dir = sys.argv[1]

print("I'm printing the target dir:")
print(target_dir+"*.html")

listing = glob.glob(target_dir+"*.htm")
for filename in listing:
    with open(filename, encoding='Latin1') as htmfile:
        print(filename)
#        spellFile = yaml.load(htmfile,Loader=yaml.FullLoader)
        fullFile = htmfile.readlines()
        pprint(fullFile)
        
#        print(dir(spellFile))