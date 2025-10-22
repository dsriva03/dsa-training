def combination_sum(candidates, target):
    res = []

    def backtrack(i, path, total):

        #i base case
        if i == len(candidates):
            res = []
        #base case
        if total > target:
            return
        
        if total == target:
            res.append(path[:])
            return
        #take it
        path.append(candidates[i])
        backtrack(i, path, total + candidates[i])
        path.pop()
        #leave it
        backtrack(i + 1, path, total)
    
    backtrack(0, [], 0)
    return res
