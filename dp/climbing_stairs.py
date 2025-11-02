def climbing_stairs(n):
    #build out dp array
    dp = [0] * (n + 1) 

    #base cases
    dp[0] = 1
    dp[1] = 1
 

    #recurrence
    for x in range(2, n + 1):
        dp[x] = dp[x - 1] + dp[x - 2]
        print(dp)
    
    return dp[n]

print(climbing_stairs(5))
