def num_of_islands(grid):

    count = 0

    def dfs(r, c):

        directions = [(0, -1), (0, 1), (-1, 0), (1,0)]

        if grid[r][c] == "0":
            return 
        
        if r >= 0 and r <= len(grid) - 1 and c >= 0 and c <= len(grid[0]):
            for dr, dc in directions:
                dfs(r + dr, c + dc)
        else:
            return 


    
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "1":
                count += 1
                dfs(i, j)
    return count


