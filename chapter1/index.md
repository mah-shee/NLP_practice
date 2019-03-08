やる。

# 第一章
## 00
https://stackoverflow.com/questions/3705670/best-way-to-create-a-reversed-list-in-python
https://note.nkmk.me/python-reverse-reversed/

vimで外部コマンドを打つとき
```
:!python3 %
```
### 回答
```
s = 'stressed'
print(s[::-1])
```

## 01
https://www.headboost.jp/python-how-to-slice-strings/

文字列から1要素おきにスライスして取り出す
コロン(:)を2個つなげると1要素おきや2要素おきに呼び出すことができる。

### 回答
```
s = 'パタトクカシーー'
print(s[::2])
```

## 02
https://qiita.com/hbkr/items/64ac81a84ddfe93641fc
https://note.nkmk.me/python-zip-usage-for/
https://note.nkmk.me/python-string-concat/
https://note.nkmk.me/python-list-comprehension/

リスト内包表記を使う。
`[式 for 任意の変数名 in イテラブルオブジェクト]`
リストやタプルなどのイテラブルオブジェクトの各要素を任意の変数名で取り出し式で評価、その結果が要素となる新たなリストが返される。

zip関数は複数のリストの要素をまとめられる関数。
zip関数でパトカーとタクシーのリテラル要素を一文字ずつ取り出したものをforループで回してそれぞれiとjに代入。
式で`i+j`をして、新しいリストが作成されたものを区切り文字なしでjoin

### 回答
```
s = "".join(i+j for i,j in zip("パトカー", "タクシー"))
print(s)
```

## 03
http://python-remrin.hatenadiary.jp/entry/2017/04/24/174405
https://note.nkmk.me/python-split-rsplit-splitlines-re/

split関数はデフォルト空白文字で分割をする。
分割された単語をリスト内包表記の式で単語ごとの長さに評価して、countへ代入する。
len()で単語の長さ（文字数）を評価するときに、","と"."をstrip()を使って消している。

### 回答
```
s = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
count = [len(i.strip(",.")) for i in s.split()]
print(count)
```

## 04
https://note.nkmk.me/python-enumerate-start/

emurate()関数を使うとforループの中でリスト（配列）などのイテラブルオブジェクトの要素と同時にインデックス番号（カウント、順番）を取得できる。
第二因数に任意の開始数値を指定することもできる。

https://note.nkmk.me/python-str-replace-translate-re-sub/
第一引数に置換元文字列、第二引数に置換先文字列を指定する。
replace()関数を使って文章中の"."を空文字に置き換えて、処理をしやすくする。

https://www.javadrive.jp/python/list/index10.html
in演算子は左辺のオブジェクトを持つ値が右辺のリストオブジェクトの要素の中に存在している場合は「True」を返します。存在しない場合は「False」を返す。
TrueとFalseのbool値はそれぞれ1,0と等価。
1, 5, 6, 7, 8, 9, 15, 16, 19番目の単語は一文字のみ表示させないといけない。
だから1, 5, 6, 7, 8, 9, 15, 16, 19の単語のときのみin演算子を使ってTrueの値（1）を引いて文字数を1文字にしている。

### 回答
```
s = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
dic = {word[:2-(i in (1,5,6,7,8,9,15,16,19))]:i for i, word in enumerate(s.replace(".", "").split() , 1)}
print(dic)
```

## 05
http://gihyo.jp/dev/serial/01/make-findspot/0005
N-gramは検索エンジンの仕組みの一つ。文字列をN文字づつ切り分けて、その文字ごとにインデックスを作成する方法。
Uni-gramは一文字ずつ、Bi-gramは二文字ずつ、Tri-gramは三文字ずつわけて、先頭から順番にインデックスする。
切り分け方は一文字ずつずらして、重複するものは度にも対応している。
この問題では度数はカウントしないでいいので集合型にして重複をなくすだけにする。

https://note.nkmk.me/python-range-usage/
len()関数で文字列の全体の長さを出したものからnを引いて1を足したものをrenge()関数の引数に取る。
こうすることでどこまで処理したらいいかを明示できる。

https://www.javadrive.jp/python/tuple/index6.html
tuple()関数はタプルをつくることができる。

s[i:i+n]としてリスト内包表記を使うことでsをはじめからn文字ずつスライスすることができる。
range関数でiもsに合わせてあるので文字数にも対応している。
iは連続しているからスライスが始まるのは一文字ずつ。

### 回答
```
def n_gram(s, n):
    return {tuple(s[i:i+n]) for i in range(len(s)-n+1)}

s = "I am an NLPer"

print(n_gram(s, 2))
print(n_gram([t.strip(".,") for t in s.split()], 2))
```

## 06
2つの文字列の文字bi-gramは05でつくった`n_gram()`関数を使う。

https://note.nkmk.me/python-set/
和集合（合併、ユニオン）は|演算子またはunion()メソッドで取得できる。
積集合（共通部分、交差、インターセクション）は&演算子またはintersection()メソッドで取得できる。
差集合は-演算子またはdifference()メソッドで取得できる。
ある集合が別の集合の部分集合かを判定するには、<=演算子またはissubset()メソッドを使う。

### 回答
```
def n_gram(s, n):
    return {tuple(s[i:i+n]) for i in range(len(s)-n+1)}

x = "paraparaparadise"
y = "paragraph"

X = n_gram(x, 2)
Y = n_gram(y, 2)

print("X: %s" % X)
print("Y: %s" % Y)
print("Union: %s" % str(X|Y))
print("Intersection: %s" % str(X&Y))
print("Difference: %s" % str(X-Y))

if n_gram("se", 2) <= X:
    print("'se' is included in X.")

if n_gram("se", 2) <= Y:
    print("'se' is included in X.")
```


## 07
https://note.nkmk.me/python-f-strings/
f-stringを使えばかなり簡単にできるしわかりやすい

### 回答
```
def hoge(x, y, z):
    return f"{x}時の{y}は{z}" 

print(hoge(x=12, y="気温", z=22.4))
```

## 08
https://docs.python.org/ja/3/library/functions.html#chr
https://docs.python.org/ja/3/library/functions.html#ord
文字コードに変換はこの式をつかう。

https://qiita.com/kokorinosoba/items/eb72dac6b68fccbac04d
リスト内包表記にifを使うと三項演算子みたいなかんじも使ってかなりいい感じになるっぽい。
if説がTrueのとき（cが小文字のとき）は219-cの文字コードの文字に置換して、elseのときはcをそのまま入れる。

### 回答
```
def cipher(s):
    return "".join(chr(219-ord(c)) if c.islower() else c for c in s)

s = "Hi He Lied Because Boron Could Not Oxidize Fluorine."

print(cipher(s))
print(cipher(cipher(s)))
```


## 09
https://note.nkmk.me/python-random-shuffle/
random.sample()で文字列のシャッフルを返してくれる。

https://note.nkmk.me/python-random-choice-sample-choices/
第二引数に取得したい要素の個数を必要とするので、len(t)-2で長さを指定する。

random()関数を実行して帰ってきたリストを文字列で返すためにもう一度join()関数を使う。
split()関数で単語の区切りがなくなっているので、" ".join()とすることにより単語の区切りにスペースを入れている

### 回答
```
import random

def typo(s):
    return " ".join(t[0] + "".join(random.sample(t[1:-1], len(t)-2)) + t[-1] if len(t) > 4 else t for t in s.split())

s = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
print(typo(s))
```
