s1 = input("Inserisci una stringa: ")
s2 = input("Inserisci una stringa: ")
s3 = ''
n = int(input("Inserisci un numero intero: "))
for i in range(0,len(s1)):
    for j in range(0,len(s2)):
            if s1[i] == s2[j] and i-j<=n:
                s3 = s3+s1[i]
                   
print(s3)
