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
