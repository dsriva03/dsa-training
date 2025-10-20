def subsets(nums):
    res = []

    def backtrack(i, path):
        #base case 
        if i == len(nums):
            res.add(path)
        
        #choice 1: add num to path
        backtrack(i, path)

        #choice 2: skip to next one
        backtrack(i + 1, path)
    
    return res


print(subsets([1,2]))