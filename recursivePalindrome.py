def palindromeCheck(word:str,tail1=0,tail2=1):
    if word[tail1]!=word[-tail2]:
        return ("Not a palindrome")
    elif tail2 == len(word)//2:
        return("is a palindrome")
    else: 
        return palindromeCheck(word,tail1+1,tail2+1)
print(palindromeCheck("tacocat"))
