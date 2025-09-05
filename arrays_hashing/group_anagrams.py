#Group Anagrams
# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

# time complexity: o(log k log n)
# for each word of length k: sorting costs O(k log k)
# you do that for n words → O(n · k log k)

#space complexity: o(n * k)
# dict stores up to n groups → O(n · k) in the worst case (since storing each word and its key).

def group_anagrams(strs):
    map = {}

    for str in strs:
        key = ''.join(sorted(str))
        if (key not in map):
            map[key] = []
        map[key].append(str)
    
    return list(map.values())

# Input: 
strs = ["eat","tea","tan","ate","nat","bat"]
print(group_anagrams(strs))
            


# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]