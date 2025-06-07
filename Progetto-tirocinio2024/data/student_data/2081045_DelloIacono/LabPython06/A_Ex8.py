s1 = input("Inserisci una stringa: ")
s2 = input("Inserisci una stringa: ")
n = int(input("Inserisci un numero intero: "))
s3 = ""
sf = ""
for i in range (len(s1)):
    if s2.rfind(s1[i])!=-1:
        s3 = s3 + s1[i]
for i in range (len(s3)-1,-1,-1):
    l = s1.find(s3[i]) - s1.find(s3[i-1])
    if (l<=n):
        sf = sf + s3[i]
print(sf[::-1])
