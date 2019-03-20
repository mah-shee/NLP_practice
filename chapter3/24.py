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
