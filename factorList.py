def factorChecker(num:int,k:int):
    rightFactors = []
    leftFactors = []
    if num==1:
        return-1
    elif num<=3:
        if k==1:
            return num
        else: 
            return -1
    else:
        for i in range(1,(int(num**0.5))):
                if num%i==0:
                    leftFactors.append(i)
                    rightFactors.append((num//i))
        if len(leftFactors)<k:
            if len(leftFactors)+len(rightFactors)<k:
                return -1
            else:
                return rightFactors[-1*(k-len(leftFactors))]
        else:
            return leftFactors[k-1]
print(factorChecker(48,6))
