s1=input('inserisci la prima stringa ')
s2=input('inserisci la seconda stringa ')
trovato=False
ss=''
for i in range(len(s1)):
    trovato=False  
    for c in range(len(s2)):
         # print(s1[i], s2[c])
             
         if s1[i] == s2[c]:
             trovato=True
             
    if trovato==False:
               ss=ss+s1[i]
    
print (ss)
