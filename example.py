# Python Iterators, Generators​ 
# 1
 mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)
print(next(myit))
print(next(myit))
print(next(myit))
# output:
# apple
# banana
# cherry

# 2
mystr = "banana"
myit = iter(mystr)
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
# output:
# b
# a
# n
# a
# n
# a

# 3
mytuple = ("apple", "banana", "cherry")
for x in mytuple:
  print(x)
#output:
# apple
# banana
# cherry

# 4
mystr = "banana"
for x in mystr:
  print(x)
#output:
# b
# a
# n
# a
# n
# a

# 5
class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self
  def __next__(self):
    x = self.a
    self.a += 1
    return x
myclass = MyNumbers()
myiter = iter(myclass)
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
#output:
# 1
# 2
# 3
# 4
# 5

# 6
class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self
  def __next__(self):
    if self.a <= 20:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration
myclass = MyNumbers()
myiter = iter(myclass)
for x in myiter:
  print(x)
#output:
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10
# 11
# 12
# 13
# 14
# 15
# 16
# 17
# 18
# 19
# 20




# Python Scope​ 
# 1
def myfunc():
  x = 300
  print(x)
myfunc()
#output:
# 300

# 2
def myfunc():
  x = 300
  def myinnerfunc():
    print(x)
  myinnerfunc()
myfunc()
#output:
# 300

# 3
x = 300
def myfunc():
  print(x)
myfunc()
print(x)
#output:
# 300
# 300

# 4
x = 300
def myfunc():
  x = 200
  print(x)
myfunc()
print(x)
#output:
# 200
# 300

# 5
def myfunc():
  global x
  x = 300
myfunc()
print(x)
#output:
# 300

# 6
x = 300
def myfunc():
  global x
  x = 200
myfunc()
print(x)
#output:
# 200




# Python Modules​ 
# 1
import mymodule
mymodule.greeting("Jonathan")
#output:
# Hello, Jonathan

# 2
import mymodule
a = mymodule.person1["age"]
print(a)
#output:
# 36

# 3
import mymodule as mx
a = mx.person1["age"]
print(a)
#output:
# 36

# 4
import platform
x = platform.system()
print(x)
#output:
# Windows

# 5
import platform
x = dir(platform)
print(x)
#output:
# ['DEV_NULL', '_UNIXCONFDIR', 'WIN32_CLIENT_RELEASES', 'WIN32_SERVER_RELEASES',
# '__builtins__', '__cached__', '__copyright__', '__doc__', '__file__', '__loader
# __', '__name__', '__package __', '__spec__', '__version__', '_default_architecture',
# '_dist_try_harder', '_follow_symlinks', '_ironpython26_sys_version_parser', 
# '_ironpython_sys_version_parser', '_java_getprop', '_libc_search', '_linux_distribution', 
# '_lsb_release_version', '_mac_ver_xml', '_node', '_norm_version', '_perse_release_file', 
# '_platform', '_platform_cache', '_pypy_sys_version_parser', '_release_filename', 
# '_release_version', '_supported_dists', '_sys_version', '_sys_version_cache', 
# '_sys_version_parser', '_syscmd_file', '_syscmd_uname', '_syscmd_ver', '_uname_cache', 
# '_ver_output', 'architecture', 'collections', 'dist', 'java_ver', 'libc_ver', 'linux_distribution', 
# 'mac_ver', 'machine', 'node', 'os', 'platform', 'popen', 'processor', 'python_branch', 'python_build',
# 'python_compiler', 'python_implementation', 'python_revision', 'python_version', 'python_version_tuple', 
# 're', 'release', 'subprocess', 'sys', 'system', 'system_aliases', 'uname', 'uname_result', 'version',
# 'warnings', 'win32_ver']

# Python Dates​ 
# 1
import datetime
x = datetime.datetime.now()
print(x)
#output:
# 2024-02-21 23:34:25.059001

# 2
import datetime
x = datetime.datetime.now()
print(x.year)
print(x.strftime("%A"))
#output:
# 2024
# Wednesday

# 3
import datetime
x = datetime.datetime(2020, 5, 17)
print(x)
#output:
# 2020-05-17 00:00:00

# 4
import datetime
x = datetime.datetime(2018, 6, 1)
print(x.strftime("%B"))
#output:
# June




# Python Math​ 
# 1
x = min(5, 10, 25)
y = max(5, 10, 25)
print(x)
print(y)
#output:
# 5
# 25

# 2
x = abs(-7.25)
print(x)
#output:
# 7.25

# 3
x = pow(4, 3)
print(x)
#output:
# 64

# 4
import math
x = math.sqrt(64)
print(x)
#output:
# 8.0

# 5
import math
x = math.ceil(1.4)
y = math.floor(1.4)
print(x)
print(y)
#output:
# 2
# 1

# 6
import math
x = math.pi
print(x)
#output:
# 3.141592653589793

# Python JSON​
# 1
import json
x = '{ "name":"John", "age":30, "city":"New York"}'
y = json.loads(x)
print(y["age"])
#output:
#30

# 2
import json
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}
y = json.dumps(x)
print(y)
#output:
# {"name": "John", "age": 30, "city": "New York"}
# 3
import json
print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))
#output:
# {"name": "John", "age": 30}
# ["apple", "bananas"]
# ["apple", "bananas"]
# "hello"
# 42
# 31.76
# true
# false
# null

# 4
import json
x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}
y = json.dumps(x)
print(y)
#output:
# {"name": "John", "age": 30, "married": true, "divorced": false, 
# "children": ["Ann","Billy"], "pets": null, "cars": [{"model": "BMW 230", "mpg": 27.5}, 
# {"model": "Ford Edge", "mpg": 24.1}]}

# 5
import json
x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}
print(json.dumps(x, indent=4))
#output:
# {
#     "name": "John",
#     "age": 30,
#     "married": true,
#     "divorced": false,
#     "children": [
#         "Ann",
#         "Billy"
#     ],
#     "pets": null,
#     "cars": [
#         {
#             "model": "BMW 230",
#             "mpg": 27.5
#         },
#         {
#             "model": "Ford Edge",
#             "mpg": 24.1
#         }
#     ]
# }

# 6
import json
x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}
print(json.dumps(x, indent=4, separators=(". ", " = ")))
#output:
# {
#     "name" = "John".
#     "age" = 30.
#     "married" = true.
#     "divorced" = false.
#     "children" = [
#         "Ann".
#         "Billy"
#     ].
#     "pets" = null.
#     "cars" = [
#         {
#             "model" = "BMW 230".
#             "mpg" = 27.5
#         }.
#         {
#             "model" = "Ford Edge".
#             "mpg" = 24.1
#         }
#     ]
# }

# 7
import json
x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}
print(json.dumps(x, indent=4, sort_keys=True))
#output:
# {
#     "age": 30,
#     "cars": [
#         {
#             "model": "BMW 230",
#             "mpg": 27.5
#         },
#         {
#             "model": "Ford Edge",
#             "mpg": 24.1
#         }
#     ],
#     "children": [
#         "Ann",
#         "Billy"
#     ],
#     "divorced": false,
#     "married": true,
#     "name": "John",
#     "pets": null
# }


