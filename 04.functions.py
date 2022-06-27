

def sayHello():
    print("Hello")


sayHello()



def findBmi(height,weight):

    bmi = weight/(height * height)
    
    return bmi


mybmi = findBmi(1.67,78)


def findarea(length,breadth):
    area = length * breadth
    return area


area = findarea(5,10)
print(area)