def recursion(i):
    if i<=0:
        return 1
    print(i)
    i=i-1
    recursion(i)

recursion(6)