def valid_pal(s):
    def is_pal(sub):
        l = 0
        r = len(sub) - 1

        while l < r:
            if sub[l] != sub[r]:
                return False
            l += 1
            r -= 1
        
        return True
    
    l = 0
    r = len(s) - 1

    while l < r:
        if s[l] != s[r]:
            left_del = is_pal(s[l + 1: r + 1])
            right_del = is_pal(s[l: r])

            return left_del or right_del
        
        l += 1
        r -= 1
    
    return True

print(valid_pal("racedcar")) #true
print(valid_pal("abcd")) #false
print(valid_pal("abba")) #true