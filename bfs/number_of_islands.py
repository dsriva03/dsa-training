from collections import deque

def num_of_islands_bfs(grid):
    rows = len(grid)
    cols = len(grid[0])

    count = 0

    directions = [(-1,0), (1,0), (0,-1), (0,1)]

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1":
                count += 1 
                #sink island
                grid[r][c] = "0"
                #create queue #add coord to queue
                q = deque([(r,c)])
                #while queue is vaild:
                while q:
                    row, col = q.popleft()
                #pop first in line
                    for dr, dc in directions:
                        new_r = row + dr
                        new_c = col + dc
                #process coords - delta directions
                #if coords not oob and are not "0"
                        if new_r >= 0 and new_r <= rows  - 1 and new_c >= 0 and new_c <= cols - 1 and grid[new_r][new_c] == "1":
                            grid[new_r][new_c] = "0"
                            q.append((new_r, new_c))
                        #turn into 0
                        #add to queue
    return count




grid = [
  ["1","1","0","0"],
  ["1","0","0","1"],
  ["0","0","1","1"]
]
print(num_of_islands_bfs(grid))  # → 2
