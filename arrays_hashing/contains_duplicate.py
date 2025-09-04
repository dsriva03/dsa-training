# Problem: Contains Duplicate
# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

def contains_duplicate(nums):
    #approach: use a set to track iterated elements, return true if set already contains element
    #time complexity: o(n), iterating once thru nums
    #space complexity: o(n), creating set in memory
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False

print(contains_duplicate([1,2,2,1])) #TRUE
print(contains_duplicate([1,2,12,15])) #FALSE