# Initializing an empty Dictionary
Dictionary = {}
print("The empty Dictionary: ")
print(Dictionary)

# Inserting key:value pairs one at a time
Dictionary[0] = 'Java'
Dictionary[2] = 'Python'
Dictionary.update({ 3 : 'Dictionary'})
print("\nDictionary after addition of these elements: ")
print(Dictionary)

# Adding a list of values to a single key
Dictionary['list_values'] = 3, 4, 6
print("\nDictionary after addition of the list: ")
print(Dictionary)

# Updating values of an already existing Key
Dictionary[2] = 'Tutorial'
print("\nUpdated dictionary: ")
print(Dictionary)

# Adding a nested Key to our dictionary
Dictionary[5] = {'Nested_key' :{1 : 'Nested', 2 : 'Key'}}
print("\nAfter addtion of a Nested Key: ")
print(Dictionary)