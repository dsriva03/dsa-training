"""
❗ Given a string s, return the first non-repeating character. If it doesn’t exist, return _.

Examples:

s = "aabbcd" → "c"

s = "aabb" → "_"

s = "leetcode" → "l"

You may assume s consists only of lowercase letters.
"""

def repeating_char(s):
    count = {}

    for char in s:
        count[char] = count.get(char, 0) + 1
    
    for char in s:
        if count[char] == 1:
            return char
    
    return "_"

print(repeating_char("leetcode"))