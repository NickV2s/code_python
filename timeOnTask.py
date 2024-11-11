def choreCompletion(time, numOfChores):
    choreTimes = []
    for i in range(1,numOfChores+1):
        choreTimes.append(int(input()))
    if sum(choreTimes)<=time:
        return numOfChores
    else:
        sortedTimes=sorted(choreTimes)
        timeUsed = 0
        completedChores = 0
        for i in sortedTimes:
            timeUsed+=i
            if timeUsed>time:
                return completedChores
            else:
                completedChores+=1
time = int(input("How much time do you have "))
numOfChores = int(input("How many chores do you have "))
print(choreCompletion(time,numOfChores))