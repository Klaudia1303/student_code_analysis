s=input("Inserisci una stringa alfanumerica")
magg=0
for i in range (len(s)):
    if s.count(s[i])>=magg:
        magg=s.count(s[i])
        car=s[i]
print(car,magg)    
