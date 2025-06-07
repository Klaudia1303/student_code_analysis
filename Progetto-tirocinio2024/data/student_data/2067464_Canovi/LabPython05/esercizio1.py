s1 = input("inserisci una stringa: ")
s2 = input("inserisci un'altra stringa della stessa lunghezza della prima: ")
s = ""
for i in range(len(s1)):
    s = s + s1[i] + s2[i]
print(s)
