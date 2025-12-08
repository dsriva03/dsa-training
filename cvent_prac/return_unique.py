def return_unique(s):
    seen = set()
    res = ""

    for char in s:
        if char in seen:
            continue
        seen.add(char)
        res += char
    

    return res