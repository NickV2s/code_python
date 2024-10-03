num = int(input("Input a number greater than 0: "))
factorList = []
counter = 0
for i in range (1,num+1):
    if num%i==0:
        factorList.append(i)
        counter +=1
print(f"The number of factors for {num} is {counter}")
print(f"The factors of {num} are: {factorList}")