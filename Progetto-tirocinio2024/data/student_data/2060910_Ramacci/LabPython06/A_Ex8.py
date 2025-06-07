s1=input("inserire una stringa: ")
s2=input("inserire una stringa: ")
n=int(input("inserire un numero intero: "))
s=""
for i in range(len(s1)):
    for j in range(len(s2)):
        if s1[i]==s2[j] and abs(j-i)<=n:
            s+=s1[i]
print(s)
