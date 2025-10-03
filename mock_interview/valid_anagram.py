def valid_anagram(s: str, t: str) -> bool:

    #edge case
    if len(s) != len(t):
        return False



    #if input is lowercase only
    freq_arr = [0] * 26

    for char in s:
        c = ord(char) - ord("a")
        print("char", char)        
        print("char code", c)
        freq_arr[c] += 1
    
    for char in t:
        c = ord(char) - ord("a")
        freq_arr[c] -= 1
    
    return all(val == 0 for val in freq_arr)

    

print(valid_anagram("anagram", "nagaram"))
print(valid_anagram("", ""))

def valid_anagram_unicode(s: str, t: str) -> bool:
    counts = {}

    for char in s:
        counts[char] = counts.get(char, 0) + 1
    
    for char in t:
        counts[char] -= 1
    
    return all(val == 0 for val in counts.values())