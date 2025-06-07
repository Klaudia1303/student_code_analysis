s1=input("inserisci una stringa: ")
s2=input("inserisci una stringa: ")
a=""
b=""
for i in range (len(s1)):
    for j in range (len(s2)):
        if s1[i]==s2[j]:
            b=""
            for x in range (len(s2)-j):
                if s1[i+x]==s2[j+x]:
                    b+=s1[i+x]
                else:
                    break
            if len(b)>len(a):
                a=b
print(a)
