def consonantCount(word):
    '''consonantChecker() returns an integer representing the number of consonants
    arguments
        word: string
    return
        an integer'''
    vowels="aeiou"
    consonantCounter=0    
    for character in word:
            if not(vowels.__contains__(character)) and character.isalpha():
                  consonantCounter+=1
    return consonantCounter
word = input("Input a word or sentance: ")
consonants = consonantCount(word)
print(f"{word} contains {consonants} consonants. ")