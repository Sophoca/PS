def main():
    N = int(input())
    keywords = []
    for _ in range(N):
        keywords.append(input())

    T = int(input())
    for _ in range(T):
        word = input()
        word_len = len(word)
        count = 0
        for keyword in keywords:
            if keyword[:word_len] == word:
                count += 1
        print(count)


if __name__ == "__main__":
    main()