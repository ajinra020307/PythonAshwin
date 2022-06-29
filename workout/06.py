

def findSum(fileName):
    file = open(fileName, 'r')
    content = file.read()
    content = content.split('\n')
    for x in range(0, len(content)):
        line = content[x].split(',')
        
        sum = 0
        for number in line:
            sum =sum + int(number)
        print(sum)


findSum('document.txt')
