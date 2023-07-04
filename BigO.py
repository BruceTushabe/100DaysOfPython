#BigO

def linear_search (list, target):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = list [mid]

        if guess == target:
            return True
        elif guess < target:
            low = mid + 1
        else :
            high = mid - 1
    return False

