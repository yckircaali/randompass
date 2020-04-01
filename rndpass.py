import sys
from random import *

character = "abcdefghijklmnoprstuvyzwxABCDEFGHIJKLMNOPQRSTUVWXYZ"
number = "0123456789"
custom = "' !#@.,$-_:;"

answer = input ("Is there a number in the password? [Y / N]")
if answer in ('y','Y'):
    print("Number added.")
elif answer in ('n','N'):
    print("No numbers added.")

answer2 = input ("Is there a letter in the password? [Y / N]")
if answer2 in ('y','Y'):
    print("Letter added.")
elif answer2 in ('n','N'):
    print("No letters added.")

answer3 = input ("Is there any special character in the password? [Y / N]")
if answer3 in ('y','Y'):
    print("Special character added.")
elif answer3 in ('n','N'):
    print("No special characters added.")

if answer in ('y','Y') and answer2 in ('y','Y') and answer3 in ('y','Y'):
    all = number + character + custom
if answer in ('y','Y') and answer2 in ('y','Y') and answer3 in ('n','N'):
    all = number + character
if answer in ('y','Y') and answer2 in ('n','N') and answer3 in ('y','Y'):
    all = number + custom
if answer in ('y','Y') and answer2 in ('n','N') and answer3 in ('n','N'):
    all = number
if answer in ('n','N') and answer2 in ('y','Y') and answer3 in ('y','Y'):
    all = character + custom
if answer in ('n','N') and answer2 in ('y','Y') and answer3 in ('n','N'):
    all = character
if answer in ('n','N') and answer2 in ('n','N') and answer3 in ('y','Y'):
    all = custom
if answer in ('n','N') and answer2 in ('n','N') and answer3 in ('n','N'):
    print ("Please select an entry.")
    sys.exit ()
min = int (input ("Min:"))
max = int (input ("Max:"))
password = "". join (choice (all) for x in range (randint (min, max)))
print ("Your password =", password)
