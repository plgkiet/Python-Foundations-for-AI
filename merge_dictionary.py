dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
dict1.update(dict2)
print("Dictionary after merging: ", dict1)

dict3 = {'a': 1, 'b': 2}
dict4 = {'c': 3, 'd': 4}
merged_dict = {**dict3, **dict4}
print("Dictionary after merging: ", merged_dict)


dict5 = {'a': 1, 'b': 2}
dict6 = {'c': 3, 'd': 4}
print("Dictionary after merging: ", dict5 | dict6)
