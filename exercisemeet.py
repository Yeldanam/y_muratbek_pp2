# 1 - Write a Python program to convert degree to radian.
#  Input degree: 15
#  Output radian: 0.261904
#  import math

def degree_to_radian(degrees):
    radians = degrees * (math.pi / 180)
    return radians
def main():
    degrees = float(input("Input degree: "))
    radians = degree_to_radian(degrees)
    print("Output radian:", radians)
if __name__ == "__main__":
    main()

# 2 - Write a Python program to calculate the area of a trapezoid.
#   Height: 5
#   Base, first value: 5
#   Base, second value: 6
#   Expected Output: 27.5
#  def trapezoid_area(height, base1, base2):
#     area = 0.5 * (base1 + base2) * height
#     return area

def main():
    height = float(input("Height: "))
    base1 = float(input("Base, first value: "))
    base2 = float(input("Base, second value: "))
    area = trapezoid_area(height, base1, base2)
    print("Expected Output:", area)

if __name__ == "__main__":
    main()

# 3 - Write a Python program to calculate the area of regular polygon.
#   Input number of sides: 4
#   Input the length of a side: 25
#   The area of the polygon is: 625

import math
def polygon_area(n, length):
    area = (n * length ** 2) / (4 * math.tan(math.pi / n))
    return area
def main():
    n = int(input("Input number of sides: "))
    length = float(input("Input the length of a side: "))
    area = polygon_area(n, length)
    print("The area of the polygon is:", area)
if __name__ == "__main__":
    main()
 
# 4 - Write a Python program to calculate the area of a parallelogram.
#   Length of base: 5
#   Height of parallelogram: 6
#   Expected Output: 30.0
def parallelogram_area(base_length, height):
    area = base_length * height
    return area
def main():
    base_length = float(input("Length of base: "))
    height = float(input("Height of parallelogram: "))
    area = parallelogram_area(base_length, height)
    print("Expected Output:", area)
if __name__ == "__main__":
    main()

# Date
# 1 - Write a Python program to subtract five days from current date.
# from datetime import datetime, timedelta
def subtract_days_from_current_date(days):
    current_date = datetime.now()
    result_date = current_date - timedelta(days=days)
    return result_date
def main():
    result_date = subtract_days_from_current_date(5)
    print("Current Date:", datetime.now().strftime("%Y-%m-%d"))
    print("Date five days ago:", result_date.strftime("%Y-%m-%d"))
if __name__ == "__main__":
    main()

# 2 - Write a Python program to print yesterday, today, tomorrow.
from datetime import datetime, timedelta
def get_dates():
    today = datetime.now().strftime("%Y-%m-%d")
    yesterday = (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d")
    tomorrow = (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d")
    return yesterday, today, tomorrow
def main():
    yesterday, today, tomorrow = get_dates()
    print("Yesterday:", yesterday)
    print("Today:", today)
    print("Tomorrow:", tomorrow)
if __name__ == "__main__":
    main()

# 3 - Write a Python program to drop microseconds from datetime.
from datetime import datetime
def drop_microseconds(dt):
    dt_without_microseconds = dt.strftime("%Y-%m-%d %H:%M:%S")
    return dt_without_microseconds
def main():
    current_datetime = datetime.now()
    datetime_without_microseconds = drop_microseconds(current_datetime)
    print("Datetime without microseconds:", datetime_without_microseconds)
if __name__ == "__main__":
    main()

# 4 - Write a Python program to calculate two date difference in seconds.
 from datetime import datetime
def date_difference_in_seconds(date1, date2):
    difference = date2 - date1
    difference_in_seconds = difference.total_seconds()
    return difference_in_seconds
def main():
    date1 = datetime(2022, 1, 1, 12, 0, 0)  
    date2 = datetime(2022, 1, 2, 12, 0, 0)  
    difference_seconds = date_difference_in_seconds(date1, date2)
    print("Difference between the two dates in seconds:", difference_seconds)
if __name__ == "__main__":
    main()

Generators
# 1 - Create a generator that generates the squares of numbers up to some number N.
def squares_generator(N):
    for i in range(N):
        yield i ** 2

# 2 - Write a program using generator to print the even numbers between 0 and n in comma separated form where n is input from console.
def even_numbers_generator(n):
    for i in range(n + 1):
        if i % 2 == 0:
            yield i

# 3 - Define a function with a generator which can iterate the numbers, which are divisible by 3 and 4, between a given range 0 and n.
def divisible_by_3_and_4_generator(n):
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

# 4 - Implement a generator called squares to yield the square of all numbers from (a) to (b). 
Test it with a "for" loop and print each of the yielded values.
def squares_generator(a, b):
    for i in range(a, b + 1):
        yield i ** 2

# 5 - Implement a generator that returns all numbers from (n) down to 0.
def countdown_generator(n):
    while n >= 0:
        yield n
        n -= 1

# Json
# Using data file sample-data.json, create output that resembles the following by parsing the included JSON file.
import json
with open('sample-data.json', 'r') as file:
    data = json.load(file)
output = ""
for item in data['people']:
    output += f"Name: {item['name']}\n"
    output += f"Age: {item['age']}\n"
    output += f"City: {item['city']}\n\n"
print(output)