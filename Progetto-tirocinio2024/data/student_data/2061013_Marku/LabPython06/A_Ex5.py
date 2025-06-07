s=input('inserire stringa alfanumerica: ')
if s!='':
    massimo=0
    for i in range(len(s)):
        conta=1
        while i+1<len(s) and s[i]==s[i+1]:
            conta+=1
            i+=1
        if conta>=massimo:
            massimo=conta
            carattere=s[i]
print(carattere,massimo)

