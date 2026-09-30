'''
Question 26:
a. Read num1_UserID with value 100 and num2_UserID with value 0 from keyboard.
b. Use casting operator int( ) on num1_UserID and num2_UserID. Then, divide num1_UserID by num2_UserID and store result in div1_UserID. Display the result div1_UserID on console. 
c. Which type of error will get for above mentioned scenario?
d. Handle the exception using different blocks such as try, except and finally for above mentioned scenario. 

Question 27:
a. Create an dictionary dict3_UserID as follows: 
dict3_UserID = {“k1” : 10,  “k2” : 20,  “k3” : 30}
b. Print the dict3_UserID[“k5”] on console.
c. Which type of error will get for above mentioned scenario?
d. Handle the exception using different blocks such as try, except and finally for above mentioned scenario.
'''

# Solution for question 26:
num1_UserID = int(input("Enter the first number: "))
num2_UserID = int(input("Enter the second number: "))

try:
    div1_UserID = num1_UserID / num2_UserID
    print(div1_UserID)
except ZeroDivisionError as e:
    print("Number is not divided by zero", e)
else:
    print("Operation successfully done")
finally:
    print("DONE")


# Solution for ques 27:
dict3_UserID = {'k1' : 10,  'k2' : 20,  'k3' : 30}
mylist = [10, 20, 30, 40]
num1 = 20
num2 = 30
try:
    print(dict3_UserID['k5'])
    print(mylist[6])
except KeyError as e:
    print("Key is not defined", e)
except IndexError as e:
    print("Index is not defined", e)
finally:
    print("printing key and value")

print(num1 - num2)

