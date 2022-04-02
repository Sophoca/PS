def main():
    numbers = list(map(int, input().split()))
    N = int(input())
    for idx in range(1, N + 1):
        numbers.extend(list(map(int, input().split())))
        numbers.sort()
        print(numbers[idx], numbers[idx * 2 + 1])


if __name__ == "__main__":
    main()