s=input("Inserisci una stringa alfanumerica non vuota: ")
ma=1
car="*"
for i in range (1,len(s)-1):
    if s[i]==s[i+1]:
        if car!=s[i+1]:
            ma=1
            car=s[i+1]
        ma+=1
        car=s[i+1]
    else:
        continue
print(car,ma)
