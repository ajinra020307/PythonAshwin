def findSum(x,y):
    sum = x + y
    return sum
sums = findSum(5,5)
print(sums)

def findvalue(x,y,z):
    value = x + y * z
    return value 
values = findvalue(2,3,4)
print(values)


def findlist(x,y):
    total = sum(x)
    totals= sum(y)
    return total+totals
sums=findlist([5,5],[8,8])
print(sums)

def findarray(x1,x2):
    sum = 0
    mergedList = x1 + x2

    for number in mergedList:
        sum = sum + number

    return sum

s = findarray([1,2],[3,4])
print(s)