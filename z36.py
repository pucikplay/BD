import mmh3
from sklearn.cluster import KMeans
import z1
from z1 import re

def getActs(path, stop_words):
    text_file = open(path, mode="r", encoding="utf8")
    raw_text = text_file.read()
    text_file.close()
    acts = raw_text.split("ACT")
    words_from_acts = []
    for act in acts:
        lower = act.lower()
        clean = re.sub("[^a-z]+", " ", lower)
        T = clean.split(" ")
        T1 = []
        for word in T:
            if not (len(word) < 3 or word in stop_words):
                T1.append(word)
        words_from_acts.append(T1)
    
    return words_from_acts

def getDocuments():
    # Shakespeare
    dramas = ["hamlet", "KingLear", "Othello", "RomeoJuliet"]
    stop_words = z1.importStopWords()
    documents = {}
    for drama in dramas:
        acts = getActs("Szekspir/{}.txt".format(drama), stop_words)
        for i,act in enumerate(acts[1:]):
            documents["{}_act_{}".format(drama,i)] = act

    # Joyce
    text_file = open("ulyss12.txt", mode="r", encoding="utf8")
    raw_text = text_file.read()
    text_file.close()
    acts_small = raw_text.split("* * * * * * *")
    acts_big = []
    words_from_acts_small = []

    for act in acts_small:
        lower = act.lower()
        clean = re.sub("[^a-z]+", " ", lower)
        T = clean.split(" ")
        T1 = []
        for word in T:
            if not (len(word) < 3 or word in stop_words):
                T1.append(word)
        words_from_acts_small.append(T1)
    
    for i in range(0,len(words_from_acts_small),3):
        j = i
        joined = []
        while j < len(words_from_acts_small) and j < i+3:
            joined += words_from_acts_small[j]
            j += 1
        acts_big.append(joined)

    for i,act in enumerate(acts_big[1:]):
            documents["ulysses_act_{}".format(i)] = act
    
    return documents

def kGrams(X, k):
    Y = [[y for y in X[i:i+k]] for i in range(len(X)-k+1)]
    return [''.join(map(str,y)) for y in Y]

def kGramMin(X, k, h):
    Y = [[y for y in X[i:i+k]] for i in range(len(X)-k+1)]
    Y1 = [''.join(map(str,y)) for y in Y]
    return min([h(y) for y in Y1])

# returns vector of n minHashes for differen hash functions
def getMinHashVect(X, n):
    min_hash_vect = []
    for i in range(n):
        def h(x): return mmh3.hash(x,i)
        min_hash_vect.append(kGramMin(X, 7, h))
    return min_hash_vect

def jackard(A,B):
    A_set, B_set = set(kGrams(A,7)), set(kGrams(B,7))
    sum_set = A_set.union(B_set)
    intersection_set = A_set.intersection(B_set)
    return len(intersection_set)/len(sum_set)

def approx(A_vect, B_vect, n):
    count = 0
    for i in range(n):
        if A_vect[i] == B_vect[i]:
            count += 1
    return count/n

if __name__ == "__main__":
    documents = getDocuments()
    for key,document in documents.items():
        print(key, len(document))
    
    for n in [64,128,256]:
        print('n: {}'.format(n))
        min_hashes = {}
        jackard_exact = {}
        jackard_approx = {}
        for key,document in documents.items():
            min_hashes[key] = getMinHashVect(document, n)
        for key1 in documents.keys():
            for key2 in documents.keys():
                if key1 < key2:
                    jackard_exact["{},{}".format(key1,key2)] = jackard(documents[key1],documents[key2])
                    jackard_approx["{},{}".format(key1,key2)] = approx(min_hashes[key1],min_hashes[key2], n)
        for key,value in jackard_approx.items():
            if value != 0.0:
                print(key, value, jackard_exact[key])

        print("5 clusters:")
        kmeans = KMeans(n_clusters=5).fit(list(min_hashes.values()))
        labels = kmeans.labels_
        for i,key in enumerate(documents.keys()):
            print(key, labels[i])

        print("2 clusters:")
        kmeans = KMeans(n_clusters=2).fit(list(min_hashes.values()))
        labels = kmeans.labels_
        for i,key in enumerate(documents.keys()):
            print(key, labels[i])
        
    