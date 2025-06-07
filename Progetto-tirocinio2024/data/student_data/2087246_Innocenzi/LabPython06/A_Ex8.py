s1=input("Inserisci una stringa: ")
s2=input("Inserisci una stringa: ")
n=int(input("Inserisci un numero: "))
s3=s4=''

for i in range(len(s1)):
    if s1[i] in s2:
        if s1[i] not in s3:
            s3=s3+s1[i]

for i in range(len(s3)):
    if i<len(s3)-1:
        if abs(s1.find(s3[i])-s1.find(s3[i+1])) <= n:
            s4=s4+s3[i]+s3[i+1]
    else:
        break
print(s4)

