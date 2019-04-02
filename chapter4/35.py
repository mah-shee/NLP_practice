# -*- coding: utf-8 -*-
import MeCab

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

lines = neko_lines()

list_series_noun = []
for line in lines:
    nouns = []
    for morpheme in line:
        if morpheme["pos"] == "名詞":
            nouns.append(morpheme["surface"])
        else:
            if len(nouns) > 1:
                list_series_noun.append("".join(nouns))
                nouns = []

    if len(nouns) > 1:
        list_series_noun.append("".join(nouns))

series_noun = set(list_series_noun)
print(series_noun)
