def unique_paths(m, n):

    dp = []

    for _ in range(m):
        dp.append([1] * n)

    for r in range(1, m):
        for c in range(1, c):
            dp[r][c] = dp[r-1][c] + dp[r][c-1]
    
    return dp[-1][-1]