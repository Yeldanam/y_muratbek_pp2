# 1
from functools import reduce 
 
def multiply_list_numbers(lst): 
    result = reduce(lambda x, y: x*y, lst) 
    return result 
 
# Example usage 
numbers = [1, 2, 3, 4, 5] 
result = multiply_list_numbers(numbers) 
print(f"The result of multiplying all the numbers in the list {numbers} is: {result}")

# 2
def count_upper_lower(string): 
    upper_count = sum(1 for char in string if char.isupper()) 
    lower_count = sum(1 for char in string if char.islower()) 
    return upper_count, lower_count 
 
if name == "__main__": 
    user_input = input("Enter a string: ") 
    upper_count, lower_count = count_upper_lower(user_input) 
    print(f"Number of uppercase letters: {upper_count}") 
    print(f"Number of lowercase letters: {lower_count}")

# 3
def is_palindrome(string): 
    # Remove spaces and convert to lowercase for case-insensitive comparison 
    cleaned_string = string.replace(" ", "").lower() 
    # Check if the cleaned string is equal to its reverse 
    return cleaned_string == cleaned_string[::-1] 
 
if name == "__main__": 
    user_input = input("Enter a string: ") 
    if is_palindrome(user_input): 
        print("The string is a palindrome.") 
    else: 
        print("The string is not a palindrome.")

# 4
import time 
import math 
 
def square_root_after_milliseconds(milliseconds): 
    time.sleep(milliseconds / 1000)  
    number = float(input("Enter a number to calculate its square root: ")) 
    square_root = math.sqrt(number) 
    print(f"The square root of {number} is {square_root}") 
 
if name == "__main__": 
    milliseconds = int(input("Enter the number of milliseconds to wait: ")) 
    square_root_after_milliseconds(milliseconds)

# 5
def all_true(tuple_of_bools): 
    return all(tuple_of_bools) 
 
if name == "__main__": 
    tuple_of_bools = (True, True, True, False) 
    if all_true(tuple_of_bools): 
        print("All elements in the tuple are True.") 
    else: 
        print("Not all elements in the tuple are True.")




# 1
import os 
 
def ldirfiles(path): 
    print("Directories:") 
    for item in os.listdir(path): 
        if os.path.isdir(os.path.join(path, item)): 
            print(item) 
 
    print("\nFiles:") 
    for item in os.listdir(path): 
        if os.path.isfile(os.path.join(path, item)): 
            print(item) 
 
def lalldirfiles(path): 
    print("All Directories and Files:") 
    for root, dirs, files in os.walk(path): 
        for dir in dirs: 
            print(os.path.join(root, dir)) 
        for file in files: 
            print(os.path.join(root, file)) 
 
if name == "__main__": 
    sp = input("Enter the specified path: ") 
 
    print("\nListing directories and files in the specified path:") 
    ldirfiles(sp) 
 
    print("\nListing all directories and files in the specified path:") 
    lalldirfiles(sp)
# 2
import os 
 
def check_access(path): 
    if os.path.exists(path): 
        print(f"'{path}' exists.") 
    else: 
        print(f"'{path}' does not exist.") 
        return  
    if os.access(path, os.R_OK): 
        print(f"'{path}' is readable.") 
    else: 
        print(f"'{path}' is not readable.") 
    if os.access(path, os.W_OK): 
        print(f"'{path}' is writable.") 
    else: 
        print(f"'{path}' is not writable.") 
    if os.access(path, os.X_OK): 
        print(f"'{path}' is executable.") 
    else: 
        print(f"'{path}' is not executable.") 
 
if name == "__main__": 
    specified_path = input("Enter the specified path: ") 
    check_access(specified_path)
# 3
import os 
 
def path_details(path): 
    if os.path.exists(path): 
        print(f"The path '{path}' exists.") 
        directory = os.path.dirname(path) 
        print(f"Directory portion: '{directory}'") 
        filename = os.path.basename(path) 
        print(f"Filename portion: '{filename}'") 
    else: 
        print(f"The path '{path}' does not exist.") 
 
if name == "__main__": 
    specified_path = input("Enter the path: ") 
    path_details(specified_path)
# 4
def count_lines_in_file(file_path): 
    try: 
        with open(file_path, 'r') as file: 
            lines = sum(1 for line in file) 
        print(f"The file '{file_path}' contains {lines} lines.") 
    except FileNotFoundError: 
        print(f"The file '{file_path}' was not found.") 
    except Exception as e: 
        print(f"An error occurred: {e}") 
 
if name == "__main__": 
    file_path = input("Enter the path to the text file: ") 
    count_lines_in_file(file_path)
# 5
def write_list_to_file(file_path, data): 
    try: 
        with open(file_path, 'w') as file: 
            for item in data: 
                file.write(str(item) + '\n') 
        print(f"The list has been successfully written to the file '{file_path}'.") 
    except Exception as e: 
        print(f"An error occurred: {e}") 
 
if name == "__main__": 
    my_list = ['apple', 'banana', 'orange', 'grape'] 
    file_path = input("Enter the path for the file to write the list to: ") 
    write_list_to_file(file_path, my_list)

# 6
import os 
import string 
def generate_alphabet_files(directory): 
    if not os.path.exists(directory): 
        os.makedirs(directory) 
     
    for letter in string.ascii_uppercase: 
        filename = f"{letter}.txt" 
        filepath = os.path.join(directory, filename) 
        with open(filepath, 'w') as file: 
            file.write(f"This is the file for letter {letter}.\n") 
    print(f"Generated 26 text files named A.txt, B.txt, ..., Z.txt in '{directory}'.") 
 
if name == "__main__": 
    directory = "alphabet_files" 
    generate_alphabet_files(directory)

# 7
def copy_file(source_path, destination_path): 
    try: 
        with open(source_path, 'r', encoding='utf-8') as source_file, \ 
             open(destination_path, 'w', encoding='utf-8') as destination_file: 
            content = source_file.read() 
            destination_file.write(content) 
        print(f"Contents copied from {source_path} to {destination_path}.") 
    except FileNotFoundError: 
        print("The source file does not exist.") 
    except Exception as e: 
        print(f"An error occurred: {e}") 
 
if name == "__main__": 
    source_path = input("Enter the source file path: ") 
    destination_path = input("Enter the destination file path: ") 
    copy_file(source_path, destination_path)
# 8
import os 
def delete_file_if_possible(file_path): 
    if not os.path.exists(file_path): 
        print(f"The file '{file_path}' does not exist.") 
        return 
 
    if not os.access(file_path, os.W_OK): 
        print(f"The file '{file_path}' is not writable (permission denied).") 
        return 
    try: 
        os.remove(file_path) 
        print(f"The file '{file_path}' has been successfully deleted.") 
    except Exception as e: 
        print(f"An error occurred while trying to delete the file: {e}") 
if name == "__main__": 
    specified_path = input("Enter the path of the file to be deleted: ") 
    delete_file_if_possible(specified_path)
