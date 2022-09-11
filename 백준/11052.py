N = int(input())
cost = [0] + list(map(int, input().split()))
dp = [0] * (N + 1)

for idx in range(1, N + 1):
    dp[idx] = cost[idx]
    for compare in range(1, idx + 1):
        dp[idx] = max(dp[compare] + dp[idx - compare], dp[idx])

print(dp[N])
