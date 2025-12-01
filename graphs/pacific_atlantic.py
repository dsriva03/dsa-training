def pacific_atlantic(heights):
    if not heights:
        return []

    def dfs(r, c, visited, heights):
        
        #if visited
        if (r, c) in visited: 
            return
        
        #otherwise, mark visited
        visited.add((r,c))

        directions = [(-1,0), (1,0), (0,-1), (0,1)]

        for dr, dc in directions:
            nr, nc = r + dr, c + dc

            #if in bounds
            if nr >= 0 and nr <= len(heights)-1 and nc >= 0 and nc <= len(heights[0]) - 1:
                #if larger
                if heights[nr][nc] >= heights[r][c]:
                    dfs(nr, nc, visited, heights)


