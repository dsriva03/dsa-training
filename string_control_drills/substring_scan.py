def substrings(s):
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            print(s[i:j])

substrings("abc")

def while_substrings(s):
    i = 0
    j = i + 1

    while i < len(s):
        while j <= len(s):
            print(s[i:j])
            j += 1
        i += 1

while_substrings("abc")