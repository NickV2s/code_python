def maxFind(arr):
    if len(arr)<=1:
        return arr
    else:
        if arr[-1]>arr[-2]:
            arr[-2]=arr[-1]
        return maxFind(arr[:-1])
    
data = ["h","H", "z"]
print(maxFind(data))

def maxFindTail(arr):
    def helper(arr,tail):
        if not arr:
            return tail
        else:
            if arr[-1]>tail[0]:
                return(helper(arr[:-1],arr[-1]))
            else:
                return(helper(arr[:-1],tail))
    return helper(arr[:-1],arr[-1])
print(maxFindTail(data))