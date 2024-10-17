def factorChecker(num:int):
    factors = []
    isPrime = True
    tupleReturn=(isPrime,factors)
    if num<2:
        tupleReturn = (False,factors)
        return tupleReturn
    elif num<4:
        return tupleReturn
    else:
        for i in range(2,(num//2)+1):
            if num%i==0:
                factors.append(i)
                tupleReturn = (False,factors)
        return tupleReturn
print(factorChecker(16))
