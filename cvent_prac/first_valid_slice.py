def first_valid_slice(s):
    curr = ""
    has_num = False
    has_al = False

    for char in s:
        if char.isalnum():
            curr += char
            if char.isalpha():
                has_al = True
            if char.isdigit():
                has_num = True
        else:
            if has_al and has_num:
                return curr
            else:
                curr = ""
                has_al = False
                has_num = False
    
    if has_al and has_num:
        return curr
    
    return "NONE"