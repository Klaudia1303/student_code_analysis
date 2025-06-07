s1 = input('Inserisci la prima stringa: ')
s2 = input('Inserisci la seconda stringa: ')
s3 = input('Inserisci la terza stringa: ')
while len(s1)+len(s2)!=len(s3):
    s1 = s2
    s2 = s3
    s3 = input('Inserisci una stringa: ')
print(s1,s2,s3)
