my_dict = {'banana': 3, 'apple': 4, 'pear': 1, 'orange': 2}

sorted_dict_by_keys = dict(sorted(my_dict.items()))
print("Dictionary sorted by keys:", sorted_dict_by_keys)

sorted_dict_by_only_value =  sorted(my_dict.values())
print("Dictionary sorted by values:", sorted_dict_by_only_value)

sorted_dict_by_values = dict(sorted(my_dict.items(), key=lambda item: item[1]))
print("Dictionary sorted by values:", sorted_dict_by_values)


