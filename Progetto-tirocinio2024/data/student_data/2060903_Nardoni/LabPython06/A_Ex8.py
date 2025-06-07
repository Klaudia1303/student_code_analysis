s1=input("Inserire una stringa")
s2=input("Inserire una stringa")
n=int(input("Inxerire un numero intero"))
c=""
for i in range (0,len(s1)):
    for j in range (len(s2)):
        if s1[i] in s1:
            p=i
            k=s2.find(s1[i])
            if abs(p-k)<=n:
                c<=s1[i]
                break
print(c)
