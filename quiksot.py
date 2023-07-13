def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else: 
        pivot = arr[-1]
        smaller = [x for x in arr[:-1] if x < pivot]
        greater = [x for x in arr[:-1] if x > pivot]
        return quicksort(smaller) + [pivot] + quicksort(greater)
    
    print(quicksort([10,5]))
