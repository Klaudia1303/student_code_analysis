s1=input('Inserisci stringa:')
s2=input('Inserisci stringa:')
s3=input('Inserisci stringa:')
while len(s1)+len(s2)!=len(s3):
    s1=s2
    s2=s3
    s3=input('Inserisci stringa:')
print(s1,s2,s3)