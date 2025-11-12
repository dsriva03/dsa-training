
# def func(inp, n):
#     words = inp.split()
#     line = []
#     lines = []
#     line_length = 0

#     for w in words:
#         if len(w) + line_length + len(line) > n:
#             lines.append(line)
#             line_length = len(w)
#             line = [w]
#         else:
#             line.append(w)
#             line_length += len(w)
    
#     if line:
#         lines.append(line)
    
#     def center(word, width):
#         total = width - len(word)
#         left = total // 2
#         right = total - left

#         return left*"_" + word + right*"_"


#     res = []

#     for line in lines:
#         if len(line) == 1:
#             res.append(center(line[0], n))
#         else:
#             joined = "_".join(line)
#             padding = n - len(joined)
#             res.append(joined + "_" * padding)

#     return resok






# for w in words:
#     if len(w) + len(line) + line_length <= n:
#         line.append(w)
#         line_length += len(w)
#     else:
#         if '-' in w:
#             parts = w.split('-')
#             chunks = []
#             for i in range(len(parts)):
#                 if i < len(parts) - 1:
#                     chunks.append(parts[i] + '-')
#                 else:
#                     chunks.append(parts[i])
#             for chunk in chunks:
#                 if line_length + len(line) + len(chunk) <= n:
#                     line.append(chunk)
#                     line_length += len(chunk)
#                 else:
#                     lines.append(line)
#                     line_length = len(chunk)
#                     line = [chunk]
#     else:
#         lines.append(line)
#         line = [w]
#         line_length = len(w)

# if line: 
#     lines.append(line)


# if '-' in w:
#     parts = w.split("-")
#     chunks = []
#     for i in range(len(parts)):
#         if i < len(parts) - 1:
#             chunks.append(parts[i] + "-")
#         else:
#             chunks.append(parts[i])
#     for chunk in chunks:
#         if line_length + len(chunk) + len(line) <= n:
#             line.append(chunk)
#             line_length += len(chunk)
#         else:
#             lines.append(line)
#             line = [chunk]
#             line_length += len(chunk)



def final(inp, n):
    lines = []
    line = []
    line_length = 0
    words = inp.split()

    for w in words:
        if line_length + len(w) + len(line) <= n:
            line.append(w)
            line_length += len(w)
        else:
            if "-" in w:
                parts = w.split("-")
                chunks = []
                for i in range(len(parts)):
                    if i < len(parts) - 1:
                        chunks.append(parts[i] + "-")
                    else:
                        chunks.append(parts[i])
                for chunk in chunks:
                    if len(chunk) + len(line) + line_length <= n:
                        line.append(chunk)
                        line_length += len(chunk)
                    else:
                        lines.append(line)
                        line = [chunk]
                        line_length = len(chunk)
            else:
                lines.append(line)
                line = [w]
                line_length = len(w)
    

    if line:
        lines.append(line)

    
    res = []

    def center(word, width):
        total = width - len(word)
        left = total // 2
        right = total - left

        return left*"_" + word + right*"_"
    
    for line in lines:

        if len(lines) == 1 and len(line) == 1 and not line[0].endswith('-'):
            res.append(center(line[0], n))
        else:
            joined = "_".join(line)
            padding = n - len(joined)
            res.append(joined + "_"*padding)
    return res

print(final("welcome to hacker rank", 10))
# ['welcome___', 'to_hacker_', 'rank______']

print(final("watermelon", 13))
# ['__watermelon__']

print(final("ultra-super-light-speed", 10))
# ['ultra-', 'super-', 'light-', 'speed_____']


