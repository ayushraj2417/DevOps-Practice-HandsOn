'''
Question 20:
a. Open the file, newfile1_UserID.txt from your current working directory in read mode. This file is not there in current working directory. What will the output? 
b. Write string s1_UserID=“This is the newline added at end” to the newfile1_UserID.txt file. Display the content of newfile1_UserID.txt file on console. 
c. Again write, string s1_UserID=“This is the newline added at end” to the newfile1_UserID.txt file. Display the content of newfile1_UserID.txt file on console. Any observation w.r.t output?

Question 21:
a. Use file in1_UserID.txt which was created in python script fileio1_UserID.py
b. Open the file in1_UserID.txt  in read mode as follows: 
fd1=open(“in1_UserID.txt”, “r”)
c. What will the output of fd1.name
d. What will the output of fd1.closed
e. What will the output of fd1.mode
f. Close the file using fd1.close(). Then find out the output of fd1.closed and display on console.
'''

# file = open("newfile1_UserID.txt", "r")
#print(file.read()) # FileNotFoundError: [Errno 2] No such file or directory: 'newfile1_UserID.txt'
#file.close()
file = open("newfile1_UserID.txt", "w")
s1_UserID = 'This is the newline added at end'
file.write(s1_UserID)

file = open("newfile1_UserID.txt", "r")
content = file.read()
print(content)

file = open("newfile1_UserID.txt", "a")
s2_UserID = '\nThis is the second newline added at end'
file.write(s2_UserID)
file.close()

fd1 = open("newfile1_UserID.txt", "r")
print(fd1.name)  # Output: newfile1_UserID.txt
print(fd1.closed)  # Output: False
print(fd1.mode)  # Output: r
fd1.close()
print(fd1.closed)  # Output: True