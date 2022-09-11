import re


def solution(birth):
    answer = 0
    for obj in birth:
        if check_format(obj) is None:
            continue

        year, month, day = map(int, obj.split("-"))
        if not (check_year(year) and check_month(month) and check_day(year, month, day)):
            continue

        answer += 1

    print(answer)
    return answer


def check_format(obj):
    pattern = re.compile(r"^\d{4}-\d{2}-\d{2}$")
    return pattern.search(obj)


def check_year(year):
    return 1900 <= year <= 2021


def check_month(month):
    return 1 <= month <= 12


def check_day(year, month, day):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 1 <= day <= 31
    elif month in [4, 6, 9, 11]:
        return 1 <= day <= 30
    elif month == 2:
        if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
            return 1 <= day <= 29
        return 1 <= day <= 28
    return False


# solution(["-2019-12-29-", "1945--10-31", "----------", "20000-123-567"])

print(check_format("1234-1234-11-33"))