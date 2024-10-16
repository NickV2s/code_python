
def convertSring(strings:str):
    strings.split(",")
    nums = []
    for i in strings:
        nums.append(int(i))
    return nums
def frequency(start:int, end:int, frequency:int):
    from random import randrange
    a_list = []
    for i in range(0, frequency):
        value = randrange(start, end+1)
        a_list.append(value)
    return a_list

#convertSring(input("Input a string: "))
print(frequency(7,12031,7))