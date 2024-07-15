my_dict = {
    'name' : 'phamlegiakiet',
    'age' : 20,
    'city' : 'binhduong'
}
print("Initial Dictionary",  my_dict)

# Adding a new key-value pair to the dictionary
my_dict['profession'] = 'SoftWare Engineer'
print("After adding profession:", my_dict)

# Updating the value of an existing key
my_dict['age'] = 21
print("After updating age:", my_dict)

# Removing a key-value pair from the dictionary
del my_dict['city']
print("After removing city:", my_dict)

# Iterating through the dictionary keys and values
print("Dictionary elements:")
for key, value in my_dict.items():
    print(f"{key}: {value}")