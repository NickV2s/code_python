def listMerge(list_a,list_b):
    merged = []
    def helper(list_a,list_b,merged,tail_a,tail_b):
        if not(list_a and list_b):
            return merged
        elif not(list_a):
            merged.append(list_a)
            return merged
        elif not(list_b):
            merged.append(list_b)
            return merged
        if tail_a<tail_b:
            merged.append(tail_a)
            if not(list_a[1:]):
                return helper(False,list_b,merged,0,tail_b)
            else:
                return helper(list_a[1:],list_b,merged,list_a[1],tail_b)
        else:
            merged.append(tail_b)
            if not(list_b[1:]):
                return helper(list_a,False,merged,tail_a,0)
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
data1 =[2,4,6,7,8,9,10]
data2 = [1,2,4,5,7,12,15]
print(listMerge(data1,data2))
