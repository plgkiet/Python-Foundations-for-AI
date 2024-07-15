def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    
    return -1

arr = [12, 24, 32, 39, 45, 50, 54] 
target = 45 

result = linear_search(arr, target)
if result != -1:
    print(f"Element is present at index {result}")
else:
    print("Element is not present in array")


