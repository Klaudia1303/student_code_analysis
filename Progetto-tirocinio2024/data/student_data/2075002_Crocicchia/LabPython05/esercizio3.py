s1=input('inserisci una stringa: ')
s2=input('inserisci una stringa: ')
for a in range(len(s1)):
    if s1[a] not in s2:
         print(s1[a],sep='',end='')
    
