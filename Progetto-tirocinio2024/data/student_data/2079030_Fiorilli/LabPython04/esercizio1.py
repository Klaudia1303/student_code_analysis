s=input('inserisci una stringa: ')
t=1
while s.count('a')==0 or s.count('c')==0:
    t+=1
    s=input('inserisci una stringa: ')
print (t)
