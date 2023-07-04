#BigO

def linear_search (1st, target):
    low = 0
    high = len(1st) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = 1st [mid]

        if guess == target;
            return True
        elif guess < target:
            low = mid + 1
        else :
            high = mid - 1
    return False

