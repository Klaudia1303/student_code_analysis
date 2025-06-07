s1=input('inserire la prima stringa: ')
s2=input('inserire la seconda stringa: ')
if s1==s2:
      print('')
else:
      risultato=s1
      for i in range(len(s1)):
            for j in range(len(s2)):
                  x=s1[i]
                  y=s2[j]
                  if x==y:
                        risultato=risultato.replace(s1[i],'')
      print(risultato)
                  
                  
            
            
            
            
