#BigO

def binary_search(list, target):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = list [mid]
        
        
        if guess  == target:
            
            return  True 
    
    
        elif guess < target:
            low = mid + 1

        else:
            
            high = mid - 1
            
    return False


my_list = [1, 3, 5, 7, 9]

print (binary_search(my_list, 3))
print (binary_search(my_list, -1))
print (binary_search(my_list, 9))
print (binary_search(my_list, 4))