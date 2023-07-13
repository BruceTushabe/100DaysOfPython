def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else: 
        pivot = arr[-1]
        smaller = [x for x in arr[:-1] if x < pivot]
        greater = [x for x in arr[:-1] if x > pivot]
        return quicksort(smaller) + [pivot] + quicksort(greater)


input_str = input("Enter a list of numbers separated by space:")

input_arr = [int(x) for x in input_str.split()]

sorted_arr = quicksort(input_arr)

print (sorted_arr)

