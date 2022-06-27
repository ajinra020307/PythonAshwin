
a = (1,2,3,4,3,2,3,3,5,3)
count = 0

for x in range(0,len(a)):
    number = a[x]
    if number == 3:
    
        count = count + 1
print(count)