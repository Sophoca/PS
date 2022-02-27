mylist=['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']
a=[mylist.index(input()) for _ in range(3)]
print(int(str(a[0])+str(a[1]))*(10**a[2]))