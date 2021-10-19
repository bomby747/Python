from functools import reduce

def sumOfDigits_map(num):
    list_num = []
    while num > 0 :
        num, s = divmod(num, 10)
        list_num.append(s)
    sum = reduce(lambda x, y: x+y, list_num)
    print(sum)
