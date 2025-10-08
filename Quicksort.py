# Find the maximum element in an array using recursion
def maximumus(arr):
    if len(arr) == 1:
        return arr[0]
    
    elif len(arr) == 0:
        return None
    
    else:
        max_rest = maximumus(arr[1:])
        return arr[0] if arr[0] > max_rest else max_rest
    
def main():
    arr = [3, 5, 2, 8, 1, 20, 40, 100, 99]
    print("Array:", arr)
    max_value = maximumus(arr)
    print("Maximum value:", max_value)  
    
if __name__ == "__main__":
    main()
        
    
# Quicksort implementation
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quicksort(left) + middle + quicksort(right)