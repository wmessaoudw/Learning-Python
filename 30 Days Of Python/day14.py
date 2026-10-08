#Day 14 cover Python High Order Functions
import string

from functools import reduce
from operator import concat

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark','Norway', 'Iceland','S']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#1/Map Is A function that takes a function and an iterable its apply the function on every item on the iterable
#and returns a list with the function effects While Filter take the same parameters it returns a list with the items
#that returns a true in the function meanwhile reduce doesn't return a list but a single value after applying the function
#on the iterable
#2/A high order function is a function that is treated a variable/object it can be passed a parameter be returned assigned
#to a variable / closure is when the inner function can access the outer scope of the function to get a value without being
#passed as a parameter /decorators is when wanting to modify a function without changing the source code using wrapper function
#and @decorator
def call(x):
    return  x+1
add1=map(call,numbers)
add2=filter(call,numbers)

print(list(add1))
print(list(add2))
def call2(x,y):
    return x+1
add3=reduce(call2,numbers)
print(add3)
for i in range(len(countries)-1):
    print(countries[i])
for i in range(len(names)):
    print(names[i])
for i in range(len(numbers)):
    print(numbers[i])
upper_c=map(str.upper,countries)
print(list(upper_c))
square=map(lambda x:x**2,numbers)
print(list(square))
upper_n=map(str.upper,names)
print(list(upper_n))
def noland(x):
    if "land" in x :
        return False
    return True

no_land=filter(noland,countries)
print(list(no_land))
def six(x):
    if len(x)==6:
        return True
    return False
six_lett=filter(six,countries)
print(list(six_lett))
def six2(x):
    if len(x)>=6:
        return True
    return False
six_lett_=filter(six2,countries)
print(list(six_lett_))
def E(x):
    if x[0]=="E":
        return True
    return False
E_S=filter(E,countries)
print(list(E_S))
def iseven(x):
    if x%2==0:
        return True
    return False
def add(x,y):
    return x+y
test=reduce(add,filter(iseven,map(lambda x:x**2,numbers)))
print(test)
def get_string_lists(lis):
    lis1=[]
    for i in range(len(lis)-1):
        lis1.append(str(lis[i]))
    return lis1
def summ(x,y):
    return x +y

summing=reduce(summ,numbers)
print(summing)
def concat_(x,y):
        return x+","+y
concate=reduce(concat_,countries)
print(f"{concate} are north european countries")
def categorize(x):
    all_=[]
    land=[]
    ia=[]
    island=[]
    stan=[]
    for i in range(len(x)-1):
        if "land" in  x[i]:
            land.append(x[i])
        if "ia" in x[i]:
            ia.append(x[i])
        if "island" in x[i]:
            island.append(x[i])
        if "stan" in x[i]:
            stan.append(x[i])
    all_.append(island)
    all_.append(land)
    all_.append(ia)
    all_.append(stan)
    return all_
print(categorize(countries))
def dict_countr(countrys):
    dicto={}
    lis=[]
    letters=list(string.ascii_uppercase)
    for j in letters:
        for i in range(len(countrys)):

            if j==countrys[i][0]:
                lis.append(countrys[i])
            dicto[j]=lis
        lis=[]
    return dicto
dict_countr(countries)
print(dict_countr(countries))
