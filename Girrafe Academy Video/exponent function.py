def expo(num1,num2):
    expon=1
    for index in range(num2):
        expon*=num1
    return expon
print(expo(2,4))