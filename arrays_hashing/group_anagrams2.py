# You’re given an array of strings. You need to group the anagrams together.

# An anagram is a word formed by rearranging the letters of another.

# You should return the groups in any order.

# Each group contains words that are anagrams of each other.

# Constraints:

# 1 <= len(strs) <= 10^4

# 0 <= len(str) <= 100

# Strings contain only lowercase English letters.

def groupAnagrams(strs: list[str]) -> list[list[str]]:
    #create a map to store sorted anagrams as keys, and matching anagrams in arrays
    dict = {}
    for string in strs:
        sorted_str = tuple(sorted(string))
        if sorted_str not in dict.keys():
            dict[sorted_str] = []
        dict[sorted_str].append(string)
    
    return list(dict.values())
        
             
print(groupAnagrams(["cat", "tac", "dog", "god", "ogd"])) #[[cat, tac], [dog, god, ogd]]
print(groupAnagrams([" ", " "])) #[[" ", " "]]
