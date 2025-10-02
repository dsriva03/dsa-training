def valid_anagram_optimized(s,t):
    if len(s) != len(t):
        return False
    
    count = [0] * 26

    for char in s:
        c = ord(char) - ord("a")
        count[c] += 1
    #print("before t", count)

    for char in t:
         c = ord(char) - ord("a")
         count[c] -= 1
    #print("after t", count)

    return all(c == 0 for c in count)

print(valid_anagram_optimized("acecarr", "racecar"))
print(valid_anagram_optimized("thist", "shit"))