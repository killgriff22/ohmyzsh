import subprocess
import platform
import os
from sys import argv, stdout
from termcolor import colored
import themeloader
theme = themeloader.themeloader.gettheme("Sky")
colors = theme.colorset
my_system = platform
logo = f"""{theme.logo}"""
topline = ""
logosplt = logo.splitlines()
counter = 0
maxlinelen = 0
NN = f"Node Name: {my_system.node()}"
AR = f"Arch : {my_system.machine()}"
OSR = f"OS Release : {my_system.release()}"
CPU = f"CPU : {platform.processor()}"
SYS = f"System : {my_system.system()}"
#we need this to find the longest line (usually the node name or GPU)
infopanetmp = f"""
{CPU}
{OSR}
{AR}
{NN}
"""
bottomline = ""
#finding out what the longest line is for centering
infosplt = infopanetmp.splitlines()
for line in infosplt:
    if len(line) <= maxlinelen:
        pass
    elif len(line) > maxlinelen:
        maxlinelen = len(line)
    newtopline = ""
    topline = "_"*(maxlinelen+2)
    bottomline = "¯"*(maxlinelen+2)


def center(txt):
    center = ""
    for x in range(int(((int(len(topline))-2)-int(len(txt)))/2)):
        center += " "
    if len(txt) % 2 == 0:
        return center + txt + " " + center
    return center + txt + center


def filler():
    fill = ""
    for x in range(len(topline)-2):
        fill += " "
    return fill


def vcenter():
    center = ""
    if len(logosplt) > len(infosplt):
        buffer = int((len(logosplt)-len(infosplt))/2)
        for i in range(buffer):
            center += " "
        return center


infopane = f"""
{topline}
|{center("@Loader")}|
|{center("Version 1.0.0")}|
|{center(f"{CPU}")}|
|{center(f"{OSR}")}|
|{center(f"{AR}")}|
|{center(F"{SYS}")}|
|{center(f"{NN}")}|
|{filler()}|
{bottomline}
{vcenter()}
"""
infosplt = infopane.splitlines()
for index in range(len(logosplt)):
    #if the logo is bigger than the infopane then
    #we need to add lines to make them even
    #this may be redundant due to the "vcenter" (vertical center) 
    #in the infopane
    if len(logosplt) > len(infosplt):
        buffer = int((len(logosplt)-len(infosplt)))
        for i in range(buffer):
            infosplt.append(" ")
    try:
        print(colored(logosplt[index], colors[counter]), end="")
        print(infosplt[index])
    except Exception as err:
        print(err)
    if counter == len(colors)-1:
        counter = 0
    counter += 1
