'''
Input: 5
Output:

*****
*   *
*   *
*   *
*****

'''

import sys

def hollow_square_1(num):
    myList = []
    for row in range(num):
        start = ''
        for col in range(num):
            if (row==0) or (row == num-1) or (col==0) or (col== num-1):
                start += '*'
            else:
                start += ' '
        myList.append(start)
    print(myList)

def hollow_square_2(num):
    myList = []
    for row in range(num):
        if (row == 0 or row == num-1):
            myList.append(num * '*')
        else:
            myList.append('*'+' '*(num-2)+'*')
    print(myList)

num = int(sys.argv[1])
hollow_square_1(num)
hollow_square_2(num)
