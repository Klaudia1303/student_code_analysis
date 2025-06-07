s=input('inserisci una stringa alfanumerica: ')
massimo=0
for i in range(0,len(s)):
    n=s.count(s[i])
    if n>=massimo:
        massimo=n
        c=s[i]
print(massimo,' ',c)
