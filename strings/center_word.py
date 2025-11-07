def center_word(word, width):
    rem_space = width - len(word)
    left_amount = rem_space // 2
    right_amount = rem_space - left_amount

    return "_" * left_amount + word + "_" * right_amount

print(center_word("watermelon", 11))
