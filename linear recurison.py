def sum_list(arr):
    # Base case: if the list is empty, return 0
    if not arr:
        return 0
    # Recursive case: sum the first element with the sum of the rest
    return arr[0] + sum_list(arr[1:])

# Example usage
data = [1, 2, 3, 4, 5]
result = sum_list(data)
print(f"The sum of the list is: {result}")
