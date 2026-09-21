'''
Question 22:
a. Open the file, in1_UserID.txt from your current working directory in read mode. Use tell() function to find out the position of cursor. What will the output? 
b. Use seek() function to read 11 characters from the beginning of file. Display the read characters on console. 
c. Use seek() function to read 11 characters from the end of file. Display the read characters on console. 
d. Now display the position of cursor using tell() function. Move the cursor to beginning of file using seek() function. Again display the position of cursor using tell() function.

Question 23:
a. Open the file, in1_UserID.txt from your current working directory in read mode. Read 11 characters from end of file. Display read characters on console.
b. Use seek(-13, 1) function then use readline() function to read one line. Display the read line on console. 
c. Use seek(5, 0) function then use readline() function to read one line. Display the read line on console. 
d. Now display the position of cursor using tell() function. 
'''

# Solution for Question 22
fd2 = open('in1_UserID.txt', 'r')
fd2_position = fd2.tell()
print(fd2_position)  # Output: 0 (initial position of cursor)
fd2.seek(0)  # Move cursor to the beginning of the file
print(fd2.read(11))  # Read 11 characters
fd2.seek(0, 2)  # Move cursor to the end of the file
print(fd2.tell())  # Display position of cursor
fd2.seek(fd2.tell() - 11)  # Move cursor 11 characters back from the end
print(fd2.read(11))
print(fd2.tell())  # Display position of cursor
fd2.seek(0)  # Move cursor to the beginning of the file
print(fd2.tell())  # Display position of cursor
fd2.close()

# Solution for Question 23:
# fd23 = open('in1_UserID.txt', 'r')
# fd23.seek(0, 2)  # Move cursor to the end of the file
# fd23.seek(fd23.tell() - 11)
# print(fd23.read(11))  # Read 11 characters from end of file



