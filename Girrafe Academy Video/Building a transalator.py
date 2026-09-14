def Transalator(phrase):
    translation=""
    for row in phrase:
        for col in row:
            if col =='a' or col=='e' or col=='i' or col =='o' or col=='u' or col=='y':
                col='g'
            translation+=col
    return translation
print(Transalator("dog"))