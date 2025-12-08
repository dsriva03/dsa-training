def almost_palindrome(s):
    #helper to check if palindrome
    def is_pal(sub):
        l = 0
        r = len(sub) - 1

        while l < r:
            if sub[l] != sub[r]:
                return False
            l += 1
            r -= 1
        return True
    
    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return is_pal(s[left + 1: right + 1]) or is_pal(s[left:right])
        left += 1
        right -= 1
    
    return True #no mismatch means it is a palindrome




print(almost_palindrome("racecar")) #true
print(almost_palindrome("abca")) #true
print(almost_palindrome("abc")) #false
print(almost_palindrome("deeee")) #true
print(almost_palindrome("cbbcc")) #true

