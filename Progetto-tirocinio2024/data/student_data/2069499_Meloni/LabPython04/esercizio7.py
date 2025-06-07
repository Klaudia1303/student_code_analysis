s=input('Inserisci la stringa ')
i=0
mass=0
while i<len(s):
    freq=s.count(s[i])
    if freq>=mass:
        mass=freq
        lettera=s[i]
    i+=1
print(lettera)
