def longest_unique_sub(s):
    #create a set
    seen = set()

    #max variable = 0
    max_length = 0
    #define left p starting at zero 
    left = 0

    #iterate over input string 
    for right in range(len(s)):
        while s[right] in seen:
        #while s[right] is in seen
            #if so, shrink from the left
            seen.remove(s[left])
            left += 1
        #add char into our set
        seen.add(s[right])
        #update max
        max_length = max(max_length, len(seen))

    #return max
    return max_length


