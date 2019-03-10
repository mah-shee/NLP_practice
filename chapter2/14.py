import sys

assert len(sys.argv) == 2, "[usage]: python 14.先頭からN行を出力.py [N]"
with open('hightemp.txt') as f:
    print("".join(f.readlines()[:int(sys.argv[1])]), end="")
