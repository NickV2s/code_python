def exponentReg(num,exp):
    if exp in {0,1}:
        return num
    else:
        return num*exponentReg(num,exp-1)
print(exponentReg(3,4))

def exponentTail(num,exp,tail=1):
    if exp in {0}:
        return tail
    else:
        return exponentTail(num,exp-1,tail*num)
print(exponentTail(3,4))
