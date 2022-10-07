from collections import deque

T = int(input())

for _ in range(T):
    functions = list(input().replace("RR", ""))

    N = int(input())
    temp = input().replace('[', '').replace(']', '')
    numbers = [] if len(temp) == 0 else deque(list(map(int, temp.split(','))))
    r_count = 0
    for function in functions:
        if function == 'R':
            r_count += 1
        elif function == 'D':
            if len(numbers) == 0:
                print('error')
                break
            if r_count % 2 == 1:
                numbers.pop()
            else:
                numbers.popleft()
    else:
        if r_count % 2 == 1:
            numbers.reverse()
        print('[' + ','.join(map(str, numbers)) + ']')
