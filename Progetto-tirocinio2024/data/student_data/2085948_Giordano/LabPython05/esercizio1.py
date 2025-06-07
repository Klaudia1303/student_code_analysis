s1 = input("Inserisci la prima stringa: ")
len1 = len(s1)
s2 = input("Inserisci la seconda stringa: ")
len2 = len(s2)
if len1 != len2:
    print("Le stringhe devono avere la stessa lunghezza.")
else:
    result = ""
    for i in range(len1):
        result += s1[i]
        result += s2[i]
    print(result)
