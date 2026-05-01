# String Slicing in Python
name = "Radhe Krishna"

# To find the length of the string
print(len(name))    # Output: 13

print(name[0:5])    # Output: Radhe         -> starts from index 0 and ends at index 4 (5-1)

print(name[:3])     # Output: Rad           -> starts from index 0 and ends at index 2 (3-1)

print(name[6:])     # Output: Krishna       -> starts from index 6 and goes till the end of the string

print(name[:])      # Output: Radhe Krishna -> starts from index 0 and goes till the end of the string

print(name[0:-4])   # Output: Radhe Krish   -> starts from index 0 and ends at index -5 (length of the string - 4 - 1) is same as print(name[0:len(name)-4])

print(name[-5:-2])
# print(name[len(name)-5 : len(name)-2])
# print(name[8:11]) # including 8 but excluding 11
# Output: ish


firstName = "Krish"
print(firstName[-4:-2]) # Output: ri