def valid_parens(str):
    map = {
        ")":"(",
        "}":"{",
        "]":"["
    }

    stack = []

    for char in str:
        if char == "(" or char == "[" or char == "{":
            stack.append(char)
        if map[char] == stack[len(stack)-1]:
            stack.pop(char)
    
    if len(stack) == 0:
        return True
    return False
