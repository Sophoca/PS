N = int(input())
dice = list(map(int, input().split()))

if N == 1:
    print(sum(dice) - max(dice))
else:
    tempA = min(dice[0], dice[5])
    tempB = min(dice[2], dice[3])
    tempC = min(dice[1], dice[4])

    min3 = tempA + tempB + tempC
    min2 = min(tempA + tempB, tempB + tempC, tempC + tempA)
    min1 = min(tempA, tempB, tempC)
    print(4 * min3 + 4 * (2 * N - 3) * min2 + (N - 2) * (5 * N - 6) * min1)
