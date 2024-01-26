#task 1
print("Hello, World!")  #output:Hello,world!


#task 2
if 5 > 2:
  print("Five is greater than two!") 

#task 3
#This is a comment

#task 4
x = 5
y = "John"
print(x)    #output:5
print(y)    #John

#task 5
x = 4       
x = "Sally" #output:Sally
print(x)
 

#task 6
x = 5
y = "John"
print(type(x)) #output:int
print(type(y)) #output:str


#task 7
x, y, z = "Orange", "Banana", "Cherry"
print(x)    
print(y)
print(z) 
#output:
#Orange
#Banana
#Cherry

#task 8
x = y = z = "Orange"
print(x)
print(y)
print(z)
#output:
#Orange
#Orange
#Orange

#task 9
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)        #apple
print(y)        #banana
print(z)        #cherry

#task 10
x = "Python is awesome"
print(x)        #Python is awesome

#task 11
x = "Python"
y = "is"
z = "awesome"
print(x, y, z) #Python is awesome

#task 12
x = "Python "
y = "is "
z = "awesome"
print(x + y + z) #Python is awesome

#task 13
x = 5
y = 10
print(x + y) #15

#task 14
x = 5
y = "John"
print(x, y)  #5,John

#task 15
x = "awesome"
def myfunc():
  print("Python is " + x)

myfunc()      #Python is awesome
myfunc()      


#task 16
x = "awesome"
def myfunc():
  x = "fantastic"
  print("Python is " + x)
myfunc()
print("Python is " + x)
#Python is fantastic
#Python is awesome

#task 17
def myfunc():
  global x
  x = "fantastic"
myfunc()
print("Python is " + x)
#Python is fantastic

#task 18
x = "awesome"
def myfunc():
  global x
  x = "fantastic"
myfunc()
print("Python is " + x)
#Python is fantastic


#task 19
x = 5
print(type(x))
#int

#task 20
x = 1
y = 35656222554887711
z = -3255522
print(type(x))
print(type(y))
print(type(z))
#int
#int
#int

#task 21
x = 1.10
y = 1.0
z = -35.59
print(type(x))
print(type(y))
print(type(z))
#float
#float
#float

#task 22
x = 35e3
y = 12E4
z = -87.7e100
print(type(x))
print(type(y))
print(type(z))
#float
#float
#float

#task 23
print("Hello")
print('Hello')
#Hello
#Hello

#task 24
a = "Hello"
print(a)
#Hello

#task 25
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)
#Lorem ipsum dolor sit amet,
#consectetur adipiscing elit,
#sed do eiusmod tempor incididunt
#ut labore et dolore magna aliqua.


#task 26
a = "Hello, World!"
print(a[1])
#e

#task 27
for x in "banana":
  print(x)
#n
#a
#n
#a

#task 28
a = "Hello, World!"
print(len(a))
#13

#task 29
txt = "The best things in life are free!"
print("free" in txt)
#True

#task 30
txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")
  #Yes, 'free' is present.

#task 31
txt = "The best things in life are free!"
print("expensive" not in txt)
#True

#task 32
txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")
#No, 'expensive' is NOT present.

#task 33
b = "Hello, World!"
print(b[2:5])
#llo

#task 34
b = "Hello, World!"
print(b[:5])
#Hello

#task 35
b = "Hello, World!"
print(b[2:])
#llo, World!

#task 36
b = "Hello, World!"
print(b[-5:-2])
#orl

#task 37
a = "Hello, World!"
print(a.upper())
#HELLO, WORLD!

#task 38
a = "Hello, World!"
print(a.lower())
#Hello, World!

#task 39
a = " Hello, World! "
print(a.strip()) 
#Hello, World! 


#task 40
a = "Hello, World!"
print(a.replace("H", "J"))
#Jello, World!

#task 41
a = "Hello, World!"
print(a.split(",")) 
#['Hello', ' World!']


#task 42
a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")
#b is not greater than a


#task 43
print(bool("Hello"))
print(bool(15))
#True
#True

#task 44
x = "Hello"
y = 15
print(bool(x))
print(bool(y))
#True
#True

#task 45
class myclass():
  def __len__(self):
    return 0
myobj = myclass()
print(bool(myobj))
#False

#task 46
def myFunction() :
  return True
print(myFunction())
#True

#task 47
def myFunction() :
  return True
if myFunction():
  print("YES!")
else:
  print("NO!")
#YES!

#task 48
print(10 + 5)
#15

#task 49
thislist = ["apple", "banana", "cherry"]
print(thislist)
#['apple', 'banana', 'cherry']

#task 50
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)
#['apple', 'banana', 'cherry', 'apple', 'cherry']

#task 51
thislist = ["apple", "banana", "cherry"]
print(len(thislist))
#3


#task 52
thistuple = ("apple", "banana", "cherry")
print(thistuple)
#('apple', 'banana', 'cherry')


#task 53
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)
#apple,banana,cherry,apple,cherry

#task 54
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))
#3

#task 55
thistuple = ("apple",)
print(type(thistuple))
#tuple

#task 56
thistuple = ("apple")
print(type(thistuple))
#str

#task 58
thisset = {"apple", "banana", "cherry"}
print(thisset)
#cherry , apple , banana

#task 59
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
#brand : Ford, model : Mustang , year : 1964

#task 60
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])
#Ford

#task 61
a = 33
b = 200
if b > a:
  print("b is greater than a")
#b is greater than a

#task 62
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
#a and b are equal

#task 63
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")
#a is greater than b

