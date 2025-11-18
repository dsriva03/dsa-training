def winning_pair(nums, target):

    left = 0
    right = len(nums) - 1

    while (left < right):
        pair_sum = nums[left] + nums[right]
        if pair_sum == target:
            return [nums[left], nums[right]]
        elif pair_sum < target: 
            left += 1
        else:
            right -= 1
    
    return [-1,-1]


print(winning_pair([1,3,5,6,9], 9)) #[3,6]
print(winning_pair([1,3,4,5,6], 23)) #[-1,-1]