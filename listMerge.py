def listMerge(list_a,list_b):
    merged = []
    def helper(list_a,list_b,merged,tail_a,tail_b):
        if not(list_a) and not(list_b):
            return merged
        elif not(list_a):
            for i in list_b:
                merged.append(i)
            return merged
        elif not(list_b):
            for i in list_a:
                merged.append(i)
            return merged
        if tail_a<tail_b:
            merged.append(tail_a)
            if not(list_a[1:]):
                if not(list_a):
                    return helper(False,list_b,0,tail_b)
                else:
                    num = list_a[0]
                    return helper(list_a[1:],list_b,merged,num,tail_b)
            else:
                return helper(list_a[1:],list_b,merged,list_a[1],tail_b)
        else:
            merged.append(tail_b)
            if not(list_b[1:]):
                if not(list_b):
                    return helper(list_a,False,tail_a,0)
                else:
                    num = list_b[0]
                    return helper(list_a,list_b[1:],merged,tail_a,num)
            else:
                return helper(list_a,list_b[1:],merged,tail_a,list_b[1])
    if not(list_a and list_b):
        return merged
    elif not(list_a):
        merged.append(list_a)
        return merged
    elif not(list_b):
        merged.append(list_b)
        return merged
    else:
        return helper(list_a,list_b,merged,list_a[0],list_b[0])
data1 =[2,4,6,7,8,9,10,90,281,292,300]
data2 = [1,2,4,5,7,12,15,34]
print(listMerge(data1,data2))
