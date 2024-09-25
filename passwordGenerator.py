import random

lowercase = list(range(97, 123))
uppercase = list(range(65, 91))
digits = list(range(48, 58))
special = list(range(33, 48)) + list(range(58,65)) + list(range(91,97)) + list(range(123,127))
usableCharacters = lowercase.copy()
length = int(input("Enter the Length of password "))
def include(check, inclusion:bool, characters:list):
    if check == "Y":
        inclusion == True
        usableCharacters.extend(characters)
    else:
        inclusion = False   
Upper = input("Should the password include capital letters Y/N? ")
includeUpper = False
include(Upper, includeUpper,uppercase)
Num = input("Should the password include numbers Y/N? ")
includeNum = False
include(Num, includeNum,digits)
Specials = input("Should the password include special characters Y/N? ")
includespecial = False
include(Specials, includespecial,special)
password = ""

while len(password)<length:
    password += chr(random.choice(usableCharacters))

print(f"The randomly generated password is {password}")

