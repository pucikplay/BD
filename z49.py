import random
from skspatial.objects import Vector,Plane,Point
import matplotlib.pyplot as plt

def randVect():
    x = random.uniform(-1.0, 1.0)
    y = random.uniform(-1.0, 1.0)
    z = random.uniform(-1.0, 1.0)
    p = Vector.from_points([0,0,0], [x,y,z])
    return p.unit()

def ortonormalBase():
    n1 = randVect()
    n2 = randVect()
    n3 = n1.cross(n2).unit()
    n2 = n1.cross(n3).unit()
    return [n1, n2, n3]

def matrixL():
    L = []
    for x in [-1,1]:
        for y in [-1,1]:
            for z in [-1,1]:
                L.append(Point([x,y,z]))
    return L


if __name__ == "__main__":
    base = ortonormalBase()
    print(base)
    plane = Plane.from_vectors([0,0,0],base[0],base[1])
    L = matrixL()
    L_proj = []
    _, ax = plt.subplots()
    for point in L:
        point_proj = plane.project_point(point)
        point_proj.plot_2d(ax, s=50)

    plt.show()