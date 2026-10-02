'''
input = 3

'  *  '

' *** '

'*****'

' *** '

'  *  '
 
'''

n = 3 
myList1 = []
for row in range(1, n + 1):
    spaces = ' ' * (n - row)
    stars = '*' * (row * 2 - 1)
    myList1.append(spaces + stars + spaces)

for row in range(2, 0, -1):
    spaces = ' ' * (n - row)
    stars = '*' * (row * 2 - 1)
    myList1.append(spaces + stars + spaces)
print(myList1) 