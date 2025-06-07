s = input("Inserisci una stringa alfanumerica non vuota s: ")
a = 0
while a<len(s)-1:
    c = s.count(s[a])
    a = a+1    
print(s[a], c)
