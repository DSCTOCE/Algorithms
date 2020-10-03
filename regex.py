# Importing libraries
import re

# matching AV in the given sentence
result = re.match(r'AV', 'AV Analytics Vidhya AV')
print ('\n',result)

# The output shows that pattern match has been found. To print the matching string we’ll use method group (It helps to return the matching string). Use “r” at the start of the pattern string, it designates a python raw string.

# printing the matching string
result = re.match(r'AV', 'AV Analytics Vidhya AV')
print ('\nMatching string :',result.group(0))

# Let’s now find ‘Analytics’ in the given string. Here we see that string is not starting with ‘AV’ so it should return no match. Let’s see what we get:

# matching Analytics in the given sentence
result = re.match(r'Analytics', 'AV Analytics Vidhya AV')
print ('\nResult :', result)

# There are methods like start() and end() to know the start and end position of matching pattern in the string.
result = re.match(r'AV', 'AV Analytics Vidhya AV')
print ('\nStarting position of the match :',result.start())
print ('Ending position of the match :',result.end())
