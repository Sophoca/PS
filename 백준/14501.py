# start: 18:48 -> end: 20: 07

N = int(input())

T, P, dp = [0], [0], [0]
for _ in range(N):
    t, p = map(int, input().split())
    T.append(t)
    P.append(p)
    dp.append(p)
dp.append(0)

for day in range(N, 0, -1):
    if day + T[day] > N + 1:
        dp[day] = dp[day + 1]
    else:
        dp[day] = max(dp[day + 1], P[day] + dp[day + T[day]])

print(max(dp))