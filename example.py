#Python Functions
#1
def my_function():
  print("Hello from a function")

my_function()
#terminal:
# Hello from a function

#2
def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")
# terminal:
# Emil Refsnes
# Tobias Refsnes
# Linus Refsnes

#3
def my_function(fname):
  print(fname + " Refsnes")
my_function("Emil")
my_function("Tobias")
my_function("Linus")
#terminal:
# Emil Refsnes
# Tobias Refsnes
# Linus Refsnes

#4
def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")
#terminal:
#The youngest child is Linus

#5
def my_function(child3, child2, child1):
  print("The youngest child is " + child3)
my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")
#terminal:
# The youngest child is Linus

#6
def my_function(**kid):
  print("His last name is " + kid["lname"])
my_function(fname = "Tobias", lname = "Refsnes")
#terminal:
# His last name is Refsnes

#7
def my_function(country = "Norway"):
  print("I am from " + country)
#terminal:
my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")
#terminal:
# I am from Sweden
# I am from India
# I am from Norway
# I am from Brazil

#8
def my_function(food):
  for x in food:
    print(x)
fruits = ["apple", "banana", "cherry"]
my_function(fruits)
#terminal:
# apple
# banana
# cherry

#9
def my_function(x):
  return 5 * x
print(my_function(3))
print(my_function(5))
print(my_function(9))
#terminal:
# 15
# 25
# 45

#10
def myfunction():
  pass
# having an empty function definition like this, would raise an error without the pass statement

#11
def my_function(x, /):
  print(x)
my_function(3)
#terminal:
# 3

#12
def my_function(x):
  print(x)
my_function(x = 3)
#terminal:
# 3

#13
def my_function(*, x):
  print(x)
my_function(x = 3)
#terminal:
# 3

# 14
def my_function(x):
  print(x)
my_function(3)
#terminal:
# 3

#15
def my_function(a, b, /, *, c, d):
  print(a + b + c + d)
my_function(5, 6, c = 7, d = 8)
#terminal:
# 26

#16
def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result
print("\n\nRecursion Example Results")
tri_recursion(6)
#terminal:
# Recursion Example Results
# 1
# 3
# 6
# 10
# 15
# 21




# Python Lambda
# 1
x = lambda a: a + 10
print(x(5))
#output:
#15

# 2
x = lambda a, b: a * b
print(x(5, 6))
#output:
# 30

# 3
x = lambda a, b, c: a + b + c
print(x(5, 6, 2))
#output:
# 13

# 4
def myfunc(n):
  return lambda a : a * n
mydoubler = myfunc(2)
print(mydoubler(11))
#output:
# 22

# 5
def myfunc(n):
  return lambda a : a * n
mytripler = myfunc(3)
print(mytripler(11))
# 33

# 6
def myfunc(n):
  return lambda a : a * n
mydoubler = myfunc(2)
mytripler = myfunc(3)
print(mydoubler(11)) 
print(mytripler(11))
#output:
# 22
# 33




# Python Classes and Objects
# 1
class MyClass:
  x = 5
#output:
#<class '__main__.MyClass'>

#2
class MyClass:
  x = 5

p1 = MyClass()
print(p1.x)
#output:
# 5

#3
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)
# output:
# John
# 36

#4
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1)
# <__main__.Person object at 0x15039e602100>

#5
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name}({self.age})"    

p1 = Person("John", 36)

print(p1)
# John(36)

#6
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()
#Hello my name is John







# Python Inheritance
# 1
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
p1 = Person("John", 36)
print(p1.name)
print(p1.age)
#output:
# John
# 36

#2
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
p1 = Person("John", 36)
print(p1)
#output:
# <__main__.Person object at 0x15039e602100>

# 3
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def __str__(self):
    return f"{self.name}({self.age})"
p1 = Person("John", 36)
print(p1)
#output:
# John(36)

# 4
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def myfunc(self):
    print("Hello my name is " + self.name)
p1 = Person("John", 36)
p1.myfunc()
#output:
# Hello my name is John

# 5
class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age
  def myfunc(abc):
    print("Hello my name is " + abc.name)
p1 = Person("John", 36)
p1.myfunc()
#output:
# Hello my name is John

# 6
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def myfunc(self):
    print("Hello my name is " + self.name)
p1 = Person("John", 36)
p1.age = 40
print(p1.age)
#output:
# 40

# 7
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def myfunc(self):
    print("Hello my name is " + self.name)
p1 = Person("John", 36)
del p1.age
print(p1.age)
#output:
Traceback (most recent call last):
  File "demo_class7.py", line 13, in <module>
    print(p1.age)
AttributeError: 'Person' object has no attribute 'age'

# 8
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def myfunc(self):
    print("Hello my name is " + self.name)
p1 = Person("John", 36)
del p1
#output:
print(p1)
Traceback (most recent call last):
  File "demo_class8.py", line 13, in <module>
    print(p1)
NameError: 'p1' is not defined

# 9
class Person:
  pass
# having an empty class definition like this, would raise an error without the pass statement




# Python Inheritance
# 1
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname
  def printname(self):
    print(self.firstname, self.lastname)
#Use the Person class to create an object, and then execute the printname method:
x = Person("John", "Doe")
x.printname()
#output:
# John Doe

# 2
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname
  def printname(self):
    print(self.firstname, self.lastname)
class Student(Person):
  pass
x = Student("Mike", "Olsen")
x.printname()
#output:
# Mike Olsen

# 3
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname
  def printname(self):
    print(self.firstname, self.lastname)
class Student(Person):
  def __init__(self, fname, lname):
    Person.__init__(self, fname, lname)
x = Student("Mike", "Olsen")
x.printname()
#output:
# Mike Olsen

# 4
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname
  def printname(self):
    print(self.firstname, self.lastname)
class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)
x = Student("Mike", "Olsen")
x.printname()
#output:
# Mike Olsen

# 5
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname
  def printname(self):
    print(self.firstname, self.lastname)
#output:
# 2019

# 6
class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)
    self.graduationyear = 2019
x = Student("Mike", "Olsen")
print(x.graduationyear)
#output:
# 2019

# 7
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname
  def printname(self):
    print(self.firstname, self.lastname)
class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year
  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)
x = Student("Mike", "Olsen", 2019)
x.welcome()
#output:
# Welcome Mike Olsen to the class of 2019

