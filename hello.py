# get name
name = input("What's your name? ")

# s1 = input
# s2 = input
# name = input

# print(s1+name+s2)

# Return a copy of the string with leading and trailing whitespace removed
strip = name.strip()
# clean_name = name.rstrip()
# clean_name = name.lstrip()
# trim

#  Make the first character have upper case and the rest lower case.
capitalize = strip.capitalize()

# words start with uppercased characters and all remaining cased characters have lower case
title = strip.title()

# print out to console
print('Hello,', name)
print('Hello,', strip)
print('Hello,', capitalize)
print('Hello,', title)
