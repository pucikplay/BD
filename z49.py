import random
from skspatial.objects import Vector,Plane,Point
import matplotlib.pyplot as plt
import numpy as np
import math

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
    # return [n1, n2, n3]
    return [Vector.from_points([0,0,0],[-0.42223698, 0.90647432, 0.00449915]),
            Vector.from_points([0,0,0],[-0.86421138, -0.40104291, -0.30381456]),
            Vector.from_points([0,0,0],[ 0.27359574, 0.13216996, -0.95272056])]

def matrixL():
    L = []
    for x in [-1,1]:
        for y in [-1,1]:
            for z in [-1,1]:
                L.append(Point([x,y,z]))
    return L

def matrixA():
    A = np.random.rand(2,3)
    # return A * (1/math.sqrt(2))
    return np.array([[0.00431902, 0.0879098,  0.44337079],
    [0.35332662, 0.15498393, 0.4102104]])

if __name__ == "__main__":
    base = ortonormalBase()
    for vect in base:
        print(vect)
    plane = Plane.from_vectors([0,0,0],base[0],base[1])
    L = matrixL()
    _, ax = plt.subplots()
    for point in L:
        point_proj = plane.project_point(point)
        point_proj.plot_2d(ax, s=50)
    plt.savefig("z49_plane.png", dpi=300)
    plt.close()

    A = matrixA()
    for row in A:
        print(row)
    L_proj = []
    _, ax = plt.subplots()
    for point in L:
        point_proj = Point(A.dot(point))
        print
        point_proj.plot_2d(ax, s=50)
    plt.savefig("z49_A.png", dpi=300)
    plt.close()
