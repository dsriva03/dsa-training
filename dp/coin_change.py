def coin_change(coins, total):
    dp = [float('inf')] * (total + 1)

    dp[0] = 0

    for c in coins:
        for x in range(c, total + 1):
            dp[x] = min(dp[x], 1 + dp[x-c])
    
    if dp[total] != float('inf'):
        return dp[total]
    else:
        return -1
    

print(coin_change([1,2,5], 11))  # → 3
print(coin_change([2], 3))       # → -1
print(coin_change([1], 0))       # → 0
