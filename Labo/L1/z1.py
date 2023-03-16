import re

# open files
text_file = open("Labo/L1/Szekspir/hamlet.txt", mode="r", encoding="utf8")
stop_words_file = open("Labo/L1/Szekspir/stop_words_english.txt", mode="r", encoding="utf8")

# import stop words
stop_words = []
for word in stop_words_file:
    stop_words.append(word[:-1])

# clean the text
raw = text_file.read()
lower = raw.lower()
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

words = sorted(dict.items(), key=lambda x:x[1], reverse=True)

output_file = open("Labo/L1/output.csv", "w")
output_file.write("\"weight\";\"word\"\n")
for word in words:
    output_file.write("\"{}\";\"{}\"\n".format(word[1], word[0]))

text_file.close()
stop_words_file.close()
output_file.close()
