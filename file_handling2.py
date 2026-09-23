# Reading a file
# Reading a file can be achieved by file.read() which reads the entire content of the file. After reading its good practice to close the file to free up system resources.
file = open("geek.txt","r")
content = file.read()
print(content)
file.close()     # O/P is Hello world, GeeksforGeeks, 123 456

# Writing a file
# Writing a file is done using the mode "w". This creates a new file if it doesn't exist or overwrites the existing file if it does. The write() method is used to add content After writing make sure to close the file
with open("geeks.txt","w") as file:
    file.write("Hello, Python! \n")
    file.write("File handling is easy with Python.")
print("File written successfully")     # O/P is Hello, Python!  File Handlingg is easy with Python

# "w" mode opens the file for writing
# write() method adds new text to the file
# When using with the file closes automatically at the end of the block


# Using with Statement
# Instead of manually opening and closing the file you can use the with statement, which automatically handless closing. This reduce the risk of file corruption and resource leakage

with open("geeks.txt","r") as file:
    content = file.read()
    print(content)  # O/P is Hello, World!

# Handling Exceptions when closing a file
# It's important to handle exception to ensure that files are closed properly even if an error occurs during file operations. Here finally block ensures the file is closed even if an error occurs.

try:
    file = open("geek.txt","r")
    content = file.read()
    print(content)
except FileNotFoundError as e:
    print("Error :", e)
finally:
    file.close()    # Hello, world!

# try block contain code that may raise an error
# except block handles specific error like missing file
# finally block ensure the file is always closed even if an error occurs