def longestEvenSubstring(s):
    n = len(s)

    max_length = 0

    for i in range(n):
        #create freq array
        freq = [0] * 26
        #iterate from i to n
        for j in range(i, n):

            #populate array
            char = ord(s[j]) - ord('a')
            #check if counts are even
            freq[char] += 1
            #if even
            if all(count % 2 == 0 for count in freq):
                length = j - i + 1
                #if count is larger than max, update max
                if length > max_length:
                    max_length = length
        
    #return max

    return max_length

s = "aabccb"
print(longestEvenSubstring(s))