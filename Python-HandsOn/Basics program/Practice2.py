'''
Question 4:
Create a list mylist2_UserID consists of 10 elements.
Elements will have 5 numbers and 5 strings.
 
a. Print the contents of mylist2_UserID on console.
b. Add one element 100, at the end of list mylist2_UserID. Use appropriate function to do this task. Print the contents of mylist2_UserID on console.
c. Add one element “wipro”, at the end of list mylist2_UserID. Use appropriate function to do this task. Print the contents of mylist2_UserID on console.


Question 5:
Write a python script list2_UserID.py for the above mentioned requirements.
Hint: Use for loop to display the contents of list. Create a list mylist3_UserID consists of 5 elements. All Elements are strings. 
 
a. Print the contents of mylist3_UserID on console.
b. Add one element “Bangalore”, at the beginning of list mylist3_UserID. Use appropriate function to do this task. Print the contents of mylist3_UserID on console.
c. Remove one element from the end of list mylist3_UserID. Use appropriate function to do this task. Print the contents of mylist3_UserID on console.


Question 6:
Write a python script list3_UserID.py for the above mentioned requirements.
Hint: Use for loop to display the contents of list.
Create a list mylist4_UserID consists of 5 elements. All Elements are numbers. 
 
a. Print the contents of mylist4_UserID on console.
b. Use reverse() function on mylist4_UserID and display the contents on console.
c. Create another list, m1_UserID = [5, 10, 15]. Add this list m1_UserID at the end of mylist4_UserID list. Use appropriate function.
'''

# Solution for Question 4:
mylist2_UserID = [10, 20, 30, 40, 50, "apple", "banana", "cherry", "date", "elderberry"]

print("Contents of mylist2_UserID: ", mylist2_UserID)

mylist2_UserID.append(100)
print("Contents of mylist2_UserID after adding 100: ", mylist2_UserID)

mylist2_UserID.append("wipro")
print("Contents of mylist2_UserID after adding 'wipro': ", mylist2_UserID)


# Solution for Question 5:
mylist3_UserID = ["apple", "banana", "cherry", "date", "elderberry"]
print("Contents of mylist3_UserID: ", mylist3_UserID)
mylist3_UserID.insert(0, "Bangalore")
print("Contents of mylist3_UserID after adding 'Bangalore' at the beginning: ", mylist3_UserID)
mylist3_UserID.pop()
print("Contents of mylist3_UserID after removing the last element: ", mylist3_UserID)


# Solution for Question 6:
mylist4_UserID = [1, 2, 3, 4, 5]
for item in mylist4_UserID:
    print(item)

mylist4_UserID.reverse()   
print("Contents of mylist4_UserID after reversing: ", mylist4_UserID)
m1_UserID = [5, 10, 15]
mylist4_UserID.extend(m1_UserID)
print("Contents of mylist4_UserID after adding m1_UserID: ", mylist4_UserID)