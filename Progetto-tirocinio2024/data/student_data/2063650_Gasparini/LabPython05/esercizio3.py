s1 = input("Stringa 1: ")
s2 = input("Stringa 2: ")

r = ""
for c in s1:
    if c not in s2:
        r += c
print(r)
