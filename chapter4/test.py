dict1 = {"a": "1", "b": "b", "c": "c"}
dict2 = {"a": "2", "b": "b", "c": "c"}
dict3 = {"a": "3", "b": "b", "c": "c"}
list = [dict1, dict2, dict3]


dada = [dict["b"] for dict in list if dict["a"] == "2"]

print(dada)
