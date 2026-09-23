from math import sqrt
from os import MFD_ALLOW_SEALING


def add_two_numbs(num1,num2):
    return num1 + num2
def area_of_circle(radius):
    return radius*radius*3.14
def add_all_nums(*nums):
    sum=0
    for num in nums :
        sum=sum+num
    return sum
print(add_all_nums(1,2,3))
def convertC_toF(C):
    F = (C * 9 / 5) + 32
    return F
print(convertC_toF(0))
def check_season(month):
    month_=str(month).lower()
    if month_ in ["june","july","august"]:
        return "summer"
    elif month_ in ["september","october","november"]:
        return "autumn"
    elif month_ in ["december","january","february"]:
        return "winter"
    elif month_ in ["march","april","may"]:
        return "spring"
    else :
        return "Note A valid month"
print(check_season("sdsds"))
def calculate_slope(x1,y1,x2,y2):
    if x2-x1!=0:
        return (y2-y1)/(x2-x1)
    return "error"
print(calculate_slope(4,2,4,5))
def cal_quad_eq(a,b,c):
    delta=b**2 -4*a*c
    if delta<0:
        return  "no soultion"
    elif delta==0:
        return -b/(2*a)
    else:
        x1=-(b+sqrt(delta))/(2*a)
        x2=-(b-sqrt(delta))/(2*a)
        return [x1,x2]
print(cal_quad_eq(3,2,0))
def print_list(lis):
    for i in range(len(lis)):
        print(lis[i])
print_list([0,1,2,3,4])
def reverse_array(array):
    reverse=[]

    for i in range(len(array)-1,-1,-1):
        reverse.append(array[i])

    return reverse
print(reverse_array([1,2,3,4,5]))


def capitalize_list_items(lis):
    for i in range(len(lis)):
        lis[i]=lis[i].upper()
    return lis
li=["a","b","ACdAvssd"]
print(capitalize_list_items(li))
def add_item(lis,item):
    lis.append(item)
    return lis
def remove_item(lis,item):
    lis.remove(item)
    return lis
l=["a,b,c","d"]
remove_item(l,"d")
print(l)
def sum_of_nums(num):
    sum=0
    for i in range(num+1):
        sum=sum+i
    return sum
print(sum_of_nums(5))
def sum_of_odds(num):
    sum=0
    for i in range(num+1):
        if i%2!=0:
            sum=sum+i
    return sum
def sum_of_evens(num):
    sum=0
    for i in range(num+1):
        if i%2==0:
            sum=sum+i
    return sum
print(sum_of_evens(5))
print(sum_of_odds(5))
def evens_and_odds(integer):
    evens,odds=0,0
    for i in range(integer+1):
        if i%2==0:
            evens=evens+1
        else:
            odds=odds+1
    return f"odds={odds} evens={evens}"
print(evens_and_odds(100))
def factorial(num):
    num_=int(num)
    f=1
    for i in range(1,num_+1):
        f=f*i
    return f
print(factorial(5))
def is_empty(item):

    if len(item)==0:
        return True
    else:
        return False
a=[]
is_empty("")
def calculate_mean(lis):
    mean=0
    if is_empty(lis)==True:
        print("List is empty")
        return
    for i in range(len(lis)):
        mean=mean+lis[i]

    return mean/len(lis)

print(calculate_mean([2,4,6,8]))
def calculate_median(lis):
    if is_empty(lis)==True:
        return
    if len(lis)%2!=0:
        return lis[(len(lis))//2]
    else:
        return (lis[len(lis)//2]+lis[(len(lis)-1)//2])/2

print(calculate_median([1,2,3,4]))

def calculate_mode(lis):
    if is_empty(lis)==True:
        return
    cal=[0]
    k=0
    max_=0

    for i in lis:
        cal.append(0)
        cal[k]=lis.count(i)
        if cal[k]>cal[k-1]:
            max_=[i,cal[k]]
        k=k+1



    return max_
print(calculate_mode([0,0,2,2,2,2,2,2,3,3,3,3,3,3,3,3,3,3,3]))
def calculate_range(lis):
    if is_empty(lis)==True:
        return

    for i in range(len(lis)):
        if i==0:
            max_=lis[i]
            min_=lis[i]
        #finding max and min in list
        if lis[i]>max_:
            max_=lis[i]
        if lis[i]<min_:
            min_=lis[i]
    return max_- min_
print(calculate_range([4,6,3,9,7]))
def calculating_variance(lis):
    if is_empty(lis)==True:
        return
    sum_=0
    mean=calculate_mean(lis)
    for i in range(len(lis)):
        lis[i]=(lis[i]-mean)**2
    for i in range(len(lis)):
        sum_=sum_+lis[i]
    return sum_/(len(lis)-1)
print(calculating_variance([4,8,6,5,12]))
def calculating_standard_deviation(lis):
    if is_empty(lis)==True:
        return
    variance=calculating_variance(lis)
    return sqrt(variance)
print(calculating_standard_deviation([1,2,2,4,6]))
def greet(name="guest"):
    print(f"hello {name}")
greet("Messaoud")
def show_args(**args):
    for k,v in args.items():
        print(f"{k}:{v} ",end="")

show_args(name="alice",pet="brian")
def is_prime(num):
    c=0
    for i in range(1,num+1):
        if num%i==0:
            c+=1

    if c==2:
        return True
    else:
        return False


print()
print(is_prime(9))
def unique_items(lis):
    if is_empty(lis)==True:
        return
    for i in range(len(lis)):
        for j in range(i+1,len(lis)):
            if lis[i]==lis[j]:
                return False
    return True
print(unique_items([0,1,2]))
def same_data_type(lis):
    if is_empty(lis) == True:
        return
    for i in range(len(lis)):
        for j in range(i+1, len(lis)):

            if type(lis[i])!=type(lis[j]):
                return False
    return True
print(same_data_type([0,0,0,1,2,'a']))
def is_python_var(var):
    var_=str(var)

    return var_.isidentifier()
print(is_python_var("int"))

