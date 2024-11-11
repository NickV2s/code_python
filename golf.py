distance = int(input())
clubAmount = int(input())
clubType = []
strokes = 0
table = [0]
for i in range (0,clubAmount):
    clubType.append(int(input()))
for i in range (distance):
    table.append(float("Infinity"))
while table[-1]==float("Infinity"):
    for i in range(len(table)):
        if table[i]!=float("Infinity"):
            for club in clubType:
                new_location = i + club
                if new_location<(len(table)):
                    table[new_location] = min(table[new_location],table[i]+1)
print(f"it would take {table[-1]} strokes")
