print("34. Opening Files")
# open function
myFile = open("filename.txt")
myFile.close()
# argument is path to the file
# Specify mode to open the file, which is the second argument to open function
# "r" - read mode, default
# "w" - write
# "a" - append, adding new content to the end of the file
# "b" - binary mode, for non text files such as images and sound files
# write mode
open("filename.txt", "w")
# read mode
open("filename.txt", "r")
open("filename.txt")
# binary write mode
open("filename.txt", "wb")
# Use + sign with each of the modes above to give them extra access.
# r+ open the file for both read and writing
# Closing
file2 = open("filename.txt", "w")
# do stuff to the file
file2.close()


print("35. Reading Files")
# read method: myFile.read()
file = open("filename.txt", "r")
cont = file.read()
print(cont)
file.close()
# This will print all the contents of the filename.txt file
# To read certain amount of file (to read the number of bytes), we can provide the second argument
file = open("filename.txt", "r")
print(file.read(16))
print(file.read(4))
print(file.read())
file.close()
# Just like passing no arguments, negative values will return the entire contents
# After file is read, any re-read attempt will return an empty string
file = open("filename.txt", "r")
file.read()
print("Re-reading")
print(file.read())
print("Finished")
file.close()
# To retrieve each line in the file, use readlines method
# file.readlines()
# This will return a list which each element is a line in the file
file = open("filename.txt", "r")
print(file.readlines())
file.close()
# Can also use for loop for iteration
file = open("filename.txt", "r")
for line in file:
    print(line)
file.close()


print("36. Writing Files")
# write method: file.write(string)
file = open("newfile.txt", "w")
file.write("This has been written to a file")
file.close()
file = open("newfile.txt", "r")
print(file.read())
file.close()
# w mode will create a file if it does not already exists
# When file is opened in write mode, the file's existing content is deleted
file = open("newfile.txt", "r")
print("Reading initial contents")
print(file.read())
print("Finished")
file.close()
file = open("newfile.txt", "w")
file.write("Some new text")
file.close()
file = open("newfile.txt", "r")
print("Reading new contents")
print(file.read())
print("Finished")
file.close()
# write method returns the number of bytes (number of characters) written to a file
msg = "Hello World"
file = open("newfile.txt", "w")
amountWritten = file.write(msg)
print(amountWritten)
file.close()


print("37. Working with Files")
# make sure files are always closed
try:
    f = open("filename.txt")
    print(f.read())
finally:
    f.close()
# Alternate way is using with statement
with open("filename.txt") as f:
    print(f.read())
# File is automatically closed at the end of with statement