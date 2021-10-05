# -*- coding: utf-8 -*-
"""
Created on Tue Aug 17 15:38:11 2021

@author: FranJa
"""
# re.search() retuns a True/False depending on wheter the string matches tehe regular expression

"""

https://docs.python.org/3/howto/regex.html

Python Regular Expression Quick Guide

^        Matches the beginning of a line
$        Matches the end of the line
.        Matches any character
\s       Matches whitespace
\S       Matches any non-whitespace character
*        Repeats a character zero or more times
*?       Repeats a character zero or more times 
         (non-greedy)
+        Repeats a character one or more times
+?       Repeats a character one or more times 
         (non-greedy)
[aeiou]  Matches a single character in the listed set
[^XYZ]   Matches a single character not in the listed set
[a-z0-9] The set of characters can include a range
(        Indicates where string extraction is to start
)        Indicates where string extraction is to end

"""

# If we actually want the matching strings to be extracted, we use re.findall()

# [0-9]+ One or more digits between 0-9

import re
my_string = "My 2 favorite numbers are 19 and 42"
result = re.findall("[1-9]+", my_string)

result = re.findall("[AEIOU]+", my_string)

# Greedy matching
# ^F Start with "F"
# . Any character
my_string = "From: Using the: Character"
greedy = re.findall("^F.+:", my_string)

# Non greedy matching
non_greedy = re.findall("^F.+?:", my_string)

# Fine-Tuning string extraction
# \S+ one or more non-whitespace character
my_string = "From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16"
fine_tuning_1 = re.findall("\S+@\S+", my_string)
fine_tuning_2 = re.findall("^From (\S+@\S+)", my_string)
fine_tuning_3 = re.findall("\S+?@\S+", my_string)

data = "From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008"
at_pos = data.find("@")

sp_pos = data.find(" ", at_pos)

host = data[at_pos+1 : sp_pos]

# Double Split Pattern

words = data.split()
email = words[1]
pieces = email.split("@")
print(pieces[1])

# Regular Expression version
# Look through the data until you find an at sign
# [] Match non-blank character
# * Match many of them
# ^x Everything but x

user_1 = re.findall("@([^ ]*)", data)

user_2 = re.findall("^From .*@([^ ]*)", data)

# Spam Confidence
file_handler = open("mbox-short.txt")
num_list = list()
for line in file_handler:
    line = line.rstrip()
    stuff = re.findall("X-DSPAM-Confidence: ([0-9.]+)", line)
    if len(stuff) != 1: 
        continue
    num = float(stuff[0])
    num_list.append(num)

print("Maximum:",max(num_list))

# \$ backslash to match any regular expression character:
my_string = "We just received $10.00 for cookies."
result = re.findall("\$[0-9.]+",my_string)


