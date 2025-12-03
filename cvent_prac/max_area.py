def max_area(grid):
    max_area = 0

    def dfs(r, c):
        if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or grid[r][c] == 0:
            return 0
        
        grid[r][c] = 0

        return 1 + dfs(r - 1, c) + dfs(r + 1, c) + dfs(r, c - 1) + dfs(r, c + 1)

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                area = dfs(i, j)
                max_area = max(max_area, area)
    
    return max_area

grid = [
    [1,1,0,0,0],
    [1,1,0,0,0],
    [0,0,0,1,1],
    [0,0,0,1,1]
]

print(max_area(grid))  # should return 4