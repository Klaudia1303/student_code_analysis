s=str(input("Inserisci la prima stringa>> "))
s1=str(input("Inserisci la seconda stringa>> "))
for i in range(len(s)):
    if s1.find(s[i])== -1:
        print(s[i],end='')
