def backspace_string_compare(s, t):

    sStr = ""
    tStr = ""

    for c in s:
        if c != "#":
            sStr += c
        else:
            sStr -= c
    
    for c in t:
        if c != "#":
            tStr += c
        else:
            tStr -= c
    

    return sStr == tStr