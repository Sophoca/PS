N, D = map(int, input().split())
arr = list(map(int, input().split()))
if D == 0:
    print(1)
else:
    arr.sort()
    if arr[-1] - arr[0] <= D:
        print(len(arr))
    else:
        arr2=[]
        for i in range(len(arr)-1):
            arr2.append(arr[i+1]-arr[i])
        maxStation=0
        for i in range(len(arr2)):
            sum = arr2[i]
            for j in range(i+1, len(arr2)-i-1):
                sum += arr2[j]
                if sum > 2*D:
                    maxStation = max(j - i + 1, maxStation)
                    break
        print(maxStation)