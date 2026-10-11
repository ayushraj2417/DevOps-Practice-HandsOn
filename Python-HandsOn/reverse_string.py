'''
def reverse_string(s):
    """
    Function to return the reversed version of the input string.
    Parameters:
    s (str): The input string to be reversed.
    Returns:
    str: The reversed string.
    """
'''
#1st way
def reverse_string1(s):
    return s[::-1]
#2nd way
def reverse_string2(s):
    return ''.join(reversed(s))

print(reverse_string1('Hello World'))
print(reverse_string1('Ayush'))

print(reverse_string2('Hello World'))
print(reverse_string2('Ayush'))
