from random import randint
import time
import os,sys
import sys,string
import string

print "Welcome to Mr.Gilbert's Mad Libs Laboratory!"
name = raw_input("What is your name? ")
print "So your name is "+name+". Welcome "+name+"!"
print "We're going to make a short mad libs game."
print "Fill in the given blanks first, "+name+"!"

noun1 = raw_input("Your singular noun is..\n*")
pnoun1 = raw_input("Your plural noun is..\n*")
female = raw_input("Type in the name of a female you know\n*")
adj1 = raw_input("Your first adjective is..\n*")
adj2 = raw_input("Your second adjective is..\n*")
noun2 = raw_input("Your second singular noun is..\n*")
city = raw_input("Type in the name of any city you've been\n*")
pnoun2 = raw_input("Your second plural noun is..\n*")
adj3 = raw_input("Your third adjective is..\n*")
body = raw_input("Type in any part of the body\n*")
adj4 = raw_input("Your fourth adjective is..\n*")
place = raw_input("Type in the name of a place\n*")
body2 = raw_input("Type in any part of the body\n*")
pnoun3 = raw_input("Your plural noun is\n*")
number = raw_input("Type in any number\n*")

print "There are many %s ways to choose a/an %s to read. \nFirst, you could ask for recommendations from your friends and %s. \nJust don't ask %s. \nIf your friends and family are no help, try checking out the %s Review in The %s Times. \nIf the %s featured there are too %s for your taste, try something a litter more low-%s. \nYou could also choose a book the %s-fashioned way. \nHead to your local library or %s and browse the shelves until something catches your %s. \nWith all the time you'll save not having to search for %s, you can read %s more books!" % (adj1, noun1, pnoun1, female, noun2, city, pnoun2, adj2, body, adj3, place, body2, pnoun3, number)
