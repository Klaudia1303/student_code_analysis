#trova una stringa che ha l'ultimo carattere uguale al primo carattere della stringa successiva

s = input("input = ")
m = input("input = ")
i = 0

while s[len(s)-1] != m[i]:
    s = m
    m = input("input = ")

print(s,m)
