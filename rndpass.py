import sys
from random import *

character = "abcdefghijklmnoprstuvyzwxABCDEFGHIJKLMNOPQRSTUVWXYZ"
number = "0123456789"
custom = "'! # @., $"

answer = input ("Is there a number in the password? [Y / N]")
if answer == "E":
    print ("Number added.")
elif answer == "H":
    print ("No numbers added.")

answer2 = input ("Is there a letter in the password? [Y / N]")
if answer2 == "E":
    print ("Letter added.")
elif answer2 == "H":
    print ("No letters added.")

answer3 = input ("Is there any special character in the password? [E / H]")
if answer3 == "E":
    print ("Special character added.")
elif answer3 == "H":
    print ("No special characters added.")

if answer == "E" and answer2 == "E" and answer3 == "E":
    all = number + character + special
if answer == "E" and answer2 == "E" and answer3 == "H":
    all = number + character
if answer == "E" and answer2 == "H" and answer3 == "E":
    all = number + special
if answer == "E" and answer2 == "H" and answer3 == "H":
    all = number
if answer == "H" and answer2 == "E" and answer3 == "E":
    all = character + special
if answer == "H" and answer2 == "E" and answer3 == "H":
    all = character
if answer == "H" and answer2 == "H" and answer3 == "E":
    all = special
if answer == "H" and answer2 == "H" and answer3 == "H":
    print ("Please select an entry.")
    sys.exit ()
min = int (input ("Min:"))
max = int (input ("Max:"))
password = "". join (choice (all) for x in range (randint (min, max)))
print ("Your password =", password)
