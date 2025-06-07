s1=input("Inserire una stringa:  ")
s2=input("Inserire un'altra stringa:  ")
n=int(input("Inserire un numero intero:  "))
s=''
for i in range(len(s1)):
    for k in range(len(s2)):
        if s1[i]==s2[k] and abs(k-i)<=n:
            s=s+s1[i]
print(s)
