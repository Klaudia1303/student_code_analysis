

s1=input("Inserire stringa:\t")
s2=input("Inserire stringa:\t")

for i in s1:
    if i not in s2:
        print(i, sep='', end='')
