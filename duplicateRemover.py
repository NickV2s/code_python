def duplicateRemover(givenList:list):
    cleanList = []
    for i in givenList:
        if i not in cleanList:
            cleanList.append(i)
    return cleanList
print(duplicateRemover([1,4,2,1,5,2,2,2,5]))