def primeChecker(num):
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            return False
    return True

def averagePrime(num):
    i=1
    if primeChecker(num):
        return (f"{num} {num}")
    else:
        while True:
            while not(primeChecker(num+i)):
                i+=1
            if primeChecker(num-i):
                return(f"{num+i} {num-i}")
            else:
                i+=1
                continue
averages = int(input())
nums = []
for i in range(0,averages):
    nums.append(int(input()))
for i in nums:
    print(averagePrime(i))
