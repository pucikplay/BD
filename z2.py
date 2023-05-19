import z1
import re
import math

dramas = ["hamlet", "KingLear", "Othello", "RomeoJuliet"]
n = 4

if __name__ == "__main__":
    stop_words = z1.importStopWords()
    documents = {}
    for drama in dramas:
        documents[drama] = z1.cleanText("Szekspir/{}.txt".format(drama), stop_words)

    for drama in dramas:
        TFIDF = {}
        for word in documents[drama]:
            k = 0
            for _drama in dramas:
                if word in documents[_drama]:
                    k += 1
            IDF = math.log2(n/k)
            TFIDF[word] = int(documents[drama][word] * IDF)

        output_file = open("data_out/{}_out.csv".format(drama), "w")
        output_file.write("\"weight\";\"word\"\n")
        for word in documents[drama]:
            output_file.write("\"{}\";\"{}\"\n".format(TFIDF[word], word))

        output_file.close()
