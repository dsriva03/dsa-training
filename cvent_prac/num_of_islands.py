def num_of_islands(grid):

    def dfs(r, c):

        #if out of bounds - return
        if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]):
            return
        #if water - return
        if grid[r][c] == 0:
            return

        #turn 1 into 0
        grid[r][c] = 0

        #call dfs on adjacent 1s
        dfs(r - 1, c)
        dfs(r + 1, c)
        dfs(r, c - 1)
        dfs(r, c + 1)
    
    count = 0 

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                count += 1
                dfs(i, j)
    
    return count



print(num_of_islands([[1,1,1,1], 
                      [1,0,1,1]])) #1
            


