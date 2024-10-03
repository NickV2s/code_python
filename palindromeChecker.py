string = input("Input a word: ")
flipped = ""
for character in range(-1,string.__len__()*-1-1,-1):
    flipped+= string[character]
if flipped==string:
    print(f"{string} is a palindrome")
else:
    print(f"{string} is not a palindrome")