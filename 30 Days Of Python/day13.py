#Day 13 Cover List Comprehension
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
numbers2=[x for x in numbers if x<=0]
print(numbers2)
list_of_lists =[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
list_=[x for row in list_of_lists for x in row] #row takes a list from the lists then x takes the value of list item in row
print(list_)
tup=(0,1,0,0,0,0,0)
listuple1=[(x,1,x,x**2,x**3,x**4,x**5) for x in range(0,11)  ]
print(listuple1)
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
countries_=[[x[0].upper(),x[0].upper()[0:3],x[1].upper()] for row in countries for x in row    ]
print(countries_)
countries__=[{'country':x[0].upper(),'city':x[1].upper()} for row in countries for x in row]
print(countries__)
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
names_=[ str(x[0])+" "+str(x[1]) for row in names for x in row]
print(names_)
solve_slope=lambda x1,y1,x2,y2:(y2-y1)/(x2-x1)
print(solve_slope(3,2,5,7))
solve_y_intercept=lambda x,y,m:y-(m*x)
print(solve_y_intercept(3,2,4))