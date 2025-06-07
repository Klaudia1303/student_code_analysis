i=True
c='1'
while(True):
    s=input("Inserisci una stringa: ")
    if(s[0]==c[-1]):
        break
    else:
        c=s

print(c, s)