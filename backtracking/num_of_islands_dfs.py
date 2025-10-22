def num_of_islands(grid):

    rows = len(grid)
    cols = len(grid[0])

    count = 0

    def dfs(r, c):

        #base case - of oob or 0 return
        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == "0":
            return 
        
        #otherwise sink
        grid[r][c] = "0"


        directions = [(-1, 0), (1,0), (0,-1), (0,1)]

        for dr, dc in directions:
            new_r = r + dr
            new_c = c + dc
            dfs(new_r, new_c) #needs to be in loop
    
    #iterate thru grid - if el is 1, count ++ and call dfs
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1":
                count += 1
                dfs(r, c)
    
    return count
        

