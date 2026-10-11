'''
Design a Python function named count_word_frequency to count the frequency of words in a sentence and store the counts in a dictionary.
 
Input: "hello world hello"
Output: {'hello': 2, 'world': 1}
'''

def count_word_frequency(sentence):
    myList = sentence.split()
    word_count = {}
    for word in myList:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count

print(count_word_frequency("hello world hello")) 