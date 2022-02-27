T = int(input())
tc = [int(input()) for i in range(T)]
print(tc)

dp = [0] * 41
dp[1] = 1
for i in range(2, 41):
    dp[i] = dp[i - 1] + dp[i - 2]
