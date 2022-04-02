def calc(num):
    dp = [0] * 11
    dp[1] = 1
    dp[2] = 2
    dp[3] = 4
    for idx in range(4, 11):
        dp[idx] = dp[idx - 1] + dp[idx - 2] + dp[idx - 3]
    return dp[num]


for _ in range(int(input())):
    print(calc(int(input())))
