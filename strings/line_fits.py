def line_fits(line, word, width):
    #find length of words in line
    len_words = 0
    for x in line:
        len_words += len(x)
    #find amount of underscores needed
    underscores = len(line)
    #find length of word
    new_word = len(word)

    #add them up 
    total = len_words + underscores + new_word

    #return <= width
    return total <= width
print(line_fits(["hi", "queen"], "how", 10))