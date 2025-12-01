def valid_parenthesis(str):

    key = {
        "(": ")",
        "{": "}",
        "[": "]"
    }

    stack = []

    for char in str:
        if char == "[" or char == "{" or char == "(":
            stack.append(char)
        elif char == "]" or char == ")" or char == "}":
            if len(stack) == 0:
                return False
            if key[stack.pop()] != char:
                return False
        else:
            return False
    
    return len(stack) == 0





