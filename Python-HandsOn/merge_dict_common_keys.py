'''
Merge Dictionaries with Common Keys
A single dictionary where values for overlapping keys are summed.
Input: [{'a': 1, 'b': 2}, {'b': 3, 'c': 4}, {'c': 5, 'd': 6}]
Output: {'a': 1, 'b': 5, 'c': 9, 'd': 6}
Input: [{'x': 10, 'y': 20}, {'y': 30, 'z': 40}, {'z': 50, 'x': 60}]
Output: {'x': 70, 'y': 50, 'z': 90}
'''


def merge_dict_common_keys(dict_list):
    my_dict = {}
    for item in dict_list:
        for key, value in item.items():
            if key in my_dict:
                my_dict[key] += value
            else:
                my_dict[key] = value
    return my_dict

print(merge_dict_common_keys([{'a': 1, 'b': 2}, {'b': 3, 'c': 4}, {'c': 5, 'd': 6}]))
print(merge_dict_common_keys([{'x': 10, 'y': 20}, {'y': 30, 'z': 40}, {'z': 50, 'x': 60}]))