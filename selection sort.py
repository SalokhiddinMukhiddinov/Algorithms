def smallest(arr):
    small = arr[0]
    
    for i in arr:
        if i < small:
            small = i
    return small

def selection_sort(arr):
    new_arr = []
    copied_arr = list(arr)
    
    for i in range(len(arr)):
        small = smallest(copied_arr)
        new_arr.append(small)
        copied_arr.remove(small)
    return new_arr

def main():
    arr = [5, 3, 6, 2, 10]
    print("Unsorted array:", arr)
    sorted_arr = selection_sort(arr)
    print("Sorted array:", sorted_arr)

if __name__ == "__main__":
    main()