# You’re given an array of strings. You need to group the anagrams together.

# An anagram is a word formed by rearranging the letters of another.

# You should return the groups in any order.

# Each group contains words that are anagrams of each other.

# Constraints:

# 1 <= len(strs) <= 10^4

# 0 <= len(str) <= 100

# Strings contain only lowercase English letters.

def groupAnagrams(strs):
    map = {}
    for str in strs:
        chars = [0] * 26
        for ch in str:
            c = ord(ch) - ord('a')
            chars[c] += 1
            #print(chars)
        key = tuple(chars)
        if key not in map.keys():
            map[key] = []
        map[key].append(str)
    print(list(map.values()))
    return list(map.values())

print(groupAnagrams(['red', 'der', 'cat', 'tac', 'erd'])) #[[red, der, erd], [cat, tac]]