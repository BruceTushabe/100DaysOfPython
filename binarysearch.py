from typing import List

def binary_search(self, nums: List[int], target: int) -> int:
    #Set search space equal to sorted list
    low = 0
    high = len(nums) - 1

    while low <= high:
        # Get the middle element of the search space

        mid = (high + low) // 2

        # Compare middle element to target

        if nums[mid] == target:
            return mid
        
        if target < nums[mid]:
            high = mid - 1

        else :
            low = mid + 1
    return -1 

nums = [1,2,3,4,5,6,7,8,9,10]

print(binary_search(nums, target))

