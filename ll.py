#!/bin/python3
import datetime
name=input("Your:::Name==\n")
age=int(input("Your:::Age==\n"))
d=datetime.datetime.now()

print("{} you will turn 95 by the year : {}".format(name,(95-age)+d.year))
