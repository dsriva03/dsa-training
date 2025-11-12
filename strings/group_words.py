def group_words(words, width):
    res = []

    line, curr = []
    line_len = 0

    for w in words:
        if line_len + len(w) + len(line) > width:
            res.append("_".join(line))
            line, line_len = [], 0
        line.append(w)
        line_len += len(w)
    
    if line:
        res.append("_".join(line))



            




#underscore, new word, and current length needs to be less than width to add new word
#otherwise, add current array to res and restart
#if line is not empty at end, add remaining block to res

def func(words, width):


    res = []
    curr = []

    curr_len = 0

    for w in words:
        if len(curr) + len(w) + curr_len <= width:
            curr.append(w)
            curr_len += len(w)
        else:
            res.append("_".join(curr))
            curr = [w]
            curr_len = len(w)
    
    if curr != []:
        res.append("_".join(curr))
    
    return res


print(func(["hi","queen","how","are","you"], 10))
# expected → ['hi_queen', 'how_are', 'you']




        






    

