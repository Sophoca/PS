def count_zero_durability():
    return durability.count(0)


def move_conveyor():
    return current_load_location - 1 if current_load_location > 0 else 2 * N - 1


def move_robot():
    current_release_location = get_release_location()
    for i in range(1, N):
        cur_idx = (current_release_location - i + 2 * N) % (2 * N)
        next_idx = (cur_idx + 1) % (2 * N)
        if isLoaded[cur_idx] is True and isLoaded[next_idx] is False and durability[next_idx] != 0:
            isLoaded[cur_idx] = False
            isLoaded[next_idx] = True
            durability[next_idx] -= 1
            unload_robot()


def get_release_location():
    return (current_load_location + N) % (2 * N) - 1


def unload_robot():
    current_release_location = get_release_location()
    isLoaded[current_release_location] = False


def load_robot():
    if durability[current_load_location] != 0:
        durability[current_load_location] -= 1
        isLoaded[current_load_location] = True


N, K = map(int, input().split(' '))
durability = list(map(int, input().split(' ')))
isLoaded = list(False for _ in range(2 * N))

current_load_location = 0
flag = 0

while count_zero_durability() < K:
    flag += 1
    current_load_location = move_conveyor()
    unload_robot()
    move_robot()
    load_robot()

print(flag)
