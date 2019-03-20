参考
http://saneeeatsu.hatenablog.com/entry/nlp100-3
https://qiita.com/segavvy/items/fb50ba8097d59475f760

## 20
https://docs.python.org/ja/3/library/gzip.html
gzipファイルを圧縮、展開するための標準ライブラリにあるモジュール

https://note.nkmk.me/python-json-load-dump/
https://docs.python.org/ja/3/library/json.html
json形式のファイルや文字列をパースできるモジュール。
標準ライブラリ。
jsonファイルを辞書として読み込むときはjson.load()
json文字列を辞書として読み込むときはjson.loads()

### 回答
```
import gzip
import json

fname = "jawiki-country.json.gz"

with gzip.open(fname, "rt", encoding="utf-8_sig") as jsonfile:
    for jsonline in jsonfile:
        line = json.loads(jsonline)
        if line["title"] == "イギリス":
            print(line["text"])
            break
```


## 21
https://qiita.com/luohao0404/items/7135b2b96f9b0b196bf3
https://docs.python.org/ja/3/howto/regex.html#regular-expression-howto
https://docs.python.org/ja/3/library/re.html#module-re
正規表現について学習。
なんだかよくわかっていないけどとりあえずこの章を終わらせてからもう一回考える。
とりあえずreという標準ライブラリを使う。

正規表現結構複雑だから使って覚えるしかない。

### 回答
'''
import gzip
import json
import re

fname = "jawiki-country.json.gz"


def get_UK_article():
    with gzip.open(fname, "rt") as jsonfile:
        for line in jsonfile:
            line_json = json.loads(line)
            if line_json["title"] == "イギリス":
                return line_json["text"]
    raise ValueError("Not Found Article.")


pattern = re.compile(
    r"""
    ^ # 行頭
    ( # キャプチャ対象のグループ開始
    .* # 任意の文字0文字以上
    \[\[Category:
    .* # 任意の文字0文字以上
    \]\]
    .* # 任意の文字0文字以上
    ) #グループ終了
    $ # 行末
""",
    re.M + re.X,
)

result = pattern.findall(get_UK_article())

for line in result:
    print(line)
'''


## 22
貪欲マッチと非貪欲マッチという言葉に初めてぶち当たった。
正規表現そのものをまず勉強しないと話にならなそうなので、
https://www.hackerrank.com/
このサイトで正規表現を少し練習することにする。

### 回答
'''
import gzip
import json
import re

fname = "jawiki-country.json.gz"


def get_UK_article():
    with gzip.open(fname, "rt", encoding="utf-8_sig") as jsonfile:
        for line in jsonfile:
            line_json = json.loads(line)
            if line_json["title"] == "イギリス":
                return line_json["text"]

    raise ValueError("Not Found Article.")


pattern = re.compile(
    r"""
^ # 行頭
.* # 任意の文字0文字以上
\[\[Category:
( # キャプチャ対象のグループ開始
.*? # 任意の文字0文字以上、非貪欲マッチ
) # グループ終了
(?: # キャプチャ対象外のグループ開始
\|.* # '|'に続く0文字以上
)? # グループ終了, 0か1回の出現
\]\]
.* # 任意の0文字以上
$ # 行末
""",
    re.M + re.X,
)

result = pattern.findall(get_UK_article())

for line in result:
    print(line)
'''


## 23
セクション名は'='が2個以上で挟まれているので、行頭から'='の個数、空白文字をスキップ、セクション名、空白文字をスキップ、'='の個数の順で引っかかる。
後方参照を行うことによって同じ数の'='で囲まれているもの（＝セクション名）を正しくマッチできる。

複数のパターンがマッチした場合、タプルで返してくれる。
今回の場合は('=が２個以上', 'セクション名')となる。

### 回答
'''
import gzip
import json
import re

fname = "jawiki-country.json.gz"


def get_UK_article():
    with gzip.open(fname, "rt", encoding="utf-8_sig") as jsonfile:
        for line in jsonfile:
            line_json = json.loads(line)
            if line_json["title"] == "イギリス":
                return line_json["text"]

    raise ValueError("Not Found Article.")


pattern = re.compile(
    r"""
    ^ # 行頭
    (={2,})  # キャプチャ対象,2個以上の'='
    \s* # 余分な0個以上の空白
    (.+?)  # キャプチャ対象、任意の文字が1文字以上、非貪欲（以降の条件の巻き込み防止）
    \s* # 余分な0個以上の空白
    \1 # 後方参照 最初にキャプチャ対象と同じ対象
    .* # 任意の文字が0文字以上
    $ # 行末
    """,
    re.M + re.X,
)

result = pattern.findall(get_UK_article())

for line in result:
    level = len(line[0]) - 1
    print(
        "{indent}{sect}({level})".format(
            indent="\t" * (level - 1), sect=line[1], level=level
        )
    )
'''


## 24

### 回答
'''
import gzip
import json
import re

fname = "jawiki-country.json.gz"


def get_UK_article():
    with gzip.open(fname, "rt", encoding="utf-8_sig") as jsonfile:
        for line in jsonfile:
            line_json = json.loads(line)
            if line_json["title"] == "イギリス":
                return line_json["text"]

    raise ValueError("Not Found Article.")


pattern = re.compile(
    r"""
    (?:ファイル|File) # 非キャプチャのグループ,'File'か'ファイル'
    :
    (.+?) # キャプチャ対象, 任意の1文字以上の文字列, 非貪欲
    \|
    """,
    re.X,
)

result = pattern.findall(get_UK_article())

for line in result:
    print(line)
'''


## 25
https://ja.wikipedia.org/wiki/Template:%E5%9F%BA%E7%A4%8E%E6%83%85%E5%A0%B1_%E5%9B%BD

re.DOTALLオプションを追加することで改行も'.'対象に入るようにする。

'(?=...)'を使うことで「先読みアサーション」となる。
改行を含んでいる値（公式国名など）があるので「改行と'|'」がある"まで"をキャプチャ対象にしたいが、次の「改行と'|'」をキャプチャしてしまうとその行がキャプチャできなくなってしまう。
なので先読みアサーションを利用して、行頭の'|'を消費せずに改行と'|'をキャプチャ対象外にすることができる。

### 回答
```
import gzip
import json
import re

fname = "jawiki-country.json.gz"


def get_UK_article():
    with gzip.open(fname, "rt", encoding="utf-8_sig") as jsonfile:
        for line in jsonfile:
            line_json = json.loads(line)
            if line_json["title"] == "イギリス":
                return line_json["text"]

    raise ValueError("Not Found Article.")


pattern = re.compile(
    r"""
    ^\{\{基礎情報.*?$ # 基礎情報で始まる行
    (.*?) # キャプチャ対象, 任意の0文字以上, 非貪欲
    ^\}\}$ # '}}'の行
    """,
    re.MULTILINE + re.VERBOSE + re.DOTALL,
)


contents = pattern.findall(get_UK_article())

pattern = re.compile(
    r"""
^\| # '|'で始まる行
(.+?) # キャプチャ対象(フィールド名), 任意の1文字以上, 非貪欲
\s* # 空白文字0文字以上
=
\s* # 空白文字0文字以上
(.+?) # 2つ目のキャプチャ対象(値), 任意の1文字以上, 非貪欲
(?: #キャプチャ対象外のグループ
    (?=\n\|) # 改行+'|'の手前（肯定の先読み）
    | (?=\n$) # または、改行+終端の手前（肯定の先読み）
)
""",
    re.MULTILINE + re.VERBOSE + re.DOTALL,
)


fields = pattern.findall(contents[0])

result = {}
keys_test = []

for field in fields:
    result[field[0]] = field[1]
    keys_test.append(field[0])

for item in sorted(result.items(), key=lambda field: keys_test.index(field[0])):
    print(item)
```


## 26
25で抽出した文字列からさらに強調マークアップ('', ''', ''''')を除去する。

remobe_markup()関数を定義して、引数に文字列を取り、強調マークアップで括られている部分だけを取り出して返すようにする。

'''
import gzip
import json
import re

fname = "jawiki-country.json.gz"


def get_UK_article():
    with gzip.open(fname, "rt", encoding="utf-8_sig") as jsonfile:
        for line in jsonfile:
            line_json = json.loads(line)
            if line_json["title"] == "イギリス":
                return line_json["text"]

    raise ValueError("Not Found Article.")


def remove_markup(target):
    """マークアップの除去
    強調マークアップを除去する

    引数：
    target -- 対象の文字列
    戻り値：
    マークアップを除去した文字列
    """

    pattern = re.compile(
        r"""
        (\'{2,5}) #2〜5個の'（マークアップの開始）
        (.*?) # 任意の1文字以上の文字列
        (\1) # 1番目のキャプチャ対象と同じ内容
        """,
        re.MULTILINE + re.VERBOSE,
    )

    return pattern.sub(r"\2", target)


pattern = re.compile(
    r"""
    ^\{\{基礎情報.*?$ # 基礎情報で始まる行
    (.*?) # キャプチャ対象, 任意の0文字以上, 非貪欲
    ^\}\}$ # '}}'の行
    """,
    re.MULTILINE + re.VERBOSE + re.DOTALL,
)


contents = pattern.findall(get_UK_article())

pattern = re.compile(
    r"""
    ^\| # '|'で始まる行
    (.+?) # キャプチャ対象(フィールド名), 任意の1文字以上, 非貪欲
    \s* # 空白文字0文字以上
    =
    \s* # 空白文字0文字以上
    (.+?) # 2つ目のキャプチャ対象(値), 任意の1文字以上, 非貪欲
    (?: #キャプチャ対象外のグループ
        (?=\n\|) # 改行+'|'の手前（肯定の先読み）
        | (?=\n$) # または、改行+終端の手前（肯定の先読み）
    )
    """,
    re.MULTILINE + re.VERBOSE + re.DOTALL,
)


fields = pattern.findall(contents[0])

result = {}
keys_test = []

for field in fields:
    result[field[0]] = remove_markup(field[1])
    keys_test.append(field[0])

for item in sorted(result.items(), key=lambda field: keys_test.index(field[0])):
    print(item)
'''


## 27
内部リンク用のマークアップは'[[]]'で囲まれ、中に'|'が0か1以上ある

### 回答
'''
import gzip
import json
import re

fname = "jawiki-country.json.gz"


def get_UK_article():
    with gzip.open(fname, "rt", encoding="utf-8_sig") as jsonfile:
        for line in jsonfile:
            line_json = json.loads(line)
            if line_json["title"] == "イギリス":
                return line_json["text"]

    raise ValueError("Not Found Article.")


def remove_markup(target):
    """マークアップの除去
    強調マークアップを除去する

    引数：
    target -- 対象の文字列
    戻り値：
    マークアップを除去した文字列
    """

    pattern = re.compile(
        r"""
        (\'{2,5}) #2〜5個の'（マークアップの開始）
        (.*?) # 任意の1文字以上の文字列
        (\1) # 1番目のキャプチャ対象と同じ内容
        """,
        re.MULTILINE + re.VERBOSE,
    )

    target = pattern.sub(r"\2", target)

    pattern = re.compile(
        r"""
        \[\[ # '[['マークアップの開始
        (?: # キャプチャ対象外のグループ開始
            [^|]*? #'|'以外の文字が0文字以上、非貪欲
            \| # '|'
        )?? # グループ終了、このグループが0か1回出現、非貪欲
        ([^|]*?) # キャプチャ対象, '|'以外の文字が0文字以上,非貪欲
        \]\] # ']]'マークアップの終了
        """,
        re.MULTILINE + re.VERBOSE,
    )

    target = pattern.sub(r"\1", target)

    return target


pattern = re.compile(
    r"""
    ^\{\{基礎情報.*?$  # 基礎情報で始まる行
    (.*?)  # キャプチャ対象, 任意の0文字以上, 非貪欲
    ^\}\}$  # '}}'の行
    """,
    re.MULTILINE + re.VERBOSE + re.DOTALL,
)


contents = pattern.findall(get_UK_article())

pattern = re.compile(
    r"""
    ^\|  # '|'で始まる行
    (.+?)  # キャプチャ対象(フィールド名), 任意の1文字以上, 非貪欲
    \s*  # 空白文字0文字以上
    =
    \s*  # 空白文字0文字以上
    (.+?)  # 2つ目のキャプチャ対象(値), 任意の1文字以上, 非貪欲
    (?:  # キャプチャ対象外のグループ
        (?=\n\| ) # 改行+'|'の手前（肯定の先読み）
        | (?=\n$)  # または、改行+終端の手前（肯定の先読み）
    )
    """,
    re.MULTILINE + re.VERBOSE + re.DOTALL,
)


fields = pattern.findall(contents[0])

result = {}
keys_test = []

for field in fields:
    result[field[0]] = remove_markup(field[1])
    keys_test.append(field[0])

for item in sorted(result.items(), key=lambda field: keys_test.index(field[0])):
    print(item)
'''


## 28

### 回答
'''
import gzip
import json
import re

fname = "jawiki-country.json.gz"


def get_UK_article():
    with gzip.open(fname, "rt", encoding="utf-8_sig") as jsonfile:
        for line in jsonfile:
            line_json = json.loads(line)
            if line_json["title"] == "イギリス":
                return line_json["text"]

    raise ValueError("Not Found Article.")


def remove_markup(target):
    """マークアップの除去
    強調マークアップを除去する

    引数：
    target -- 対象の文字列
    戻り値：
    マークアップを除去した文字列
    """

    pattern = re.compile(
        r"""
        (\'{2,5}) #2〜5個の'（マークアップの開始）
        (.*?) # 任意の1文字以上の文字列
        (\1) # 1番目のキャプチャ対象と同じ内容
        """,
        re.MULTILINE + re.VERBOSE,
    )

    target = pattern.sub(r"\2", target)

    pattern = re.compile(
        r"""
        \[\[ # '[['マークアップの開始
        (?: # キャプチャ対象外のグループ開始
            [^|]*? #'|'以外の文字が0文字以上、非貪欲
            \| # '|'
        )*? # グループ終了、このグループが0以上出現,非貪欲
        ([^|]*?) # キャプチャ対象, '|'以外の文字が0文字以上,非貪欲
        \]\] # ']]'マークアップの終了
        """,
        re.MULTILINE + re.VERBOSE,
    )

    target = pattern.sub(r"\1", target)

    pattern = re.compile(
        r"""
        \{\{lang # {{lang マークアップの開始
        (?: # キャプチャ対象外のグループ開始
            [^|]*? # '|'以外の文字が0文字以上, 非貪欲
            \| # '|'
        )*? # グループ終了, このグループが0以上出現, 非貪欲
        ([^|]*?) # キャプチャ対象, '|'以外が0文字以上、非貪欲（表示対象の文字列）
        \}\} # '}}'マークアップの終了
        """,
        re.MULTILINE + re.VERBOSE,
    )
    target = pattern.sub(r"\1", target)

    pattern = re.compile(
        r"""
        \[http:\/\/ # '[http://'（マークアップの開始）
        (?: # キャプチャ対象外のグループ開始
            [^\s]*? # 空白以外の文字が0文字以上, 非貪欲
            \s # 空白
        )? # グループ終了, このグループが0か1出現
        ([^]]*?) # キャプチャ対象、']'以外が0文字以上、非貪欲（表示対象の文字列）
        \] # ']' マークアップの終了
        """,
        re.MULTILINE + re.VERBOSE,
    )
    target = pattern.sub(r"\1", target)

    pattern = re.compile(
        r"""
        < # マークアップの開始
        \/? # '/'が0か1出現（終了タグの場合は/がある）
        [br|ref] # brかref
        [^>]*? # '>'以外が0文字以上, 非貪欲
        > # マークアップの終了
    """,
        re.MULTILINE + re.VERBOSE,
    )
    target = pattern.sub("", target)

    return target


pattern = re.compile(
    r"""
    ^\{\{基礎情報.*?$  # 基礎情報で始まる行
    (.*?)  # キャプチャ対象, 任意の0文字以上, 非貪欲
    ^\}\}$  # '}}'の行
    """,
    re.MULTILINE + re.VERBOSE + re.DOTALL,
)


contents = pattern.findall(get_UK_article())

pattern = re.compile(
    r"""
    ^\|  # '|'で始まる行
    (.+?)  # キャプチャ対象(フィールド名), 任意の1文字以上, 非貪欲
    \s*  # 空白文字0文字以上
    =
    \s*  # 空白文字0文字以上
    (.+?)  # 2つ目のキャプチャ対象(値), 任意の1文字以上, 非貪欲
    (?:  # キャプチャ対象外のグループ
        (?=\n\| ) # 改行+'|'の手前（肯定の先読み）
        | (?=\n$)  # または、改行+終端の手前（肯定の先読み）
    )
    """,
    re.MULTILINE + re.VERBOSE + re.DOTALL,
)


fields = pattern.findall(contents[0])

result = {}
keys_test = []

for field in fields:
    result[field[0]] = remove_markup(field[1])
    keys_test.append(field[0])

for item in sorted(result.items(), key=lambda field: keys_test.index(field[0])):
    print(item)
'''


## 29
これはapiを叩くためにhttpリクエストを送るためのライブラリの使い方に慣れろ的な問題っぽい

### 回答
'''
import gzip
import json
import re
import urllib.parse
import urllib.request

fname = "jawiki-country.json.gz"


def get_UK_article():
    with gzip.open(fname, "rt", encoding="utf-8_sig") as jsonfile:
        for line in jsonfile:
            line_json = json.loads(line)
            if line_json["title"] == "イギリス":
                return line_json["text"]

    raise ValueError("Not Found Article.")


def remove_markup(target):
    """マークアップの除去
    強調マークアップを除去する

    引数：
    target -- 対象の文字列
    戻り値：
    マークアップを除去した文字列
    """

    pattern = re.compile(
        r"""
        (\'{2,5}) #2〜5個の'（マークアップの開始）
        (.*?) # 任意の1文字以上の文字列
        (\1) # 1番目のキャプチャ対象と同じ内容
        """,
        re.MULTILINE + re.VERBOSE,
    )

    target = pattern.sub(r"\2", target)

    pattern = re.compile(
        r"""
        \[\[ # '[['マークアップの開始
        (?: # キャプチャ対象外のグループ開始
            [^|]*? #'|'以外の文字が0文字以上、非貪欲
            \| # '|'
        )*? # グループ終了、このグループが0以上出現,非貪欲
        ([^|]*?) # キャプチャ対象, '|'以外の文字が0文字以上,非貪欲
        \]\] # ']]'マークアップの終了
        """,
        re.MULTILINE + re.VERBOSE,
    )

    target = pattern.sub(r"\1", target)

    pattern = re.compile(
        r"""
        \{\{lang # {{lang マークアップの開始
        (?: # キャプチャ対象外のグループ開始
            [^|]*? # '|'以外の文字が0文字以上, 非貪欲
            \| # '|'
        )*? # グループ終了, このグループが0以上出現, 非貪欲
        ([^|]*?) # キャプチャ対象, '|'以外が0文字以上、非貪欲（表示対象の文字列）
        \}\} # '}}'マークアップの終了
        """,
        re.MULTILINE + re.VERBOSE,
    )
    target = pattern.sub(r"\1", target)

    pattern = re.compile(
        r"""
        \[http:\/\/ # '[http://'（マークアップの開始）
        (?: # キャプチャ対象外のグループ開始
            [^\s]*? # 空白以外の文字が0文字以上, 非貪欲
            \s # 空白
        )? # グループ終了, このグループが0か1出現
        ([^]]*?) # キャプチャ対象、']'以外が0文字以上、非貪欲（表示対象の文字列）
        \] # ']' マークアップの終了
        """,
        re.MULTILINE + re.VERBOSE,
    )
    target = pattern.sub(r"\1", target)

    pattern = re.compile(
        r"""
        < # マークアップの開始
        \/? # '/'が0か1出現（終了タグの場合は/がある）
        [br|ref] # brかref
        [^>]*? # '>'以外が0文字以上, 非貪欲
        > # マークアップの終了
    """,
        re.MULTILINE + re.VERBOSE,
    )
    target = pattern.sub("", target)

    return target


pattern = re.compile(
    r"""
    ^\{\{基礎情報.*?$  # 基礎情報で始まる行
    (.*?)  # キャプチャ対象, 任意の0文字以上, 非貪欲
    ^\}\}$  # '}}'の行
    """,
    re.MULTILINE + re.VERBOSE + re.DOTALL,
)


contents = pattern.findall(get_UK_article())

pattern = re.compile(
    r"""
    ^\|  # '|'で始まる行
    (.+?)  # キャプチャ対象(フィールド名), 任意の1文字以上, 非貪欲
    \s*  # 空白文字0文字以上
    =
    \s*  # 空白文字0文字以上
    (.+?)  # 2つ目のキャプチャ対象(値), 任意の1文字以上, 非貪欲
    (?:  # キャプチャ対象外のグループ
        (?=\n\| ) # 改行+'|'の手前（肯定の先読み）
        | (?=\n$)  # または、改行+終端の手前（肯定の先読み）
    )
    """,
    re.MULTILINE + re.VERBOSE + re.DOTALL,
)


fields = pattern.findall(contents[0])

result = {}

for field in fields:
    result[field[0]] = remove_markup(field[1])

fname_flag = result["国旗画像"]

url = (
    "https://www.mediawiki.org/w/api.php?"
    + "action=query"
    + "&titles=File:"
    + urllib.parse.quote(fname_flag)
    + "&format=json"
    + "&prop=imageinfo"
    + "&iiprop=url"
)

request = urllib.request.Request(
    url, headers={"User-Agent": "NLP100_Python(@mah_shee)"}
)
connection = urllib.request.urlopen(request)

data = json.loads(connection.read().decode())

url = data["query"]["pages"].popitem()[1]["imageinfo"][0]["url"]
print(url)
'''
