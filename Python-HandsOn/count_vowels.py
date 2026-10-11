'''
def count_vowels(s):

Example:
Plain Text
Input: "Hello, World!"Output: 3 Input: "Python Programming"Output: 4
'''

def count_vowels(s):    
    vowels = 'aeiouAEIOU'
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

print(count_vowels('Hello, World!'))
print(count_vowels('Python Programming'))