'''
Binary to Decimal
Input: binary_str = "101"
Output: 5
 
Input: binary_str = "1101"
Output: 13

def binary_to_decimal(binary_str):
'''

def binary_to_decimal1(binary_str):
    return int(binary_str, 2)

def binary_to_decimal2(binary_str):
    # (2 ** 0) * 1 + 2 ** 1
    bin_str = binary_str[::-1]
    power = 0
    result = 0
    for digit in bin_str:
        result += (2 ** power) * int(digit)
        power += 1 
    return result

print(binary_to_decimal1('101'))
print(binary_to_decimal1('1101'))

print(binary_to_decimal2('101'))
print(binary_to_decimal2('1101'))