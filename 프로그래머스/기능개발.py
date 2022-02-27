import math


def calc_days(days, answer=None):
    if len(days) == 0:
        return answer
    elif answer is None:
        answer = []
    count = 0
    days = list(map(lambda x: max(0, x - days[0]), days))
    for day in days:
        if day == 0:
            count += 1
        else:
            break
    answer.append(count)
    calc_days(days[count:], answer)

    return answer


def solution(progresses, speeds):
    answer = []
    days = []
    for progress, speed in zip(progresses, speeds):
        days.append(math.ceil((100 - progress) / speed))
    answer = calc_days(days)

    return answer
