s1=input("Inserisci una stringa: ")
s2=input("Inserisci una stringa: ")
n=int(input("Inserisci un numero intero: "))
for i in range(len(s1)):
    if s1[i] in s2:
        j=s2.find(s1[i])
        if i-n<=j and j<=i+n:
            print(s2[j],end="",sep="")
        else:
            continue
    else:
        continue
