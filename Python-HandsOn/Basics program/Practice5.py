'''
Question 12:
a. Read 5 linux usernames from keyboard. The linux usernames are user1_UserID, user2_UserID, user3_UserID, user4_UserID, user5_UserID.
b. Store these usernames in list and name the list as userlist_UserID.
c. Read 5 CIS stream names from keyboard. The CIS stream names are unix_UserID, wintel_UserID, networking_UserID, helpdesk_UserID and bsm_UserID. 
d. Store these CIS stream names in list and name the list as stream_UserID.
e. Create a dictionary userdict_UserID. The key of dictionary is username stored in userlist_UserID. 
The value for corresponding key is stream name stored in stream_UserID. 
For example: 
Key1 -> user1_UserID and Value1 -> UNIX_UserID.
Key2 -> user2_UserID and Value2 -> WINTEL_UserID etc…..
Hint: Use for loop 

Question 13:
a. Pass 2 variables A_UserID and B_UserID from command line.
b. Pass condition to con1_UserID variable from keyboard.
c. If condition con1_UserID equals to “add” then do addition of 2 numbers. If condition con1_UserID equals to “sub” then do subtraction of 2 numbers.
d. If condition con1_UserID equals to “mul” then do multiplication of 2 numbers. If condition con1_UserID equals to “div” then do division of 2 numbers.
e. If there is no match for condition con1_UserID, then it should display “Enter proper input condition” on console.
 
'''

# Solution for Question 12:
userlist_UserID = []
for i in range(5):
    username = input(f"Enter linux username {i+1}: ")
    userlist_UserID.append(username)

stream_UserID = []
for i in range(5):
    streamname = input(f"Enter CIS stream name {i+1}: ")
    stream_UserID.append(streamname)

userdict_UserID = {}
for i in range(5):
    userdict_UserID[userlist_UserID[i]] = stream_UserID[i]

# Note: We have to unpack the dictionary to print the key and value pairs.
for key, value in userdict_UserID.items():
    print(f"Key -> {key} and Value -> {value}") 


# Solution for Question 13:

A_userID = int(input("Enter first number: "))
B_UserID = int(input("Enter second number: "))
con1_UserID = input("Enter condition (add/sub/mul/div): ")
match con1_UserID:
    case "add":
        result = A_userID + B_UserID
        print(f"Addition of {A_userID} and {B_UserID} is: {result}")
    case "sub":
        result = A_userID - B_UserID
        print(f"Subtraction of {A_userID} and {B_UserID} is: {result}")
    case "mul":
        result = A_userID * B_UserID
        print(f"Multiplication of {A_userID} and {B_UserID} is: {result}")
    case "div":
        result = A_userID / B_UserID
        print(f"Division of {A_userID} and {B_UserID} is: {result}")
    case _:
        print("Enter proper input condition")