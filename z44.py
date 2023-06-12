import random as rand
import math
import matplotlib.pyplot as plt

def getPoints(n, k): 
    return [[rand.random() for _ in range(n)] for _ in range(k)]

def getDist(a, b):
    return math.sqrt(sum((a[i]-b[i])**2 for i in range(len(a))))

def getDists(points, n):
    dists = []
    for p_i in points:
        for p_j in points:
            if p_i != p_j:
                dists.append(getDist(p_i, p_j)/math.sqrt(n))
    return dists
    
if __name__ == "__main__":
    N = [1,10,100,1000]
    k = 100

    for n in N:
        plt.hist(getDists(getPoints(n,k), n), bins=100)
        plt.savefig('z44_n={}.png'.format(n), dpi=300)
        plt.xlabel('Odległość')
        plt.ylabel('Liczba wystąpień')
        plt.title('n = {}'.format(n))
        plt.close()