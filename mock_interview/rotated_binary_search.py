def rotated_binary_search(nums, target):

    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right ) // 2
        print(f"nums[mid]={nums[mid]}, target={target}, nums[right]={nums[right]}")
        if nums[mid] == target:
            return mid
        #check sorted side
        if nums[left] <= nums[mid]:
            #check if target is found 
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
        
    return -1


print(rotated_binary_search([6,7,0,1,2,3,3,5], 7))