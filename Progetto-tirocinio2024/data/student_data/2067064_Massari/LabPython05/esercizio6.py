s=input('inserire una parola: ')
for i in range(len(s)):
    parola=s[i]
    primaoccsx=s.find(parola)
    primaoccdx=s.rfind(parola)
    if primaoccsx!=primaoccdx:
        distanza=primaoccdx-primaoccsx
print(distanza)
