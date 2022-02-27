N = int(input())
arr = list(map(int, input().split()))

sum = 0
for i in range(len(arr) - 1):
  if(arr[i] > arr[i + 1]):
    sum += (i + 1)

print(sum)
