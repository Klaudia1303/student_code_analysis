s1=input('inserisci una stringa: ')
s2=input('inserisci una stringa: ')
i=True

while i:
    s3=input('inserisci una stringa: ')
    if len(s1)+len(s2)==len(s3):
        i=False
    else:
        s1=s2
        s2=s3


print(s1,s2,s3)
        
        
