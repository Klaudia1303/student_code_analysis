s=input('inserisci una stringa: ')
for c in s:
    if s.count(c)>1:
        print(True)
    else:
        print(False)

