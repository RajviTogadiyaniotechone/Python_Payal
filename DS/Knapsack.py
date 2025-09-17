def knapsack(W, wt, v):
    n = len(wt)
    dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]

    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                dp[i][w] = 0  
            elif wt[i - 1] <= w:    
                dp[i][w] = max(v[i - 1] + dp[i - 1][w - wt[i - 1]], dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]
    
    return dp[n][W]  

profit = [100, 150, 120]
weight = [10, 20, 35]
W = 50

print(knapsack(W, weight, profit))
