
def findFactorial(number):
    # a = 1

    # for x in range(1,number+1):
    #     a = a*x 
    # return a
    a = 1
    while number>1:
        a = a* number
        number = number-1

    return a

f = findFactorial(10)
print(f)
f = findFactorial(3)
print(f)
f = findFactorial(2)
print(f)