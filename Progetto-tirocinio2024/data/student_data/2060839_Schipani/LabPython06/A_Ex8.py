s1=input('inserisci una stringa ')
s2=input('inserisci una stringa ')
n=int(input('inserisci un intero '))
s3=''
for i in range(len(s1)):
    if i-n<0:
        j=0
    else:
        j=i-n
    if i+n+1>=len(s2):
        k=len(s2)
    else:
        k=i+n+1
    if s1[i] in s2[j:k]:
        s3+=s1[i]
print(s3)
