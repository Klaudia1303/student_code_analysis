s1=input("Inserisci una stringa: ")
s2=input("Inserisci una stringa: ")
n=int(input("inserisci un numero intero: "))
s3=""
for i in range(len(s1)):
    if s1[i] in s2:
       for j in range(n+1):
           if s1.find(s1[i])+j == s2.find(s1[i]) or s1.find(s1[i])-j == s2.find(s1[i]):
              s3+=s1[i]
       
print(s3)
