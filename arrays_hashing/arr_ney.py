# 1) Baby Warmup — Arrays (5–10 min)

# Problem:
# Given an array of integers, return the index of the first number that is strictly greater than its left neighbor.
# If none exists, return -1.

# Examples:
# Input: [1,1,1,1] → -1
# Input: [1,2,1] → 1
# Input: [5,9,12,3] → 1
def arr_neighbor(nums):
    for i in range(len(nums) - 1):
        if nums[i + 1]:
            if nums[i] < nums[i + 1]:
                return i + 1
    
    return -1

print(arr_neighbor([1,1,1,1]))

