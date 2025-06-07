s1=input("Inserisci una stringa: ")
s2=input("Inserisci una stringa: ")
for i in range(0, len(s1)):
    if not (s1[i] in s2):
        print(s1[i], end='')
