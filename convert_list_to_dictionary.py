list_of_tuples = [('a', 1), ('b', 2), ('c', 3)]
dictionary = dict(list_of_tuples)
print("Dictionary from list of tuples:", dictionary)

keys = ['a', 'b', 'c']
values = [1, 2, 3]
dictionary = dict(zip(keys, values))
print("Dictionary from two lists:", dictionary)

