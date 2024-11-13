def reverseTail(word, flipped= ""):
    if not word:
        return flipped
    else:
        return reverseTail(word[:-1], flipped+word[-1])
print(reverseTail("sleep"))