import gzip
import json

fname = "jawiki-country.json.gz"

with gzip.open(fname, "rt", encoding="utf-8_sig") as jsonfile:
    for jsonline in jsonfile:
        line = json.loads(jsonline)
        if line["title"] == "イギリス":
            print(line["text"])
            break
