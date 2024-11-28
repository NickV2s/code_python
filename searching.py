#Linear
data=[1,1,4,5,8,12,15,32,36,57,90]
def linearSearch(data,target):
    for i in range (0,len(data)):
        if data[i]==target:
            return(i)
print(linearSearch(data,8))
#binary
def binarySearchRecursion(data:list,target:int):
    left = 0
    right = len(data)-1
    middle = (left+right)//2
    def helper(data,target,left,right,middle):       
        if not data:
            return -1
        elif data[middle]==target:
            return middle
        elif left>right:
            return -1
        else:
            if target>data[middle]:
                return helper(data,target,middle+1,right,(middle+right+1)//2)
            else:
                return helper(data,target,left,middle-1,(middle+left-1)//2)
    return helper(data,target,left,right,middle)
print(binarySearchRecursion(data,8))
def binarySearch(data:list,target:int):
    left = 0
    right = len(data)-1
    while True:
        middle = (left+right)//2
        if target==data[middle]:
            return middle
        elif left>right:
            return -1
        elif data[middle]<target:
            left = middle+1
        else: 
            right = middle-1
print(binarySearch(data,3))
#Bubble sort
def bubbleSort(data:list):
    swap = True
    while swap == True:
        swap = False
        for i in range(0,len(data)-1):
            if data[i]>data[i+1]:
                placeholder = data[i+1]
                data[i+1]= data[i]
                data[i] = placeholder
                swap = True
    return data
data2 = [5,2,7,1,9]
print(bubbleSort(data2))
#Insertion sort
def insertionSort(data:list):
    i = 1
    while i <len(data):
        j = i
        swap = True
        while j>0 and swap==True:
            if data[j-1]>data[j]:
                placeholder = data[j]
                data[j]=data[j-1]
                data[j-1] = placeholder
                j-=1
            else:
                swap = False
        i+=1
    return data
print(insertionSort(data2))
#destructive selection sort
def destructiveSelectionSort(data:list):
    sortedData = []
    while data:
        lowest = data[0]
        for i in data:
            if i<lowest:
                lowest = i
        sortedData.append(lowest)
        data.remove(lowest)
    return sortedData
print(destructiveSelectionSort(data2))
#Mutating selection sort
def mutatingSelectionSort(data):
    i = 1
    while i<len(data):
        lowest = data[i-1]
        for j in range(i,len(data)):
            if data[j]<lowest:
                lowest = data[j]
                indexHolder = j
        if lowest!= data[i-1]:
            numHolder = data[i-1]
            data[i-1]=lowest
            data[indexHolder] = numHolder
        i+=1
    return data
data3 = [5,2,7,1,9]
print(mutatingSelectionSort(data3))

