'''
Question 7:
Create a tuple mytuple1_UserID consists of 10 elements. All Elements are numbers. 
a. Print the contents of tuple mytuple1_UserID on console.
b. Add new element to this tuple as follows:
mytuple1_UserID[1] = 100. What will be the output and give justification for this.

Question 8:
Create an dictionary dict1_UserID as follows: 
dict1_UserID = {“k1” : 10,  “k2” : 20,  “k3” : 30}
a. Print the dictionary dict1_UserID on console.
b. Print all the keys in dictionary dict1_UserID. Use appropriate function.
c. Print all the values in dictionary dict1_UserID. Use appropriate function.

Question 9:
Create an dictionary dict2_UserID as follows: 
dict2_UserID = {“Bangalore” : 1,  “Chennai” : 2,  “Kochi” : 3}
a. Print the dictionary dict2_UserID on console.
b. Add new element to dictionary dict2_UserID. 
Key is “Hyderabad” and value is 4. Print the dictionary dict2_UserID.
c. Delete the key “Kochi” from the dictionary dict2_UserID. Print the dictionary dict2_UserID.
d.  Delete all the elements of dictionary dict2_UserID using appropriate function. Print the dictionary dict2_UserID.
'''

# Solution for Question 7:
mytuple1_UserID = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print("Contents of mytuple1_UserID: ", mytuple1_UserID)
# mytuple1_UserID[1] = 100  # This will raise a TypeError because tuples are immutable in Python.

# Solution for Question 8:
dict1_UserID = {"k1": 10, "k2": 20, "k3": 30}
for key, value in dict1_UserID.items():
    print(f"Key: {key}, Value: {value}")
print("Keys in dict1_UserID: ", dict1_UserID.keys())
print("Values in dict1_UserID: ", dict1_UserID.values())

# Solution for Question 9:
dict2_UserID = {"Bangalore": 1, "Chennai": 2, "Kochi": 3}
print("Contents of dict2_UserID: ", dict2_UserID)
dict2_UserID["Hyderabad"] = 4
print("After adding Hyderabad: ", dict2_UserID)
del dict2_UserID["Kochi"]
print("After deleting Kochi: ", dict2_UserID)
dict2_UserID.clear()
print("After clearing all elements: ", dict2_UserID)