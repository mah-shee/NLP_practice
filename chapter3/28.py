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
