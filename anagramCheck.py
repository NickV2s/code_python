first = input("Input first word: ")
second = input("Input second word: ")
def anagramChecker(word1:str, word2:str):
    for i in word1:
        for j in word2:
            if i==j:
                word1=word1.replace(i, "",1)
                word2=word2.replace(j, "",1)
    if word2==word1:
        print("anagram")
    else:
        print("not an anagram")
anagramChecker(first, second)