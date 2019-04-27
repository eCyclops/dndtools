import json
import re
import sys
import mysql.connector
#from bs4 import BeautifulSoup
import glob
from pprint import pprint

arguments=sys.argv[1:]
count_args=len(arguments)
if count_args!=1:
    if count_args == 0:
        print("spell2csv needs to have a directory argument")
    elif count_args > 1:
        print("spell2csv needs to have only one directory argument")
    sys.exit(1)

print(sys.argv)

target_dir = sys.argv[1]

#print("I'm printing the target dir:")
#print(target_dir+"*.html")

listing = glob.glob(target_dir+"*.htm*")
#print("Printing the listing")
#print(listing)

for filename in listing:
 #   print(filename)
     justname=re.search('[^/]+?\.htm',filename).string
     pprint(justname)
     with open(filename, encoding='Latin1') as htmfile:
#        fulltext = ""
#        for html in htmfile:
        fulltext=htmfile.readlines() # result is a list
        html = " ".join(fulltext)
        reverse=False
        reversible=0
#            print("-----------------------------")
        print(html)
#            fulltext = fulltext+html

        nameMatch       =re.search(r'<p><font size=\"5\" color=\"#000000\"><u><b>(?P<name>.+?)</b></u></font></p>',html)
        classMatch      =re.search(r'Class\: <a href=\"(.*?)\">(?P<name>.+?)</a><br>',html)
        levelMatch      =re.search(r'Level: (?P<level>\d) <br>',html)
        schoolMatch     =re.search(r'School: (?P<school>.+?)<br>',html)
        rangeMatch      =re.search(r'Range: (?P<range>.+?)<br>',html)
        componentsMatch =re.search(r'Components: (?P<components>.+?) <br>',html)
        durationMatch   =re.search(r'Duration: (?P<duration>.+?) <br>',html)
        castTimeMatch   =re.search(r'Casting Time: (?P<castTime>.+?) <br>',html)
        areaMatch       =re.search(r'Area of Effect: (?P<area>.+?) <br>',html)
        saveMatch       =re.search(r'Saving Throw: (P?<save>.+?) <br>',html)
        descriptionMatch=re.search(r'<p><!-- Insert description under here-->.+?(?P<description>.+?)</p>',html)

        if nameMatch:
            spell_name=nameMatch.name
            reverse          =re.search(r'(?P<spell_name>.*?)- Reversible',spell_name)
            print(spell_name)
        if reverse:
            spell_name=reverse.spell_name
            reversible=1
        if classMatch:
            char_class=classMatch.name
            print(char_class)
        if levelMatch:
            level=levelMatch.level
            print(level)
        if schoolMatch:
            school=schoolMatch.school
            print(school)
        if rangeMatch:
            spell_range = rangeMatch.range
            print(spell_range)
        if componentsMatch:
            components=componentsMatch.components
            print(components)
        if durationMatch:
            duration=durationMatch.duration
            print(duration)
        if castTimeMatch:
            castTime=castTimeMatch.castTime
            print(castTime)
        if areaMatch:
            area=areaMatch.area
            print(area)
        if saveMatch:
            save=saveMatch.save
            print(save)
        if descriptionMatch:
            description=descriptionMatch.description
            description=re.sub(r'\n',' ',description)
            print(description)
        
#        print('insert into spells (class,level,name,school,range,components,duration,cast,area,save,description) values "'+'","'.join(char_class,level,spell_name,school,spell_range,components,duration,castTime,area,save,description)+'"')

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="alatariel"
)

cursor = mydb.cursor()



#insert into spells (class,level,name,school,