def merge_intervals(nums):

    if not nums:
        return []
    #sort nums in place
    nums.sort(key=lambda x: x[0])

    #res
    res = [nums[0]]


    #loop through nums
    for start, end in nums[1:]:
        last_end = res[-1][1]

        if start < last_end:
            #update 
            res[-1][1] = max(res[-1][1], end)
        else:
            res.append([start, end])

    return res












def merge(nums):
    nums.sort(key=lambda x: x[0])

    res = [nums[0]]

    for start, end in nums[1:]:
        #check if beginning of start is < end. 
        if start < res[-1][1]:

            #if so, update end interval of res[-1]
            res[-1][1] = max(end, res[-1][1])
        else:
            #if not, they dont overlap so append
            res.append([start, end])


    return res

