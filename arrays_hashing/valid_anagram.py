# Valid Anagram
# Given two strings s and t, return true if t is an
# of s, and false otherwise.

#approach: create freq. maps of s and t, and check if they contain the same key value frequencies

def valid_anagram(s, t):
    if len(s) != len(t):
        return False
    
    sMap = {}
    tMap = {}

    #loop thru s and t
    for char in s:
        sMap[char] = sMap.get(char, 0) + 1
     
    for char in t:
        tMap[char] = tMap.get(char, 0) +1

    if sMap == tMap:
        return True

    return False;
print(valid_anagram("acecarr", "racecar"))
print(valid_anagram("thist", "shit"))