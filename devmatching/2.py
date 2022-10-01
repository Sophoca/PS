from collections import defaultdict


def solution(maps):
    answer = 0
    countries = []
    for row in range(len(maps)):
        for col in range(len(maps[0])):
            if maps[row][col] == '.':
                continue
            for country in countries:
                if row > 0 and ((row - 1, col) in country) or (col > 0 and (row, col - 1) in country):
                    country.append((row, col))
                    break
            else:
                countries.append((row, col))

            print(countries)
    return answer