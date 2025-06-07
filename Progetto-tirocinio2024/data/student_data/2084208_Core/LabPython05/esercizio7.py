s=input('Inserire una stringa: ')
uguali=False
u=0
while u<len(s) and not uguali:
    i=1
    while i<u and not uguali:
        if s[i]==s[u]:
            uguali=True
        else:
            uguali=False
        i+=1
    u+=1
print(uguali)

