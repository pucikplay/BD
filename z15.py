import mmh3
from bitarray import bitarray
import z1

WORD_NO = 4183

class Bloom:
    def __init__(self, n):
        self.n = n
        self.k = 8
        self.X = bitarray(n)
        self.X.setall(0)

    def add(self, x):
        for i in range(self.k):
            self.X[mmh3.hash(x, i**2) % self.n] = 1

    def check(self, x):
        return all(self.X[mmh3.hash(x, i**2) % self.n] == 1 for i in range(self.k))
    
if __name__ == "__main__":
    B = Bloom(WORD_NO)
    stop_words = z1.importStopWords()
    words = z1.cleanText("Szekspir/hamlet.txt", stop_words).keys()
    print(words)

    for word in words:
        B.add(word)
    
    print(B.check('hamlet'))
    print(B.check('thou'))
    print(B.check('lupa'))

