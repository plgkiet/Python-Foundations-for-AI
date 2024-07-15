my_list = [1,2,3,4,5]
print('My list: ', my_list)

my_list.append(6)
print('After appending 6: ', my_list)

my_list.insert(2,7)
print("After inserting 7 at index 2:", my_list)

my_list.remove(3)
print("After removing 3:", my_list)

another_list = [1, 2, 7, 4, 5, 6]
if my_list == another_list:
    print("Lists are equal.")
else:
    print("Lists are not equal.")

print("Length of the list:", len(my_list))

my_list.clear()
print("Cleared list:", my_list)

