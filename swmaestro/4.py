def main():
    N = int(input())
    menu = list(map(int, input().split()))
    count = 0
    for i in range(N - 2):
        for j in range(i + 1, N - 1):
            for k in range(j + 1, N):
                if 2000 <= menu[i] + menu[j] + menu[k] <= 2500:
                    count += 1
    print(count)


if __name__ == "__main__":
    main()
