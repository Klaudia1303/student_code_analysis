s=input()
a=s[0:1]
b=s[-1:-2:-1]
c=ord(a)
d=ord(b)
if c==d:
    print("caratteri iniziale e finale uguali")
else:
    print("caratteri iniziale e finale diversi")
