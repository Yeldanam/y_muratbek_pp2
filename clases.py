#1
# Define a class which has at least two methods: getString: to get a string from
#  console input printString: to print the string in upper case.
class StringManipulator:
    def __init__(self):
        self.string = ""
    def getString(self):
        self.string = input("Enter a string: ")
    def printString(self):
        print(self.string.upper())
# 2
# Define a class named Shape and its subclass Square. The Square class has an init 
# function which takes a length as argument. Both classes have a area function which can 
# print the area of the shape where Shape's area is 0 by default.
class Shape:
    def __init__(self):
        pass
    def area(self):
        return 0
class Square(Shape):
    def __init__(self, length):
        super().__init__()
        self.length = length
    def area(self):
        return self.length * self.length
# 3
# Define a class named Rectangle which inherits from Shape class from task 2.
#  Class instance can be constructed by a length and width. The Rectangle class has a method which can compute the area.
class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__()
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width
# 4
# Write the definition of a Point class. Objects from this class should have a
# a method show to display the coordinates of the point
# a method move to change these coordinates
# a method dist that computes the distance between 2 points
import math
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    def show(self):
        print("Coordinates of the point: ({}, {})".format(self.x, self.y))
    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y
    def dist(self, other_point):
        return math.sqrt((self.x - other_point.x)**2 + (self.y - other_point.y)**2)
# 5
# Create a bank account class that has attributes owner, balance and two methods deposit
# and withdraw. Withdrawals may not exceed the available balance. Instantiate your class,
# make several deposits and withdrawals, and test to make sure the account can't be overdrawn.
# class Account:
#     pass
class Account:
    def __init__(self, owner, initial_balance=0):
        self.owner = owner
        self.balance = initial_balance
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposit of {amount} accepted. New balance is {self.balance}.")
        else:
            print("Deposit amount should be greater than zero.")
    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrawal of {amount} accepted. New balance is {self.balance}.")
            else:
                print("Insufficient funds. Withdrawal not processed.")
        else:
            print("Withdrawal amount should be greater than zero.")
# 6
# Write a program which can filter prime numbers in a list by using filter
#  function. Note: Use lambda to define anonymous functions.
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True
