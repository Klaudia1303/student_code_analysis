s1 = input('inserisci una stringa: ')
s2 = input('inserisci una stringa: ')
for c in s1: #fissa ciclicamente un  carattere c in s1
    if s2.count(c) == 0:#se il carattere c non compare in s2
        print(c,end='') #scrivilo
