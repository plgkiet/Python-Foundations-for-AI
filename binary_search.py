def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2

        if target < arr[mid]:
            right = mid - 1
        elif target > arr[mid]:
            left = mid + 1
        else:
            return mid

    return -1


arr = [12, 24, 32, 39, 45, 50, 54] 
target = 45 

result = binary_search(arr, target)

if result != -1:
    print(f"Element is present at index {result}")
else:
    print("Element is not present in array")




