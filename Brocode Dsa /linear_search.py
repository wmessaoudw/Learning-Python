def linear_search(itter,target):
    for i in range(len(itter)):
        if itter[i]==target:
            return  i

    return -1
lis=[0,3,1,4,5]
print(linear_search(lis,3))
#o(n)
#best for unsorted data
# or for data structures without indexing
#doesn't need to be sorted to work