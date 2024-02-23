# task 1
# Write a Python program that matches a string that has an 'a' followed by zero or more 'b''s.
import re
pattern = re.compile(r'ab*')
def match_string(text):
    if pattern.fullmatch(text):
        return True
    else:
        return False

# task 2
# Write a Python program that matches a string that has an 'a' followed by two to three 'b'.
import re
pattern = re.compile(r'ab{2,3}')
def match_string(text):
    if pattern.fullmatch(text):
        return True
    else:
        return False

# task 3
# Write a Python program to find sequences of lowercase letters joined with a underscore.
import re
pattern = re.compile(r'[a-z]+_[a-z]+')
def find_sequences(text):
    return pattern.findall(text)

# task 4
# Write a Python program to find the sequences of one upper case letter followed by lower case letters.
import re
pattern = re.compile(r'[A-Z][a-z]+')
def find_sequences(text):
    return pattern.findall(text)

# task 5
# Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'.
import re
pattern = re.compile(r'a.*b$')
def match_string(text):
    if pattern.match(text):
        return True
    else:
        return False

# task 6
# Write a Python program to replace all occurrences of space, comma, or dot with a colon.
import re
def replace_chars(text):
    return re.sub(r'[ ,.]', ':', text)



# task 7
# Write a python program to convert snake case string to camel case string.
def snake_to_camel(snake_str):
    components = snake_str.split('_')
    return components[0] + ''.join(x.title() for x in components[1:])

# task 8
# Write a Python program to split a string at uppercase letters.
import re
def split_at_uppercase(text):
    return re.findall('[A-Z][^A-Z]*', text)


# task 9
# Write a Python program to insert spaces between words starting with capital letters.
import re
def insert_spaces(text):
    return re.sub(r'(?<!^)(?=[A-Z])', ' ', text)

# task 10
# Write a Python program to convert a given camel case string to snake case.
import re
def camel_to_snake(camel_str):
    return re.sub(r'(?<!^)(?=[A-Z])', '_', camel_str).lower()
print(camel_to_snake("camelCaseString")) 