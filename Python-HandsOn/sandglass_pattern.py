'''
Function to return a sandglass pattern of '*' of side n as a list of strings.
Input n = 3
 
*****
 ***
  *
 ***
*****

'''
n = 3
myList = []
for row in range(n, 0 , -1):
    stars = '*' * (2 * row - 1)
    spaces = ' ' * (n - row)
    print(spaces + stars + spaces)

for row in range(2, n + 1):
    stars = '*' * (2 * row - 1)
    spaces = ' ' * (n - row)
    print(spaces + stars + spaces)
