# -*- coding: utf-8 -*-
from collections import Counter

import matplotlib
import matplotlib.pyplot as plt
import MeCab
from matplotlib.font_manager import FontProperties

matplotlib.use("TkAgg")

fname = "neko.txt"
fname_parsed = "neko.txt.mecab"


def parse_neko():
    with open(fname) as data_file, open(fname_parsed, mode="w") as out_file:

        mecab = MeCab.Tagger()
        out_file.write(mecab.parse(data_file.read()))


def neko_lines():
    with open(fname_parsed) as file_parsed:
        morphemes = []
        for line in file_parsed:

            cols = line.split("\t")
            if len(cols) < 2:
                continue
            res_cols = cols[1].split(",")

            morpheme = {
                "surface": cols[0],
                "base": res_cols[6],
                "pos": res_cols[0],
                "pos1": res_cols[1],
            }
            morphemes.append(morpheme)

            if res_cols[1] == "句点":
                yield morphemes
                morphemes = []


parse_neko()

word_counter = Counter()

for line in neko_lines():
    word_counter.update([morpheme["surface"] for morpheme in line])

size = 10
list_word = word_counter.most_common(size)
print(list_word)

list_zipped = list(zip(*list_word))
words = list_zipped[0]
counts = list_zipped[1]
matplotlib.rcParams["font.family"] = "AppleGothic"

plt.bar(range(0, 10), counts, align="center")

plt.xticks(range(0, 10), words)

plt.xlim(xmin=-1, xmax=size)
plt.title("37. 頻度上位10語")
plt.xlabel("出現頻度が高い10語")
plt.ylabel("出現頻度")

plt.grid(axis="y")

plt.show()
