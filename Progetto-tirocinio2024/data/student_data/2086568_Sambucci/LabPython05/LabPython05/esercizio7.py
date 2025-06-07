s=input('Inserire stringa: ')
presente=False
i=0
while not presente and i<len(s):
    if s.count(s[i])>=2:
        presente=True
    i+=1
print(presente)

