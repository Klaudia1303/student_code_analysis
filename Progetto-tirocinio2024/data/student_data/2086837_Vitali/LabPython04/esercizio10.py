s1=input("Inserisci una stringa s: ")
l1=len(s1)
s2=input("Inserisci una stringa s: ")
l2=len(s2)
s3=input("Inserisci una stringa s: ")
somma=l1+l2
while somma!=len(s3):
    s1=s2
    s2=s3
    l1=l2
    l2=len(s3)
    somma=l1+l2
    s3=input("Inserisci una stringa s: ")
print(s1,s2,s3)
