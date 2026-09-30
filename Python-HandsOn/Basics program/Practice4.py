'''
Question 10:
Create a string s1_UserID initialized with “we are learning Python”. 
a. Find the length of string s1_UserID and display on console.
b. Print how many times ‘e’ occurs in string s1_UserID.
c. What will be the output of s1_UserID.split(‘  ‘). Here ‘  ‘ is whitespace, which is delimiter.

Question 11:
a. Read num1_UserID with value 100 from keyboard
b. Read num2_UserID with value 200 from keyboard
c. Add num1_UserID and num2_UserID and store result in sum1_UserID. Display the result sum1_UserID on console. 
d. Is there any observation in output? Please give justification. 

Question 12:
a. Read 5 linux usernames from keyboard. The linux usernames are user1_UserID, user2_UserID, user3_UserID, user4_UserID, user5_UserID.
b. Store these usernames in list and name the list as userlist_UserID.
c. Display the elements of userlist_UserID list on console.
d. Display the elements of userlist_UserID on console using for loop. 
 
Hint: Use for loop "
'''

# Solution for Question 10:
s1_UserID = "we are learning Python"
length_of_string = len(s1_UserID)
print("Length of string s1_UserID:", length_of_string)
s1_UserID_count_e = s1_UserID.count('e')
print("Number of times 'e' occurs in string s1_UserID:", s1_UserID_count_e)
s1_User_ID_Split = s1_UserID.split(' ')
print("Output of s1_UserID.split(' '):", s1_User_ID_Split)

# Solution for Question 11:
num1_UserID = int(input("Enter the first number: "))
num2_UserID = int(input("Enter the second number: "))
sum1_UserID = num1_UserID + num2_UserID
print("The sum of num1_UserID and num2_UserID is:", sum1_UserID)

# Solution for Question 12:
userlist_UserID = ['user1_UserID', 'user2_UserID', 'user3_UserID', 'user4_UserID', 'user5_UserID']
print("Elements of userlist_UserID list:", userlist_UserID)
print("Elements of userlist_UserID list using for loop:")
for user in userlist_UserID:
    print(user)
