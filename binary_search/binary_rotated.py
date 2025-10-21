def binary_search_rotated(nums, target):
    #identify sorted half of array
    left = 0
    right = len(nums) - 1
    #compare nums[mid] w target

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid

        if nums[left] <= nums[mid]:
            #left is sorted, check if target lies
            if nums[left] <= target < nums[mid]:
                right = mid - 1

            else:
                #target is not in left side, move left pointer right
                left = mid + 1
        else:
            #left is unsorted, move right and check if target is in right side
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                #move right pointer to the left
                right = mid - 1
    
    return - 1





            

