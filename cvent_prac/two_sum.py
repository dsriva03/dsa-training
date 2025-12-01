def two_sum(nums, target):
    seen = {}

    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        
        seen[num] = i


print(two_sum([2,3,4,5,6], 8)) #[0, 4]
print(two_sum([-2,3,-4,-5,-6], 1)) #[0, 1]
print(two_sum([2,3,4,5,6], 9)) #[2, 3]
print(two_sum([3,3,3,3,3], 6)) #[0, 1]
