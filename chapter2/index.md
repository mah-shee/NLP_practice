## 10
https://stackoverflow.com/questions/845058/how-to-get-line-count-cheaply-in-python
`num_lines = sum(1 for line in open('myfile.txt'))`
この書き方が1番早いっぽい。

http://www.ritsumei.ac.jp/~tomori/unix.html
`$wc (file名)`でファイルの行数、単語数、文字数を表示

### 回答
```
print(sum(1 for line in open('hightemp.txt')))
```


## 11
https://hydrocul.github.io/wiki/commands/sed.html
`sed 's/\t/ /g' (filename)`でいける。
自分がちゃんとカレントディレクトリに要ることも大事。

https://pythonmemo.hatenablog.jp/entry/2018/05/05/135955
https://note.nkmk.me/python-str-replace-translate-re-sub/
withオプションを付けてopen()関数でファイルを開き、replace()でタブをスペースに置換する。

### 回答
```
with open('hightemp.txt') as f:
    print(f.read().replace("\t"," "))
```


## 12
https://eng-entrance.com/linux-command-cut
cutはテキストファイルを横方向に分割するコマンドだ。
`cut -f 項目数 -d 区切り文字 ファイル名`
でそれぞれの行で必要な情報を切り出した列を出力できる。

http://d.hatena.ne.jp/psappho/20120802/1343840823
`with`文はカンマ区切りで複数のファイルを開くことができる。
これで3つファイルを開いてそれぞれ編集する。

open()関数が返してくるファイルオブジェクトはイテラブルだからforループで回せる。
詳しい説明は自分で記事を書いた
https://sorededou.com/python-reason-textobject-is-iterable

### 回答
```
with open('hightemp.txt') as f1, open("col1.txt", "w") as f2, open("col2.txt", "w") as f3:
    cols = list(zip(*[row.split("\t") for row in f1]))
    f2.write("\n".join(cols[0]))
    f3.write("\n".join(cols[1]))
```


## 13
https://eng-entrance.com/linux-command-paste
paseteコマンドはテキストファイルを列方向に結合する。
オプション無しでの結合文字はタブになるので、オプション無しで`$paste col1.txt col2.txt`を実行すれば良い。

col1.txtとcol2.txtをテキストオブジェクトとして開いてそれぞれzip関数で各要素を順番に取り出す。
strip()関数でcol1.txtの各要素の後ろについている改行を取り除いてタブとcol2.txtの各要素を足したものをjoin()関数で記入する。
https://dackdive.hateblo.jp/entry/2015/02/13/174206
strip()関数はデフォルトで空白文字（改行も含む）を取り除いてくれる。

### 回答
```
with open('col1.txt') as f1, open('col2.txt') as f2, open('output.txt', 'w') as f3:
    f3.write("".join([c1.strip() + '\t' + c2 for c1, c2 in zip(f1, f2)]))
```


## 14
https://eng-entrance.com/linux-command-head
headコマンドはファイルの先頭からデフォルト10行を表示する。
-nオプションで表示する行数を指定することができる。
`head -n N hightemp.txt`

https://qiita.com/orange_u/items/3f0fb6044fd5ee2c3a37<Paste>
コマンドライン引数を使うとPythonプログラムを実行時にコマンドライン上から引数を渡すことができる。
sysモジュールのargvを使う。
最初に実行するファイル名を含んだリスト型で渡される。
リストの各要素は文字列として扱われるので注意。

https://qiita.com/nannoki/items/15004992b6bb5637a9cd
sys.argvを使用して引数が不足しているとエラーを吐くのでassert文を利用してテストを書いておく。

https://note.nkmk.me/python-file-io-open-with/
テキストファイル全体を改行文字で区切ったリストとして取得するreadlines()メソッドを利用してリストとして取得したテキストファイルをスライスして入力された引数分の行数を表示する。

https://www.lifewithpython.com/2017/06/python-3-print.html
print()関数は末尾の文字はデフォルトで改行文字になっているのでendパラメーターで空文字を指定しておく。

### 回答
```
import sys

assert len(sys.argv) == 2, "[usage]: python 14.先頭からN行を出力.py [N]"
with open('hightemp.txt') as f:
    print("".join(f.readlines()[:int(sys.argv[1])]), end="")
```


## 15
https://eng-entrance.com/linux-command-tail
tailコマンドはheadの反対でファイルの末尾からデフォルト10行表示するコマンド。
ちなみに、-fコマンドを利用するとファイルの追記を監視することができるらしい。

14の問題とやることは一緒
リストのスライスをマイナスN行から最後までと表示することで順番は逆にならないようにしている。
```
import sys

assert len(sys.argv) == 2, "[usage]: python 15.末尾からN行を出力.py [N]"
with open('hightemp.txt') as f:
    print("".join(f.readlines()[-int(sys.argv[1]):]), end="")
```

## 16
https://eng-entrance.com/linux-command-split
splitコマンドはファイルを複数のファイルに分割できる。

-lオプションで行単位で分割することができる。
この場合、N行ごとに分割することはできてもN個に分割することはできない。
linuxコマンドをざっと探しても小数点の切り上げをしてくれるコマンドは見つからなかったから難しそう。

元のデータ(24行)をN分割をしないといけないから、余りの扱いが大変になる。
N=5の場合とかは5行分のリストが4つと4行分のリストが1つできることになる。

https://docs.python.org/ja/3/library/math.html
数学関数のmath.ceil(x)はxの切り上げをしてくれるのでコレを使う。
ファイルの行数をNで割ったものを切り上げれば分割する行数が得られるのでそれでリストを分割する方針。

テキストファイルを作れとは言われていないけど、他の記事とか見るとみんなテキストファイルも作成しているので乗ることにする。

### 回答
```
import math
import sys

n = int(sys.argv[1])
with open("hightemp.txt") as f:
    lines = f.readlines()

count = len(lines)
unit = math.ceil(count / n)

for i in range(n):
    with open("file" + str(i + 1) + ".txt", "w") as f:
        f.write("".join(lines[i * unit : (i + 1) * unit]))
```
