def S(s,k,m):
    return 1 - (1 - s**k)**m

eps = 0.0105

if __name__ == "__main__":
    for k in range(100):
        for m in range(1000):
            S1 = S(1/3,k,m)
            S2 = S(1/2,k,m)
            d1 = abs(S1 - 1/10)
            d2 = abs(S2 - 9/10)
            if d1 < eps and d2 < eps:
                print("k = {}, m = {}, S1 = {}, S2 = {}".format(k,m,S1,S2))
