s1=input("Inserisci una stringa")
s2=input("Inserisci una stringa")
s3=input("Inserisci una stringa")
x=0
y=0
z=1

while x+y!=z:
    s1=s2
    s2=s3
    s3=input ("Inserisci una stringa:")
    x=len(s1)
    y=len(s2)
    z=len(s3)
    if x+y==z:
        print(s1, s2, s3)
