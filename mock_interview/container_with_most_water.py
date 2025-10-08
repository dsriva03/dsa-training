def container(nums):
    l = 0
    r = len(nums) - 1

    max_area = 0

    while l < r:
        area = min(nums[l], nums[r]) * (r - l)

        max_area = max(area, max_area)

        if nums[l] < nums[r]:
            l += 1
        else:
            r -= 1
    
    return max_area


