# “Alright. Classic warm-up. You’re given an array of integers and a target. Return the indices of the two numbers that add up to the target. Assume exactly one valid pair exists. Let’s go.”

def two_sum (nums: list[int], target: int) -> list[int]:

    seen = {}
    
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
        
    
    return []




print(two_sum([1,2,3,45], 5))
print(two_sum([1,2,2,1,1], 3))
print(two_sum([-3,-1,4,-5], -8))


def two_sum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    
    return []