def dfs(x, y):
    if x == N - 1 and y == N - 1:
        return 1
    if dp[x][y] == -1:
        dp[x][y] = 0
        if board[x][y] + x < N:
            dp[x][y] += dfs(board[x][y] + x, y)
        if board[x][y] + y < N:
            dp[x][y] += dfs(x, board[x][y] + y)
    return dp[x][y]


N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
dp = [[-1] * N for _ in range(N)]
print(dfs(0, 0))
