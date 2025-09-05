# 283. Move Zeroes
# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# Note that you must do this in-place without making a copy of the array.
#* approach: pack array with nonzeroes in the front, then overwrite rest with zeroes . do two passes
#* overwrite indexes where checkLastZero is 
def move_zeroes(nums):
    checkLastZero = 0 #c
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[checkLastZero] = nums[i]
            checkLastZero += 1
    
    for i in range(checkLastZero, len(nums)):
        nums[i] = 0
    print(nums)

move_zeroes([0,1,0,3,12])

# Example 1:

# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]

# Example 2:

# Input: nums = [0]
# Output: [0]

