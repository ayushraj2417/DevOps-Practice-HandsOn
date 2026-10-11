'''
Decimal to Binary
def int_to_binary(n)

Input: n = 5
Output: "101"
 
Input: n = -5
Output: "-101"
'''

# 1st way
def int_to_binary1(n):
    result = bin(abs(n))[2:]
    if n >= 0: 
        return result
    else:
        return '-'+result

# 2nd way
def int_to_binary2(n):
    result = ''
    num = abs(n)
    while (num > 0):
        bit = num % 2
        result = str(bit) + result
        num = num // 2
    if n >= 0:
        return result
    else:
        return '-'+result

print(int_to_binary1(5))
print(int_to_binary1(-5))

print(int_to_binary2(5))
print(int_to_binary2(-5))