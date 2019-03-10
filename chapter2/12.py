with open('hightemp.txt') as f1, open("col1.txt", "w") as f2, open("col2.txt", "w") as f3:
    cols = list(zip(*[row.split("\t") for row in f1]))
    f2.write("\n".join(cols[0]))
    f3.write("\n".join(cols[1]))
