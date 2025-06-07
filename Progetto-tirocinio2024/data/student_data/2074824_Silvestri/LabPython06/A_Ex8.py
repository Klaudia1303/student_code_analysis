s1 = input("Inserisci una stringa: ")
s2 = input("Inserisci una stringa: ")
n = int(input("Inserisci un nujmero n: "))

s3 = ""

for i in range(0,len(s1)):
    
    if s1[i] in s2:
        sub1 = s1[i]
        for j in range(0,n+1):
            if s1.find(sub1)+j == s2.find(sub1) or s1.find(sub1)-j == s2.find(sub1):
                s3 += s1[i]

print(s3)
