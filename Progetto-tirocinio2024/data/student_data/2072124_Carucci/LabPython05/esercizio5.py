s = input('Inserire una stringa contenente almeno due cartatteri: ')
n = int(input('Inserire un numero intero positivo: '))

uguali = False
i = 0
while (not uguali) and (i<(len(s)-n)):
    if s[i] == s[i+n]:
        uguali = True
    i+=1
print('Nella stringa compaiono 2 lettere uguali a distanza', n, ':', uguali)

