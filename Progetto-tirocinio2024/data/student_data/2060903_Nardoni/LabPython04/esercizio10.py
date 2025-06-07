s1=input("Inserisci una stringa")
s2=input("Inserisci una stringa")
s3=input("Inserisci una stringa")
cond = False
while not cond:
    if len(s1)+len(s2)!=len(s3):
        s1=s2
        s2=s3
        s3=input("Inserisci una stringa")
    else:
       print(s1,s2,s3)
       cond = True
