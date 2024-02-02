#task 1
print("Hello, World!")  #output:Hello,world!


#task 2
if 5 > 2:
  print("YES") #output: YES

#task 3
#This is a comment

#task 4
"""This is a comment
written in 
more than just one line
"""

#task 5
carname = "Volvo"

#task 6
x = 50

#task 7
x = 5
y = 10
print(x + y)  #output: 15

#task 8
x = 5
y = 10
z = x + y
print(z)    #output: 15

#task 9
x, y, z = "Orange", "Banana", "Cherry"

#task 10
x = y = z = "Orange"

#task 11
def myfunc():
global x
x = "fantastic"

#task 12
x = 5
print(type(x))    #output: int

#task 13
x = "Hello World"
print(type(x))    #output: str

#task 14
x = 20.5
print(type(x))    #output: float

#task 15
x = ["apple", "banana", "cherry"]
print(type(x))    #output: list

#task 16
x = ("apple", "banana", "cherry")
print(type(x))    #output: tuple

#task 17
x = {"name" : "John", "age" : 36}
print(type(x))    #output: dict

#task 18
x = True
print(type(x))    #output: bool

#task 19
x = 5
x = float(x)

#task 20
x = 5.5
x = int(x)    

#task 21
x = 5
x = complex(x)

#task 22
x = "Hello World"
print(len(x))

#task 23
txt = "Hello World"
x = txt[0]

#task 24
txt = "Hello World"
x = txt[2:5]

#task 25
txt = " Hello World "
x = txt.strip()

#task 26
txt = "Hello World"
txt = txt.upper()

#task 27
txt = "Hello World"
txt = txt.lower()

#task 28
txt = "Hello World"
txt = txt.replace("H","J")

#task 29
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

#task 30
print(10 > 9)   #True

#task 31
print(10 == 9)    #False

#task 32
print(10 < 9)   #False

#task 33
print(bool("abc"))    #True

#task 34
print(bool(0))    #False

#task 35
print(10 * 5)     #50

#task 36
print(10 / 2)     #5

#task 37
fruits = ["apple", "banana"]
if "apple" in fruits:
  print("Yes, apple is a fruit!")

#task 38
if 5 != 10:
  print("5 and 10 is not equal")

#task 39
if 5 == 10 or 4 == 4:
  print("At least one of the statements is true")

#task 40
fruits = ["apple", "banana", "cherry"]
print(fruits[1])

#task 41
fruits = ["apple", "banana", "cherry"]
fruits[0] = "kiwi"

#task 42
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")

#task 43
fruits = ["apple", "banana", "cherry"]
fruits.insert(1, "lemon")

#task 44
fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")

#task 45
fruits = ["apple", "banana", "cherry"]
print(fruits[-1])

#task 46
fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(fruits[2:5])

#task 47
fruits = ["apple", "banana", "cherry"]
print(len(fruits))

#task 48
fruits = ("apple", "banana", "cherry")
print(fruits[0])

#task 49
fruits = ("apple", "banana", "cherry")
print(len(fruits))

#task 50
fruits = ("apple", "banana", "cherry")
print(fruits[-1])

#task 51
fruits = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(fruits[2:5])

#task 52
fruits = {"apple", "banana", "cherry"}
if "apple" in fruits:
  print("Yes, apple is a fruit!")

#task 53
fruits = {"apple", "banana", "cherry"}
fruits.add("orange")

#task 54
fruits = {"apple", "banana", "cherry"}
more_fruits = ["orange", "mango", "grapes"]
fruits.update(more_fruits)

#task 55
fruits = {"apple", "banana", "cherry"}
fruits.remove("banana")

#task 56
fruits = {"apple", "banana", "cherry"}
fruits.discard("banana")

#task 57
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(car.get("model"))

#task 58
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car["year"] = 2020

#task 59
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car["color"] = "red"

#task 60
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.pop("model")

#task 61
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.clear()

#task 62
a = 50
b = 10
if a > b:
  print("Hello World")

#task 63
a = 50
b = 10
if a != b:
  print("Hello World")

#task 64
a = 50
b = 10
if a == b:
  print("Yes")
else:
  print("No")

#task 65
a = 50 
b = 10
if a == b:
  print("1")
elif a > b:
  print("2")
else:
  print("3")

#task 66
if a == b and c == d:
  print("Hello")

#task 67
if a == b or c == d:
  print("Hello")

#task 68
if 5 > 2:
    print("YES")

#task 69
a = 2
b = 5
print("YES") if a == b else  print("NO")

#task 70
a = 2
b = 50
c = 2
if a == c or b == c:
  print("YES")


