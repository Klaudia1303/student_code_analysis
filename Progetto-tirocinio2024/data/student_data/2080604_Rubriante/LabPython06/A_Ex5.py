s=input("Inserisci una stringa: ")
k=1
j=0
lett=""
for i in range(0,len(s)-1):
    if s[i]==s[i+1]:
        k+=1
        if j<=k:
            j=k
            lett=s[i]
    else:
        k=1
        continue
print("la tellera \"",str(lett),"\" appare",str(j),"volte")
