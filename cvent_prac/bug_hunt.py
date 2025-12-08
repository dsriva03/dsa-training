def check_pal(s):
    left = 0
    right = len(s) #len(s) - 1

    while left <= right: #left < right
        if s[left] != s[right]:
            return False
        left += 1 
        right += 1 #right -=1
    return True