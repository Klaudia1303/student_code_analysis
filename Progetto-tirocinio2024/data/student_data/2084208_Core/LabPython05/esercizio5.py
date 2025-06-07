s=input('Inserire una stringa contenente almeno due caratteri: ')
n=int(input('Inserire un intero positivo: '))
uguali=False
for i in range(0,len(s)):
    u=1
    while u<len(s) and not uguali:
        if s[i]==s[u]:
            if abs(u-i)==n:
                uguali=True
        else:
            uguali=False
        u+=1
print(uguali)

