number = int(input("Input a number "))
previousNum = 0
previousPreviousNum = 0
finalNum = 0
for i in range(0,number+1):
    finalNum = previousPreviousNum + previousNum
    if i == 1:
        finalNum=1
    previousPreviousNum = previousNum
    previousNum = finalNum


print(f"{number} is {finalNum}")