#ex1 Open the file "demofile2.txt" and append content to the file:
f = open("demofile2.txt", "a")
f.write("Now the file has more content!")
f.close()
#open and read the file after the appending:
f = open("demofile2.txt", "r")
print(f.read())

#ex2 Open the file "demofile3.txt" and overwrite the content:
f = open("demofile3.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()
#open and read the file after the overwriting:
f = open("demofile3.txt", "r")
print(f.read())

#ex3 Create a file called "myfile.txt":
f = open("myfile.txt", "x")

#ex4 Create a new file if it does not exist:
f = open("myfile.txt", "w")

#ex1 
f = open("demofile.txt", "r")
print(f.read())

#ex2 Read Only Parts of the File
f = open("demofile.txt", "r")
print(f.read(5))    #Return the 5 first characters of the file:

#ex3 Read Lines
f = open("demofile.txt", "r")
print(f.readline())

#ex4 
f = open("demofile.txt", "r")
for x in f:
  print(x)

#ex5 Close the file when you are finish with it:
f = open("demofile.txt", "r")
print(f.readline())
f.close()

#ex1 Delete a File
import os
os.remove("demofile.txt")

#ex2 Check if File exist:
if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
else:
  print("The file does not exist")

#ex3 Delete Folder
#os.rmdir("myfolder")
