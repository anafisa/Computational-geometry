from math import *

H = []

class Vector:
        def __init__(self, x, y, z):
                self.x = x
                self.y = y
                self.z = z


        def minusV(self, vec):
                return Vector(self.x-vec.x, self.y-vec.y, self.z-vec.z)
    
    
        def xV(self, vec):
                x = self.y*vec.z - self.z*vec.y
                y = self.z*vec.x - self.x*vec.z
                z = self.x*vec.y - self.y*vec.x
                return (x, y, z)


def GetZ(x,y):
    x_m, x_a = modf(x)
    y_m, y_a = modf(y)
    x_a = int(x_a)
    y_a = int(y_a)
    if (x_a + y_a)%2 == 0:
        if y_m > x_m:
            p1 = Vector(x_a, y_a, H[x_a][y_a])
            p2 = Vector(x_a, y_a+1, H[x_a][y_a+1])
            p3 = Vector(x_a+1,y_a+1, H[x_a+1][y_a+1])
        else:
            p1 = Vector(x_a, y_a, H[x_a][y_a])
            p2 = Vector(x_a+1, y_a, H[x_a+1][y_a])
            p3 = Vector(x_a+1, y_a+1, H[x_a+1][y_a+1])                    
    elif y_m > 1-x_m:
        p1 = Vector(x_a+1, y_a+1, H[x_a+1][y_a+1])
        p2 = Vector(x_a, y_a+1, H[x_a][y_a+1])
        p3 = Vector(x_a+1, y_a, H[x_a+1][y_a])    
    else: 
        p1 = Vector(x_a, y_a, H[x_a][y_a])
        p2 = Vector(x_a, y_a+1, H[x_a][y_a+1])
        p3 = Vector(x_a+1, y_a, H[x_a+1][y_a])
        
    vec1 = p1.minusV(p2)
    vec2 = p3.minusV(p2)
    A,B,C = vec1.xV(vec2)
    D = -(A*p1.x + B*p1.y +C*p1.z)
    z = - (A*x + B*y + D) / C
    return z
    
def strR(r):
    return '{0:.2f}'.format(r)

# f = open('H.txt', 'r')
# wH = int(f.readline())
# hH = int(f.readline())
# for x in range(wH):
#     H.append([])
#     for y in range(hH):
#         z = float(f.readline())
#         H[x].append(z)
# f.close()
#
# x, y = map(float, input().split())
# print(strR(GetZ(x, y)))
