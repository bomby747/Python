def sumOfDigits(num):
    sum = 0
    for i in list(str(num)):
        sum = sum + int(i)
    print(sum)

