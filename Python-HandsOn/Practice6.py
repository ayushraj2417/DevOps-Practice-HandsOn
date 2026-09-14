'''
Question 14:
a. Read 2 numbers n1_UserID=100 and n2_UserID =200 from Commandline. Display the argv output on console.
b. Add n1_UserID and n2_UserID and store the result in another number whose name is sum_UserID. Display the sum_UserID on console. If you are not getting the correct output, give the justification.
c. For task (b), use casting operator int for n1_UserID and n2_UserID numbers. Display the sum_UserID on console.
d. Display how many commandline arguments passed. 
e. Display datatype of commandline arguments passed on console.


Question 15:
Write a python script commandline3_UserID.py for the below mentioned requirements. 
a. Pass 5 arguments 10, 20, 30, 40, 50 from commandline. 
b. Display only the first and third commandline arguments passed, on console.
c. Display the zeroth commandline ie. argv[0] argument on console.
d. Display how many commandline arguments passed, on console.
e. Find the average of all numbers and store in avg_UserID. Display avg_UserID on console. 

Question 16: 
a. Pass first 2 letters of your name as first command line argument.
b. Pass your employee number as second command line argument.
c. Add the first and second commandline arguments and store in “result_UserID” variable.
d. Display result_UserID on console. What will the output?

Question 17:
a. Pass first name of your name as first command line argument.
b. Pass @wipro.com as second command line argument.
c. Add the first and second commandline arguments and store in “result_UserID” variable.
d. Display result_UserID on console. What will the output?
'''

# Solution for Question 14 and 15:
import sys
user_input = sys.argv

if (len(user_input) - 1) == 2:
    print("Command line arguments passed are:", user_input)
    n1_userID = int(user_input[1])
    n2_userID = int(user_input[2])
    sum_userID = n1_userID + n2_userID
    print(f"Sum of {n1_userID} and {n2_userID} is: {sum_userID}")

elif (len(user_input) - 1) == 5:
    print("Command line arguments passed are:", user_input)
    first_arg = user_input[1]
    third_arg = user_input[3]
    print(f"first arguments is: {first_arg} and third argument is: {third_arg}")
    zeroth_arg = user_input[0]
    print(f"Zeroth argument is: {zeroth_arg}")
    total_args = len(user_input) - 1  # Exclude the script name
    print(f"Total command line arguments passed are: {total_args}")
    # Calculate average
    for num in user_input[1:]:
        numbers = [int(num)]
    avg_userID = sum(numbers) / len(numbers)
    print(f"Average of all numbers is: {avg_userID}")
else:
    print("Please provide exactly 2 or 5 numbers as command line arguments.")

# Solution for Question 16 and 17:
import sys
user_input = sys.argv
result_UserID = user_input[1] + user_input[2]
print(f"Result of adding first 2 letters of name and employee number is: {result_UserID}") 

