import sys
from random import *

character = "abcdefghijklmnoprstuvyzwxABCDEFGHIJKLMNOPQRSTUVWXYZ"
number = "0123456789"
custom = "'! # @., $"

answer = input ("Is there a number in the password? [Y / N]")
if answer == "Y":
    print("Number added.")
elif answer == "N":
    print("No numbers added.")

answer2 = input ("Is there a letter in the password? [Y / N]")
if answer2 == "Y":
    print("Letter added.")
elif answer2 == "N":
    print("No letters added.")

answer3 = input ("Is there any special character in the password? [Y / N]")
if answer3 == "Y":
    print("Special character added.")
elif answer3 == "N":
    print("No special characters added.")

if answer == "Y" and answer2 == "Y" and answer3 == "Y":
    all = number + character + custom
if answer == "Y" and answer2 == "Y" and answer3 == "N":
    all = number + character
if answer == "Y" and answer2 == "N" and answer3 == "Y":
    all = number + custom
if answer == "Y" and answer2 == "N" and answer3 == "N":
    all = number
if answer == "N" and answer2 == "Y" and answer3 == "Y":
    all = character + custom
if answer == "N" and answer2 == "Y" and answer3 == "N":
    all = character
if answer == "N" and answer2 == "N" and answer3 == "Y":
    all = custom
if answer == "N" and answer2 == "N" and answer3 == "N":
    print ("Please select an entry.")
    sys.exit ()
min = int (input ("Min:"))
max = int (input ("Max:"))
password = "". join (choice (all) for x in range (randint (min, max)))
print ("Your password =", password)
