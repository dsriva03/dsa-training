def threeSum(nums):

    result = []

    s = sorted(nums)

    for i in range(len(s)):

        #dupe check
        if i > 0 and s[i] == s[i-1]:
            continue

        #use l and r pointers
        l = i + 1
        r = len(s) - 1

        while l < r:
            #calculate total
            total = s[i] + s[l] + s[r]
            #if total == 0,
            if total == 0:
                #add result to list
                result.append([s[i], s[l], s[r]])
                #move pointers forward
                l += 1
                r -= 1
                #check for duplicates - if l - 1 or r + 1 is dupe, move up again
                while l < r and s[l] == s[l-1]:
                    l += 1
                while l < r and s[r] == s[r + 1]:
                    r -= 1
            #if total is < 0
            elif total < 0:
                l += 1
                #move l up 
            #otherwise, move r down
            else:
                r -= 1


    #return res
    return result
        
