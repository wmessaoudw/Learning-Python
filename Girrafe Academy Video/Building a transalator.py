def Transalator(phrase):
    translation=""
    for letter in phrase:
        if letter in "AEIOU":

                letter='G'
        elif letter in "aeiou":
            letter='g'
        translation+=letter
    return translation
print(Transalator(input("enter phrase: ")))