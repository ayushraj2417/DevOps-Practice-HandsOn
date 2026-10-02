'''
Function to return a hollow right-angled triangle of '*' of side n as a list of strings.
input n = 5
 
*
**
* *
*  *
*****
'''

n = 5
myList = []

for row in range(1, n + 1):
    if (row == 1) or (row == n):
        myList.append('*' * row)
    else:
        spaces = ' ' * (row - 2)
        myList.append('*' + spaces + '*')
print(myList)