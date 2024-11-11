def factorialTail(n,tail=1):
    if n in {0,1}:
        return tail
    else: 
        return factorialTail(n-1,n*tail)
    
def factorialReg(n):
    if n in {0,1}:
        return 1
    else:
        return(factorialTail(n-1)*n)
print(factorialTail(8))
print(factorialReg(3))