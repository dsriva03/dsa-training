def valid_anagram_one_map(t, s):
    if len(s) != len(t):
        return False

    counts = {}
    
    for char in s:
        counts[char] = counts.get(char, 0) + 1
    
    for char in t:
        if char not in counts: 
            return False
        
        counts[char] -= 1

        if counts[char] < 0:
            return False
    
    return True

print(valid_anagram_one_map("anagram", "nagaram"))  # True
print(valid_anagram_one_map("rat", "car"))          # False