#python intro
print("Hello, World!")  #output:Hello,world!



#python syndax
if 5 > 2:
  print("Five is greater than two!") 
#output: Five is greater than two!

if 5 > 2:
 print("Five is greater than two!") 
if 5 > 2:
        print("Five is greater than two!") 
#output: 
#Five is greater than two!
#Five is greater than two!

x = 5
y = "Hello, World!"
#output: 
# 5
# Hello, World!

#This is a comment.
print("Hello, World!")
#Hello, World!



#Python Comments
#This is a comment
print("Hello, World!")
#output: Hello, World!

print("Hello, World!") #This is a comment
#output: Hello, World!

#print("Hello, World!")
print("Cheers, Mate!")
#output: Hello, World!
#output: Cheers, Mate!

#This is a comment
#written in
#more than just one line
print("Hello, World!")
#output:Hello, World!

"""
This is a comment
written in
more than just one line
"""
print("Hello, World!")
#output:Hello, World!



#Python Variables
x = 5
y = "John"
print(x)
print(y) #output: 5
          #John

x = 4       
x = "Sally" 
print(x)      #output: Sally

x = str(3)    # 3
y = int(3)    # 3
z = float(3)  # 3.0

x = 5
y = "John"
print(type(x))
print(type(y))
# output:
# <class 'int'>
# <class 'str'>

x = "John"
x = 'John'
#output:
#John
#John

a = 4
A = "Sally"
print(a)
print(A)
#output:
# 4
# Sally

#Python - Variable Names
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"
print(myvar)
print(my_var)
print(_my_var)
print(myVar)
print(MYVAR)
print(myvar2)
# output
# John
# John
# John
# John
# John
# John

#Python Variables - Assign Multiple Values
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)
#output:
# Orange
# Banana
# Cherry

x = y = z = "Orange"
print(x)
print(y)
print(z)
#output:
# Orange
# Orange
# Orange

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)
#output:
# apple
# banana
# cherry



#Python - Output Variables
x = "Python is awesome"
print(x)
#output:
#Python is awesome

x = "Python"
y = "is"
z = "awesome"
print(x, y, z)
#output: Python is awesome

x = "Python "
y = "is "
z = "awesome"
print(x + y + z)
#output: Python is awesome

x = 5
y = 10
print(x + y) #output :15

x = 5
y = "John"
print(x, y) #output : 5 John



#Python - Global Variables
x = "awesome"
def myfunc():
  print("Python is " + x)
myfunc()
# output:
# Python is awesome

x = "awesome"
def myfunc():
  x = "fantastic"
  print("Python is " + x)
myfunc()
print("Python is " + x)
# output:
# Python is fantastic
# Python is awesome

def myfunc():
  global x
  x = "fantastic"
myfunc()
print("Python is " + x)
# output:
# Python is fantastic

x = "awesome"
def myfunc():
  global x
  x = "fantastic"
myfunc()
print("Python is " + x)
# output:
# Python is fantastic



#Python Data Types
x = 5
print(type(x)) 
# output:
<class 'int'>

x = "Hello World"
print(x)
print(type(x)) 
# Hello World
# <class 'str'>

x = 20
print(x)
print(type(x)) 
#output :
# 20
# <class 'int'>

x = 20.5
print(x)
print(type(x))
#output :
# 20.5
# <class 'float'>

print(x)
print(type(x))
#output :
# lj
# <class 'complex'>

print(x)
print(type(x)) 
#output :
# ['apple', 'banana', 'cherry']
# <class 'list'>

print(x)
print(type(x)) 
#output :
# ('apple', 'banana', 'cherry')
# <class 'tuple'>

print(x)
print(type(x)) 
range(0, 6)
#output :
# <class 'range'>

print(x)
print(type(x)) 
#output :
# {'name': 'John', 'age': 36}
# <class 'dict'>

x = set(("apple", "banana", "cherry"))
print(x)
print(type(x)) 
#output :
# {'banana', 'apple', 'cherry'}
# <class 'set'>

print(x)
print(type(x)) 
#output :
# frozenset({'apple', 'cherry', 'banana'})
# <class 'frozenset'>

print(x)
print(type(x)) 
#output :
# True
# <class 'bool'>

print(x)
print(type(x)) 
#output :
# <class 'bytes'>

print(x)
print(type(x)) 
#output :
#<class 'bytearray'>

print(x)
print(type(x)) 
#output :
# <class 'memoryview'>




#Python Numbers
x = 1
y = 2.8
z = 1j
print(type(x))     
print(type(y))
print(type(z))
#output :
# <class 'int'>
# <class 'float'>
# <class 'complex'>


y = 35656222554887711
z = -3255522
print(type(x))
print(type(y))
print(type(z))
#output :
# <class 'int'>
# <class 'int'>
# <class 'int'>


y = 1.0
z = -35.59
print(type(x))
print(type(y))
print(type(z))
#output :
# <class 'float'>
# <class 'float'>
# <class 'float'>

y = 12E4
z = -87.7e100
print(type(x))
print(type(y))
print(type(z))
#output :
# <class 'float'>
# <class 'float'>
# <class 'float'>

y = 5j
z = -5j
print(type(x))
print(type(y))
print(type(z))
#output :
# <class 'complex'>
# <class 'complex'>
# <class 'complex'>

x = float(1)
y = int(2.8)
z = complex(1)
print(x)
print(y)
print(z)
print(type(x))
print(type(y))
print(type(z))
#output :
# 1.0
# 2
# (1+0j)
# <class 'float'>
# <class 'int'>
# <class 'complex'>

import random
print(random.randrange(1, 10))
#output :
#9




#Python Casting
x = int(1)
y = int(2.8)
z = int("3")
print(x)
print(y)
print(z)
#output :
# 1
# 2
# 3

x = float(1)
y = float(2.8)
z = float("3")
w = float("4.2")
print(x)
print(y)
print(z)
print(w)
#output :
# 1.0
# 2.8
# 3.0
# 4.2


y = str(2)
z = str(3.0)
print(x)
print(y)
print(z)
#output :
# s1
# 2
# 3.0




#Python Strings
print("Hello")
print('Hello')
#output :
# Hello
# Hello

a = "Hello"
print(a)
#output :
# Hello

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)
#output :
# Lorem ipsum dolor sit amet,
# consectetur adipiscing elit,
# sed do eiusmod tempor incididunt
# ut labore et dolore magna aliqua.

a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)
#output :
# Lorem ipsum dolor sit amet,
# consectetur adipiscing elit,
# sed do eiusmod tempor incididunt
# ut labore et dolore magna aliqua.

a = "Hello, World!"
print(a[1])
#output :
#e

for x in "banana":
  print(x) 
  #output :
# b
# a
# n
# a
# n
# a

a = "Hello, World!"
print(len(a))
#output :
#13

txt = "The best things in life are free!"
print("free" in txt)
#output :
#True

txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")
#output :
#Yes, 'free' is present.

txt = "The best things in life are free!"
print("expensive" not in txt)
#output :
#True

txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")
#output :
#No, 'expensive' is NOT present.




#Python - Slicing Strings
b = "Hello, World!"
print(b[2:5])
#output :
#llo

b = "Hello, World!"
print(b[:5])
#output :
#Hello

b = "Hello, World!"
print(b[2:])
#output :
#llo, World!

b = "Hello, World!"
print(b[-5:-2])
#output :
#orl




#Python Booleans
print(10 > 9)
print(10 == 9)
print(10 < 9)
#output :
# True
# False
# False

a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")
b is not greater than a
print(bool("Hello"))
print(bool(15))
#output :
# True
# True

x = "Hello"
y = 15
print(bool(x))
print(bool(y))
#output :
# True
# True

print(bool("abc"))
print(bool(123))
print(bool(["apple", "cherry", "banana"]))
#output :
# True
# True
# True

print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))
#output :
# False
# False
# False
# False
# False
# False
# False

class myclass():
  def __len__(self):
    return 0
myobj = myclass()
print(bool(myobj))
#output :
#False

def myFunction() :
  return True
print(myFunction())
#output :
#True

def myFunction() :
  return True
if myFunction():
  print("YES!")
else:
  print("NO!")
#output :
#YES!

x = 200
print(isinstance(x, int))
#output :
#True




#Python Operators
print(10 + 5)
#output :
#15

print(5 + 4 - 7 + 3)
"""
Additions and subtractions have the same precedence, and we need to calculate from left to right.
The calculation above reads:
5 + 4 = 9
9 - 7 = 2
2 + 3 = 5
"""
#output :
#5





#Python Lists
thislist = ["apple", "banana", "cherry"]
print(thislist)
#output :
#['apple', 'banana', 'cherry']

thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)
#output :
#['apple', 'banana', 'cherry', 'apple', 'cherry']

thislist = ["apple", "banana", "cherry"]
print(len(thislist))
#output :
#3

list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
print(list1)
print(list2)
print(list3)
#output :
# ['apple', 'banana', 'cherry']
# [1, 5, 7, 9, 3]
# [True, False, False]

list1 = ["abc", 34, True, 40, "male"]
print(list1)
#output :
# ['abc', 34, True, 40, 'male']

mylist = ["apple", "banana", "cherry"]
print(type(mylist))
#output :
# <class 'list'>

thislist = list(("apple", "banana", "cherry"))
print(thislist)
#output :
# ['apple', 'banana', 'cherry']




#Python Tuples
thistuple = ("apple", "banana", "cherry")
print(thistuple)
#output :
#('apple', 'banana', 'cherry')

thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)
#output :
#('apple', 'banana', 'cherry', 'apple', 'cherry')

thistuple = tuple(("apple", "banana", "cherry"))
print(len(thistuple))
#output :
#3

thistuple = ("apple",)
print(type(thistuple))
thistuple = ("apple")
print(type(thistuple))
#output :
# <class 'tuple'>
# <class 'str'>

tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)
print(tuple1)
print(tuple2)
print(tuple3)
#output :
# ('apple', 'banana', 'cherry')
# (1, 5, 7, 9, 3)
# (True, False, False)

tuple1 = ("abc", 34, True, 40, "male")
print(tuple1)
#output :
# ('abc', 34, True, 40, 'male')

mytuple = ("apple", "banana", "cherry")
print(type(mytuple))
#output :
# <class 'tuple'>

thistuple = tuple(("apple", "banana", "cherry"))
print(thistuple)
#output :
# ('apple', 'banana', 'cherry')




#Python Sets
thisset = {"apple", "banana", "cherry"}
print(thisset)
#output :
# {'cherry', 'banana', 'apple'}

thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)
#output :
# {'banana', 'cherry', 'apple'}

thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset)
#output :
# {True, 2, 'banana', 'cherry', 'apple'}

thisset = {"apple", "banana", "cherry", False, True, 0}
print(thisset)
#output :
# {False, True, 'cherry', 'apple', 'banana'}

thisset = {"apple", "banana", "cherry"}
print(len(thisset))
#output :
# 3

set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}
print(set1)
print(set2)
print(set3)
#output :
# {'cherry', 'apple', 'banana'}
# {1, 3, 5, 7, 9}
# {False, True}

set1 = {"abc", 34, True, 40, "male"}
print(set1)
#output :
# {True, 34, 40, 'male', 'abc'}

myset = {"apple", "banana", "cherry"}
print(type(myset))
#output :
# <class 'set'>




# Python Dictionaries
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
#output :
# {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])
#output :
# Ford

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)
#output :
# {'brand': 'Ford', 'model': 'Mustang', 'year': 2020}

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(len(thisdict))
#output :
# 3

thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
print(thisdict)
#output :
# {'brand': 'Ford', 'electric': False, 'year': 1964, 'colors': ['red', 'white', 'blue']}

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(type(thisdict))
#output :
# <class 'dict'>

thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict) 
#output :
# {'name': 'John', 'age': 36, 'country': 'Norway'}





# Python If ... Else
a = 33
b = 200
if b > a:
  print("b is greater than a")
  #output :
# b is greater than a

a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
  #output :
# a and b are equal

a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")
  #output :
# a is greater than b

a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")
  #output :
# b is not greater than a

a = 200
b = 33
if a > b: print("a is greater than b")
#output :
# "a is greater than b"

a = 2
b = 330
print("A") if a > b else print("B")
#output :
# B

a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")
#output :
# =

a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")
#output :
# Both conditions are True

a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")
#output :
# At least one of the conditions is True

a = 33
b = 200
if not a > b:
  print("a is NOT greater than b")
#output :
# a is NOT greater than b

x = 41
if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")
#output :
# Above ten,
# and also above 20!

a = 33
b = 200
if b > a:
  pass

 








