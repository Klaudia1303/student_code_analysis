caratteriac=True
i=0
while caratteriac:
    s=input('inserisci una stringa: ')
    if s.count('a')>0 and s.count('c')>0:
        caratteriac=False
    i+=1
print(i)
