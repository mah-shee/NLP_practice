import sys

assert len(sys.argv) == 2, "[usage]: python 15.末尾からN行を出力.py [N]"
with open('hightemp.txt') as f:
    print("".join(f.readlines()[-int(sys.argv[1]):]), end="")
