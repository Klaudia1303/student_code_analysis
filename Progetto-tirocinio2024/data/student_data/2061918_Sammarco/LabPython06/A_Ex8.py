s1=input("inserisci una stringa:")
s2=input("inserisci una seconda stringa:")
n=int(input("inserisci un numero intero:"))
s3=""
for i in range(len(s1)):
    for j in range(len(s2)):
        if s1[i]==s2[j] and abs(j-i)<=n:
            s3=s3+s1[i]
print(s3)
