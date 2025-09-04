# Problem: Two Sum
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

#!brute force
#time complexity: o(n)^2 due to iterating twice over each element
#space: o(1) nothing new created in memory
def two_sum_brute(nums, target):
    #approach is: compare manually if elements in nums add up to target using two loops to check each number against eachother

    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
             #j will start after i 
             if nums[i] + nums[j] == target:
                return i, j
    
    return []

print("two_sum_brute:",two_sum_brute([1,222,2,1], 3))
print("two_sum_brute:",two_sum_brute([1,222,222,1], 212))



#?optimal
#time complexity: o(n) since we are iterating thru nums once
#space: o(n) since we are using a hashmap

def two_sum_optimal(nums, target):
    #approach is: create a hashmap to store each complement of nums[i] + indice. loop over nums, identify the missing part of target - nums[i]. if missing part is in hashmap, return indice of nums[i], complement

    seen = {}

    #use a for loop 
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return seen[complement], i #seen[complement] is indice
        seen[num] = i #store num and i as future complement
    return []
print(two_sum_optimal([1,222,222,1], 2))
print(two_sum_optimal([1,222,222,1], 12))