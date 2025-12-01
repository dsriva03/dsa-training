def valid_anagram(s, t):

    if len(s) != len(t):
        return False
    
    count = {}


    for char in s:
        count[char] = count[char].get(0, count[char]) + 1

    for i in range(len(s)):
        if s[i] in count:
            count[s[i]] += 1
        else:
            count[s[i]] = 1
    
    for j in range(len(t)):
        if t[j] in count:
            count[t[j]] -= 1
        else:
            return False
    
    for key in count:
        if count[key] != 0:
            return False
    
    return True
                   