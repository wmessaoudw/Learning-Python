password="Thursday"
guess=""
i=1
while guess!=password and i<4:
    guess=input("Enter The Correct Password: ")
    if guess!=password:
        print("Try Again ",i)

    else:
     print("You Win")
    i+=1
if guess!=password:
    print("you lose")


