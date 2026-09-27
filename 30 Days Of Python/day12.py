#This Day Covers Python Modules https://github.com/Asabeneh/30-Days-Of-Python/blob/master/12_Day_Modules/12_modules.md
from random import random,randint
import random
import string
def random_user_id():
    lis=""

    char=string.ascii_letters+string.digits
    for i in range(6):
        lis+=random.choice(char)
    return lis
def random_user_id2(mny):
    lis=[]
    for i in range(mny):
        lis.append(chr(randint(48,122)))
    lis="".join(lis)
    return lis


def user_id_gen_by_user():
    mny=int(input("enter how many chars"))
    usr = int(input("enter how many users "))


    lis=""
    for i in range(usr):
        lis=lis +random_user_id2(mny)+"\n"

    return lis
def rgb_color_gen():
    return f"rgb({randint(0,255)},{randint(0,255)},{randint(0,255)})"





print(rgb_color_gen())
def list_of_hexa_colors(amount):
    hex_colors="0123456789abcdef"
    colors=[]
    for _ in range(amount):
        color="#"

        for _ in range(6):
            color+=random.choice(hex_colors)
        colors.append(color)
    return colors

def list_of_rgb_colors():
    array=[]



    for i in range(3):
        array.append(randint(0,255))
    return array
print(list_of_rgb_colors())
def generate_colors(type,number):
    array=[]
    if str(type).lower()=='rgb':
        for i in range(number):
            array.append(rgb_color_gen())
    elif str(type).lower()=='hexa':
        for i in range(number):
            array.append(list_of_hexa_colors(number))
    return array
print(generate_colors("hexa",3))
print(generate_colors("rgb",3))
def shuffle_list(lis):
    random.shuffle(lis)
    return lis


def seven_unique_numbers():
    return random.sample(range(10),7)



lis=[1,2,3,4,5,6,7]
print(shuffle_list(lis))