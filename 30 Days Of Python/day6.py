tpl=tuple()
print(tpl)
brothers=("Brother1","Brother2")
sisters=("Sister1","Sister2")
siblings=brothers+sisters
print(siblings)
print(len(siblings))
siblings=list(siblings)
siblings.append("Father")
siblings.append("Mother")
family_members=tuple(siblings)
print(family_members)
siblings_=family_members[0:4]
print(siblings_)
parents_=family_members[4:6]
print(parents_)
fruits=("fruit1","fruit2")
vegatable=("veg1","veg2")
animals=("animale1","animale2")
food_stuff_tp=fruits+vegatable+animals
food_stuff_lst=list(food_stuff_tp)
food_stuff_tp_middle=food_stuff_lst[0:len(food_stuff_lst)//2]
food_stuff_tp_first=food_stuff_lst[0:3]
food_stuff_tp_last=food_stuff_lst[-3:]
print(food_stuff_tp_middle)
print(food_stuff_tp_first)
print(food_stuff_tp_last)
del food_stuff_tp
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print("Estonia" in nordic_countries)
print("Iceland" in nordic_countries)
