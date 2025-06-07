s=input("Inserire una stringa: ")
b=True
while b:
    n=int(input("Inserire un numero intero positivo (ripeterà i singoli \
 caratteri della stringa): "))
    if n>0: b=False
    else:   print("\n\t\tIl numero non è positivo (>0)")
s1=""
for c in s:
    s1+=(c*n)
print("\n\nValori inseriti:\n\t-Stringa: ",s,"\n\t-Numero: ",n,"\n\n\
Risultato finale: ",s1)
