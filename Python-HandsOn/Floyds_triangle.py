'''
Function to return the first n rows of Floyd's Triangle as a list of strings.
Input 3:
1
2 3
4 5 6
'''

def floyds_triangle(n):
    myList1 = []
    count = 1
    for row in range(1, n + 1):
        item  = ''
        for col in range(row):
            item += str(count) + ' '
            count += 1
        myList1.append(item.strip())
    return myList1

print(floyds_triangle(3))