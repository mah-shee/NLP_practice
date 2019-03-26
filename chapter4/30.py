import MeCab

fname = "neko.txt"
fname_parsed = "neko.txt.mecab"


def parse_neko():
    with open(fname) as data_file, open(fname_parsed, mode="w") as out_file:

        mecab = MeCab.Tagger()
        out_file.write(mecab.parse(data_file.read()))


def neko_lines():
    with open(fname_parsed) as file_parsed:
        morphems = []
        for line in file_parsed:
            cols = line.split("\t")
            if len(cols) < 2:
                raise StopIteration
            res_cols = cols[1].split(",")

            morphem = {
                "surface": cols[0],
                "base": res_cols[6],
                "pos": res_cols[0],
                "pos1": res_cols[1],
            }
            morphems.append(morphem)

            if res_cols[1] == "句点":
                yield morphems
                morphems = []


parse_neko()

lines = neko_lines()
for line in lines:
    print(line)
