def is_subsequence(s, t):
    i = 0 # s pointer
    j = 0 # t pointer
    for j in range(len(t)):

        if t[j] == s[i]:
            i += 1
            if i == len(s):
                return True
    
    return False


# print(is_subsequence("abc", "abcd")) #true
print(is_subsequence("fgb", "fbg")) #false
# print(is_subsequence("ghhd", "ruty")) #false
# print(is_subsequence("rfg", "arjfng")) #true