c=input('inserisci carattere: ')
s=input('inserisci stringa')
 counter=0
 lettera=0
 while counter <=2:

     if lettera<len(s):
         if s[lettera]==c:
             counter=counter+1
             lettera=lettera+1
             else:
                 lettera +=1
         if lettera== len(s):
             s=input('inserisci stringa: '))
print(counter)
