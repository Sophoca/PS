def main():
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    a, b = map(int, input().split())
    T = list(input())
    for t in T:
        idx = alphabet.index(t)
        while (idx - b) % a != 0:
            idx += 26
        print(alphabet[(idx - b) // a], end="")


if __name__ == "__main__":
    main()