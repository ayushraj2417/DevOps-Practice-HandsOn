'''
Input : 3
Output:

  *
 ***
*****

'''

num = 3
myList = []
for row in range(num):
    spaces = ' ' * (num - row - 1)
    star = '*' * (2 * row + 1)
    myList.append(spaces+star+spaces)
print(myList)