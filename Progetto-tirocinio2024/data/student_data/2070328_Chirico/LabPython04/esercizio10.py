#trova 2 stringhe che siano lunghe in totale quanto la stringa successiva

s = input("input = ")
n = input("input = ")
m = input("input = ")

while len(s)+len(n) != len(m):
    s = n
    n = m
    m = input("input = ")

print(s,n,m)
