def insertion_sort(lis):
    for i in range(1,len(lis)):
        temp=lis[i]
        j=i-1
        while j>=0 and lis[j]>temp:
            lis[j+1]=lis[j]
            j=j-1
        lis[j+1]=temp
lis=[2,3,1,3,45,6,7]
insertion_sort(lis)
print(lis)