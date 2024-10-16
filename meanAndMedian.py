def mean(nums:list) -> float:
    total = 0
    for i in nums:
        total+=int(i)
    return total / len(nums)
# def median(nums:list):
#     lowest = 0
#     largest = 0
#     for i in nums:
#         if lowest == 0 or int(i)<lowest:
#             lowest = int(i)
#         if largest== 0 or int(i)>largest:
#             largest = int(i)
#     counter = 10
#     median1 = float(lowest)
#     while counter!=0:
#         counter=0
#         median1+=0.5
#         for i in nums:
#             if int(i)>median1:
#                 counter+=1
#             elif int(i)<median1:
#                 counter-=1
#     counter = 1
#     median2 = float(largest)
#     while counter!=0:
#         counter=0
#         median2-=0.5
#         for i in nums:
#             if int(i)>median2:
#                 counter+=1
#             elif int(i)<median2:
#                 counter-=1
#     medianList = [median1, median2]
#     trueMedian=mean(medianList)   
#    return trueMedian
def median(nums:list):
    newNums = []
    for i in nums:
        newNums.append(int(i))
    length = len(newNums)
    newNums = sorted(newNums)
    middle = len(newNums)//2
    if len(nums)%2!=0:
        return newNums[middle]
    else:
        return ((int(newNums[middle])+int(newNums[middle-1]))/2)
listOfNums = input("input a list of numbers using a space to seperate each number: ")
listOfNums=listOfNums.split(" ")
meanOfNum = mean(listOfNums)
print(f"The mean of your numbers is {meanOfNum}")
medianOfNum = median(listOfNums)
print(f"The median of your numbers is {medianOfNum}")

