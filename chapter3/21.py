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
