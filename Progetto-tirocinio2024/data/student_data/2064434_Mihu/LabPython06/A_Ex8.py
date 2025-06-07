s1=input("inserisci la prima stringa: ")
s2=input("inserisci la seconda stringa: ")
n=int(input("inserisci l'intero: "))
for i in range(len(s1)):
    for j in range(len(s2)):
        if s1[i] in s2:
            P=i
            p=s2.find(s1[i])
            if abs(P-p)<=n:
                print(s1[i],end="")
                break
