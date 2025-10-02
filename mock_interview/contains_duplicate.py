# ‘You’re given an array of integers. Return true if any value appears at least twice, otherwise false.’

#brute force - compare every element against each other
def contains_dupe_brute(nums):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j]:
                return True
    
    return False

#SORT = sort and compare

def contains_dupe_sort(nums):
    sortedNums = sorted(nums)

    for i in range(len(sortedNums) - 1): #dont go out of bounds
        if sortedNums[i] == sortedNums[i + 1]:
            return true
    
    return False

#optimized

def contains_dupe_optimal(nums):
    seen = set()

    for i in range(len(nums)):
        if nums[i] in seen:
            return True
        
        seen.add(nums[i])

    return False