def subsets(nums):
    res = []

    def backtrack(i, path):
        #base case 
        if i == len(nums):
            res.append(path[:])
            return
        
        #choice 1: add num to path
        backtrack(i + 1, path + [nums[i]])
        print("take it path: ", path)

        #choice 2: skip to next one
        backtrack(i + 1, path)
        print("leave it path: ", path)
    backtrack(0, [])
    
    return res


# print(subsets([1,2]))


def subsets_with_pop(nums):
    res = []

    def backtrack(i, path, depth = 0):
        indent = "  " * depth
        #base case
        if i == len(nums):
            res.append(path[:])
            print(f"{indent} -> base case reached - add {path[:]}")
            return
        
        #take it 
        print(f"{indent} -> take {nums[i]}")
        path.append(nums[i])
        backtrack(i + 1, path, depth + 1)
        print(f"{indent} -> back from deeper call, popping {nums[i]}")
        path.pop()

        #option 2 : skip
        print(f"{indent} -> skip {nums[i]}")
        backtrack(i + 1, path, depth + 1)

    backtrack(0, [])
    return res

print(subsets_with_pop([1,2]))