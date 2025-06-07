s=input('inserisci una stringa:')
for c in s:
    if s.count(c)>1:
        cs=s.find(c)
        cd=s.rfind(c)
        print(cd-cs)
if s.count(c)==1:
    print('0')
   
 
