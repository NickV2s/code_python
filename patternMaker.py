def patternMaker(num:int):
    pattern = ""
    while num>0:
        pattern+=str(num%2)
        print(pattern)
        num = num-1
num = int(input("Input a number greater than 0"))
patternMaker(num)