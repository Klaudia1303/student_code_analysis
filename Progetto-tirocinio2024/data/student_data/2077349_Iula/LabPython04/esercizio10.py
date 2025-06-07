s3=input("Inserisci una stringa: ")
s2=input("Inserisci una stringa: ")
s1=input("Inserisci una stringa: ")
while len(s1)!=len(s3)+len(s2):
    s3=s2
    s2=s1
    s1=input("Inserisci una stringa: ")
print(s3,s2,s1)

