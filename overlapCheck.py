def overlapChecker(word1, word2):
    word1=set(word1)
    word2=set(word2)
    word1 = word1.intersection(word2)
    print(word1)
first = input("input first word: ")
second = input("input first second: ")
overlapChecker(first, second)