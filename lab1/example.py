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
# <class 'range'

#display x:
print(x)

#display the data type of x:
print(type(x)) 
{'name': 'John', 'age': 36}
<class 'dict'>

x = set(("apple", "banana", "cherry"))

#display x:
print(x)

#display the data type of x:
print(type(x)) 
{'banana', 'apple', 'cherry'}
<class 'set'>



#display x:
print(x)

#display the data type of x:
print(type(x)) 
frozenset({'apple', 'cherry', 'banana'})
<class 'frozenset'>



#display x:
print(x)

#display the data type of x:
print(type(x)) 
True
<class 'bool'>



#display x:
print(x)

#display the data type of x:
print(type(x)) 
<class 'bytes'>



#display x:
print(x)

#display the data type of x:
print(type(x)) 
<class 'bytearray'>



#display x:
print(x)

#display the data type of x:
print(type(x)) 
<class 'memoryview'>