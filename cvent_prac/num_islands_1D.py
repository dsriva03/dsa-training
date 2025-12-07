# Given an array nums consisting only of integers 0 and 1, return the number of 1-islands in the array.

# A 1-island is defined as:

# a contiguous sequence of one or more 1s`

# surrounded by 0s or the boundaries of the array

# Constraints

# 1 <= len(nums) <= 10^5

# nums[i] is either 0 or 1

# The array may start or end with an island.

# You must solve it in O(n) time.


def num_islands(islands):
    count = 0

    for i in range(len(islands)):
        if islands[i] == 1 and (islands[i - 1] == 0 or i == 0):
            count += 1

    return count

nums = [1,1,0,1,0,0,1,1,1]
print(num_islands(nums))