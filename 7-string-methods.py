# String Methods in Python

# Strings are immutable sequences of characters. They are used to store and manipulate text.
a = "Radha!"

print(a.upper())  # Output: RADHA!

print(a.lower())  # Output: radha!


#rstrip() method removes any leading and trailing characters (space is the default character to remove)
b = "   Radha!   "
print(b.rstrip())  # Output: "   Radha!" -> removes trailing spaces

c = "   Radha!"
print("Rstrip with '!' removed:", c.rstrip("!"))  # Output: "   Radha" -> removes trailing spaces

d = "Rad!ha!"
print(d.rstrip("!"))  # Output: "Rad!ha" -> removes trailing exclamation mark


# replace() method replaces a specified phrase with another specified phrase.
e = "Radha--Radha"
print(e.replace("Radha", "Krishna"))  # Output: Krishna--Krishna -> replaces all occurrences of "Radha" with "Krishna"


# split() method splits a string into a list items
f = "Radha Krishna"
print(f.split(" "))     # Output: ['Radha', 'Krishna']


# capitalize() method turns the first character of the string to uppercase and rest in lowercase
heading = "introduction to Python"
print(heading.capitalize())     # Output: Introduction to python

# center() method returns a centered string of a specified width
g = "Radha"
print(g.center(20))     # Output: '       Radha       ' -> centers the string within a width of 20 characters

# count() method returns the number of occurrences of a substring in the string
h = "Radha loves Radha"
print(h.count("Radha"))     # Output: 2 -> counts the number of times "Radha" appears in the string


# endswith() method returns True if the string ends with the specified suffix, otherwise returns False
i = "Radha!"
print(i.endswith("!"))          # Output: True -> checks if the string ends with "!"
print(i.endswith("h", 0, 5))    # Output: True -> checks if the substring "Radha" (from index 0 to 5) ends with "h"


# find() method returns the lowest index of the substring if it is found in the string. If it is not found, it returns -1
j = "Radha loves Krishna"
print(j.find("Radha"))          # Output: 0 -> returns the index of the first occurrence of "Radha"
print(j.find("Krishna"))        # Output: 10 -> returns the index of the first occurrence of "Krishna"
print(j.find("Python"))         # Output: -1 -> returns -1 since "Python" is not found in the string


# isalpha() method returns True if all characters in the string are alphabetic and there is at least one character, otherwise returns False
k = "Radha"
print(k.isalpha())     # Output: True -> checks if all characters in the string are alphabetic


#isalnum() method returns True if all characters in the string are alphanumeric (either alphabets or numbers) and there is at least one character, otherwise returns False
l = "Radha123"
print(l.isalnum())     # Output: True -> checks if all characters in the string are alphanumeric


# isspace() method returns True if all characters in the string are whitespace characters and there is at least one character, otherwise returns False
m = "   "
print(m.isspace())     # Output: True -> checks if all characters in the string are whitespace characters


# istitle() method returns True if the string is a titlecased string and there is at least one character, otherwise returns False
n = "Radha Loves Krishna"
print(n.istitle())     # Output: True -> checks if the string is a titlecased string


# swapcase() method returns a string where all the uppercase letters are converted to lowercase and all the lowercase letters are converted to uppercase
o = "Radha Loves Krishna"
print(o.swapcase())     # Output: rADHA lOVES kRISHNA -> converts uppercase letters to lowercase and vice versa]]]