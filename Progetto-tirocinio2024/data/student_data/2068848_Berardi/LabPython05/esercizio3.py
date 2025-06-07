s1 = input("inserisci la prima stringa: ")
s2 = input("insersici la seconda stringa: ")
for i in s1:
    if i not in s2:
        print(i, end="")