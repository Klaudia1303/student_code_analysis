print("Inserisci due stringhe della stessa lugnhezza")
s1=input("Inserisci una stringa:")
s2=input("Inserisci un\'altra stringa:")
for i in range(len(s1)):
    k=s1[i]+s2[i]
    print(k,end="")
