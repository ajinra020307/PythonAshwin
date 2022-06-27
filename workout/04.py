

def findMidpoint(p1,p2):
    m1=(p1[0]+p2[0])/2
    m2=(p2[1]+p1[1])/2
    return [m1,m2]

n= findMidpoint([3,4],[4,5])
 
def perpendicular(p1,p2,p3,p4):

    m1 =( p2[1] - p1[1]) / (p2[0] - p1[0])
    m2 =( p4[1] - p3[1]) / (p4[0] - p3[0])

    if m1 * m2 == -1:
        return True

    else:
        return False


result = perpendicular([1,1],[2,3],[4,4],[7,7])

print(result)