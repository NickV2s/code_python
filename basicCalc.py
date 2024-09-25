num1=int(input("Input first number "))
num2=int(input("Input second number "))
calcType=input("Input symbol for type of calculation ")

if calcType=="+":
    result = num1+num2
elif calcType=="-":
    result = num1-num2
elif calcType=="*":
    result = num1*num2
elif calcType=="/":
    result = num1/num2
else:
    print("Invalid symbol")
print(result)