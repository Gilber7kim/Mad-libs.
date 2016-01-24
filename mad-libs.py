from random import randint
import time
import os
import sys
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

print "There are many %s ways to choose a/an %s to read." % (adj1, noun1)
print "First, you could ask for recommendations from your %s." % (pnoun1)
print "Just don't ask %s." % (female)
print "If your friends and family are no help,"
print "try checking out the %s Review in The %s Times." % (noun2, city)
print "If the %s featured there are too %s for your taste," % (pnoun2, adj2)
print "try something a little more low-%s." % (body)
print "You could also choose a book the %s-fashioned way." % (adj3)
print "Head to your local library or %s and" % (place)
print "browse the shelves until something catches your %s." % (body2)
print "With all the time you'll save not having to search for %s," % (pnoun3)
print "you can read %s more books!" % (number)
