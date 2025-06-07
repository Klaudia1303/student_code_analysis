s1=input('inserisci stringa: ')
s2=input('inserisci altra stringa: ')
s3=input('inserisci altra stringa: ')
while len(s1)+len(s2)!=len(s3):
    s1=s2
    s2=s3
    s3=input('inserisci una stringa: ')
print(s1,s2,s3)
