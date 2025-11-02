def word_break(s, wordDict):
    dp = [False] * (len(s) + 1)

    dp[0] = True

    for i in range(1, (len(s) + 1)):
        for j in range(i):
            if s[j:i] in wordDict and dp[j]:
                dp[i] = True
    
    return dp[-1]
