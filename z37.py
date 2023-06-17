import csv
import random
import numpy as np

def randVectors(n):
    vectors = []
    for _ in range(1024):
        vectors.append([random.randrange(-1,2) for _ in range(n)])
    return vectors

def cosineDist(v1, v2):
    return np.dot(v1,v2)/(np.linalg.norm(v1) * np.linalg.norm(v2))

if __name__ == "__main__":
    dramas = ["hamlet", "KingLear", "Othello", "RomeoJuliet"]
    words = {drama: [] for drama in dramas}
    omega = []
    for drama in dramas:
        with open("data_out/{}_words.csv".format(drama), 'r') as csvfile:
            reader = csv.reader(csvfile, delimiter=';')
            for row in reader:
                words[drama].append((int(row[0]),row[1]))
                omega.append(row[1])

    omega = set(omega)
    n = len(omega)
    print(n)
    vectors = randVectors(n)
    scalar_products = {drama: [] for drama in dramas}

    for drama in dramas:
        drama_words = set([pair[1] for pair in words[drama][:]])
        diff = omega.difference(drama_words)
        for word in diff:
            words[drama].append((0,word))
        words[drama] = sorted(words[drama], key=lambda x:x[1])
        drama_counts = [pair[0] for pair in words[drama][:]]
        for vector in vectors:
            scalar_products[drama].append(np.sign(np.dot(vector,drama_counts)))
        
    for drama_1 in dramas:
        for drama_2 in dramas:
            if drama_1 != drama_2:
                print("{},{}:{}".format(drama_1,drama_2,cosineDist(scalar_products[drama_1],scalar_products[drama_2])))
