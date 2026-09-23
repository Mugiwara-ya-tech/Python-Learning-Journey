# File Handling refer to the process of performing operation on a file such as creating, opening, reading, writing and closing it through a programming interface.
# It involves managing the data flow between the ensuring that data is handled safely and efficiently

'''
Need for file handling

1. Stores data permanently even after the programs ends
2. Access external files like .txt, .csv, .json etc
3. Process large files efficiently without using much memory
4. Automate taks like reading configs or saving output
'''

# Opening a file
# To open a file we can use open() function which requires fiel-path and mode as arguments

#               file = open('filename.txt','mode')
# filename.txt  -> name (or path) of the file to be opened
# mode  -> mode in which you want to open the file (read, write, append etc)

# Note:- If you dont specify the mode, Python uses 'r' (read mode) by default

f = open("geek.txt","r")
print(f)


# Closing a file
# file.close() method closes the file and releases the System resources. If the file was opened in write or append mode, closing ensure that all changes are properly saved

file = open("geek.txt","r")
file.close()

# Checking the file properties
# Once the file is open we can check some of its properties

f = open("geek.txt","r")
print("Filename :", f.name)         # O/P is Filename: geek.txt
print("Mode :",f.mode)              # O/P is r
print("Is Closed?",f.closed)        # O/P is Is Closed? False
f.close()
print("Is Closed?",f.closed)        # O/P is Is Closed? True

# f.name  -> Returns the name of the file that was opened
# f.mode  -> Tells us the mode in which the file was opened
# f.closed  -> Returns a boolean value- False when file is currently open otherwise True.