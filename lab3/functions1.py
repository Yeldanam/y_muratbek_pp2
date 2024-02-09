#1
def grams_ounces(grams):
    ounces = 28.3495231 * grams
    return ounces

#2
def fahrenheit_celsius(fahrenheit):
    celsius = (5 / 9) * (fahrenheit - 32)
    return celsius

#3
def solve(numheads, numlegs):
numheads = 35
numlegs = 94
chickens, rabbits = solve(numheads, numlegs)
print("Number of chickens:", chickens)
print("Number of rabbits:", rabbits)

#4
def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def filter_prime(numbers):
    prime_numbers = []
    for num in numbers:
        if is_prime(num):
            prime_numbers.append(num)
    return prime_numbers

#5
from itertools import permutations
def print_permutations(input_str):
    perms = permutations(input_str)
    for perm in perms:
        print(''.join(perm))

#6
def reverse_sentence(sentence):
    words = sentence.split()
    reversed_words = words[::-1]
    reversed_sentence = ' '.join(reversed_words)
    return reversed_sentence

#7
def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False

#8
def spy_game(nums):
    zeros_count = 0
    for num in nums:
        if num == 0 and zeros_count > 0:
            zeros_count += 1
            zeros_count = 1
        elif num == 7 and zeros_count == 2:
            return True
    return False

#9
import math

def sphere_volume(radius):
    volume = (4/3) * math.pi * (radius ** 3)
    return volume

#10
def unique_elements(input_list):
    unique_list = []
    for element in input_list:
        if element not in unique_list:
            unique_list.append(element)
    return unique_list
#11
def is_palindrome(word):
    word = word.replace(" ", "").lower()
    return word == word[::-1]

#12
def histogram(numbers):
    for num in numbers:
        print('*' * num)
histogram([4, 9, 7])

#13
import random

def guess_the_number():
    secret_number = random.randint(1, 20)
    print("Hello! What is your name?")
    name = input()
    print(f"Well, {name}, I am thinking of a number between 1 and 20.")
    attempts = 0
    while True:
        print("Take a guess.")
        guess = int(input())
        attempts += 1
        if guess == secret_number:
            print(f"Good job, {name}! You guessed my number in {attempts} guesses!")
            break
        elif guess < secret_number:
            print("Your guess is too low.")
        else:
            print("Your guess is too high.")

#14
from task_5 import *
from task_7 import *
from task_9 import *
def main():
    fahrenheit_temp = 212
    celsius_temp = fahrenheit_to_celsius(fahrenheit_temp)
    print(f"{fahrenheit_temp} Fahrenheit is equal to {celsius_temp:.2f} Celsius.")
    number = 17
    if is_prime(number):
        print(f"{number} is a prime number.")
    else:
        print(f"{number} is not a prime number.")
    sentence = "Hello, world!"
    reversed_sentence = reverse_sentence(sentence)
    print("Reversed sentence:", reversed_sentence)
if __name__ == "__main__":
    main()
