s1 = input("Inserisci una stringa: ")
s2 = input("Inserisci una stringa: ")

for i in range(len(s1)):
    if s1[i] not in s2:
        print(s1[i], end='')
