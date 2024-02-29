# Python RegEx​
# 1
import re
txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
if x:
  print("YES! We have a match!")
else:
  print("No match")
# output:
# YES! We have a match!

# 2
import re
txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)
# output:
# ['ai', 'ai']

# 3
import re
txt = "The rain in Spain"
x = re.findall("Portugal", txt)
print(x)
if (x):
  print("Yes, there is at least one match!")
else:
  print("No match")
# output:
# []
# No match

# 4
import re
txt = "The rain in Spain"
x = re.search("\s", txt)
print("The first white-space character is located in position:", x.start()) 
# output:
# The first white-space character
# is located in position: 3

# 5
import re

txt = "The rain in Spain"
x = re.search("Portugal", txt)
print(x)

# output:
# None

# 6
import re
txt = "The rain in Spain"
x = re.split("\s", txt)
print(x)
# output:
# ['The', 'rain', 'in', 'Spain']

# 7
import re
txt = "The rain in Spain"
x = re.split("\s", txt, 1)
print(x)
# output:
# ['The', 'rain in Spain']

# 8
import re
txt = "The rain in Spain"
x = re.sub("\s", "9", txt)
print(x)
# output:
# The9rain9in9Spain

# 9
import re
txt = "The rain in Spain"
x = re.sub("\s", "9", txt, 2)
print(x)
# output:
# The9rain9in Spain

# 10
import re
txt = "The rain in Spain"
x = re.search("ai", txt)
print(x)
# output:
# <_sre.SRE_Match object; span=(5, 7), match='ai'>

# 11
import re
txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.span())
# output:
# (12, 17)

# 12
import re
txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.string)
# output:
# The rain in Spain

# 13
import re
txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.group())
# output:
# Spain




# Metacharacters​
# 1
import re
txt = "The rain in Spain"
x = re.findall("[a-m]", txt)
print(x)
# output:
# ['h', 'e', 'a', 'i', 'i', 'a', 'i']

# 2
import re
txt = "That will be 59 dollars"
x = re.findall("\d", txt)
print(x)
# output:
# ['5', '9']

# 3
import re
txt = "hello planet"
x = re.findall("he..o", txt)
print(x)
# output:
# ['hello']

# 4
import re
txt = "hello planet"
x = re.findall("^hello", txt)
if x:
  print("Yes, the string starts with 'hello'")
else:
  print("No match")
  # output:
# Yes, the string starts with 'hello'

# 5
import re
txt = "hello planet"
x = re.findall("planet$", txt)
if x:
  print("Yes, the string ends with 'planet'")
else:
  print("No match")
  # output:
# Yes, the string ends with 'planet'

# 6
import re
txt = "hello planet"
x = re.findall("he.*o", txt)
print(x)
# output:
# ['hello']

# 7
import re
txt = "hello planet"
x = re.findall("he.+o", txt)
print(x)
# output:
# ['hello']

# 8
import re
txt = "hello planet"
x = re.findall("he.?o", txt)
print(x)
# output:
# []

# 9
import re
txt = "hello planet"
x = re.findall("he.{2}o", txt)
print(x)
# output:
# ['hello']

# 10
import re
txt = "The rain in Spain falls mainly in the plain!"
x = re.findall("falls|stays", txt)
print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
['falls']
# output:
# Yes, there is at least one match!




# Special Sequences​
# 1
import re
txt = "The rain in Spain"
x = re.findall("\AThe", txt)
print(x)
if x:
  print("Yes, there is a match!")
else:
  print("No match")
['The']
# output:
# Yes, there is a match!

# 2
import re
txt = "The rain in Spain"
x = re.findall(r"\bain", txt)
print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
  # output:
# []
# No match

# 3
import re
txt = "The rain in Spain"
x = re.findall(r"ain\b", txt)
print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
  # output:
# ['ain', 'ain']
# Yes, there is at least one match!

# 4
import re
txt = "The rain in Spain"
x = re.findall(r"\Bain", txt)
print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
  # output:
# ['ain', 'ain']
# Yes, there is at least one match!

# 5
import re
txt = "The rain in Spain"
x = re.findall("\D", txt)
print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
  # output:
# ['T', 'h', 'e', ' ', 'r', 'a', 'i', 'n', ' ', 'i', 'n', ' ', 'S', 'p', 'a', 'i', 'n']
# Yes, there is at least one match!

# 6
import re
txt = "The rain in Spain"
x = re.findall("\s", txt)
print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
  # output:
  # [' ', ' ', ' ']
# Yes, there is at least one match!

# 7
import re
txt = "The rain in Spain"
x = re.findall("\S", txt)
print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
  # output:
# ['T', 'h', 'e', 'r', 'a', 'i', 'n', 'i', 'n', 'S', 'p', 'a', 'i', 'n']
# Yes, there is at least one match!

# 8
import re
txt = "The rain in Spain"
x = re.findall("\w", txt)
print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
# output:
# ['T', 'h', 'e', 'r', 'a', 'i', 'n', 'i', 'n', 'S', 'p', 'a', 'i', 'n']
# Yes, there is at least one match!

# 9
import re
txt = "The rain in Spain"
x = re.findall("\W", txt)
print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
  # output:  
  # [' ', ' ', ' ']
# Yes, there is at least one match!

# 10
import re
txt = "The rain in Spain"
x = re.findall("Spain\Z", txt)
print(x)
if x:
  print("Yes, there is a match!")
else:
  print("No match")
  # output:
  # ['Spain']
# Yes, there is a match!




# Compile function​