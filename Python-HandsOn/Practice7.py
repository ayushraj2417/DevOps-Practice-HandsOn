'''
Question 18:
in1_UserID.txt  File
We are learning file input output operation in Python
Completed learning w.r.t command line arguments topic
CIS trainings going on well"	
a. Use file in1_UserID.txt which was created in python script fileio1_UserID.py. 
b. Use the read() function to read the 11 characters from the beginning of file in1_UserID.txt and display read information on console.
c. Use the readline() function to read first line from file in1_UserID.txt and display read information on console. Any observation w.r.t output?
d. Use read() function to read the content of file in1_UserID.txt and display read information on console."	0
e. Read the entire content of file in1_UserID.txt and display on console.

Question 19:
a. Use file in1_UserID.txt which was created in python script fileio1_UserID.py 
b. Use the readlines() function to read line by line from file in1_UserID.txt and store result in list1_UserID. Display list1_UserID on console.
c. Display size of list,  list1_UserID on console.
d. Use close() function to close the file handler. Then read all the content of file using read() function. What will be the output?
'''

# Solution for Question 18:
file = open('in1_UserID.txt', 'w')
file.write("We are learning file input output operation in Python\n")
file.write("Completed learning w.r.t command line arguments topic\n")
file.write("CIS trainings going on well\n")

file = open('in1_UserID.txt', 'r')
print(file.read(11))
print(file.readline())
print(file.read())
file.seek(0)  # Reset the file pointer to the beginning of the file
print(file.read())
file.close()

# Solution for Question 19:
file = open('in1_UserID.txt', 'r')
list1_UserID = file.readlines()
print(list1_UserID)
print(len(list1_UserID))
file.close()

print(file.read()) # This will raise a ValueError because the file is already closed. You cannot read from a closed file.


