s1 = input("inserisci una stringa: ")
s2 = input("inserisci una stringa: ")
s3 = input("inserisci una stringa: ")
somma = s1 + s2
while len(somma) != len(s3):
    s1 = s2
    s2 = s3
    somma = s1 + s2
    s3 = input("inserisci una stringa: ")
     
print(s1, s2, s3)
