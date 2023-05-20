import mmh3

def minHash(L, k):
    min_hash = []
    for i in range(1,k+1):
        min_hash.append(min(mmh3.hash(x, i**2) for x in L))

    return min_hash