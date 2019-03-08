# 00
s = 'stressed'
print(s[::-1])

# 01
s = 'パタトクカシーー'
print(s[::2])

# 02
s = "".join(i+j for i,j in zip("パトカー", "タクシー"))
print(s)

# 03
s = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
count = [len(i.strip(",.")) for i in s.split()]
print(count)

# 04
s = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
dic = {word[:2-(i in (1,5,6,7,8,9,15,16,19))]:i for i, word in enumerate(s.replace(".", "").split() , 1)}
print(dic)

# 05
def n_gram(s, n):
    return {tuple(s[i:i+n]) for i in range(len(s)-n+1)}

s = "I am an NLPer"

print(n_gram(s, 2))
print(n_gram([t.strip(".,") for t in s.split()], 2))

# 06
def n_gram(s, n):
    return {tuple(s[i:i+n]) for i in range(len(s)-n+1)}

x = "paraparaparadise"
y = "paragraph"

X = n_gram(x, 2)
Y = n_gram(y, 2)

print("X: %s" % X)
print("Y: %s" % Y)
print("Union: %s" % str(X|Y))
print("Intersection: %s" % str(X&Y))
print("Difference: %s" % str(X-Y))

if n_gram("se", 2) <= X:
    print("'se' is included in X.")

if n_gram("se", 2) <= Y:
    print("'se' is included in X.")

# 07
def hoge(x, y, z):
    return f"{x}時の{y}は{z}" 

print(hoge(x=12, y="気温", z=22.4))

# 08
def cipher(s):
    return "".join(chr(219-ord(c)) if c.islower() else c for c in s)

s = "Hi He Lied Because Boron Could Not Oxidize Fluorine."

print(cipher(s))
print(cipher(cipher(s)))


# 09
import random

def typo(s):
    return " ".join(t[0] + "".join(random.sample(t[1:-1], len(t)-2)) + t[-1] if len(t) > 4 else t for t in s.split())

s = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
print(typo(s))
