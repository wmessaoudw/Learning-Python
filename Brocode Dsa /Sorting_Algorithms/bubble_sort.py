def bubble_sort(lis):
    n=len(lis)
    for i in range(n-1):
        for j in range(n-i-1):
            if lis[j]>lis[j+1]:
                temp=lis[j]
                lis[j]=lis[j+1]
                lis[j+1]=temp
lis=[0,6,5,2,7,9,3]
bubble_sort(lis)
prin