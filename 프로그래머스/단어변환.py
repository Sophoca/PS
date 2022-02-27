from collections import deque


def solution(begin, target, words):
    answer = 0

    if target not in words:
        return 0

    words.insert(0, begin)
    words_len = len(words)
    tree = dict()
    for i in range(words_len):
        for j in range(1, words_len):
            if len(set(words[i]) & set(words[j])) == 2:
                if words[i] not in tree:
                    tree[words[i]] = []
                tree[words[i]].append(words[j])

    visited = [0] * words_len
    queue = deque([begin])

    count = 0
    while queue:
        word = queue.popleft()
        if word == target:
            return count
        for sub_word in tree[word]:
            if visited[words.index(sub_word)] == 0:
                visited[words.index(sub_word)] = 1
                queue.append(sub_word)
        count += 1

    return count


print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
