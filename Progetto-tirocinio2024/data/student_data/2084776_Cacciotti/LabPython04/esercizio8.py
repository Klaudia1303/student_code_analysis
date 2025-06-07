s0=input('inserisci stringa: ')
s1=input('inserisci stringa: ')
while True:
    if s0[len(s0)-1]==s1[0]:
        break
    s0=s1
    s1=input('inserisci stringa: ')
print (s0+' '+s1)
