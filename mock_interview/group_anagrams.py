# Given an array of strings, group the anagrams together. Return them in any order.

def group_anagrams_sorted(strs: list[str]) -> list[list[str]]:
    group = {}

    for str in strs:
        sortedStr = "".join(sorted(str))
        if sortedStr not in group:
            group[sortedStr] = []
        group[sortedStr].append(str)
    
    return list(group.values())


print( group_anagrams_sorted(["cat", "dog", "tac", "god"]))
    

def group_anagrams_optimal(strs: list[str]) -> list[list[str]]:

    group = {}

    for str in strs:
        counts = [0] * 26
        for char in str:
            c = ord(char) - ord("a")
            counts[c] += 1
        countTuple = tuple(counts)
        if countTuple not in group: 
            group[countTuple] = []
        
        group[countTuple].append(str)

    print(group.values())
    return list(group.values())

print( group_anagrams_optimal(["cat", "dog", "tac", "god"]))
