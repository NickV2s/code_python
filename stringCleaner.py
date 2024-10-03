unclean = input("input a string")
clean=""
for character in unclean:
    if character.isalpha():
        clean+=(character.lower())
print(clean)
