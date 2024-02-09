#Python While Loops 
#1
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")
#terminal:
#1
#2
#3
#4
#5
#6 i is no longer less than 6

#2
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")
#terminal:
#1
#2
#3
#4
#5




#Python Lists
#1
thislist = ["apple", "banana", "cherry"]
print(thislist)
#terminal:
#['apple' , 'banana' , 'cherry']

#2
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)
#terminal:
#['apple' , 'banana', 'cherry', 'apple', 'cherry']

#3
thislist = ["apple", "banana", "cherry"]
print(len(thislist))
#terminal:
#3

#4
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
#terminal:
#['apple' , 'banana' , 'cherry']
1, 5, 7, 9, 3
True, False, False

#5
list1 = ["abc", 34, True, 40, "male"]
#terminal:
#abc , 34, True, 40, male

#6
mylist = ["apple", "banana", "cherry"]
print(type(mylist))
#terminal:
#list

#7
thislist = list(("apple", "banana", "cherry")) 
print(thislist)
#terminal:
#['apple', 'banana', 'cherry']




#Python For Loops
#1
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
#terminal:
#apple
#banana
#cherry

#2
for x in "banana":
  print(x)
#terminal:
#b
#a
#n
#a
#n
#a

#3
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break
#terminal:
#apple

#4
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)
#terminal:
#apple
#cherry

#5
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)
#terminal:
#apple
#cherry

#6
for x in range(6):
  print(x)
#terminal: 1 2 3 4 5

#7
for x in range(2, 6):
  print(x)
#terminal: 2 3 4 5

#8
  for x in range(2, 30, 3):
  print(x)
#terminal: 2 5 8 11 14 17 20 23 26 29

#9
  for x in range(6):
  print(x)
else:
  print("Finally finished!")
#terminal: 0 1 2 3 4 5

#10
  for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")
#terminal: 0 1 2

#11
  adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
for x in adj:
  for y in fruits:
    print(x, y)
#terminal: 
#red apple
#red banana
#red cherry
#big apple
#big banana
#big cherry
#tasty apple
#tasty banana
#tasty cherry




#Python Arrays
#1
cars = ["Ford", "Volvo", "BMW"]
#terminal:
#['Ford', 'Volvo', 'BMW']

#2
cars = ["Ford", "Volvo", "BMW"]
x = cars[0]
print(x)
#terminal:Ford

#3
cars = ["Ford", "Volvo", "BMW"]
cars[0] = "Toyota"
print(cars)
#terminal: ['Toyota', 'Volvo', 'BMW']

#4
cars = ["Ford", "Volvo", "BMW"]
x = len(cars)
print(x)
#terminal: 3

#5
cars = ["Ford", "Volvo", "BMW"]
for x in cars:
  print(x)
#terminal:
# Ford
# Volvo
# BMW

#6
cars = ["Ford", "Volvo", "BMW"]
cars.append("Honda")
print(cars)
#terminal: ['Ford', 'Volvo', 'BMW', 'Honda']

#7
cars = ["Ford", "Volvo", "BMW"]
cars.pop(1)
print(cars)
#terminal: ['Ford', 'BMW']

#8
cars = ["Ford", "Volvo", "BMW"]
cars.remove("Volvo")
print(cars)
#terminal: ['Ford', 'BMW']




#Python Tuples
#1
thistuple = ("apple", "banana", "cherry")
print(thistuple)
#terminal: ('apple', 'banana', 'cherry')

#2
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)
#terminal: ('apple', 'banana', 'cherry', 'apple', 'cherry')

#3
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))
#terminal: 3

#4
thistuple = ("apple",)
print(type(thistuple))
thistuple = ("apple")
print(type(thistuple))
#terminal:
#<class 'tuple'>
#<class 'str'>

#5
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)

print(tuple1)
print(tuple2)
print(tuple3)
#terminal:
# ('apple', 'banana', 'cherry')
# (1, 5, 7, 9, 3)
# (True, False, False)

#6
tuple1 = ("abc", 34, True, 40, "male")
print(tuple1)
#terminal: ('abc', 34, True, 40, 'male')

#7
mytuple = ("apple", "banana", "cherry")
print(type(mytuple))
#terminal: <class 'tuple'>

#8
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)
#terminal: ('apple', 'banana', 'cherry')




#Python Sets
#1
thisset = {"apple", "banana", "cherry"}
print(thisset)
#terminal: {'apple', 'cherry', 'banana'}

#2
thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)
#terminal: {'banana', 'cherry', 'apple'}

#3
thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset)
#terminal: {True, 2, 'banana', 'cherry', 'apple'}

#4
thisset = {"apple", "banana", "cherry", False, True, 0}
print(thisset)
#terminal: {False, True, 'cherry', 'apple', 'banana'}

#5
thisset = {"apple", "banana", "cherry"}
print(len(thisset))
#terminal: 3

#6
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}

print(set1)
print(set2)
print(set3)
#terminal:
# {'cherry', 'apple', 'banana'}
# {1, 3, 5, 7, 9}
# {False, True}

#7
set1 = {"abc", 34, True, 40, "male"}
print(set1)
#terminal: {True, 34, 40, 'male', 'abc'}

#8
myset = {"apple", "banana", "cherry"}
print(type(myset))
#terminal: <class 'set'>

#9
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)
#terminal: {'banana', 'cherry', 'apple'}




#Python Dictionaries
#1
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
#terminal:
#{'brand': 'Ford', 'model': 'Mustang', 'year': 1964}

#2
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])
#terminal: Ford

#3
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)
#terminal: {'brand': 'Ford', 'model': 'Mustang', 'year': 2020}

#4
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(len(thisdict))
#terminal: 3

#5
thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
#terminal:
# {'brand': 'Ford', 'electric': False, 'year': 1964, 'colors': ['red', 'white', 'blue']}

#6
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(type(thisdict))
#terminal:
# <class 'dict'>

#7
thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)
#terminal:
# {'name': 'John', 'age': 36, 'country': 'Norway'}
