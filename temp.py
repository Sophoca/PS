temp = [(6, 0, [(0, 0), (0, 1), (5, 3)], []), (6, 0, [(4, 9), (5, 10), (5, 4)], [(2, 1)]), (3, 1, [(0, 2), (1, 3)], [(0, 3)]), (2, 0, [(0, 0), (1, 0)], [])]
temp.sort(key=lambda x: (x[0], x[1], x[2][-1]))
print(temp)