'''
Question 24:
a. Open the file, in1_UserID.txt from your current working directory in read mode. Read 11 characters from end of file. Display read characters on console.
b. Use seek(-13, 1) function then use readline() function to read one line. Display the read line on console. 
c. Use seek(5, 0) function then use readline() function to read one line. Display the read line on console. 
d. Now display the position of cursor using tell() function.

Question 25:
a. Open the file, newfile1_UserID.txt from your current working directory in read mode. This file is not there in current working directory. 
b. Which type of error will get for above mentioned scenario?
c. Handle the exception using different blocks such as try, except and finally for above mentioned scenario. 
'''

# Solution for question 24
file = open('in1_UserID.txt', 'r')
file.seek(0, 2)
file.seek(file.tell() - 11)
print(file.read(11))

# file.seek(-13, 1)
# print(file.tell())
# print(file.readline())

file.seek(5, 0)
print(file.tell())
print(file.readline())
print(file.tell())

# Solution for question 25

try:
    file25 = open('newfile2_UserID.txt', 'r')
    print(file25.read())
except FileNotFoundError as e:
    print("File is not available", e)
except Exception as e:
    print(e)
else:
    print("We can able to read the content of the file")
finally:
    print("We are working on file handling with exception handling...")
