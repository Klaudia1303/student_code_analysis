s1 = input("Inserisci una stringa: ")
l1 = len(s1)

s2 = input("Inserisci una stringa: ")
l2 = len(s2)

s3 = input("Inserisci una stringa: ")
l3 = len(s3)


while l1+l2 != l3:
    s1 = s2
    l1 = l2
    s2 = s3
    l2 = l3
    s3 = input("Inserisci una stringa: ")
    l3 = len(s3)

print(s1, s2, s3, sep=" ")
