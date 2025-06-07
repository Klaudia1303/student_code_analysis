s=input("inserisci stringa alfanumerica: ")
j=0
for i in range (len(s)):
    if s.count(s[i])>=j:
        j= s.count(s[i])
        c=s[i] 
print(j,c)
