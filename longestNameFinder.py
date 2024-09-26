names = ""
longestName = ""
longestLength = 0
while names !="X":
    names = input("Enter a name ")
    if len(names)>len(longestName):
        longestName = names
        longestLength = len(names)
print(f"The longest name is {longestName} with a length of {longestLength}")