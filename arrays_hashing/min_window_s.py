from collections import Counter
from collections import defaultdict

def min_window(s, t):

    #freq map of t
    need = Counter(t)
    #rep of current window
    have = defaultdict(int) #flagging
    #needed number of chars to match - len(tfreq)
    required = len(need)
    #matchcount to compare to needed
    matchcount = 0
    #left
    l = 0
    #global min substring - return
    min_substring = ""
    #global min length
    min_length = float('inf') #! don't start at zero

    for r, char in enumerate(s):
        rc = s[r]
        #add right char to have
        have[rc] += 1

        #if right char is in need and have[rc] == need[rc]
        if rc in need and need[rc] == have[rc]:
            #increment our matchcount
            matchcount += 1

        #while matchcount is equal to req,
        while matchcount == required: #! keep while loop outside of if
            #we have a valid window,so
            #if window lenght is < global min length
            if r - l + 1 < min_length:
                min_length = r - l + 1
                #we update minlength, and min_substring
                min_substring = s[l:r +1] #! avoid off by one need plus one
            #immediately shrink from the left
            lc = s[l]
            have[lc] -= 1
            l += 1
            if lc in need and have[lc] < need[lc]: #! we can't just decrement if its in need, we need to see if it dropped below
                matchcount -= 1
                #removing leftChar's value from have
                #if leftChar is in need, -- matchcount

    #return min_substring
    return min_substring
