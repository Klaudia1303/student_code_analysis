s1 = input("stringa 1: ")
s2 = input("stringa 2: ")

for c in s1:
    if c not in s2:
        print(c,end='')
