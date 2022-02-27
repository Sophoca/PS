N = int(input())

top = 3
front = 1
right = 2
for i in range(N):
  req = input()
  if req == 'NORTH':
    tmp = top
    top = front
    front = 7 - tmp
  elif req == "SOUTH":
    tmp = front
    front = top
    top = 7 - tmp
  elif req == "WEST":
    tmp = top
    top = right
    right = 7 - tmp
  else:
    tmp = right
    right = top
    top = 7 - tmp

print(top)
