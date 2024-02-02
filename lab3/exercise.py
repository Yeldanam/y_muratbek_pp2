# task 1
def my_function():
     print("Hello from a function")


#task 2
def my_function():
  print("Hello from a function")
my_function()

#task 3
def my_function(fname, lname):
  print(fname)

#task 4
def my_function(x):
    return x + 5

#task 5
def my_function(*kids):
  print("The youngest child is " + kids[2])

#task 6
def my_function(**kid):
  print("His last name is " + kid["lname"])

#task 7
x = lambda a : a

#task 8
class MyClass:
  x = 5

#task 9
class MyClass:
  x = 5
p1 = MyClass()

#task 10
class MyClass:
  x = 5
p1 = MyClass()
print(p1.x)

#task 11
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

#task 12
class Student(Person):

#task 13
class Person:
  def __init__(self, fname):
    self.firstname = fname
  def printname(self):
    print(self.firstname)
class Student(Person):
  pass
x = Student("Mike")
x.printname()

