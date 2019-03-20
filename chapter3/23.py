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
