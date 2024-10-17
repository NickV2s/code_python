def countDuplicates(text:str):
    counter = 0
    char = ""
    condensedText = ""
    for i in text:
        if i!=char and counter!=0:
            condensedText+=char +str(counter)
            counter = 1
        else:
            counter+=1
        char = i
    condensedText+=char + str(counter)
    return condensedText
print(countDuplicates("aaaabbbbdddccaat"))