largest = 0
for left in range(100,1000):
    for right in range(100,1000):
        product = left*right
        if str(product) == str(product)[::-1]:
            largest = max(largest,product)
# print(largest)
# def palindromeCheck(firstNum):
#     num = firstNum
#     reversed_num = []
#     while num > 0:
#         digit = num%10
#         num = num//10
#         reversed_num.append(digit)
#     for i in reversed_num:
    

# print(palindromeCheck(906609))
