s1 = input("inserisci la stringa: ")
s2 = input("inserisci la stringa: ")
while s1[len(s1)-1] != s2[0]:
    s1 = s2
    s2 = input("inserisci la stringa: ")
print(s1,s2)
