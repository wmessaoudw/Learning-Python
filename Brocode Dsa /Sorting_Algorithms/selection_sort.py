def selection_sort(lis):
    n=len(lis)
    for i in range(n-1):
        min=i

        for j in range(i+1,n):
            if lis[min]>lis[j]:
                min=j
        temp=lis[i]
        lis[i]=lis[min]
        lis[min]=temp
lis=[0,6,5,2,7,9,3]
selection_sort(lis)
print(lis)