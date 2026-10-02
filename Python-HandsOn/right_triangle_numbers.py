'''
Right Angled Triangle with Numbers
 
Input: 5
Output: ['1', '22', '333', '4444', '55555']
Input: 3
Output: ['1', '22', '333']

1
22
333
'''

import sys

# 1st method
num = int(sys.argv[1])
list1 = []
list2 = []
for row in range(1, num + 1):
    list1.append(str(row) * row)
print(list1)

# 2nd method
for row in range(1, num + 1):
    item = ''
    for col in range(row):
        item += str(row)
    list2.append(item)
print(list2)