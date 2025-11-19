def shortest_subarray(nums, target):

    min_length = float('inf')
    window_sum = 0
    

    left = 0

    
    for right in range(len(nums)):
        #sum
        window_sum += nums[right]

        while window_sum >= target:
            min_length = min(min_length, (right - left) + 1)
            window_sum -= nums[left]
            left += 1

    if min_length == float('inf'):
        return 0
    
    return min_length


