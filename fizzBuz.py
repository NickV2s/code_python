num = int(input("Input a Number "))
output = ""
if num%3==0:
    output += "Fizz"
if num%5==0:
    output += "Buzz"
print(output)