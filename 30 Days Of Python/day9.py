age=int(input("Enter Age: "))
if age>=18:
   print("you are old enough to drive")
else:
    n_age=18-age
    print(f"you are short {n_age} years to drive ")
your_age=int(input("Enter Age: "))
my_age=20
if my_age==your_age:
   print("We are the same age")
elif my_age>your_age:
        print(f"Iam Older Than You BY {my_age-your_age} years")
else:
    print(f"You are older than me by {your_age-my_age} years")
a=int(input("Enter A: "))
b=int(input("Enter B: "))
if a>b:
    print(f"{a} is greater than {b}")
elif a<b:
    print(f"{b} is greater than {a}")
else :
    print(f"{b} is equal to {a}")
score=int(input("enter your score: "))
if score>=90 and score <=100:
    print("You Got an A")
elif score>=80 and score <=89:
    print("You got a B")
elif score>=70 and score <=79:
    print("you got a c")
elif score>=60 and score <=69:
    print("you got a d")
else :
    print("you got an f")
month=input("Enter Month: ")
month=month.lower()
autumn=["september","october","november"]
winter=["december","january","february"]
spring=["march", "april", "may"]
summer=["june","july","august"]
if month in autumn:
    print("the season of this month is autumn")
elif month in winter:
    print("the season of this month is winter")
elif month in summer:
   print("the season of this month is summer")
elif month in spring:
    print("the season of this month is spring")
else:
    print("Invalid Month")
fruits = ['banana', 'orange', 'mango', 'lemon']
fruit=input("enter fruit: ")
fruit=fruit.lower()
if fruit in fruits:
    print("this fruit is already in the list")
else:
        fruits.append(fruit)
        print(fruits)
person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': [ "JavaScript","React",'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}
if "skills" in person:
    skill_list=list(person["skills"])
    print(skill_list[len(skill_list)//2])
    if 'Python' in skill_list:
        print("He has python skills")
    else :
        print("he doesn't have python skills")
    if 'JavaScript' in skill_list and 'React' in skill_list and 'Node' in skill_list and 'MongoDB' in skill_list and 'Python' in skill_list:
        print("Hes a fullstack developer")
    elif  'JavaScript' in skill_list and 'React' in skill_list and ('Node' not in skill_list and 'MongoDB' not in skill_list and 'Python' not in skill_list):
        print("hes a front end developer")
    elif   "Node" in skill_list and "Python" in skill_list and "MongoDB" in skill_list and "JavaScript" not in skill_list and "React" not in skill_list :
        print("hes a back end developer")
    else :
        print("unknown")

if person['is_married']==True and person['country']=='Finland' :
    print(f"{person["first_name"]} {person["last_name"]} lives in Finland ,He is married")

