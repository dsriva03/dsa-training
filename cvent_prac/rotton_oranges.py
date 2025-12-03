from collections import deque 

def rotton_oranges(grid):

    max_minute = 0

    q = deque()

    #gather all 2s

    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == 2:
                q.append((r,c, 0))


    while q:
        r, c, minute = q.popleft()
        #update max minute
        max_minute = max(minute, max_minute)
        #explore directions
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        for dr, dc in directions:
            nr = r + dr
            nc = c + dc
            #if in bounds + "1" , add to  queue
            if nr >= 0 and nr < len(grid) and nc >= 0 and nc < len(grid[0]) and grid[nr][nc] == 1:
                grid[nr][nc] == 2
                q.append((nr, nc, minute + 1))
    
    for o in grid:
        if o == 1:
            return -1
    
    return max_minute

        



