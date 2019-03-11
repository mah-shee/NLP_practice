from collections import Counter

col1 = [line.split("\t")[0] for line in open("hightemp.txt")]

counter = Counter(col1)
for word, count in counter.most_common():
    print(word + ", " + str(count))
