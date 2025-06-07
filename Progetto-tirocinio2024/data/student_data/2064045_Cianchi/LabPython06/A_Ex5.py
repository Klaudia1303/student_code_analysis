s=input('inserire una stringa alfanumerica non vuota:')
ripetizioni=0
carattere=''
for i in range(len(s)):
    if s.count(s[i])>=ripetizioni:
        ripetizioni=s.count(s[i])
        carattere=s[i]
print(carattere, ripetizioni)
