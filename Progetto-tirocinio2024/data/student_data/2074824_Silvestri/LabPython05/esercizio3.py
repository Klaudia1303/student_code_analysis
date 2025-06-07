s1=input("Inserisci una stringa:")
s2=input("Inserisci un\'altra stringa:")
for i in list(s1):
    if i not in s2:
        print(i,end='')
