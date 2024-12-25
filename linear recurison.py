def sum_list(arr):
    
    if not arr:
        return 0
    
    return arr[0] + sum_list(arr[1:])


data = [1, 2, 3, 4, 5]
result = sum_list(data)
print(f"The sum of the list is: {result}")

