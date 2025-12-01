def isIsomorphic(s, t):
    s_map = {}
    t_map = {}

    for i, char in enumerate(s):
        if char in s_map:
            if s_map[char] != t[i]:
                return False
        if t[i] in t_map:
            if t_map[t[i]] != char:
                return False
        
        s_map[char] = t[i]
        t_map[t[i]] = char
    
    return True
       