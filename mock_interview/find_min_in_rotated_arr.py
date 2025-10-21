def find_min(nums):

    left = 0
    right = len(nums) - 1

    while left < right:
        mid = (left + right) // 2

        if nums[mid] > nums[right]:
            #min is on left side, move right
            left = mid + 1
        else:
            #move left to right side
            right = mid 
    return nums[left]
        
    
