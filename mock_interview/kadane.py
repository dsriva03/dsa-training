# You’re given an integer array nums. I want you to find the contiguous subarray (at least one element) that has the largest possible sum, and return that sum.

# For example:

# Input: [-2,1,-3,4,-1,2,1,-5,4]

# Output: 6
# (that’s the subarray [4,-1,2,1])

# Constraints: O(n) time, O(1) extra space.

def kadane(nums: list[int]) -> int:

    #declare maximum sum
    max_sum = nums[0]

    #declare running sum to keep track of as we sweep
    curr_sum = nums[0]

    for i in range(len(nums)):

        #add running sum to nums[i]
        #if nums[[i] + runningSum is smaller than nums[i], leave behind currentSum and update to nums[i] to start fresh
        curr_sum = max(nums[i], nums[i] + curr_sum)

        #update maximum sum
        max_sum = max(curr_sum, max_sum)

    
    #return maximum sum
    return max_sum