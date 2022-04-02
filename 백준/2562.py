numbers = list(((i + 1), int(input())) for i in range(9))
numbers.sort(key=lambda x: x[1], reverse=True)

print(numbers[0][1])
print(numbers[0][0])