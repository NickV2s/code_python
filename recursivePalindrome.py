def palindromeCheck(word:str,tail=True):
    if not tail:
        return ("Not a palindrome")
    elif not word:
        return("is a palindrome")
    else: 
        return palindromeCheck(word[1:-1], word[0]==word[-1])
print(palindromeCheck("tacocat"))
