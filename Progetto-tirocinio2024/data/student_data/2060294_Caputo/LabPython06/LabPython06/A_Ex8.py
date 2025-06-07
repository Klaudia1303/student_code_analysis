s1=input('inserisci una stringa: ')
s2=input('inserisci una stringa: ')
n=int(input('inserisci un numero intero: '))
s3=''
fine=''
for i in range (len(s1)):
    if s2.rfind(s1[i])!=-1: #se non lo trova restituisce -1
        s3=s3+s1[i]
for i in range(len(s3)-1, -1, -1):
    l=s1.find(s3[i])-s1.find(s3[i-1])
    if (l<=n):
        fine=fine+s3[i]
print(fine[::-1])
    
