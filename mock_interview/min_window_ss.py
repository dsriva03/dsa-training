from collections import Counter
from collections import defaultdict

def min_win(s, t):
    #need
    need = Counter(t)
    #have
    have = defaultdict(int)
    #matchcount
    matchcount = 0
    #goal count
    goal = len(need)
    #left 
    left = 0
    #min substring 
    min_substring = ''
    #min substring len
    min_len = float('inf')


    for right, char in enumerate(s):
        have[char] += 1

        if char in need and have[char] == need[char]:
            matchount += 1

        while matchcount == goal:
            
            curr_len = r - l + 1
            
            if curr_len < min_len:
                min_substring = s[l: r+1]
                min_len = curr_len
            
            #shrink
            have[s[left]] -= 1
            left += 1

            if s[left] in need and have[s[left]] < need[s[left]]:
                matchcount -= 1
            
    return min_substring

