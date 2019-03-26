https://qiita.com/Schaf_24/items/8872f8a9e56e9c546178
https://qiita.com/taroc/items/b9afd914432da08dafc8
https://mieruca-ai.com/ai/morphological_analysis_mecab/

ここらへん参考にしてMeCabをインストール&Pythonで実行できるように設定。

https://docs.python.org/ja/3/library/venv.html
https://qiita.com/fiftystorm36/items/b2fd47cf32c7694adc2e
venvで仮想環境を作ってパッケージの管理をしています。
pyenvでpythonそのもののバージョンを管理して、各プロジェクトごとにvenvを使って仮想環境を作っています。

## 30
https://pypi.org/project/mecab-python3/
https://github.com/SamuraiT/mecab-python3
MeCabをPythonで扱うためのモジュール。

https://qiita.com/rmecab/items/a970179b50176d847ddb
表層形\t品詞,品詞細分類1,品詞細分類2,品詞細分類3,活用形,活用型,原形,読み,発音
で出力されるので、問題の指定の通り表層形（surface），基本形（base），品詞（pos），品詞細分類1（pos1）をキーとする辞書に格納し、1文づつ、この辞書のリストとして返すようにする。

https://qiita.com/tomotaka_ito/items/35f3eb108f587022fa09
https://qiita.com/keitakurita/items/5a31b902db6adfa45a70
Pythonのジェネレーターについてなんとなく理解。

イテレータ: 要素を反復して取り出すことのできるインタフェース
ジェネレータ: イテレータの一種であり、1要素を取り出そうとする度に処理を行い、要素をジェネレートするタイプのもの。Pythonではyield文を使った実装を指すことが多いと思われる

これがなんだかんだ一番わかり易いかも。要素を取り出すごとに処理をして要素を返してくれるイテレータと考えれば良さそう。

形態素解析が済んだファイルオブジェクトを一行ずつ指定されたフォーマットに区切って辞書にしたものをリストに入れていく。
句点が現れた場合、リストを返すようなジェネレーターneko__lines()を作成してforループでプリントを行う。
ここですべての文章を辞書化してリストに保存すると重いので、ジェネレーターを使うことにより一文ずつプリントができるので全文をリスト化しなくて住む。

### 回答
'''
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
'''


## 31

