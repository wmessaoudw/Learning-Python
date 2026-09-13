num1=float(input("enter number 1: "))
oper=input("enter operator: ")
num2=float(input("enter number 2: "))
if oper=='+':
    print(num1+num2)
elif oper=='-':
    print(num1-num2)
elif oper=='*':
    print(num1*num2)
elif oper=='/' and num2!=0:
    print(num1/num2)
elif oper == '/' and num2 == 0:
    print("can't divide by zero")
else:
    print("False Operator")
