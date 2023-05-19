import re

def importStopWords():
    stop_words_file = open("Szekspir/stop_words_english.txt", mode="r", encoding="utf8")
    stop_words = []
    for word in stop_words_file:
        stop_words.append(word[:-1])
    stop_words_file.close()
    return stop_words

def cleanText(path, stop_words):
    text_file = open(path, mode="r", encoding="utf8")
    raw_text = text_file.read()
    text_file.close()
    lower = raw_text.lower()
    clean = re.sub("[^a-z0-9]+", " ", lower)
    T = clean.split(" ")
    T1 = []
    for word in T:
        if not (len(word) < 3 or word in stop_words):
            T1.append(word)

    dict = {}
    for word in T1:
        if word not in dict:
            dict[word] = 1
        else:
            dict[word] += 1

    return dict

def sortByFrequency(dict):
    words = sorted(dict.items(), key=lambda x:x[1], reverse=True)
    return words

if __name__ == "__main__":
    stop_words = importStopWords()
    words = sortByFrequency(cleanText("Szekspir/hamlet.txt", stop_words))

    output_file = open("data_out/output.csv", "w")
    output_file.write("\"weight\";\"word\"\n")
    for word in words:
        output_file.write("\"{}\";\"{}\"\n".format(word[1], word[0]))

    output_file.close()
