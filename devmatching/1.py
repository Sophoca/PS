import re


def solution(registered_list, new_id):
    registered_list = set(registered_list)
    if new_id not in registered_list:
        return new_id

    m = re.search('([a-zA-Z]{3,6})(\d{0,6})', new_id)
    S, N = m.groups()
    if N == '':
        N = '0'
    N = int(N)

    temp = []
    for registered in registered_list:
        if registered.find(S) != -1:
            temp.append(registered)
    while True:
        N += 1
        if S + str(N) not in temp:
            return S + str(N)
    return ''

print(solution(['aaa123', 'aaa', 'aaa1', 'aaa2'], 'aaa'))