s = str(input("Inserire una stringa alfanumerica non vuota:"))
massimo = 0
carattere = " "
for x in range(len(s)):
    i = s.count(s[x])
    if i >= massimo:
        massimo = i
        carattere = s[x]

print(massimo)
print(carattere)
    
    
