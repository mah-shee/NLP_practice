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
