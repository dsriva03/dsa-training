def valid_anagram_map(s, t):
    if len(s) != len(t):
        return False

    sMap = {}
    tMap = {}

    for char in s:
        sMap[char] = sMap.get(char, 0) + 1
    
    for char in t: 
        tMap[char] = tMap.get(char, 0) + 1
    
    return sMap == tMap

print(valid_anagram_map("anagram", "nagaram"))  # True
print(valid_anagram_map("rat", "car"))          # False