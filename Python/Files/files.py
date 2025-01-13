f = open("Python/Files/demofile.txt", "rt")

# To open the file, use the built-in open() function.

# The open() function returns a file object, which has a read() method for reading the content of the file:

f = open("Python/Files/demofile.txt", "r")
# print(f.read())

# By default the read() method returns the whole text, but you can also specify how many characters you want to return:
# print(f.read(5))

# You can return one line by using the readline() method:
# print(f.readline())

# By calling readline() two times, you can read the two first lines:
# print(f.readline())
# f.close()

#By looping through the lines of the file, you can read the whole file, line by line:
f = open("Python/Files/demofile.txt", "r")
for x in f:
    print(x)
f.close()

# Close Files
# It is a good practice to always close the file when you are done with it.
# f = open("Python/Files/demofile.txt", "r")
# print(f.readline())
# f.close()

# Note: You should always close your files, in some cases, due to buffering, changes made to a file may not show until you close the file.

# Write to an Existing File
# To write to an existing file, you must add a parameter to the open() function:
# f = open("Python/Files/demofile.txt", "a")
# f.write("Now the file has more content!")
# f.close()

# Open the file "demofile2.txt" and overwrite the content:
f = open("Python/Files/demofile2.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()

# Create a New File
# To create a new file in Python, use the open() method, with one of the following parameters:
# "x" - Create - will create a file, returns an error if the file exist
# "a" - Append - will create a file if the specified file does not exist
# "w" - Write - will create a file if the specified file does not exist

# f = open("Python/Files/demofile3.txt", "x")
# f = open("Python/Files/demofile4.txt", "w")

# Delete a File
# To delete a file, you must import the OS module, and run its os.remove() function:
import os
os.remove("Python/Files/demofile2.txt")

# Check if File exist
# To avoid getting an error, you might want to check if the file exists before you try to delete it:
if os.path.exists("Python/Files/demofile2.txt"):
    os.remove("Python/Files/demofile2.txt")
else:
    print("The file does not exist")

# Delete Folder
# To delete an entire folder, use the os.rmdir() method:
# os.rmdir("Python/Files/MyFolder")

# Note: You can only remove empty folders.
