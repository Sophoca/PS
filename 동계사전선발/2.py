arr = list(map(int, input().split()))
mul = [15, 28, 19]
while True:
  if arr[0] == arr[1] and arr[1] == arr[2] and arr[2] == arr[0]:
    break
  idx = arr.index(min(arr))
  arr[idx] += mul[idx]

print(arr[0])
