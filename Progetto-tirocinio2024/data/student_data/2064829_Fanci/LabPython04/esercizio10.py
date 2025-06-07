s1 = input("inserisci striga: ")
s2 = input("inserisci striga: ")
s3 = input("inserisci striga: ")
while len(s1)+len(s2)!=len(s3):
    s1=s2
    s2=s3
    s3 = input("inserisci stringa: ")
print(s1,s2,s3)
