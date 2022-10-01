def solution(k):
    cases = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]
    dp = [0] * 61

    if k == 1:
        return 0

    if k == 6:
        dp[6] = 1

    for i in range(1, 10):
        dp[cases[i]] += 1

    print(dp)
    for i in range(2, k):
        print(i)
        for j in range(10):
            dp[i + cases[j]] += dp[i]
            print(i, j, dp)
        print('---------')

    return dp[k]

print(solution(5))