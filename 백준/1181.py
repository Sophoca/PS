testcase=int(input())
arr=list(input() for i in range(testcase))
arr2=list(sorted(set(arr), key= lambda x: (len(x), x)))
for i in arr2:
    print(i)