with open('col1.txt') as f1, open('col2.txt') as f2, open('output.txt', 'w') as f3:
    f3.write("".join([c1.strip() + '\t' + c2 for c1, c2 in zip(f1, f2)]))
